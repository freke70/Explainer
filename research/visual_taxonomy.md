# Visual Diagram Taxonomy: Mapping Knowledge Structures to Visual Types

## Purpose

This document provides a practical decision framework for selecting the right visual diagram type when generating educational visuals for AI study summaries. It answers: given a knowledge structure identified during the diagnosis phase and a target Bloom's level, which visual diagram type should be generated, how should it be designed, and is it feasible for AI image generation or better served as text/ASCII?

This framework is designed to work directly with the knowledge structures and discipline epistemologies defined in the system prompt (`prompts/samenvatting.md`) and the cognitive science foundations in the research documents.

---

## Part 1: Knowledge Structure to Visual Type Mapping

Each knowledge structure has visual types that naturally preserve its relational architecture. The goal is not decoration — it is making the invisible structure of the knowledge visible so the learner's working memory can process it as organized chunks rather than isolated elements.

### 1. Causal Chains (X causes Y, which enables Z)

**Best visual types:**
- **Flowchart (horizontal or vertical)** — The primary choice. Nodes represent events or states; directed arrows represent causal links. Labels on arrows ("causes," "enables," "inhibits") make the causal grammar explicit. The sequential left-to-right or top-to-bottom flow matches how the brain processes cause-and-effect.
- **Process diagram with annotations** — When the causal chain involves transformation (e.g., biochemical pathways, policy cascades), a process diagram with input/output labels at each stage preserves both the sequence and the mechanism at each step.
- **Concept map (directed)** — When causal chains branch or converge (multiple causes leading to one effect, or one cause producing multiple effects), a concept map with labeled relationship arrows captures the network structure that a linear flowchart cannot.

**Avoid:** Venn diagrams (no causal directionality), matrices (causal chains are sequential, not attribute-based), mind maps (no directional relationships).

### 2. Comparative Structures (X and Y share A/B, differ on C/D)

**Best visual types:**
- **Matrix/comparison table** — The dominant choice. Rows represent the items being compared; columns represent the dimensions of comparison. This format forces relational reasoning by spatially aligning attributes, making similarities and differences instantly visible. The matrix is the native structure for discrimination tasks.
- **Venn diagram** — Effective when comparing exactly 2-3 items and the focus is on overlap vs. distinction. Works well when the shared properties are as important as the differences. Becomes unreadable with 4+ items.
- **Parallel flowcharts / side-by-side diagrams** — When compared items are processes rather than entities (e.g., comparing two diagnostic pathways or two legislative procedures), placing flowcharts side by side with aligned stages makes structural parallels and divergences visible.

**Avoid:** Mind maps (no comparative alignment), timelines (unless the comparison is temporal), tree diagrams (hierarchical, not comparative).

### 3. Hierarchical/Taxonomic (X is a type of Y, which belongs to Z)

**Best visual types:**
- **Tree diagram** — The canonical choice. Parent-child relationships map directly to branches. The visual hierarchy mirrors the conceptual hierarchy — superordinate categories at the top, subordinate instances at the bottom. This is the most cognitively natural representation for classification knowledge.
- **Layer/tier diagram** — When the hierarchy represents levels of abstraction, containment, or scope (e.g., ecological levels: organism > population > community > ecosystem), stacked horizontal layers convey the nesting relationship more effectively than a branching tree.
- **Indented outline (structured text)** — For deep hierarchies with many terminal nodes (e.g., drug classification taxonomies with 50+ items), a text-based indented outline is more space-efficient and scannable than a visual tree that would require enormous canvas size.

**Avoid:** Flowcharts (imply sequence, not classification), matrices (imply comparison, not inclusion), Venn diagrams (imply overlap, not subordination).

### 4. Procedural/Sequential (Step 1 > Step 2 > Step 3)

**Best visual types:**
- **Flowchart with decision diamonds** — The gold standard for procedures, especially when the procedure includes conditional branching (if-then logic). Decision nodes make branching conditions explicit, which is essential for Apply-level learning. Swimlane variants can show which actor or system is responsible at each step.
- **Numbered process diagram** — For strictly linear procedures without branching, a numbered step sequence with brief annotations at each step is cleaner than a full flowchart. Particularly effective for lab protocols, clinical procedures, or algorithmic steps.
- **Decision tree** — When the procedure is primarily about classification or triage through a series of binary decisions (e.g., diagnostic algorithms, legal test application), a decision tree makes the branching logic scannable.

