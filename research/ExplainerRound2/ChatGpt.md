# The Cognitive Science of Producing Genuine Understanding Through Extended Spoken Explanation

## Scope, assumptions, and what “genuine understanding” means in the research literature

You already have a solid baseline (working-memory/phonological-loop constraints, curiosity drive, seductive details, fluency illusion + misconception-first, dual coding, serial position + peak-end, strategic redundancy for audio irreversibility, and ABT micro-structure). I treat those as *assumed* and focus on additional mechanisms that—according to cognitive science, educational psychology, discourse comprehension, and expertise research—should change how a 20–30 minute spoken explanation is **structured**, **sequenced**, and **phrased**.

A useful way to operationalize “genuine understanding” (as opposed to recognition or familiarity) is: the listener can build a coherent mental representation that supports **inference**, **transfer**, **prediction**, and **explanation of how/why**, not just recall of sentences. Discourse research formalizes this as moving beyond a surface-level representation toward a **textbase** and ultimately a **situation model** (a representation of the state of affairs described, integrated with prior knowledge). citeturn18view1turn17view1turn19search1

That framing matters because it implies a core design goal for long-form audio: the script must continuously help the listener **construct, maintain, update, and repair** a situation model over time—despite limited attention, transient input, and inevitable partial forgetting. Situation-model and discourse theories imply that “the click” of understanding is often an *integration event*: incoming propositions and retrieved prior knowledge are brought into a coherent, mutually constraining structure (often characterized as a kind of constraint satisfaction/integration process). citeturn18view1turn19search13turn17view1

## Understanding as situation-model construction and repair in extended speech

### Understanding is “model building,” not “content accumulation”
In the construction–integration tradition, comprehension begins with a **construction** phase that activates multiple candidate meanings/inferences (including irrelevant ones), followed by an **integration** phase that stabilizes a coherent network and suppresses weak/incoherent elements. citeturn18view1 This matters for audio because a well-designed explanation must not only present correct statements; it must *steer which inferences get built* and *which candidate interpretations get suppressed*—otherwise listeners can form coherent-but-wrong models.

**Actionable implication for audio scripting:** treat every major section as “model work,” not “topic coverage.” In practice, that means repeatedly answering: *What are the entities/variables? What relations bind them? What causal dependencies make certain outcomes necessary?* (More on SBF and causal structure below.)

### Situation models are multidimensional—and coherence breaks are predictable
The situation-model literature emphasizes that comprehenders track multiple dimensions (in narratives and expository discourse), and coherence is disrupted when these dimensions shift without adequate support. citeturn17view1turn0search1 The event-indexing model, for example, argues that events are connected in memory along dimensions like **time**, **space**, **protagonist/entity**, **causality**, and **intentionality**; discontinuities prompt processing costs and updating. citeturn0search1turn17view1

Even in non-narrative (technical) explanation, you can map these dimensions onto explanation-friendly equivalents:
- **Time** → sequence of states/steps in a mechanism  
- **Space** → where processes happen (physical or conceptual “locations,” like layers in a stack)  
- **Protagonist/entity** → the key variables/components currently “in focus”  
- **Causality** → what makes what happen, with what constraints  
- **Intentionality/goal** → optimization pressures, design goals, or system objectives (in engineered systems; in biology/econ, functional constraints)

**Actionable implication:** design explicit “coherence maintenance moves” whenever you shift one dimension:
- announce the shift (“Now we’re switching from *what it is* to *how it changes over time*”)  
- restate the currently active entities and their roles  
- restate the causal link you want maintained before adding new elements

This is not mere signposting; it is a *working-memory externalization* of the current situation model so the listener doesn’t have to reconstruct it from fragile traces. The multidimensional nature of situation models makes these moves disproportionately important in long audio. citeturn17view1turn0search5

### Engineer “event boundaries” for conceptual updates
Event Segmentation Theory and related “event boundary” work suggests humans naturally parse continuous experience into events; boundaries trigger **updating** processes that affect memory organization and later recall. citeturn7search10turn7search13turn7search4

In explanation, you can deliberately create **conceptual event boundaries** at points where the listener’s model needs updating (new component introduced, causal reversal, change in frame/level). A boundary is where you should *compress the prior model*, *mark what stays invariant*, and *announce the new state*. This aligns with findings that segmentation scaffolds memory and learning. citeturn7search10turn7search4

