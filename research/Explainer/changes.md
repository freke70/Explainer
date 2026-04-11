# Why LLMs lose their way in long texts — and how to fix it

**Every frontier LLM degrades as it generates longer text, but a converging set of techniques from 2025–2026 research now offers reliable countermeasures.** Chroma's 2025 study of 18 frontier models — including GPT-4.1, Claude Opus 4, and Gemini 2.5 Pro — confirmed that *every single one* exhibits measurable quality degradation during long-form generation, a phenomenon researchers have formalized as **"context rot."** The degradation stems from three compounding architectural mechanisms: the U-shaped attention curve ("lost in the middle"), quadratic attention dilution across growing token counts, and distractor interference from semantically similar content. The good news: a combination of plan-then-generate scaffolding, prompt repetition, multi-agent architectures, and aggressive context engineering can restore near-full quality even for 10,000+ word outputs, as demonstrated by systems like LongWriter-Zero achieving state-of-the-art scores on long-form writing benchmarks. This report synthesizes the latest academic research, platform documentation, and practitioner techniques for maintaining generation quality at scale.

## The mechanics of quality collapse in autoregressive generation

Understanding *why* LLMs degrade is essential to fixing the problem. Research from 2024–2026 has identified five distinct failure mechanisms that compound during long-form generation.

**Positional attention bias** is the most studied. The seminal "Lost in the Middle" paper (Liu et al., TACL 2024, Stanford) showed a **30%+ accuracy drop** when relevant information sits in the middle of context versus the beginning or end. Follow-up work from MIT (Wu et al., ICML 2025) proved this is architectural — causal masking inherently biases models toward early tokens, and the effect *amplifies* with additional attention layers. A complementary study (PINE, ICLR 2025) showed that causal attention favors distant content while RoPE favors nearby content, creating the characteristic U-shaped curve.

**Heavy hitter deviation** during long decoding is a less appreciated but critical phenomenon. The SCOPE framework (ACL 2025 Oral) found that during extended generation, the tokens the model attends to shift significantly — they increasingly originate from the model's own recent output rather than the original input context. In other words, during long generation, **the model progressively forgets its instructions and starts attending primarily to its own recent text**. This is the mechanistic explanation for the "compression default" and instruction drift that practitioners observe.

**Training data bottlenecks** impose a hard ceiling on output length. Tsinghua's LongWriter research (ICLR 2025) demonstrated through controlled experiments that a model's effective maximum generation length is bounded by the longest outputs in its supervised fine-tuning data. When SFT data was filtered to outputs under 2,000 words, the model couldn't generate beyond ~1,800 words regardless of instructions. Most frontier models are fine-tuned on data where outputs rarely exceed 2,000 words, explaining the persistent compression tendency.

**Context rot accumulates non-linearly.** Testing by Demiliani (November 2025) showed GPT-5 maintaining excellent performance up to 300K characters, then degrading erratically at higher lengths, with a practical limit of ~171K tokens — significantly below its theoretical 200K limit. The HelloBench evaluation (September 2024) found that most LLMs, including GPT-4o and Claude 3.5 Sonnet, cannot generate text longer than **4,000 words** regardless of instructions, and those that can exhibit severe repetition. Perhaps most strikingly, a 2025 EMNLP paper showed that even when models perfectly retrieve all relevant information, performance still degrades **13.9%–85%** as input length increases — sheer length alone hurts performance independent of retrieval quality.

**Reasoning depth also shortens.** A 2026 paper ("Reasoning Shift," arXiv:2604.01161) found that longer input contexts cause models to produce shorter reasoning traces, with the probability of skipping self-checks rising from 57% at baseline to **68%** for long inputs. Context length silently degrades not just output quality but the depth of internal deliberation.

## Plan-generate-revise: the dominant scaffolding paradigm

Nearly all successful long-form generation systems converge on a common architecture: create a structured plan, generate sections guided by that plan, then revise. The evidence strongly favors this over single-pass generation.

**AgentWrite** (LongWriter, ICLR 2025) decomposes ultra-long generation into a planning phase followed by sequential section writing, enabling coherent outputs exceeding 20,000 words. The companion LongWriter-6k dataset — 6,000 SFT samples with 2K–32K word outputs — demonstrated that a 9B parameter model trained on these examples could match GPT-4o quality on long-form tasks. The key insight: plan-based generation consistently outperforms direct generation for any output exceeding ~2,000 words.