**Avoid:** Mind maps (no sequence), Venn diagrams (no temporal order), matrices (procedures are sequential, not attribute-based).

### 5. Feedback Loops (X increases Y, which decreases X)

**Best visual types:**
- **Circular/loop diagram** — The defining visual. Nodes arranged in a circle or loop with arrows showing direction and polarity (+ for amplifying, - for inhibiting). The circular layout is a direct spatial metaphor for the conceptual loop, making the self-reinforcing or self-correcting nature of the system immediately visible.
- **Causal loop diagram (CLD)** — A more formal systems-thinking notation: variables connected by arrows marked with "+" (same direction) or "-" (opposite direction), with "R" (reinforcing) or "B" (balancing) labels on the loop itself. Used in systems dynamics and effective when multiple interlocking loops must be shown.
- **Stock-and-flow diagram** — When the feedback loop involves accumulation and depletion (e.g., population dynamics, resource management), stocks (rectangles) and flows (arrows with valves) add precision about what accumulates and what regulates the rate.

**Avoid:** Linear flowcharts (destroy the loop structure), matrices (no cyclical relationships), tree diagrams (no feedback).

### 6. Argumentative (Claim > Evidence > Warrant > Counterargument)

**Best visual types:**
- **Argument map / structured text diagram** — A top-down or left-to-right diagram where the main claim sits at the top, supporting evidence branches downward, warrants connect evidence to claims, and counterarguments appear as opposing branches (often color-coded or visually distinguished). This preserves the logical architecture of the argument.
- **Fishbone/Ishikawa diagram** — When analyzing the causes or factors supporting a conclusion (e.g., "Why did policy X fail?"), the fishbone structure organizes contributing factors into categories along the spine, with the conclusion at the head. Effective for root-cause analysis in both STEM and social science contexts.
- **Pro/con table or T-chart** — For binary evaluative arguments (should we / should we not; strengths vs. weaknesses), a simple two-column structure forces the learner to see both sides simultaneously.
- **QEC structured text** — For humanities arguments, a text-based Question-Evidence-Conclusion format often preserves nuance better than a visual diagram, which can oversimplify the rhetorical structure.

**Avoid:** Flowcharts (arguments are not sequential procedures), Venn diagrams (arguments are not about overlap), timelines (arguments are not chronological).

### 7. Chronological/Narrative (Events over time with causal connections)

**Best visual types:**
- **Timeline (horizontal)** — The primary choice. Events placed along a horizontal axis with labeled time markers. Annotations above or below the line explain causal connections between events. The spatial metaphor of left-to-right = earlier-to-later is deeply intuitive.
- **Annotated timeline with layers** — When multiple parallel threads unfold simultaneously (e.g., political events, economic developments, and cultural shifts during the same period), stacked timelines with vertical alignment of contemporaneous events show both sequence and context.
- **Flowchart with temporal axis** — When the narrative involves branching paths or alternative outcomes at key decision points, a flowchart overlaid on a timeline combines chronological and causal structure.

**Avoid:** Matrices (destroy temporal flow), tree diagrams (imply classification, not temporal sequence), Venn diagrams (no temporal dimension).

---

## Part 2: Design Principles That Make Visuals Effective vs. Ineffective

The cognitive science is clear: a visual diagram helps learning only if it reduces extraneous cognitive load and channels working memory toward schema construction. A poorly designed diagram adds load rather than reducing it.

### Principles That Make Visuals Effective

1. **Every element earns its place.** Every node, arrow, label, color, and shape must convey meaning. Decorative elements (drop shadows, 3D effects, clip art, gradient fills) add extraneous load without cognitive value. Clean, flat design is not an aesthetic preference — it is a cognitive load management decision.

2. **Labels carry the meaning.** Arrows without labels are ambiguous. A line connecting "poverty" to "crime" could mean "causes," "correlates with," "is often conflated with," or "is an argument against." The label is what makes the relationship explicit and forces the diagram creator to commit to a specific relational claim. For AI-generated educational diagrams, text labels are not optional — they are the primary mechanism of learning.

