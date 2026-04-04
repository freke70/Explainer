# Gap Research: Logic Cage Architecture, Decision Heuristics & Adaptive Expert Reasoning

## Purpose
This document fills the gaps identified in the three existing deep research documents (1.md, 2.md, Architecting...). Those covered the cognitive science (what makes summaries work). This covers the **engineering layer**: how to encode that knowledge into a system prompt that reasons from principles rather than follows rules.

---

## PART 1: The Logic Cage — Making LLMs Reason From Principles

### The Core Problem: Soldiers vs. Thinkers

A rigid system prompt produces a "soldier" — an LLM that pattern-matches instructions and applies them mechanically. When it encounters a situation not covered by its rules, it either fails silently or hallucinates an answer. A logic cage produces a "thinker" — an LLM that has internalized the *paradigms* behind the rules and can reason about novel situations the way an expert would.

The difference:

| Rigid (Soldier) | Logic Cage (Thinker) |
|---|---|
| "Always use bullet points for definitions" | "Definitions serve the Remember level of Bloom's. At this level, discrete atomic structures (bullets, flashcard prompts) minimize cognitive load. But if the exam tests Understanding, definitions need causal context — so embed the 'why' alongside the 'what'." |
| "Include 3 examples per concept" | "Examples serve dual coding (verbal + concrete) and combat the abstraction problem. Include examples when the concept is abstract or the learner is a novice. For experts, examples become redundant (expertise reversal effect) — offer compressed references instead." |
| "Use a matrix for comparisons" | "A matrix forces relational reasoning across standardized variables. Use it when the knowledge structure is attribute-based (diseases × symptoms, theories × properties). If the relationships are causal/sequential rather than attribute-based, a flowchart or concept map better preserves the logical architecture." |

### Technique 1: Deliberative Alignment (OpenAI, arxiv 2412.16339)

**What it is:** A training paradigm where the model is taught the *text* of its governing principles and trained to explicitly reason through them in chain-of-thought before producing output.

**Key mechanism:** Rather than the model inferring rules indirectly from labeled examples (pattern-matching), it memorizes the principles in its CoT and learns how to *apply* them in context. The CoT is directly optimized during training.

**How it works at inference:**
1. Model receives a prompt
2. In its chain-of-thought, it *recalls* relevant principles from memory
3. It *reasons through* how those principles apply to this specific situation
4. It produces output grounded in that reasoning

**Example reasoning chain (adapted for summarization):**
> "The user has provided a dense pharmacology chapter and asked for an exam summary. Let me reason through my principles:
> - Cognitive Load Theory: pharmacology has high intrinsic load (many interacting elements). I must aggressively minimize extraneous load.
> - Discipline epistemology: medical content demands illness scripts and differential matrices, not narrative outlines.
> - Bloom's alignment: pharmacy exams typically test Apply (drug selection) and Analyze (drug interactions). I need decision trees and comparison matrices, not just definitions.
> - Expertise assessment: the user hasn't indicated their level. I'll include a hierarchical structure that works for both — definitions first (Remember), then mechanism groupings (Understand), then clinical decision cues (Apply).
> Therefore: I'll use a matrix (drugs × mechanisms × indications × contraindications) plus a brief mechanism narrative for each drug class."

**How to encode this in a system prompt:** Give the LLM the principles as named mental models it must reason through, not as output rules. The prompt says "before generating, reason through these frameworks" rather than "follow these formatting rules."

**Source:** [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339)

---

### Technique 2: MeMo — Mental Models for Generalist Prompting (arxiv 2402.18252)

**What it is:** Instead of prescribing specific prompting methods per task, MeMo gives the LLM a *library of mental models* and lets it autonomously select which to apply.

**Mental models provided:**
- First principles thinking
- Inversion (reason backwards from the goal)
- Analogy (map structure from familiar to unfamiliar domain)
- Cause-and-effect analysis
- Abstraction (find the general principle behind specifics)
- Domain-specific conceptual frameworks

**Selection mechanism:** Zero-shot — the LLM is given definitions of mental models + examples showing how to identify applicable ones, then it autonomously selects based on problem context. No manual specification needed.