**LongWriter-Zero** (June 2025) pushed further, using pure reinforcement learning without synthetic data to develop ultra-long generation capabilities. Built on Qwen2.5-32B, it uses specialized reward models targeting length control, writing quality, and structural formatting. Its critical innovation: having the model *think before writing* — intermediate reasoning steps before prose generation — leads to dramatically better structure and quality control. It achieved **state-of-the-art** on WritingBench (8.69 vs GPT-4o's 8.16) and win rates up to 98.2% in human evaluations.

Stanford's **STORM** system (NAACL 2024) applies multi-perspective research before generation: it discovers diverse viewpoints, simulates expert conversations from each perspective, curates an outline from collected information, then populates sections with citations. Wikipedia editors judged STORM articles as **25% more organized** and **10% broader** in coverage than baseline approaches. The Writing Path framework (NAACL 2025 Industry) showed that explicit outline augmentation via LLM feedback before generation produced "significant performance gains across all evaluated models" on 1,500 blog posts.

**CogWriter** (February 2025) formalized this as a cognitive paradigm: planning, monitoring, and revision agents that mirror human writing processes. Its key finding is that left-to-right single-pass generation is *fundamentally limited* because LLMs lack built-in monitoring to check progress against intended goals. Without external monitoring, content drift, style inconsistency, and repetition accumulate unchecked.

For creative long-form work, **RecurrentGPT** (2023) simulates RNN-style recurrence using natural language: at each paragraph, it consults a plan, a short-term memory (recent paragraph summary), and a long-term memory (semantic search over all previous content stored externally). Human evaluators preferred its output over competing systems, with advantages growing for longer texts.

## Prompt-level techniques that actually work

Several prompt engineering techniques have strong empirical support for combating quality degradation.

**Prompt repetition** is the simplest and most surprising. Research by Leviathan et al. (December 2025) showed that simply repeating the input prompt twice improves non-reasoning LLM performance by up to **76%** with zero latency cost (since prefill is parallelized). The mechanism is straightforward: due to causal attention, tokens at the beginning of a prompt receive less attention from later processing; a second copy gives the model a fresh chance to attend. This works across Gemini, GPT, Claude, and DeepSeek models, though it does *not* help reasoning models (which naturally restate premises in their thinking traces). For long-form generation, repeating system-level instructions is essentially free insurance against instruction drift.

**Instruction placement** matters enormously. Anthropic's documentation recommends placing long data at the top of prompts with queries and instructions at the end, reporting up to **30% quality improvement** from this arrangement alone. This exploits the recency end of the U-shaped attention curve. For multi-section generation, the practical recommendation is to re-include the full system prompt plus key constraints at each section-generation call, ensuring instructions are always "fresh" in the model's attention.

**Structured formatting with XML tags** helps the model parse complex, multi-part prompts. Anthropic recommends wrapping each document in `<document>` tags with content and source subtags. OpenAI similarly advocates clear delimiters (Markdown headers, XML tags) to separate instructions from context from examples. For long-form output, explicitly requesting the model to *quote relevant parts of source documents before generating* helps it cut through noise — a technique Anthropic calls "grounding responses in quotes."

**Explicit verbosity and completeness directives** are necessary for newer models. Claude 4.x and GPT-5.x documentation both note that these models default toward concision. Anthropic recommends explicit instructions like "This is a very long task, so plan clearly. Spend your entire output context working on the task" and "Include as many relevant features as possible. Go beyond the basics." OpenAI's GPT-5.2 guide similarly recommends articulating verbosity preferences explicitly.

**Few-shot examples** remain the single highest-impact prompting technique across community consensus. Providing 3–5 diverse, high-quality examples of the desired output format and detail level anchors the model's behavior throughout generation. For long documents, including a complete section example that demonstrates the expected depth and style is more effective than verbal instructions alone.

## Multi-agent architectures deliver 90% improvements

Multi-agent decomposition has emerged as the most effective architecture for book-length generation. Chroma's research found multi-agent approaches deliver a **90.2% improvement** over single-agent approaches for complex long-form tasks.

The pattern is consistent across implementations. A planning agent creates structure. Writing agents generate individual sections with full context about the overall plan and summaries of adjacent sections. Critic agents evaluate output quality, checking for consistency, instruction adherence, and repetition. A revision agent incorporates feedback. This mirrors the CogWriter cognitive paradigm but distributes it across specialized models.

Production systems validate this approach. The **Claude Book** framework (HackerNoon, January 2026) uses Claude Code with subagents for consistency checking and a **perplexity gate** — sections with unusually high perplexity (indicating "AI slop" or repetitive patterns) trigger automatic rewriting. **Laterpress** implements "chained agents" where each chapter's agent knows the full content of all previous chapters. **NovelCrafter** maintains a codex of characters, locations, and lore that gets injected into each generation call. One practitioner produced a **301,000-word novel** over 8 months using a 56,000+ word "story bible" that Claude referenced continuously.

Anthropic's own documentation endorses multi-context-window workflows for complex long tasks: use the first context window to set up framework (write tests, create verification scripts), then iterate across future windows with the model discovering state from the filesystem rather than relying on context memory. Their **Advisor tool** pairs a fast executor model with a higher-intelligence advisor model for strategic guidance mid-generation, achieving near-advisor quality at executor token rates.

Automated workflow discovery is also advancing. **AFLOW** (ICLR 2025 Oral) uses Monte Carlo Tree Search to discover optimal multi-agent workflows, achieving a 5.7% improvement over state-of-the-art baselines and enabling smaller models to outperform GPT-4o on specific tasks at **4.55% of inference cost**.

## Inference-time interventions for generation quality control

Several inference-time techniques directly address quality degradation during decoding.

**Min-P sampling** (ICLR 2025 Oral, ranked 18th highest) has become the default sampling strategy for open-source deployments. It sets a minimum probability threshold relative to the top token's probability: when the model is confident, Min-P demands high quality from every candidate; when uncertain, it allows more variety. Min-P values of 0.05–0.1 consistently outperform Top-P, particularly at higher temperatures. It is now the default in llama.cpp, vLLM, HuggingFace Transformers, and Ollama.

**Selective Sampling** (2025, under COLM review) dynamically switches between greedy and high-temperature sampling based on a learned "sampling risk" metric, balancing quality and diversity at each token position with minimal latency overhead.

**The DRY (Don't Repeat Yourself) algorithm** in llama.cpp monitors recent context for repeated patterns and suppresses tokens that would continue repetition, operating at a higher level than simple frequency penalties. For mechanistic interpretability approaches, the **"Duplicatus Charm" method** (2025) uses Sparse Autoencoders to identify and deactivate specific "Repetition Features" in model activations, effectively eliminating repetitive output at both token and paragraph levels.

**Constrained decoding** is now production-ready for structured long documents. The Outlines library uses finite state machines compiled from schemas to mask invalid tokens at each generation step with O(1) average overhead. **DOMINO** (ICML 2024) achieves subword-aligned constraint enforcement with speculative decoding, sometimes *faster* than unconstrained generation. **IterGen** (ICLR 2025) introduces semantic backtracking — when the model produces suboptimal structured output, it can backtrack just that portion using KV-cache reuse rather than regenerating everything.

For KV cache management during long generation, **SCOPE** (ACL 2025) separately optimizes prefill and decoding phase caches, using a sliding window strategy for the decoding phase to prevent heavy hitter deviation. **LASER-KV** (February 2026) combines attention scores with Locality Sensitive Hashing to maintain stability up to 128K tokens, where standard compression methods degrade 15–30%.

## The self-evaluation loop: critic models and iterative refinement

Post-generation quality control closes the remaining gap. **Self-Refine** (Madaan et al., NeurIPS 2023) established the generate → critique → revise loop, improving outputs by ~20% absolute across 7 tasks with up to 4 iterations. **CRITIC** (2023–2024) extends this with external tool verification (calculators, search engines, code executors), demonstrating that external feedback consistently outperforms pure self-assessment.

A more sophisticated variant is **Method Iteration** (2025): instead of critiquing the output, the model critiques and improves the *procedure* it uses to generate output. Each loop upgrades the "generator of plans" rather than editing individual plans, compounding improvements across iterations. Practitioners report that 5–10 loops shift the model into genuinely creative territory.

For evaluation, **LongGenBench** (ICLR 2025) introduced "Reversed Needle in a Haystack" testing — placing specific constraints at designated positions within long outputs and checking adherence. It confirmed that all 10 tested state-of-the-art LLMs show significant degradation in instruction-following as output length increases. **Long-Form RewardBench** (2026) specifically evaluates reward models on long-form tasks, addressing a critical gap for RL-based training approaches.

## A practical playbook for 10,000+ word generation

Synthesizing across all research, these are the highest-impact interventions ranked by evidence strength and practical accessibility:

- **Decompose into planned sections.** Generate an outline first, then produce each section in a separate API call with full instruction context re-injected. This is the single most important technique and is supported by LongWriter, STORM, Writing Path, CogWriter, and every production long-form system.

- **Repeat critical instructions at both the beginning and end of each prompt,** and re-include the full system prompt at each section boundary. Prompt repetition alone improves quality up to 76% for non-reasoning models at zero latency cost.

- **Maintain an external "state document"** — a structured record of characters, facts, constraints, style requirements, and summaries of completed sections. Inject the relevant portions into each generation call rather than relying on the model to remember across a growing context.

- **Use multi-agent architectures for anything exceeding ~8,000 words.** Dedicated planning, writing, and critic agents outperform single-agent approaches by 90%+. Include a perplexity gate or quality classifier to catch degraded sections automatically.

- **Minimize context noise aggressively.** Signal-to-noise ratio determines output quality more than context capacity. Every irrelevant token draws from a finite attention budget. Remove exploration artifacts, failed outputs, and redundant information before each generation call.

## Conclusion

The research landscape from 2024–2026 has transformed long-form LLM generation from a mostly unsolved problem to a tractable engineering challenge. The root causes are now well understood: positional attention bias, heavy hitter deviation during autoregressive decoding, and training data scarcity for long outputs. The most impactful finding is that **the compression default is primarily a training data problem, not an architectural limitation** — LongWriter-Zero proved that RL alone can unlock 10,000+ word generation with state-of-the-art quality from a base model with no long-output training data.

For practitioners, the convergence of evidence points to a clear hierarchy of interventions: plan-then-generate scaffolding is non-negotiable for any output exceeding 2,000 words; instruction repetition and context engineering offer outsized returns for minimal effort; multi-agent architectures are necessary for book-length work; and inference-time techniques like Min-P sampling and constrained decoding provide useful quality floors. The critical shift in framing is from "context capacity" to "context engineering" — the question is not how many tokens a model can process, but how to curate the smallest set of high-signal tokens that keep the model on task throughout generation.