3. **Spatial layout encodes structure.** Top-to-bottom should mean superordinate-to-subordinate or cause-to-effect. Left-to-right should mean earlier-to-later or input-to-output. When spatial position is arbitrary, the diagram wastes the brain's spatial processing capacity on meaningless variation.

4. **Color is semantic, not decorative.** Color should encode categories, polarity (positive/negative), or urgency — never mere visual variety. Two items in the same color should share a meaningful property. Limit the palette to 3-5 semantically distinct colors to prevent overload.

5. **Hierarchy reduces complexity.** Complex systems should use progressive disclosure: a high-level overview diagram showing major components, with detail diagrams for subsystems. One diagram trying to show everything becomes the "spaghetti code" problem that makes concept maps fail at scale.

6. **Consistent visual grammar.** Within a single diagram and across a set of related diagrams, the same shape should always mean the same thing (e.g., rectangles = processes, diamonds = decisions, ovals = start/end states). Violating this forces the learner to re-decode the visual grammar at each node, wasting working memory.

### Principles That Make Visuals Ineffective

1. **Clutter and information overload.** More than 12-15 nodes in a single diagram overwhelms visual processing. If the content requires more, split into multiple diagrams with clear cross-references.

2. **Missing or ambiguous relationships.** Lines without labels, arrows without directionality, or nodes that are spatially close but not explicitly connected create false associations or missed connections.

3. **Inconsistent abstraction level.** Mixing high-level categories with granular details in the same visual layer makes it impossible to read the diagram at any single level of understanding.

4. **Text-heavy nodes that defeat the purpose.** If a node contains a full paragraph, the diagram has become a poorly formatted text document. Nodes should contain terms, short phrases, or at most one sentence. Extended explanation belongs in accompanying text, not inside the visual.

5. **Decorative complexity.** Three-dimensional rendering, photographic backgrounds, icon overuse, and fancy typography increase processing time without increasing comprehension.

---

## Part 3: Visual Types Mapped to Bloom's Levels

Different Bloom's levels demand different cognitive operations, and different visual types naturally support those operations.

### Remember (Retrieve facts, define terms)

**Best visuals:** Flashcard-style cue-response pairs (text-based), simple labeled diagrams with blanks for self-testing, glossary tables, mnemonic visuals (visual associations for arbitrary facts).

**Why:** At the Remember level, the task is retrieval of discrete items. Visuals should be atomic and high in cue density. Complex relational diagrams are overkill and add extraneous load for a task that only requires fact recognition/recall.

### Understand (Explain, classify, summarize)

**Best visuals:** Simple flowcharts (for "how" explanations), tree diagrams (for classification), annotated concept maps (for "why" connections), Venn diagrams (for basic comparison of 2 items), analogy diagrams (mapping source domain to target domain).

**Why:** Understanding requires the learner to construct meaning from relationships. Visuals that make relationships explicit — "X causes Y," "A is a type of B" — scaffold the shift from isolated facts to connected concepts.

### Apply (Use knowledge in new situations)

**Best visuals:** Decision trees (for conditional procedure application), flowcharts with decision diamonds (for algorithmic problem-solving), worked-example diagrams with blanks (for self-explanation), process diagrams (for procedure execution).

**Why:** Application requires the learner to execute procedures or apply rules to novel cases. Visuals must make conditions and branching logic explicit, because "when do I use which rule?" is the core cognitive challenge at this level.

### Analyze (Break down, compare, relate parts to wholes)

**Best visuals:** Comparison matrices (for systematic analysis across dimensions), concept maps (for mapping complex relationships), fishbone diagrams (for root-cause analysis), argument maps (for deconstructing reasoning), layer diagrams (for structural decomposition).

**Why:** Analysis requires decomposition and systematic comparison. Visuals must spatially separate components and make their relationships to each other and to the whole visible. This is where matrices and concept maps reach their peak utility.

### Evaluate (Judge, critique, assess against criteria)

**Best visuals:** Pro/con tables, criteria matrices (options vs. evaluation criteria with ratings), argument maps with counterargument branches, annotated comparison diagrams highlighting strengths and weaknesses.