**Actionable implication:** treat boundaries as mandatory “update checkpoints,” not optional transitions. In a system prompt, this becomes a paradigm like: *Introduce → Stabilize → Boundary recap → Update → Re-stabilize.*

## Prior knowledge is not just “misconceptions”—it determines whether coherence helps or hurts

### Coherence is an interaction effect with prior knowledge
A central (often underused) result from discourse comprehension is that making a text *more coherent/explicit* is not unconditionally beneficial. McNamara & Kintsch’s work shows that **low-knowledge learners** tend to benefit from **high-coherence/high-cohesion** text (because fewer inferences must be generated), whereas **high-knowledge learners** can learn more (especially on deeper measures) from **lower-coherence** text that forces productive inference generation—*when their knowledge is sufficient to make those inferences correctly*. citeturn0search2turn0search6turn0search10

For long-form audio, that creates a design tension: explicit coherence prevents novices from losing the model; but some “strategic under-explaining” can provoke active integration for knowledgeable listeners.

**Actionable implication:** the explainer should be trained to *choose where inference is safe*. A workable audio solution is to keep **core causal links explicit** (so novices don’t break), but introduce **micro-inference prompts** in low-risk spots (“Given that, what would you expect happens next?”), then immediately confirm/correct. This leverages productive inference without letting wrong integration persist. citeturn0search2turn6search0turn8search2

### Expertise reversal and redundancy at the macro level
The **expertise reversal effect** (from cognitive load theory research) shows that instructional supports beneficial to novices can become redundant—and even harmful—for more expert learners, reversing which design is superior as expertise increases. citeturn21view3turn9search1

For audio explainers, this suggests a more nuanced rule than “redundancy is good in audio” (your baseline). Instead: redundancy should be **adaptive** in *function*:
- for novices: redundancy as *reinstatement of the model* (to prevent loss)  
- for high-knowledge listeners: redundancy as *reframing or generalization* (to avoid boredom/shallowness)

**Actionable implication:** redundancy should rarely be verbatim. Use “same causal claim, different handle” (re-expression, new example, boundary recap), not repetition that feels redundant to experts.

### Conceptual change sometimes requires category shifts, not fact replacement
Misconception correction is often treated as “swap false belief for true belief.” Conceptual change research argues that some failures are deeper: learners misassign a concept to the wrong **ontological category** (e.g., treating a process like a substance), which makes new information systematically misinterpreted. Chi and colleagues argue that these *category shifts* are qualitatively harder than adding details within a category. citeturn1search1turn1search9turn22view3

Other conceptual change traditions emphasize different structure:
- **Framework theory**: naïve “frameworks” formed early guide interpretation; learning may require reorganizing these frameworks, not just patching facts. citeturn1search3turn1search7  
- **Knowledge-in-pieces**: naïve understanding may be assembled from many context-sensitive fragments (p-prims), so “misconceptions” can be locally productive but globally misapplied. citeturn1search6turn1search2

**Actionable implication:** a misconception-first script is sometimes insufficient because the listener can accept your correction yet continue to *parse the concept with the wrong type*. Your system prompt can add a “category check” movement:
1) diagnose the likely *type error* (thing vs process; force vs impetus; information vs substance)  
2) re-describe the target concept in the correct category with multiple cues  
3) show why the old category generates wrong predictions (not just wrong statements)

### Refutation isn’t just “say the misconception then deny it”
Refutation text research (though mostly text-based) is relevant because it identifies a *knowledge revision mechanism*: making the misconception explicit, marking it as false, and giving the correct model improves learning more than presenting only correct information. citeturn21view1turn21view2 A 2022 meta-analysis found refutation texts yield a **moderate positive effect** (Hedges’ g ≈ 0.41) across 44 comparisons. citeturn21view1

But newer syntheses emphasize that refutation works best when the correction is not a bare fact but an **interconnected explanation** that supports model replacement. citeturn1search12turn9search3

**Actionable implication for audio:** refutation moments should culminate in a *new causal structure the listener can run*, not only “that’s wrong; here’s the right answer.”

## Analogies and examples: when they transform understanding versus when they mislead

### Why analogies work: relational alignment and schema abstraction
Structure-mapping theory argues that powerful analogies transfer **relational structure** (not surface attributes), and listeners preferentially project connected relational systems (systematicity principle). citeturn2search4turn2search8 This aligns with the practical goal of understanding: acquiring a schema that can organize and predict.