**Key insight for logic cage design:** Rather than telling the LLM "use a matrix here," give it the *cognitive science mental models* (CLT, schema theory, Bloom's, transfer-appropriate processing) and let it *derive* the right format. The LLM already has latent knowledge of these frameworks — the prompt activates and structures that knowledge.

**Prompt structure:**
1. **Definition layer:** "You have internalized these cognitive science paradigms: [list with descriptions]"
2. **Example layer:** Show 2-3 examples of how an expert reasons through these paradigms to make design choices
3. **Autonomy layer:** "For each summarization task, reason through the applicable paradigms to determine structure, density, and format."

**Source:** [Towards Generalist Prompting for Large Language Models by Mental Models](https://arxiv.org/abs/2402.18252)

---

### Technique 3: Fuzzy Logic Prompting — Two-Layer Architecture (arxiv 2508.06754)

**What it is:** A prompt architecture with an outer natural-language boundary and an inner structured control schema that enables adaptive behavior without fine-tuning.

**Architecture:**

**Outer Layer (Boundary Prompt):** Natural language defining identity, pedagogical intent, and adaptation policy. This is the "who you are and why" layer.

**Inner Layer (Control Schema):** A structured (JSON-like) schema encoding:
- **Knowledge level bands:** emerging → developing → proficient → advanced (with signal indicators like "I'm not sure" mapping to emerging)
- **Task type classifications:** recall, comprehension, application, analysis, evaluation
- **Scaffolding intensity rules:** high support = task breakdown + guided examples; low support = hints + challenge questions
- **Adaptation rules:** how to shift support based on learner signals across dialogue turns

**Key insight for logic cage:** The outer layer provides the *paradigmatic identity* (the LLM understands why it does what it does). The inner layer provides *graduated decision parameters* (not binary rules but continua). The LLM treats instruction as a spectrum, not a checklist.

**How it modulates behavior:** At inference, the model:
1. Parses user context via boundary instructions
2. Queries the control schema to determine task type and support requirements
3. Adapts tone, vocabulary, structure, and follow-up dynamically
4. Selects appropriate scaffolding based on learner state signals

**Source:** [A Fuzzy Logic Prompting Framework for LLMs in Adaptive and Uncertain Tasks](https://arxiv.org/abs/2508.06754)

---

### Technique 4: Meta-Reasoning Prompting — Dynamic Strategy Selection (arxiv 2406.11698)

**What it is:** Rather than applying one reasoning method to all tasks, MRP enables LLMs to dynamically select and apply different reasoning methods based on specific task requirements.

**Mechanism:** Mirrors human meta-cognition — monitoring and regulating reasoning activities, adjusting strategies based on context. The LLM reasons about *how to reason* before reasoning about the problem.

**Application to summarization:** The LLM doesn't apply a fixed summarization template. It first reasons: "What kind of knowledge is this? What kind of exam is it for? What kind of learner is asking? What cognitive level is targeted?" — and *then* selects the appropriate summarization strategy.

**Source:** [Meta Reasoning for Large Language Models](https://arxiv.org/abs/2406.11698)

---

### Technique 5: Adaptive Scaffolding Theory for LLM Pedagogical Agents (arxiv 2508.01503)

**What it is:** A theoretical framework integrating Evidence-Centered Design, Social Cognitive Theory, and ZPD for LLM-based tutoring.

**Key principles:**
- **Theory-driven design over rigid responses:** Ground feedback in learning science, not generic LLM patterns
- **Evidence-informed adaptation:** Continuous dialogue updates understanding; scaffolding is responsive, not predetermined
- **Fading:** Support diminishes as competence grows — the same summary tool should behave differently for a novice vs. an expert
- **Assessment → Adaptation loop:** At each turn, update the learner model, refine the next response

**Source:** [A Theory of Adaptive Scaffolding for LLM-Based Pedagogical Agents](https://arxiv.org/abs/2508.01503)

---

### Synthesis: The Logic Cage Prompt Architecture

Combining these techniques, the logic cage has three layers:

```
Layer 1: PARADIGMATIC IDENTITY (from Deliberative Alignment + MeMo)
  → The LLM internalizes cognitive science paradigms as its "constitution"
  → It reasons through these paradigms before every output
  → It can articulate WHY it made every design choice

Layer 2: ADAPTIVE CONTROL (from Fuzzy Logic Framework + Adaptive Scaffolding)
  → Graduated parameters (not binary rules) for learner level, task type, discipline
  → Continuous adaptation based on context signals
  → Scaffolding that fades with expertise

Layer 3: META-REASONING (from MRP + Meta-Prompting)
  → The LLM reasons about HOW to reason before reasoning about the problem
  → Autonomous selection of summarization strategy
  → Self-monitoring: "Am I being a soldier or a thinker right now?"
```

---

## PART 2: Decision Heuristics — The Expert's Reasoning Chain

### How Expert Educators Actually Decide (from Tutoring Research)

Expert tutors use a 5-phase decision process (synthesized from Chi, VanLehn, Graesser, Shulman, Kalyuga):

#### Phase 1: ASSESS — Build a Learner Model
- What does this learner already know? (Prior knowledge)
- What can they do independently vs. with help? (ZPD)
- What misconceptions are active? (Error patterns)
- What is their expertise level? (For expertise reversal calibration)
- What are their goals? (Exam type, learning objectives)

#### Phase 2: DECOMPOSE — Knowledge Component Analysis
- What are the target knowledge components?
- What are the prerequisite relationships?
- Which missing components are highest-leverage (unblock the most)?
- Are there bottleneck misconceptions that corrupt new learning?

#### Phase 3: DESIGN — Pedagogical Content Knowledge
- What representation makes this concept accessible given the learner's prior knowledge?
- What level of detail is appropriate? (Novice = worked examples; expert = summary)
- How much scaffolding vs. how much for the learner to construct?
- What misconceptions might the chosen representation introduce?
- What sequence — what comes first, what builds on what?

#### Phase 4: CALIBRATE — Trade-off Navigation
Five key trade-offs experts navigate:

| Trade-off | Expert Resolution |
|---|---|
| **Coverage vs. Depth** | Identify 2-3 threshold concepts and invest deeply. Lighter coverage of supporting material. |
| **Simplification vs. Accuracy** | Use "productive simplifications" correct at the current level. Signal boundaries: "At this level, think of it as X." |
| **Support vs. Desirable Difficulty** | Target the ZPD: effortful but achievable. Bjork's "desirable difficulties." |
| **Telling vs. Eliciting** | New information → tell. Student has enough to construct → elicit. ICAP: constructive > active > passive. |
| **Consistency vs. Multiple Representations** | Start with one clear representation. Once established, introduce alternatives and explicitly map between them. |

#### Phase 5: MONITOR — Dynamic Adaptation
- How is the learner responding?
- Increase or decrease scaffolding?
- Back up to a prerequisite that's missing?
- Time to fade support and push toward independence?

---

### When to Use Which Summary Format

This is the practical decision tree the existing research was missing:

#### Format Selection Based on Knowledge Structure

```
What is the dominant knowledge structure of the content?

├─ ATTRIBUTE-BASED (things have comparable properties)
│  → Use MATRIX / COMPARISON TABLE
│  Examples: drug classes × mechanisms × side effects,
│           historical events × causes × consequences,
│           theories × assumptions × predictions
│  Why: Forces relational reasoning across standardized variables.
│       Instantly surfaces similarities, differences, and gaps.
│
├─ SEQUENTIAL / PROCEDURAL (steps in order, decisions in sequence)
│  → Use FLOWCHART / DECISION TREE
│  Examples: diagnostic algorithms, legal tests with branching conditions,
│           experimental procedures, mathematical problem-solving strategies
│  Why: Preserves the logical flow. Makes conditions and branches explicit.
│       Essential for Apply-level Bloom's objectives.
│
├─ CAUSAL / SYSTEMIC (things cause or influence each other in networks)
│  → Use CONCEPT MAP
│  Examples: biological pathways, economic systems, feedback loops,
│           engineering systems, ecological relationships
│  Why: Makes non-linear relationships visible. Forces learner to
│       articulate the exact nature of each relationship.
│       Essential for systems thinking.
│
├─ HIERARCHICAL / TAXONOMIC (categories and subcategories)
│  → Use HIERARCHICAL OUTLINE / TREE
│  Examples: biological classification, legal doctrine hierarchy,
│           organizational structures, concept taxonomies
│  Why: Implements chunking directly. Aligns with schema theory.
│       Makes macrostructure instantly legible.
│
├─ ARGUMENTATIVE (claims, evidence, reasoning, counter-arguments)
│  → Use CORNELL-STYLE or QEC (Question-Evidence-Conclusion)
│  Examples: philosophical arguments, historical interpretations,
│           legal reasoning, policy debates, literary analysis
│  Why: Preserves the logical architecture of arguments.
│       Supports evaluation-level Bloom's objectives.
│
└─ NARRATIVE / CHRONOLOGICAL (events unfolding over time)
   → Use TIMELINE + NARRATIVE OUTLINE
   Examples: historical periods, case studies, biographical studies,
            disease progression
   Why: Preserves temporal and causal ordering.
        Supports contextual understanding.
```

#### Format Selection Based on Bloom's Level Target

```
What cognitive level does the exam primarily test?

├─ REMEMBER → Flashcard prompts, glossary lists, mnemonic devices
│  Atomic, discrete, high retrieval-cue density
│
├─ UNDERSTAND → Narrative paragraphs with "because/therefore" connectors,
│  Feynman-style simplified explanations, analogies
│
├─ APPLY → Worked examples, step-by-step procedures, if-then decision trees,
│  condition-action pairs, "when to use" discriminations
│
├─ ANALYZE → Concept maps, synthesis matrices, causal chain diagrams,
│  evidence-vs-conclusion separations
│
├─ EVALUATE → Pro/con tables, criteria checklists, methodological critiques,
│  multi-perspective comparisons
│
└─ CREATE → Gap identification prompts, open-ended synthesis questions,
   hypothesis generation scaffolds
```

#### Density Calibration Based on Learner Level

```
What is the learner's expertise level?

├─ NOVICE
│  → Lower density, higher scaffolding
│  → Worked examples over problem sets
│  → Explicit hierarchical structure with clear signposting
│  → More concrete examples, fewer abstract principles
│  → Integration of definitions within context (not assumed)
│
├─ INTERMEDIATE
│  → Moderate density, fading scaffolding
│  → Faded worked examples (some steps, some blanks)
│  → Structure present but less hand-holding
│  → Balance of concrete and abstract
│  → Retrieval cues and self-test prompts
│
└─ ADVANCED / EXPERT
   → Higher density, minimal scaffolding
   → Compressed references, not full explanations
   → Relational density can be high (many connections per concept)
   → Focus on edge cases, exceptions, boundary conditions
   → Challenge questions over guided examples
   → WARNING: Detailed explanations become HARMFUL (expertise reversal)
```

---

## PART 3: The Anti-Soldier Mechanism — Encoding Self-Monitoring

### The Meta-Cognitive Layer

The logic cage must include a self-monitoring mechanism — the LLM equivalent of an expert's metacognition. This prevents regression to mechanical rule-following.

**Anti-patterns the LLM must catch in itself:**

1. **"Am I copying the source structure?"** — If the summary mirrors the original document's organization rather than reorganizing around the learner's cognitive needs, it's failing at macrostructure extraction.

2. **"Am I applying the same format regardless of content?"** — If every summary looks the same (always bullets, always matrices, always the same density), the system is being a soldier, not reasoning about the material.

3. **"Am I optimizing for coverage or for retrieval?"** — If the summary tries to include everything rather than optimizing for the likely exam format, it's failing at transfer-appropriate processing.

4. **"Am I making this easy to read or easy to learn from?"** — These are different. Easy-to-read summaries can create illusions of fluency. Effective summaries create desirable difficulties.

5. **"Would this help a student pass the exam, or just feel prepared?"** — The distinction between recognition (passive familiarity) and recall (active retrieval). The summary must be a testing interface, not a comfort object.

6. **"Am I explaining at the right level, or at the level I default to?"** — The expertise reversal check. A novice needs worked examples; an expert needs compressed references. The same content, radically different treatment.

---

## PART 4: Key Sources

### Logic Cage & Prompt Architecture
- [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339) — OpenAI, Dec 2024
- [MeMo: Towards Generalist Prompting for LLMs by Mental Models](https://arxiv.org/abs/2402.18252) — Feb 2024
- [Fuzzy Logic Prompting Framework for LLMs in Adaptive Tasks](https://arxiv.org/abs/2508.06754) — Aug 2025
- [Meta Reasoning for Large Language Models](https://arxiv.org/abs/2406.11698) — Jun 2024
- [Meta-Prompting: Enhancing LMs with Task-Agnostic Scaffolding](https://arxiv.org/abs/2401.12954) — Jan 2024
- [Adaptive Scaffolding Theory for LLM Pedagogical Agents](https://arxiv.org/abs/2508.01503) — Aug 2025
- [Fuzzy, Symbolic, and Contextual: Enhancing LLM Instruction via Cognitive Scaffolding](https://arxiv.org/abs/2508.21204) — Aug 2025

### Expert Tutoring & Decision Heuristics
- Chi, M.T.H. (2009). Active-Constructive-Interactive: ICAP framework. *Topics in Cognitive Science.*
- VanLehn, K. (2006). The behavior of tutoring systems. *Int. J. of AI in Education.* (Inner/outer loop architecture)
- Graesser, A.C., Person, N.K., & Magliano, J.P. (1995). Collaborative dialogue patterns in naturalistic tutoring. *Applied Cognitive Psychology.*
- Shulman, L.S. (1986). Those who understand: Knowledge growth in teaching. *Educational Researcher.* (PCK framework)
- Kalyuga, S. (2007). Expertise reversal effect. *Educational Psychology Review.*
- Koedinger, K.R., Corbett, A.T., & Perfetti, C. (2012). Knowledge-Learning-Instruction framework. *Cognitive Science.* (Knowledge component analysis)
- Meyer, J.H.F. & Land, R. (2003). Threshold concepts and troublesome knowledge.
- Bjork, R.A. (1994). Desirable difficulties. In *Metacognition: Knowing about knowing.*

### Representation Selection
- [Concept Maps – UNC Learning Center](https://learningcenter.unc.edu/tips-and-tools/using-concept-maps/)
- [Mind maps, concept maps, system-diagrams, decision trees and flowcharts](https://www.kontextlab.com/en/mind-maps-concept-maps-system-diagrams-decision-trees-and-flowcharts-whats-what/)
- Kauffman & Kiewra — empirical work on why matrices work (signaling, extraction, localization)