**Why:** Evaluation requires weighing evidence against criteria and making justified judgments. The visual must present the criteria, the evidence, and the judgment in a structure that supports weighing — which is fundamentally a comparative/tabular operation.

---

## Part 4: Decision Framework — "If Structure is X and Bloom's Target is Y, Use Z"

### Quick-Reference Decision Table

| Knowledge Structure | Remember | Understand | Apply | Analyze | Evaluate |
|---|---|---|---|---|---|
| **Causal chain** | Labeled diagram with blanks | Simple flowchart with causal labels | Process diagram with worked example gaps | Concept map showing branching causes/effects | Annotated causal chain with critique prompts |
| **Comparative** | Flashcard pairs (A vs. B) | Venn diagram (2-3 items) | Side-by-side process comparison | Full comparison matrix | Criteria matrix with evaluative ratings |
| **Hierarchical** | Tree diagram with blanks | Tree diagram with relationship labels | Classification decision tree | Layer diagram with cross-references | Annotated taxonomy with critique of categories |
| **Procedural** | Numbered step list with blanks | Simple linear flowchart | Flowchart with decision diamonds and worked gaps | Swimlane flowchart showing system interactions | Process diagram with error/limitation annotations |
| **Feedback loop** | Labeled loop diagram with blanks | Circular diagram with +/- polarity labels | Causal loop with "what happens if X changes?" prompts | Multi-loop system diagram (CLDs) | Annotated loop with intervention point analysis |
| **Argumentative** | Claim-evidence flashcard pairs | Basic argument map (claim > evidence) | QEC structure with application prompts | Fishbone or full argument map with warrants | Pro/con table with criteria weighting |
| **Chronological** | Timeline with blanks | Annotated timeline with causal links | Timeline with "what if?" scenario branches | Multi-layer parallel timeline | Timeline with evaluative annotations at key events |

### Decision Flowchart (Text-Based)

```
START: What is the dominant knowledge structure?
|
|-- Causal chain?
|     |-- Is the chain linear (A > B > C)?
|     |     YES --> Flowchart
|     |     NO (branching/converging) --> Concept map
|     |-- Does the exam test Apply or higher?
|           YES --> Add decision diamonds / worked example gaps
|           NO  --> Keep labels simple, add blank nodes for retrieval practice
|
|-- Comparative?
|     |-- How many items being compared?
|     |     2-3 items --> Venn diagram (Understand) or matrix (Analyze)
|     |     4+ items  --> Matrix (always)
|     |-- Are the items processes or entities?
|           Processes --> Side-by-side flowcharts
|           Entities  --> Comparison matrix
|
|-- Hierarchical/taxonomic?
|     |-- Fewer than 15 terminal nodes?
|     |     YES --> Tree diagram
|     |     NO  --> Indented text outline (tree becomes unreadable)
|     |-- Does the exam test Apply?
|           YES --> Convert to classification decision tree
|           NO  --> Standard tree with labels
|
|-- Procedural/sequential?
|     |-- Does the procedure branch?
|     |     YES --> Flowchart with decision diamonds
|     |     NO  --> Numbered process diagram
|     |-- Multiple actors/systems involved?
|           YES --> Swimlane flowchart
|           NO  --> Standard flowchart
|
|-- Feedback loop?
|     |-- Single loop?
|     |     YES --> Circular loop diagram
|     |     NO (multiple interlocking loops) --> Causal loop diagram (CLD)
|     |-- Does the exam test Analyze or Evaluate?
|           YES --> Add intervention points and "what if?" annotations
|           NO  --> Keep polarity labels (+/-) only
|
|-- Argumentative?
|     |-- Is the argument binary (for/against)?
|     |     YES --> Pro/con table or T-chart
|     |     NO (multi-layered reasoning) --> Argument map
|     |-- Does the exam test Evaluate?
|           YES --> Add criteria weighting and counterargument branches
|           NO  --> Keep to claim-evidence structure
|
|-- Chronological/narrative?
|     |-- Single thread or parallel threads?
|     |     Single --> Horizontal timeline
|     |     Parallel --> Multi-layer timeline
|     |-- Are causal connections between events important?
|           YES --> Annotate causal arrows between events
|           NO  --> Simple date-event timeline
```

---