A key instructional refinement is **analogical encoding**: having learners *compare* cases so they abstract the common structure. Gentner, Loewenstein, & Thompson found that comparing two cases (with support) improves schema abstraction and transfer more than studying the same cases separately. citeturn17view2turn2search1

**Actionable implication:** don’t just *tell* one analogy; build a “comparison episode.” In audio, that can be:
- Case A (short)  
- Case B (short, parallel)  
- Guided alignment (“In both cases, notice the roles: X corresponds to Y…”)  
- Schema label (“This pattern is what we’ll call…”)

This is a different paradigm than “use vivid analogy,” and it is strongly grounded in analogy research. citeturn17view2turn2search1

### Progressive alignment: start near, then move far
Progressive alignment work suggests that presenting initially highly alignable examples can bootstrap the ability to notice more abstract relational commonalities later. Kotovsky & Gentner describe progressive alignment as an ordering principle where early easy alignments become entry points for later abstract mapping. citeturn10search0turn10search2

**Actionable implication:** when explaining an abstract mechanism, sequence examples from:
1) **high surface + high relational similarity** (easy mapping)  
2) **lower surface similarity with preserved relational structure** (forces abstraction)  
3) **a “far” application** (tests generalization)

This is a concrete sequencing rule that goes beyond “give examples.”

### Bridging analogies for conceptual change (and why single analogies backfire)
Work on **bridging analogies** in science learning highlights a failure mode: if the learner’s initial understanding is non-normative, a single analogy can be assimilated into the wrong model. Bridging strategies try to connect an anchoring conception to the target using intermediate analogs and guided reasoning rather than one leap. citeturn3search8turn3search12turn3search16

**Actionable implication:** for known misconception-heavy topics, use *series analogies* with explicit mapping constraints:
- anchoring case that the listener already finds intuitive  
- intermediate analog that fixes one mismatch  
- final target mapping  
- explicit “where the analogy breaks” guardrails (to prevent overextension)

### Concreteness fading: a “concrete → abstract” engine that avoids both traps
A robust line of work argues for **concreteness fading**: begin with a concrete, recognizable instantiation, then explicitly fade toward an abstract representation by stripping context-specific details. A systematic review in Educational Psychology Review argues this can support transfer by helping learners interpret abstract symbols, grounding thinking, and guiding attention toward generalizable properties. citeturn17view3turn2search2

**Actionable implication for audio:** don’t just add concrete examples; **transition through** them. A prompt-level movement could be:
- Concrete story (intuitive)  
- “Now delete the story details; keep only the roles and relations”  
- Abstract restatement (symbols/variables)  
- Re-apply to a new concrete scenario

This directly targets the “transformative vs forgettable example” problem: the example becomes a scaffold that is intentionally removed, leaving an abstract schema behind. citeturn17view3turn2search2

## Engineering deep processing inside one-way audio: generative engagement, calibration, and “productive difficulty”

One of the biggest hidden constraints of long audio isn’t only memory; it’s that listening is often **passive** unless you deliberately induce constructive processing. The research below provides mechanisms for doing that without requiring external interaction.

### Self-explanation as a mental-model construction engine
Chi and colleagues showed that prompting learners to **self-explain** can improve understanding because it drives integration of new information with prior knowledge; in their study, prompted students gained more, and “high explainers” were more likely to acquire the correct mental model. citeturn22view3turn0search7

This finding matters because it suggests that understanding is not produced solely by explanation *quality*; it is produced by **the listener generating inferences** and filling gaps. Audio can’t force self-explanation, but it can strongly *invite* it.

**Actionable implication:** embed “self-explanation invitations” at the line/claim level:
- “Why would that be true?”  
- “What has to be happening under the hood for that outcome to follow?”  
- brief pause cue (even 1–2 seconds) before answering

This is not rhetorical flourish; it is a mechanism to trigger constructive processing. citeturn22view3turn8search2

### Elaborative interrogation: “why” questions boost memory and integration
Elaborative interrogation research shows that attempting to answer “why” questions about facts enhances learning, even when learners can’t generate strong answers. citeturn8search0 Mechanistically, “why” prompts encourage linking new assertions to existing causal knowledge, creating more retrieval routes and a more interconnected representation.

**Actionable implication:** treat key claims as *answerable questions* rather than delivered facts—especially when the claim is counterintuitive. Pair with immediate resolution to prevent uncorrected inference drift.

