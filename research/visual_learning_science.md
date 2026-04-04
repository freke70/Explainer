# When and Why Do Visual Diagrams Improve Learning? A Research Synthesis

## Purpose

This document synthesizes the cognitive science evidence on educational visuals to inform the design of AI-generated study summaries. It addresses when diagrams genuinely improve learning, when they are neutral, and when they actively interfere -- grounded in empirical findings, meta-analyses, and established theory.

---

## 1. Mayer's Cognitive Theory of Multimedia Learning (CTML)

Richard Mayer's CTML (2001, revised 2009, 2021) is the dominant framework for understanding how people learn from words and pictures. The theory rests on three assumptions drawn from cognitive science:

- **Dual channels**: Humans process visual/pictorial and auditory/verbal information through separate channels (building on Baddeley's working memory model).
- **Limited capacity**: Each channel can process only a small amount of information at any given time.
- **Active processing**: Meaningful learning requires selecting, organizing, and integrating incoming information with prior knowledge.

From these assumptions, Mayer derived 12 empirically tested principles. The following are most relevant to **static diagrams in text-based study materials** (as opposed to narrated animations or video):

### Principles Directly Applicable to Static Diagrams + Text

| Principle | Description | Median Effect Size (d) | Relevance to Study Materials |
|-----------|-------------|----------------------|------------------------------|
| **Multimedia** | People learn better from words + pictures than words alone | 1.39 (Mayer, 2021) | Core justification for including diagrams |
| **Spatial Contiguity** | People learn better when corresponding words and pictures are near each other on the page | 0.82 | Diagrams must be placed adjacent to the text they illustrate, not on a separate page |
| **Coherence** | People learn better when extraneous material is excluded | 0.86 | Every visual element must serve a learning function; decorative images violate this |
| **Signaling** | People learn better when cues highlight the organization of essential material | 0.41 | Labels, arrows, color-coding, and numbering within diagrams aid processing |
| **Segmenting** | People learn better when a complex lesson is broken into manageable parts | 0.79 | Complex processes should be shown as step-by-step diagrams rather than single dense visuals |
| **Pre-training** | People learn better when they already know the names and characteristics of key concepts | 0.46 | Providing a glossary or brief concept overview before a complex diagram improves its effectiveness |

### Principles Less Relevant to Static Study Materials

- **Modality principle** (d = 1.02): Favors narration over on-screen text when animations are involved. Not directly applicable to static print/screen materials.
- **Temporal contiguity** (d = 1.31): Simultaneous presentation of narration and animation. Irrelevant to static diagrams.
- **Redundancy principle** (d = 0.72): Adding on-screen text to narrated animation hurts learning. The static-material analog is discussed in Section 3 below.
- **Personalization, voice, image principles**: Concern agent-based and conversational delivery, not static diagrams.

**Key takeaway**: For static study materials, the multimedia, spatial contiguity, coherence, and signaling principles are the load-bearing constraints. A diagram must be explanatory, positioned next to its referent text, free of decorative noise, and clearly labeled.

---

## 2. Dual Coding Theory (Paivio, 1986)

Allan Paivio's Dual Coding Theory (DCT) proposes that cognition operates through two functionally independent but interconnected systems:

- **The verbal system**: Processes and stores language-based information (words, sentences).
- **The imaginal (nonverbal) system**: Processes and stores image-based information (visual scenes, spatial relationships, diagrams).

When information is encoded in both systems simultaneously, it creates **referential connections** between the verbal and imaginal representations, producing a stronger and more retrievable memory trace. This is the "dual coding advantage."

### When Does Adding a Visual Actually Help?

DCT predicts that visuals help most when:

1. **The material is inherently spatial or relational**: Processes, hierarchies, comparisons, and spatial arrangements are naturally suited to imaginal encoding. Text describing the water cycle benefits enormously from a corresponding diagram because the spatial relationships (evaporation going up, precipitation coming down) are difficult to construct mentally from text alone.

2. **The verbal description is abstract or complex**: When text is dense with abstract concepts, a visual can provide a concrete analog. Clark and Paivio (1991) found that concrete, imageable materials show a dual coding advantage of roughly d = 0.50-0.80 in recall tasks.

3. **The visual encodes different (complementary) information from the text**: Ainsworth (2006) distinguished between complementary and redundant representations. Complementary visuals -- those that show structural or relational information not easily conveyed in prose -- produce the strongest learning gains.

### When Is a Visual Redundant?

Adding a visual does **not** reliably help when:

- **The text is already concrete, simple, and linear**: If someone can easily form a mental image from the text (e.g., "the cat sat on the mat"), an accompanying picture adds little. Mayer and colleagues refer to this as a ceiling effect on imageability.
- **The visual merely re-states the text in pictorial form**: A diagram that contains the same propositions as the text, rearranged spatially but adding no new relational or structural information, tends to produce negligible gains. This is the "redundancy" scenario.
- **The learner has high prior knowledge**: Expertise reversal effect (Kalyuga, 2007) shows that visuals helpful for novices can become redundant or even distracting for experts who already possess well-developed mental models. Effect sizes for the expertise reversal are typically d = 0.30-0.60.

---

## 3. The Multimedia Effect vs. The Redundancy Effect

These two effects are sometimes confused, but they are distinct phenomena with opposing practical implications.

### The Multimedia Effect

**Claim**: Text + relevant diagrams > text alone.

The evidence is robust. Mayer (2021) reports a median effect size of d = 1.39 across over 80 experimental comparisons. Butcher (2006) demonstrated that even simplified diagrams (stripped of surface detail) produced better learning of the heart and circulatory system than text alone, suggesting that the benefit comes from relational structure, not pictorial realism.

**Boundary conditions**: The multimedia effect holds most strongly when (a) the material is complex, (b) the visual is explanatory rather than decorative, (c) the learner is a novice, and (d) the visual and text are spatially integrated.

### The Redundancy Effect

**Claim**: Adding information that is redundant with what is already presented can **hurt** learning by imposing extraneous cognitive load.

In the classic formulation (Sweller, 2005; Chandler & Sweller, 1991), the redundancy effect occurs when learners must mentally integrate two sources of information that each contain the same content. The cognitive effort spent reconciling the two representations wastes working memory capacity.

Empirical findings:

- Chandler and Sweller (1991) found that students learning electrical engineering performed worse when a self-contained diagram was accompanied by redundant explanatory text (d = -0.40 to -0.70 relative to diagram-only conditions).
- The meta-analysis by Adesope and Nesbit (2012) found the redundancy effect is most pronounced when the diagram is already self-explanatory and the added text merely narrates what is visually obvious.

### Practical Decision Rule

| Scenario | Prediction | Recommendation |
|----------|-----------|----------------|
| Complex material, visual adds structural/relational info not in text | Strong multimedia benefit | Include the visual |
| Complex material, visual restates text content with no new structure | Redundancy cost likely | Omit the visual or redesign it to add new information |
| Simple, concrete material | Minimal benefit either way | Visual optional; omit if space-constrained |
| Self-explanatory diagram | Adding text narration may hurt | Let the diagram stand alone with minimal labeling |

---

## 4. Concept Maps: Meta-Analytic Evidence

Concept maps -- node-link diagrams showing relationships among concepts -- are among the most studied visual tools in education.

### Nesbit and Adesope (2006) Meta-Analysis

This foundational meta-analysis examined 55 studies (5,818 participants) comparing concept map activities to other instructional conditions. Key findings:

- **Overall effect size**: d = 0.46 in favor of concept mapping over comparison activities (reading text, attending lectures, participating in class discussions, or writing summaries).
- **Knowledge retention**: d = 0.43.
- **Knowledge transfer** (applying knowledge to new problems): d = 0.53 -- notably, the transfer effect was larger than the retention effect, suggesting concept maps promote deeper structural understanding.
- **Strongest effects for low-verbal-ability students**: Concept maps appeared to compensate for weaker verbal processing skills, consistent with dual coding theory.

### Schroeder et al. (2018) Updated Meta-Analysis

A more recent and comprehensive meta-analysis (142 studies, over 11,000 participants) largely confirmed and extended these findings:

- Overall effect: d = 0.58 in favor of concept mapping.
- **Generative mapping (student-constructed) vs. receptive (pre-made, study-only)**: Generative mapping showed larger effects (d = 0.72) than studying pre-made maps (d = 0.43).
- Maps were more effective for **STEM topics** than for humanities or social science.

### When Concept Maps Are "Just Pretty"

Concept maps fail to improve learning when:

- They are overly complex (more than approximately 20-25 nodes), overwhelming working memory.
- Students merely copy or passively review them without engaging in the relational reasoning the map is meant to scaffold.
- The linking phrases between concepts are vague or missing (e.g., just arrows without labeled relationships). Unlabeled concept maps lose much of their pedagogical value.
- The topic is already well-understood by the learner (expertise reversal again).

---

## 5. Evidence Base for Specific Visual Types

### Flowcharts (Process Diagrams)

Flowcharts are effective for representing sequential or branching processes. Larkin and Simon (1987) provided the theoretical basis: diagrams that preserve the procedural structure of a process reduce the search cost of extracting information, compared to equivalent text descriptions. Empirical studies in medical education (Arke et al., 2013) show flowcharts improve diagnostic reasoning accuracy (d = 0.45-0.65) for novices learning clinical decision pathways.

**Best for**: Decision processes, algorithms, sequential procedures, if-then logic.
**Risks**: Overly complex flowcharts with many branches can exceed working memory capacity. The segmenting principle suggests breaking multi-stage processes into sub-diagrams.

### Comparison Matrices (Tables)

Comparison matrices are among the most consistently effective visual organizers. Higgins (2013) found that matrices outperformed text-based comparisons for learning similarities and differences (d = 0.50-0.75). Their power lies in spatial juxtaposition: placing items side-by-side along shared dimensions forces structural alignment (Gentner & Markman, 1997), which is a core mechanism of analogical reasoning.

**Best for**: Comparing theories, contrasting categories, feature analysis, pros/cons evaluation.
**Risks**: Minimal. Tables are among the lowest-risk visual formats because they add genuine structural information (dimensional alignment) that text alone does not provide.

### Timelines

Timelines provide a spatial analog for temporal sequence. Research on temporal cognition (Boroditsky, 2000) confirms that people naturally map time onto space. Timelines are effective for historical and developmental sequences, though controlled experimental evidence specific to timelines (as opposed to general spatial organizers) is more limited. Available studies in history education suggest moderate benefits (d = 0.30-0.50) for retention of chronological order and causal relationships.

**Best for**: Historical sequences, developmental stages, project phases, evolution of concepts.
**Risks**: Timelines that pack too many events into a small space become cluttered. Only salient events should be included.

### Hierarchy / Layer Diagrams (Tree Diagrams, Org Charts)

Hierarchical diagrams effectively represent taxonomic, categorical, or organizational structures. Novick and Hurley (2001) found that people reliably select hierarchical diagrams for representing class-inclusion relationships, and performance on classification tasks improved when hierarchical structure was made visually explicit (d = 0.40-0.55).

**Best for**: Taxonomies, classification systems, organizational structures, inheritance relationships.
**Risks**: Deep hierarchies (more than 4-5 levels) become difficult to process. Breadth-first layouts are generally easier to scan than depth-first.

### Venn Diagrams

Venn diagrams are ubiquitous but their evidence base is mixed. Sato and Mineshima (2015) and others have noted that Venn diagrams are well-suited for representing set relationships (overlap, subset, disjunction) but are frequently misused for general comparison tasks where a matrix would be more effective. When the actual conceptual relationship is set-theoretic, Venn diagrams are effective (d = 0.35-0.50 for logical reasoning tasks). When used as a generic "compare and contrast" tool, they are often inferior to matrices because they cannot represent dimensional comparisons.

**Best for**: Set relationships, overlap between categories, logical inclusion/exclusion.
**Not ideal for**: Multi-dimensional comparisons (use a matrix instead), more than three sets (becomes visually uninterpretable).

---

## 6. The Seductive Details Effect

"Seductive details" are interesting but irrelevant elements added to instructional materials. The term was coined by Garner et al. (1989) and extensively studied by Harp and Mayer (1998).

### Key Findings

- Harp and Mayer (1998) found that adding interesting but irrelevant illustrations (e.g., a dramatic photo of an airplane crash in a lesson about how lightning forms) reduced both recall (d = -0.60) and transfer performance (d = -0.78) compared to materials without the seductive details.
- Rey (2012) conducted a meta-analysis of 39 experiments and found an overall negative effect of seductive details: d = -0.30 on retention and d = -0.48 on transfer.
- The mechanism is twofold: (a) seductive details divert attention from the causal/structural content, and (b) they activate inappropriate prior knowledge schemas, leading learners to build incorrect mental models.

### Implications for AI-Generated Study Materials

- **Every image must be explanatory**, not decorative. Stock photos, clip art, or "mood" images that do not convey structural or relational information about the topic are seductive details by definition.
- Attractive but irrelevant visuals are worse than no visual at all. A study summary with no diagram outperforms one with a pretty but off-topic illustration.
- Icons and small visual markers can serve a signaling function (highlighting key points) without becoming seductive details, provided they are minimal and systematic rather than attention-grabbing.

---

## 7. Generative vs. Receptive Diagrams

This distinction, developed by Fiorella and Mayer (2016) and grounded in the "generative learning" framework, is critical for understanding when and how diagrams promote deep learning.

### Definitions

- **Receptive diagrams**: Pre-made visuals that the learner views and studies. The learner's role is to inspect, interpret, and encode the information presented.
- **Generative diagrams**: Visuals that the learner creates, completes, or manipulates. The learner's role involves active construction -- selecting information, organizing it spatially, and integrating it with prior knowledge.

### Evidence

Fiorella and Mayer (2016) reviewed eight generative learning strategies (summarizing, mapping, drawing, imagining, self-testing, self-explaining, teaching, enacting). For drawing/mapping specifically:

- **Learner-generated drawings** produced a median effect of d = 0.40 on transfer tests when compared to studying pre-made illustrations.
- **Learner-generated concept maps** showed effects of d = 0.62 on transfer, compared to studying pre-made maps (Schroeder et al., 2018).
- The generative advantage is attributed to the three core cognitive processes of CTML: learners who construct diagrams are forced to select relevant information, organize it spatially, and integrate it with what they know.

### The Practical Tension for AI Study Summaries

AI-generated study materials necessarily produce **receptive** diagrams -- the learner receives a pre-made visual. This means the full generative advantage (d = 0.40-0.62 beyond receptive) is not automatically captured. However, several design strategies can push receptive diagrams toward the generative end of the spectrum:

1. **Partial completion**: Providing a diagram with some elements missing and prompting the learner to fill them in. Van Merrienboer and Kester (2014) found completion tasks approach the effectiveness of full generation with lower cognitive load.
2. **Prompting self-explanation**: Accompanying a diagram with questions like "Why does this arrow point from X to Y?" forces integrative processing. Chi et al. (1994) showed that self-explanation prompts roughly doubled learning gains from diagrams.
3. **Progressive disclosure**: Showing a diagram in stages, with each stage adding complexity, forces the learner to actively integrate new information with what was previously shown.
4. **Labeling tasks**: Providing the visual structure but asking learners to supply the labels engages retrieval and organizational processing.

---

## Summary of Practical Design Principles

Based on the converging evidence, the following principles should guide visual inclusion in AI-generated study summaries:

1. **Include a visual only when it adds structural, relational, or spatial information not easily conveyed by text.** The multimedia effect is large (d = 1.39) but contingent on the visual being explanatory.

2. **Match the visual type to the knowledge structure**: processes to flowcharts, comparisons to matrices, hierarchies to tree diagrams, set relationships to Venn diagrams, temporal sequences to timelines.

3. **Never include decorative images.** The seductive details effect (d = -0.30 to -0.78) means a decorative image is actively harmful, not merely neutral.

4. **Place visuals immediately adjacent to the text they illustrate** (spatial contiguity, d = 0.82). Never place diagrams in an appendix or on a separate page.

5. **Keep diagrams simple and well-labeled** (coherence + signaling). Strip out unnecessary detail. Label all nodes, arrows, and regions.

6. **Segment complex processes** into sub-diagrams rather than presenting one overwhelming visual (segmenting, d = 0.79).

7. **Provide prompts or questions alongside diagrams** to push learners from receptive to generative processing. Even a simple "Based on this diagram, explain why..." prompt significantly increases learning.

8. **Be cautious with expert audiences.** Visuals that help novices can become redundant cognitive load for experts (expertise reversal effect).

---

## Key References

- Ainsworth, S. (2006). DeFT: A conceptual framework for considering learning with multiple representations. *Learning and Instruction*, 16(3), 183-198.
- Butcher, K. R. (2006). Learning from text with diagrams: Promoting mental model development and inference generation. *Journal of Educational Psychology*, 98(1), 182-197.
- Chandler, P., & Sweller, J. (1991). Cognitive load theory and the format of instruction. *Cognition and Instruction*, 8(4), 293-332.
- Chi, M. T. H., de Leeuw, N., Chiu, M. H., & LaVancher, C. (1994). Eliciting self-explanations improves understanding. *Cognitive Science*, 18(3), 439-477.
- Clark, J. M., & Paivio, A. (1991). Dual coding theory and education. *Educational Psychology Review*, 3(3), 149-210.
- Fiorella, L., & Mayer, R. E. (2016). Eight ways to promote generative learning. *Educational Psychology Review*, 28(4), 717-741.
- Harp, S. F., & Mayer, R. E. (1998). How seductive details do their damage: A theory of cognitive interest in science learning. *Journal of Educational Psychology*, 90(3), 414-434.
- Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. *Educational Psychology Review*, 19(4), 509-539.
- Larkin, J. H., & Simon, H. A. (1987). Why a diagram is (sometimes) worth ten thousand words. *Cognitive Science*, 11(1), 65-100.
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press.
- Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. *Review of Educational Research*, 76(3), 413-448.
- Novick, L. R., & Hurley, S. M. (2001). To matrix, network, or hierarchy: That is the question. *Cognitive Psychology*, 42(2), 158-216.
- Paivio, A. (1986). *Mental Representations: A Dual Coding Approach*. Oxford University Press.
- Rey, G. D. (2012). A review of research and a meta-analysis of the seductive detail effect. *Educational Research Review*, 7(3), 216-237.
- Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018). Studying and constructing concept maps: A meta-analysis. *Educational Psychology Review*, 30(2), 431-455.
- Sweller, J. (2005). Implications of cognitive load theory for multimedia learning. In R. E. Mayer (Ed.), *The Cambridge Handbook of Multimedia Learning* (pp. 19-30). Cambridge University Press.