## Part 5: AI Image Generation Feasibility Assessment

The project uses Gemini's image generation model (`gemini-3.1-flash-image-preview`) for educational visuals. This model handles structured, text-label-heavy diagrams well when prompted with explicit spatial descriptions. However, not all diagram types are equally suited to AI generation.

### Well-Suited for AI Image Generation

These types have clean geometric structure, limited node count, and rely on labeled shapes and arrows — all of which current models handle reliably.

| Visual Type | Why It Works | Prompting Notes |
|---|---|---|
| **Flowchart** (linear, up to ~10 nodes) | Rectangles + arrows + text labels. Highly geometric and structured. | Specify orientation (vertical/horizontal), name every node and arrow label, specify color coding. |
| **Tree diagram** (up to ~15 nodes) | Parent-child branching is a well-understood visual pattern. | Specify depth levels, name every node, specify left-to-right or top-to-bottom layout. |
| **Timeline** (up to ~10 events) | Linear horizontal layout with labeled markers. | Specify direction (left = earliest), name every event and date, describe annotation placement (above/below line). |
| **Comparison matrix/table** (up to 6x6) | Grid structure with labeled headers and cell content. | Specify row and column headers, cell content, header shading, and font contrast. |
| **Circular loop diagram** (3-6 nodes) | Simple circular layout with directional arrows and polarity labels. | Specify clockwise/counterclockwise, name every node and arrow label, specify +/- polarity symbols. |
| **Layer/tier diagram** (3-5 layers) | Horizontal stacked rectangles with labels. | Specify layer order (top = most abstract), name every layer, specify color gradient if desired. |
| **Venn diagram** (2-3 circles) | Well-known geometric form. | Name every region (overlap and exclusive), specify labels clearly, limit to 2-3 circles maximum. |
| **Pro/con T-chart** | Two-column layout with header and bullet items. | Specify header labels, list items for each column, specify visual balance. |

### Marginal — Requires Careful Prompting

These types can work but risk visual clutter or text rendering issues at higher complexity.

| Visual Type | Risk Factor | Mitigation |
|---|---|---|
| **Concept map** (>8 nodes) | Crossing arrows, overlapping labels, unpredictable layout | Limit to 8-10 nodes. Specify spatial zones ("place X in top-left, Y in bottom-right"). Pre-plan the layout in the prompt. |
| **Decision tree** (>3 levels) | Deep branching produces tiny text or overlapping branches | Limit to 3 decision levels. For deeper trees, split into sub-diagrams. |
| **Swimlane flowchart** | Multiple parallel tracks with cross-lane arrows are complex | Limit to 2-3 lanes and 6-8 steps total. |
| **Fishbone diagram** | Diagonal lines and categorical branches can become messy | Limit to 4-5 main categories with 2-3 sub-items each. Be extremely explicit about bone angle and spacing. |

### Better as Text/ASCII or Markdown

These types are too complex, too nuanced, or too dependent on precise spatial relationships for current AI image generation to produce reliably.

| Visual Type | Why Text Is Better | Recommended Format |
|---|---|---|
| **Argument map** (multi-level) | Requires precise hierarchical layout with opposing branches, warrant links, and counterargument connections. AI generation tends to produce cluttered or misaligned results. | Markdown nested lists with indentation, or structured text using symbols (claim: > evidence: > warrant:). |
| **Causal loop diagram** (3+ interlocking loops) | Multiple overlapping cycles with +/- polarity and R/B labels. Spatial precision is critical and hard to prompt reliably. | ASCII diagram or structured text list: "A --(+)--> B --(-)-->C --(+)--> A [Balancing loop]". |
| **Multi-layer parallel timeline** | Multiple horizontal tracks with vertical alignment of contemporaneous events and cross-track causal arrows. | Markdown table with time periods as rows and parallel threads as columns. |
| **Large comparison matrix** (>6 dimensions) | Exceeds comfortable image size; text in cells becomes unreadable. | Standard Markdown table — the native format for matrices in the summary documents. |
| **Complex concept map** (>12 nodes) | "Spaghetti code" problem — too many crossing relationships for clean visual layout. | Structured text with explicit relationship statements, or split into multiple focused sub-maps of 6-8 nodes each. |

### Practical Heuristic