### ICAP: the passive→active→constructive→interactive hierarchy
The ICAP framework synthesizes evidence that deeper learning tends to increase as learners move from **passive** to **active** to **constructive** to **interactive** engagement. It explicitly links engagement modes to *knowledge-change processes*, distinguishing mere activity (e.g., copying) from constructive generation (e.g., explaining) and interactive co-construction. citeturn22view2turn8search2

Audio is naturally “passive,” so the design challenge is to simulate “constructive” moments frequently.

**Actionable implication:** in the system prompt, make “constructive turns” a first-class structural requirement every few minutes (not just at the end). A constructive turn is where the listener is asked to predict, explain, classify, or mentally simulate.

### Attention protection: mind wandering and interpolated retrieval
Mind wandering and disengagement are common during lectures and can harm learning. citeturn5search4turn5search0 A particularly actionable intervention is **interpolated testing** (short memory tests during an online lecture), which has been shown to reduce mind wandering and improve learning of lecture content. citeturn6search0turn6search4turn6search7

Audio scripts can’t administer real tests, but they can incorporate *retrieval episodes*:
- “Quick check: can you state the three parts we’ve built so far?”  
- “Pause and try to predict X before I tell you.”  
- “If you can’t, that’s the gap we’ll patch next.”

These are not only memory aids; they are **attention resets** that re-engage executive control and reduce drift—consistent with the interpolated testing literature. citeturn6search0turn6search4turn5search4

### Prequestions / pretesting: benefit from trying (even when wrong)
A growing body of research on **prequestioning/pretesting effects** suggests that attempting to answer questions before instruction can improve later learning across materials including text, video, and lectures, typically when followed by correct-answer feedback. citeturn5search3turn5search7

Mechanistically, pretesting can prime relevant semantic networks and make subsequent information “stick” by creating an organized search for answers.

**Actionable implication:** open major segments with 1–2 “prediction questions” that are directly answered in the next few minutes—and explicitly close the loop with feedback.

### “Productive confusion”: the controlled disequilibrium cycle
Research by D’Mello and colleagues argues that confusion—arising from anomalies, contradictions, or impasses—can be beneficial **if it is induced, regulated, and resolved**; unresolved confusion becomes detrimental. citeturn16search0turn16search1 This offers a rigorous framing for what many great explainers do intuitively: they create a moment of “wait, how can that be?” and then deliver a resolution that reorganizes the model.

**Actionable implication:** deliberately design “confusion arcs”:
1) present a carefully chosen contradiction or surprising prediction  
2) explicitly acknowledge the confusion (reduces disengagement/anxiety)  
3) supply the missing constraint/mechanism  
4) restate the resolved model and show it now predicts the surprising fact

This is distinct from “misconception-first”: the goal is not only to correct a known false belief, but to leverage *disequilibrium as an integration trigger*. citeturn16search0turn16search1

## Discourse mechanics that make or break 30-minute spoken understanding

### Coherence relations and connectives are not neutral—some help, some hurt
Discourse processing research on connectives suggests that explicit markers of **causal** and **contrastive** relations can improve comprehension, but effects depend on relation type; some work finds additive connectives can even impede comprehension in certain contexts. citeturn4search14turn4search4 A broader processing perspective suggests causal relations play a privileged role in coherence and memory, with discontinuous relations (e.g., concession) benefiting more from explicit connectives. citeturn4search11

**Actionable implication:** treat connectives as cognitive operators:
- use causal/contrastive connectives aggressively when a listener must revise or link states (“because,” “but,” “therefore,” “however”)  
- be cautious with “additive glue” (“also,” “moreover”) if it encourages list-like accumulation rather than structure  
- when introducing a concession (“it seems like X, but actually Y”), explicitly mark it; it triggers a discourse update

This complements your ABT baseline by grounding *why* “but” and “therefore” are powerful: they represent high-impact coherence relations, not stylistic flair. citeturn4search4turn4search11

### Rhetorical structure is a cognitive scaffolding problem, not just rhetoric
Rhetorical Structure Theory (RST) formalizes how discourse units relate (e.g., elaboration, evidence, concession, cause, purpose). citeturn4search3turn4search7 From a cognitive perspective, these relations matter because they tell the listener **what kind of integration** to perform (add detail vs revise vs infer cause vs treat as motivation).

**Actionable implication:** before each segment, the script should implicitly answer: *What relation is this segment to the previous one?* If it’s evidence, label it as evidence. If it’s an exception, label it as exception. If it’s a reframe, label it as reframe. This prevents listeners from mis-integrating a detail as a new rule (a common failure mode in long explanations).

### The Structure Building Framework: suppression and enhancement as hidden levers
Gernsbacher’s Structure Building Framework describes comprehension as building mental structures via laying foundations, mapping new information onto them, and shifting to new substructures; critically, comprehension relies on **enhancement** of relevant information and **suppression** of irrelevant competing interpretations. citeturn20search2turn20search14turn4search1

**Actionable implication:** a spoken explanation can reduce suppression demands by:
- minimizing ambiguous references (pronouns without clear antecedents)  
- keeping “who/what we’re talking about” stable for longer stretches  
- explicitly reactivating the current referent before adding complex relations (“This *rate*—the one we defined earlier—now interacts with…”)

This is a discourse-level complement to working memory limits: you’re not just limiting items; you’re limiting **competition** among interpretations. citeturn20search2turn20search14

### Prosody and information structure: spoken comprehension has extra control channels
Spoken discourse processing research shows that intonation helps listeners with **discourse segmentation** and **information status** (given/new). Venditti & Hirschberg review evidence that intonation plays a major role in these processes. citeturn23search2turn11search3 Experimental work on given/new accenting suggests comprehension is faster when accent placement matches information structure (accent new information, de-accent given). citeturn23search3turn11search15

**Actionable implication for scriptwriting:** you can embed performance cues in the script to exploit these channels:
- mark where the narrator should slow down or emphasize a newly introduced variable  
- mark where a pause should occur to signal a boundary  
- mark where a sentence carries “new” vs “given” information so delivery supports integration

Even if an LLM is only writing text, the script can contain bracketed delivery guidance that a narrator (human or synthetic voice) can follow.

## Expert explanation through a cognitive lens: why great explainers feel “effortless” but produce deep understanding

### “Clarity” is not just style—it correlates with learning at scale
Instructional communication research has long studied “teacher/instructor clarity,” often defined in terms of organization, explanation quality, examples, and assessment/checking understanding. citeturn12search8turn13search0 A large meta-analytic synthesis reports that teacher clarity accounts for a meaningful portion of variance in student learning outcomes (with stronger effects on affective learning but still positive for cognitive learning). citeturn13search0turn12search15

**Cognitive interpretation:** “clarity behaviors” are often precisely the behaviors that protect the listener’s situation model: explicit organization, defining terms, using aligned examples, and checking understanding map cleanly onto discourse and generative-learning mechanisms.

### The curse of expertise: experts miscalibrate the novice’s starting point
Experts are systematically prone to mispredict novice performance (the “curse of expertise”), and debiasing attempts may not reliably fix this. citeturn13search1turn12search14 Related work suggests expertise can create illusions of understanding even for experts regarding their own domains, implying that “felt clarity” is not a reliable indicator of novice comprehension. citeturn12search14

**Actionable implication:** a system prompt should force an LLM explainer to externalize assumptions:
- explicitly list prerequisites (“You need these 3 building blocks…”)  
- define components before mechanisms (pretraining logic; see below)  
- repeatedly restate the core model in beginner language before compressing

This isn’t just pedagogical politeness; it’s a cognitive guardrail against expert blind spots.

### Expert mental models of complex systems differ in what dimensions they include
In research on complex systems understanding, experts and novices differ not only in quantity of facts but in the *structure* of their representations. Hmelo-Silver & Pfeffer analyze understanding in terms of **Structure–Behavior–Function (SBF)**: components (structure), mechanisms/processes (behavior), and purposes/outcomes (function). Experts’ explanations tend to integrate these dimensions; novices often list structures but miss behaviors/functions. citeturn15search4turn15search5turn15search0

**Actionable implication for audio:** adopt an explicit SBF rhythm:
- **Structure:** what’s in the system (entities/parts/variables)  
- **Behavior:** what happens (mechanism, interactions, dynamic update rules)  
- **Function:** what this behavior accomplishes (constraints, objective, resulting phenomena)

This adds a validated “macro-sequencing grammar” for complex topics that is especially relevant when listeners must build a runnable model on one listen. citeturn15search0turn15search4turn15search1