**Generate an image when:**
- The diagram has fewer than 12 nodes/elements
- The structure is geometric and predictable (grid, tree, line, circle)
- Text labels are short (1-5 words per label)
- The diagram type has a well-known visual convention (flowchart, timeline, Venn)
- Spatial layout can be fully specified in the prompt

**Use text/Markdown when:**
- The diagram would exceed 12 nodes or 15 connections
- The relationships require nuanced labels longer than a short phrase
- The structure is irregular or requires precise spatial alignment of many elements
- The content is better served by a table that the learner can scan and search
- The diagram would need to be studied at length (text is more searchable and revisitable)

---

## Part 6: Discipline-Specific Guidance

### STEM (Procedural, System-Based)

**Most-used visuals:** Flowcharts (procedural algorithms), concept maps (system interactions), process diagrams (experimental methods, biochemical pathways), tree diagrams (classification of problem types or species).

**Design priority:** Precision. Every variable, unit, and condition must be labeled. Arrows must indicate directionality. Color-code by subsystem. Include decision logic for Apply-level exam targets.

### Humanities (Interpretive, Argumentative)

**Most-used visuals:** Argument maps or structured text (thesis-evidence-counterargument), comparison matrices (theorist vs. theorist, period vs. period), annotated timelines (for historical narrative with causal links).

**Design priority:** Nuance preservation. Humanities arguments are rarely binary; visuals must accommodate qualification, context-dependence, and competing interpretations. Text-heavy formats (QEC structures, annotated matrices) often serve better than purely graphical diagrams.

### Law (Rule-Based, Application-Intensive)

**Most-used visuals:** Decision trees and flowcharts (multi-part legal tests with branching conditions), hierarchical outlines (doctrine structure), matrices (comparing case holdings across elements of a test).

**Design priority:** Conditional logic clarity. Legal reasoning is fundamentally "if X, then Y; unless Z, in which case W." Every branch point must have an explicit condition label. Flowcharts are the backbone format.

### Medicine (Pattern-Based, Diagnostic)

**Most-used visuals:** Differential diagnosis matrices (diseases x discriminating features), diagnostic algorithm flowcharts (symptom to diagnosis pathway), feedback loop diagrams (physiological regulation), illness script process diagrams.

**Design priority:** Discrimination power. The visual must make it easy to distinguish between similar conditions. Comparison matrices with highlighted discriminating features are the highest-value visual for medical education.

### Social Sciences / Education (Current Use Case)

**Most-used visuals:** Concept maps (theoretical relationships), comparison matrices (paradigms, theorists, approaches), layer diagrams (ecological/systems models like Bronfenbrenner), flowcharts (intervention processes, policy implementation chains), timelines (historical development of a field or movement).

**Design priority:** Relational transparency. Social science knowledge is heavily interconnected — theories build on, critique, and modify each other. Visuals must make these intellectual lineages and tensions visible. Layer diagrams are particularly valuable for the systems-level models common in orthopedagogy and education (e.g., the bioecological model, the ICF framework).

---

## Summary of Key Takeaways

1. **Knowledge structure determines diagram type.** Causal chains need flowcharts. Comparisons need matrices. Hierarchies need trees. Procedures need decision flowcharts. Feedback needs loops. Arguments need structured maps. Timelines need timelines. Never force content into a visual type that contradicts its relational grammar.

2. **Bloom's level determines design complexity.** Remember-level visuals should be simple with blanks for retrieval practice. Apply-level visuals need decision logic and worked example gaps. Analyze-level visuals need full relational structure with all connections labeled.

3. **Design for cognitive load, not visual appeal.** Every element must earn its place. Labels carry the learning. Color is semantic. Clutter is the enemy.

4. **AI image generation works for clean, structured, low-node diagrams.** Flowcharts, tree diagrams, timelines, simple matrices, loop diagrams, and Venn diagrams are reliable targets. Complex concept maps, multi-level argument maps, and dense matrices are better rendered as Markdown text or tables.

5. **Most real content mixes structures.** A single chapter may need a tree diagram for its taxonomy, a flowchart for its procedure, a matrix for its comparison, and a timeline for its history. Use the right format for each sub-structure rather than forcing one format on the whole.