## New paradigm sections you can add to your system prompt

Below are “paradigm modules” written as cognitive mechanisms first, then what they change in script design. Each is grounded in the literatures above and is meant to be directly incorporable as a new prompt section.

### Situation model stewardship
A long explanation succeeds when it continuously helps the listener construct and maintain a coherent situation model (integrated representation), rather than merely accumulating statements. citeturn18view1turn17view1turn0search5  
**Prompt-level requirements:** force each segment to (a) name active entities, (b) state the relation being added/modified, (c) repair coherence after shifts (time/level/entity), and (d) include boundary recaps that compress the current model. citeturn0search1turn7search10

### Conceptual event boundaries and model updating
Event boundary research implies that segmentation and “update moments” shape memory organization and learning. citeturn7search10turn7search4  
**Prompt-level requirements:** every major concept shift must include: “What we had,” “What changes,” “What stays invariant,” and a short forward prediction using the updated model.

### Coherence as an expertise-sensitive dial
High explicit coherence helps low-knowledge learners; lower coherence can induce productive inference for high-knowledge learners. citeturn0search2turn0search10  
**Prompt-level requirements:** keep core causal dependencies explicit, but include safe “inference prompts” + immediate feedback loops to trigger active integration without letting wrong models persist.

### Ontological/type-error correction
Some misunderstandings are category misassignments (thing vs process), making them resistant to standard correction. citeturn1search1turn1search3  
**Prompt-level requirements:** after introducing a hard concept, explicitly state what *kind* of thing it is, contrast it with the common wrong category, and show predictions each category would imply.

### Analogical engineering (comparison, progressive alignment, and fading)
Analogies teach by relational alignment; comparing cases (analogical encoding) and ordering from near to far (progressive alignment) improves abstraction and transfer. citeturn17view2turn10search0turn10search2 Concreteness fading then strips away context so the abstract schema survives. citeturn17view3turn2search2  
**Prompt-level requirements:** mandate at least one “comparison episode” per major idea (two cases + guided mapping + schema label) and at least one “concreteness fading” movement where the story is explicitly dissolved into roles/relations.

### Constructive engagement loops inside audio
Self-explanation, elaborative interrogation, and ICAP imply deeper learning when learners generate explanations, predictions, and integrations, not only receive information. citeturn22view3turn8search0turn22view2  
**Prompt-level requirements:** every few minutes insert a “listener generation moment” (predict/explain/answer why), followed by immediate closure (correct answer + model restatement).

### Attention and calibration resets
Interpolated tests reduce mind wandering and improve learning in lecture contexts; prequestions/pretests can increase later learning even when initial answers are wrong (with feedback). citeturn6search0turn5search3turn5search7  
**Prompt-level requirements:** require periodic retrieval prompts (“Say the model so far”), and segment-openers that ask a question whose answer is delivered soon—then explicitly close the loop.

### Productive confusion arcs
Confusion can benefit learning when induced, regulated, and resolved; unresolved confusion harms learning. citeturn16search0turn16search1  
**Prompt-level requirements:** include at least one controlled contradiction/surprise per major section, followed by explicit resolution that changes the model (not just adds a fact).

### Discourse-operator discipline
Connectives and rhetorical relations guide integration; some relations (causal/contrastive) are especially important for coherence updating. citeturn4search11turn4search4turn4search3  
**Prompt-level requirements:** require explicit marking of relation type at transitions (cause, concession, evidence, example, reframe), and encourage causal/contrastive connectives where the listener must update the model.

### Spoken-only control channels (prosody + information status cues)
Intonation and accenting can signal segmentation and given/new information, facilitating spoken discourse processing. citeturn23search2turn23search3  
**Prompt-level requirements:** allow/mandate delivery annotations (pause, emphasis, slow-down) at (a) new concept introduction, (b) boundaries, (c) causal pivot points, and (d) resolution moments after confusion.

---

If you want to translate this synthesis into actual *prompt wording*, the most reliable pattern (from the literatures above) is to specify **required cognitive moves** (model-building, alignment, prediction, update, repair) rather than surface directives (“be engaging,” “be clear”). The research is unusually consistent that “understanding” emerges when explanation reliably triggers the listener’s **integration, inference generation, and model repair**—and fails when it lets listeners accumulate fluent sentences while their situation model silently fragments or calcifies into the wrong category. citeturn18view1turn22view3turn0search10turn16search0