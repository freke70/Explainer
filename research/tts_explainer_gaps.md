# Gap Research: Narrative Transportation, Threshold Concepts, and Emotional Trajectory

## Purpose

This document fills three research gaps identified in the current TTS Explainer system prompt (`prompts/tts_explainer.md`). The prompt already has deep grounding in situation model theory, event segmentation, prediction error, conceptual change, analogical reasoning, cognitive load, curiosity, productive failure, serial position effects, and the ICAP framework. What it lacks are:

1. **Narrative Transportation** — the prompt uses narrative techniques intuitively but has no theoretical grounding for *when* and *why* to deploy narrative vs. expository modes, or how transportation specifically operates in audio.
2. **Threshold Concepts** — the prompt asks the model to identify "what must be understood before what" and "the one thing the listener must understand," but lacks the diagnostic framework for identifying *which* ideas in a topic are the ones where disproportionate investment restructures everything else.
3. **Emotional Trajectory Management** — the prompt handles micro-level emotion well (surprise → curiosity → confusion → resolution) but has no framework for managing the listener's emotional state across a 30–60 minute piece, or for understanding boredom, fatigue, and delight as functional signals.

---

## PART 1: Narrative Transportation — The Missing Persuasive Channel

### The Core Theory

Narrative transportation (Green & Brock, 2000) is an experiential state of immersion in which all of the listener's mental processes — attention, emotion, and imagery — are concentrated on the events occurring in the narrative. The transported listener mentally enters a story world and temporarily loses access to some real-world facts. This is not metaphorical — it is a measurable cognitive state with distinct neural signatures and specific downstream effects on belief, memory, and attitude.

The theory sits within Bruner's (1985) distinction between two fundamental modes of human cognition:

- **Paradigmatic (logico-scientific) mode**: organizes thought through argument, reasons, evidence, and logical verification. It describes truth through abstraction and formal systems.
- **Narrative mode**: organizes thought through temporally ordered causal events, organized around agents with goals, encountering and overcoming obstacles, resulting in emotional experiences. It describes truth through stories that feel real.

These are not stylistic choices — they are cognitively distinct processing pathways. The paradigmatic pathway controls the encoding of evidence-based propositions. The narrative pathway controls the encoding of situation-based exemplars. They produce different kinds of understanding, and they are both needed for deep explanation.

### Why This Matters for TTS Explanation

A meta-analysis of over 75 samples and 33,000+ participants (Mar et al., 2021) found that narrative texts were more easily comprehended and better recalled than expository texts. The effect was robust across study designs and not moderated by various study characteristics. In a direct comparison, narrative text was read roughly twice as fast and recalled roughly twice as well, regardless of topic familiarity or interest in the content (Dahlstrom, 2014; PNAS).

The reason: stories resemble our everyday experience. People experience life as temporally ordered causal events, organized around personal goals, with encountering and overcoming obstacles. This parallels the structure of stories — and the brain has evolved dedicated, highly efficient machinery for processing this structure. Narrative processing is not just easier — it is the brain's default mode of making sense of sequential, causal, agent-driven events.

For audio specifically, the effect is even more pronounced. Research shows that narrated stories elicit somewhat more intense emotional shifts than written ones, likely due to prosodic cues. The intimate nature of listening — often done through headphones — creates a more personal engagement. And because the visual channel is dark during audio, the mental imagery generation that transportation demands becomes the *only* available dual-coding channel, making it cognitively load-bearing rather than supplementary.

### The Four Mechanisms of Transportation

Transportation changes beliefs and enhances memory through four specific mechanisms (Green & Appel, 2024):

**1. Reduced Counterarguing.** The transported listener's cognitive resources are allocated to following the story, not evaluating its claims. Cognitive effort is high (the listener is actively processing), yet counterarguing is unlikely to occur. This is not the same as reduced attention — it is attention redirected from evaluation to immersion. For explanation: facts embedded within a narrative are accepted more readily than the same facts presented as propositions to be evaluated. The listener does not need to be "convinced" — they absorb the correct model as part of understanding the story.

**2. Connections with Characters.** The listener identifies with characters in the narrative — temporarily adopting their perspective, goals, and emotional reactions. Identification means experiencing the story *from inside the character's shoes*, not just sympathizing from outside. When a listener identifies with a historical scientist struggling with a problem, the listener vicariously experiences the struggle, the dead ends, and the insight. This is not stylistic — it is a mechanism for *encoding the problem structure* through vicarious experience.

**3. Mental Imagery.** Transportation generates vivid mental images of story events. These images become linked to the beliefs and facts embedded in the narrative. The transportation-imagery model (Green, 2004) holds that this connection between vivid images and embedded beliefs is one of the primary bases for narrative persuasion. For TTS, where imagery is the *only* available non-verbal channel, this is critically important — narrative activates the imagery system more strongly and more naturally than expository instruction to "imagine" something.

**4. Emotional Engagement.** The listener responds emotionally to narrative events — not to abstract propositions about a topic, but to what happens to characters they care about. This emotional processing enhances encoding (dual-coding through affective channels) and creates the motivational energy to continue listening. Emotional engagement in narrative is not the seductive detail effect — the emotions arise *from* the core content, not tangential to it.

### When to Deploy Narrative vs. Paradigmatic Mode

This is the critical design question the current prompt lacks guidance on. Based on the research:

**Use narrative mode when:**
- Introducing a topic for the first time — narrative provides the temporal/causal scaffolding the listener needs to build an initial situation model
- The content involves causal processes unfolding over time (evolution, historical developments, how a mechanism was discovered, how a disease progresses)
- The listener needs to understand *why* something matters before learning *what* it is — narrative creates felt significance through character stakes
- Building the listener's initial model before dismantling it — a character who believes the wrong model and then discovers the right one is a vehicle for productive failure
- The listener is likely to resist the correct understanding — narrative reduces counterarguing and delivers the correction through vicarious experience rather than proposition
- Establishing a concrete anchor — a specific named case, experiment, or discovery that the listener can attach abstract principles to

**Use paradigmatic mode when:**
- Presenting formal definitions, classifications, or precise distinctions that require logical precision
- The listener already has enough narrative scaffolding and now needs the abstract principle extracted and named
- Building logical arguments where the validity depends on the structure of the reasoning, not the vividness of examples
- Comparing models or theories systematically — the paradigmatic mode's strength is parallel evaluation across consistent criteria

**The key insight: alternation is the mechanism.** The most effective explanations do not choose one mode — they oscillate. A narrative passage builds the situation model and creates felt significance. Then a paradigmatic passage extracts the principle, names it, and positions it in the conceptual framework. Then another narrative passage applies the principle to a new case, showing its predictive power. This alternation maps directly onto the semantic wave the prompt already describes (abstract ↔ concrete) — but adds a second dimension: paradigmatic ↔ narrative.

### When Narrative Backfires

The prompt must include guardrails:

**Perceived manipulation triggers reactance.** When the listener becomes aware that a story is trying to persuade them — when the persuasive intent becomes visible — transportation collapses and psychological reactance increases. The listener shifts from immersion to evaluation, and the narrative becomes *less* persuasive than a straightforward expository presentation would have been. For TTS explanation: if the narrative feels engineered to make a point rather than naturally illuminating one, it will backfire. The story must feel like the natural way to encounter the idea, not a rhetorical device deployed on the listener.

**Perceived inauthenticity and "corniness."** Stories that feel forced, overly dramatic, or emotionally manipulative elicit affective resistance — a sense of inauthenticity that functions like counterarguing in non-narrative persuasion. For TTS: the narrative voice must feel like a knowledgeable person sharing a genuine case, not a presenter performing dramatic storytelling.

**Narrative can obscure rather than illuminate.** When factual content is tangentially related to the story rather than structurally embedded in it, the narrative and the facts compete for processing resources. This is the seductive detail effect applied to narrative structure. The science embedded in the story must be *part of* the story's causal chain — not decorative context or backstory. If the listener could follow the story without understanding the science, the narrative is not serving explanation.

**Fictional elements risk misconception.** In science explanation specifically, fictional or fantastical narrative elements can blur the line between imagination and mechanism, fostering misconceptions rather than correct models. The constraint for explanatory narrative: the story must be *real* — a real experiment, a real case, a real discovery, a real person confronting a real problem — or clearly framed as a thought experiment whose purpose is to expose the logic of a principle.

### Practical Architecture: Explanatory Narrative as Carrier

The research suggests a specific structure for narrative in explanation:

1. **Narrative as opening carrier.** Begin a movement with a concrete narrative — a person, a moment, a specific situation — that naturally surfaces the misconception or question the movement will address. The listener enters the story world, which creates the felt gap (curiosity) and provides the concrete anchor simultaneously. This is more effective than starting with a proposition and then illustrating it.

2. **Paradigmatic extraction.** After the narrative has built the situation model, shift to paradigmatic mode to name the principle, define the mechanism, and position it in the framework. The listener now has both the felt experience and the abstract label.

3. **Narrative reapplication.** Return to narrative to apply the principle to a new case — showing its predictive power and testing the listener's new model against a different scenario. This is the "concreteness fading" principle applied through narrative: concrete (story 1) → abstract (extracted principle) → re-concrete (story 2).

4. **Paradigmatic synthesis.** Close the movement by restating the principle in its most compressed, transferable form — the thing the listener carries forward.

This four-beat pattern (narrative → paradigmatic → narrative → paradigmatic) can repeat within and across movements, at varying scales.

### Audio-Specific Considerations

- Narrated stories elicit more intense emotional shifts than written ones, possibly reflecting prosodic cues — punctuation and sentence structure shape TTS prosody, which means narrative passages should have more rhythmic variation, shorter sentences at dramatic moments, longer flowing sentences during development
- The listener cannot re-read; narrative coherence must be maintained through explicit causal connectives within the story, not just between expository points
- Character identification in audio is particularly strong due to the intimacy of the listening context — the voice feels like a person telling you something, which is already quasi-narrative. The prompt should exploit this by framing the entire piece as *one person explaining something fascinating to another person they respect*, which is itself a narrative frame

---

## PART 2: Threshold Concepts — The Diagnostic Framework for Depth Allocation

### The Core Theory

Threshold concepts (Meyer & Land, 2003) are ideas within a discipline that, once understood, fundamentally and irreversibly transform how the learner perceives the subject. They are "akin to a portal, opening up a new and previously inaccessible way of thinking about something." The transformation is not incremental — it is a phase transition. Before the threshold, the learner sees the subject one way. After crossing it, they see it differently and cannot return to their prior understanding.

The current prompt asks the model to "define the situation model you are building" and "state the one thing the listener must understand in one sentence." Threshold concept theory provides a principled way to identify *which* thing that should be — not just the most important fact, but the idea whose understanding restructures everything else.

### The Five Characteristics

A threshold concept is:

**1. Transformative.** Understanding it occasions a significant shift in the perception of a subject or part thereof. The learner doesn't just know more — they see differently. Examples: opportunity cost in economics transforms how one evaluates every decision; natural selection in biology transforms how one sees every adaptation; the concept of a variable in mathematics transforms how one approaches problems.

**2. Irreversible.** The change of perspective is unlikely to be forgotten or unlearned except by considerable effort. This is the "once you see it, you can't unsee it" quality. It means that the explanation's job is not to make the listener *remember* the concept — it is to make them *cross the threshold*. Once they do, the understanding maintains itself because it has restructured their model.

**3. Integrative.** It exposes the previously hidden interrelatedness of ideas within the discipline. Before the threshold, the learner sees the subject as a collection of separate topics. After crossing, they see how those topics connect through the threshold concept. This means: identifying the threshold concept also identifies the structural backbone of the explanation. Everything else connects through it.

**4. Bounded.** It defines a disciplinary boundary — a way of thinking and practising within a discipline that is characteristic of that discipline. This means different disciplines have different threshold concepts, and the model must diagnose *this topic's* threshold concepts specifically, not apply a generic template.

**5. Troublesome.** Understanding it is characteristically difficult — not just "hard" in the sense of requiring effort, but troublesome in ways that actively resist conventional instruction. The troublesomeness comes in specific, diagnosable forms.

### Perkins' Taxonomy of Troublesome Knowledge

This taxonomy (Perkins, 1999, extended by Meyer & Land) directly maps to the kinds of resistance the current prompt already describes — but provides a more complete and diagnostic framework:

**Ritual Knowledge.** Knowledge that has been ingrained as routine without genuine understanding. The learner can perform the procedure or recite the definition but cannot explain why it works or apply it in a novel context. For explanation: ritual knowledge is invisible to the learner — they believe they understand because they can produce the right words. The prompt's "synthetic model" failure mode is a form of ritual knowledge. The explanation must surface the ritual and show that it does not produce genuine understanding.

**Inert Knowledge.** Knowledge that is stored but never activated — the learner has it but cannot retrieve it when it is relevant. For explanation: this is the listener who heard and understood each part of the explanation but cannot connect the parts to solve a new problem. The architecture must create retrieval triggers — not just present concepts but create the associations that will activate them in future contexts.

**Conceptually Difficult Knowledge.** Knowledge that requires significant cognitive effort because the concepts are inherently complex — many interacting elements, non-linear relationships, multi-level causation. The prompt's cognitive load framework handles this well, but threshold concept theory adds: the difficulty is often concentrated at specific conceptual nodes, not distributed evenly. Find those nodes and invest disproportionately.

**Alien Knowledge.** Knowledge that comes from a perspective or culture fundamentally different from the learner's own — it challenges existing worldview, not just existing facts. The prompt's "ontological category error" maps onto this, but alien knowledge extends beyond ontological errors to include epistemological differences (how knowledge is *constructed* in this discipline differs from how the learner expects knowledge to work).

**Tacit Knowledge.** Knowledge that experts hold implicitly and cannot easily articulate — the assumptions, heuristics, and frameworks that operate below conscious awareness. This is particularly relevant for the model: the expert (the LLM drawing on its training distribution) may know things tacitly that it fails to make explicit for the listener. The prompt should instruct the model to surface its own tacit knowledge — the things it assumes the listener already understands.

### The Liminal Space

When a learner encounters a threshold concept, they enter a **liminal state** — an in-between space where they have begun to let go of their old understanding but have not yet stabilized in the new one. This state is characterized by:

- **Oscillation:** The learner swings between old and new understanding, sometimes using the correct model and sometimes reverting to the old one.
- **Mimicry:** Under pressure, the learner may adopt the *language* of the new understanding without having genuinely crossed the threshold — using new vocabulary within old conceptual frameworks. This maps directly to the prompt's "synthetic model" failure, but threshold concept theory provides the diagnostic: mimicry is the learner performing the language of understanding without the ontological shift that produces genuine understanding.
- **Productive discomfort:** The liminal state is inherently uncomfortable — the learner has lost the security of their old model but hasn't gained the power of the new one. This discomfort is not a failure of the explanation — it is the engine of transformation. But it must be managed (see Part 3).

For explanation, the critical implication is: **the listener will not cross the threshold during the explanation itself.** The explanation's job is to bring the listener *to* the threshold — to make the old model visibly inadequate, to surface the tacit assumptions that prevent crossing, and to provide enough scaffolding that the listener can complete the crossing on their own in the hours and days after listening. This means the architecture must plan for *threshold approach*, not *threshold delivery* — setting up the conditions for the transformation rather than attempting to force it in real time.

### Diagnostic Heuristics for the Audit Phase

The model needs specific questions to identify threshold concepts during the Audit phase:

1. **The transformation test:** "If the listener understood this one idea, would it change how they see multiple other aspects of the topic?" If yes, it is likely a threshold concept. If it only changes how they see one thing, it is an important fact but not a threshold.

2. **The irreversibility test:** "Once the listener understands this, could they go back to their previous understanding?" If the new understanding permanently restructures their model, it is likely a threshold concept.

3. **The integration test:** "Does understanding this idea reveal connections between other ideas that were previously invisible?" If yes, it is likely a threshold concept. This is the structural backbone test — the idea that connects everything else.

4. **The troublesomeness test:** "Is this the idea that experts find most difficult to explain to novices — and that novices most commonly get wrong?" The consistent location of difficulty across learners points to a threshold. Important: difficulty alone is not diagnostic — some things are hard without being transformative. The difficulty must be coupled with transformation.

5. **The mimicry test:** "Can learners produce correct-sounding statements about this without genuinely understanding it?" If learners routinely echo the right words without being able to apply, predict, or transfer, the concept is probably threshold and the listener is probably in the liminal space, performing mimicry.

6. **The expert blind spot test:** "Is this something that experts take so completely for granted that they forget it was ever non-obvious?" Tacit knowledge that experts have internalized is often the threshold that novices haven't crossed. The model must actively search for what it assumes rather than what it knows.

### Implications for Depth Allocation

Once identified, threshold concepts should receive disproportionate investment in the architecture:

- **More movements.** A threshold concept may need two or three movements rather than one — approaching from multiple angles, using multiple analogies, creating productive failure from different directions.
- **Earlier placement.** Threshold concepts should appear early in the architecture when possible — because everything after them depends on them.
- **More productive failure.** The listener needs to feel the inadequacy of their pre-threshold model more deeply for threshold concepts than for non-threshold content.
- **More constructive turns.** The listener needs to test their understanding at the threshold repeatedly — not just once — because mimicry is the default response to threshold difficulty.
- **Explicit naming.** The explanation should name the threshold as a threshold — "this is the idea that changes everything," "once you see this, the rest falls into place" — because metacognitive framing helps the listener invest appropriate effort.

---

## PART 3: Emotional Trajectory Management — Sustaining Engagement Across 30–60 Minutes

### The Missing Framework

The current prompt engineers emotion at the micro level — surprise → curiosity → confusion → resolution within individual movements. But it has no framework for managing the listener's emotional state across the full arc of a 30–60 minute piece. This matters because:

- Mental fatigue accumulates across movements and degrades emotional regulation capacity
- Boredom is a functional signal that the explanation has stopped generating prediction error — not a character flaw of the listener
- The insight-memory advantage (the "aha" moment) is neurochemically mediated and can be strategically placed
- Relief — a positive deactivating emotion — serves a restorative function that the current prompt doesn't account for

### Pekrun's Control-Value Framework

Pekrun's Control-Value Theory (2006) classifies achievement emotions along two dimensions:

|  | **Activating** | **Deactivating** |
|---|---|---|
| **Positive** | Enjoyment, hope, pride | Relief, relaxation, contentment |
| **Negative** | Anxiety, anger, shame, frustration | Boredom, hopelessness |

The effects on learning differ by quadrant:

**Positive activating emotions** (enjoyment, hope, pride) recruit cognitive resources, focus attention, promote interest and intrinsic motivation, and facilitate deep processing strategies. These are the emotions the explanation should sustain as its baseline operating state.

**Negative activating emotions** (anxiety, frustration, confusion) have complex effects. Moderate levels promote deeper processing and metacognitive engagement — confusion is the only individual emotion that significantly *predicts* learning, positively. But sustained anxiety or frustration without resolution depletes self-regulatory resources and triggers disengagement. The prompt handles this for confusion specifically but doesn't address the broader risk of sustained negative activation.

**Positive deactivating emotions** (relief, contentment) reduce immediate task attention and effort — but reinforce persistence and long-term investment. Relief after difficulty signals to the brain that the effort was worthwhile. This emotion is absent from the current prompt but is critical for sustaining engagement across long pieces: after a demanding passage, the listener needs to feel the reward of resolution before investing effort in the next challenge.

**Negative deactivating emotions** (boredom, hopelessness) reduce cognitive resources, undermine both intrinsic and extrinsic motivation, and promote surface processing. These must be prevented, not corrected.

### Boredom as Prediction Error Failure

Recent work in predictive processing (Gomez-Lavin & Ashkanasy, 2025; Elpidorou, multiple papers) reframes boredom as a signal of deviation from optimal cognitive engagement — a "cognitive homeostatic set point." The brain maintains a target level of prediction error: too much prediction error is overwhelming (anxiety); too little is boring. Boredom specifically signals that the environment has stopped generating enough prediction error to justify continued attentional investment.

This connects directly to the prompt's prediction error framework but extends it: boredom is what happens when prediction error drops to zero for too long. The listener's brain detects that its model is not being updated and signals that resources should be redirected elsewhere — manifesting as mind wandering, which occurs roughly a quarter of the time during sustained listening.

The implication for explanation design: **every stretch of the explanation must maintain non-zero prediction error.** Not constantly high — that would be exhausting — but consistently present. The listener's model must be in a state of continuous, moderate updating. When the explanation confirms expectations for too long without surprise, complication, or contradiction, boredom is the neurological consequence.

The prompt already says "engineering prediction error" at the micro level. What it lacks is the macro-level awareness that prediction error must be *paced* across the full piece — with variation in intensity but no sustained absence.

### The Insight Memory Advantage

A 2025 review in *Trends in Cognitive Sciences* (Kizilirmak et al.) synthesizes evidence that insight — the "aha!" moment — produces a specific and substantial memory advantage. The mechanism: the "insight as prediction error" hypothesis. When insight occurs, it represents a unique convergence of:

- **Novelty** — the solution was not predicted by the prior model
- **Surprise** — the prediction error is large and sudden
- **Reward** — the dopaminergic system fires because the prediction error has been *resolved*, not just detected
- **Enhanced encoding** — the hippocampus, mediated by dopamine and noradrenaline, encodes the surrounding content with enhanced strength

The nucleus accumbens — a core reward structure — activates during "aha" moments. The three primary emotions identified with insight are happiness, ease, and certainty. The "aha" experience is associated with positive affect reflecting the joy of comprehension and relief from the state of tension due to incomprehension.

For emotional trajectory: **insight moments are both encoding peaks and emotional rewards.** They are the payoff for the listener's investment of effort. They must be strategically placed — not clustered at the beginning (wasting the reward when the listener is still fresh) and not held entirely for the end (leaving the middle empty of reward).

### Fredrickson's Broaden-and-Build Theory

Fredrickson's broaden-and-build theory (2001) adds another mechanism: positive emotions don't just feel good — they broaden the listener's momentary thought-action repertoire. Joy sparks the urge to play. Interest sparks the urge to explore. Contentment sparks the urge to savor and integrate.

The cognitive implication: positive emotions expand the scope of attention, promote holistic processing, and increase attentional flexibility. A listener in a positive emotional state can hold more in working memory, see more connections, and process at a higher level of abstraction than a listener in a neutral or negative state.

This means: **the explanation should create positive emotional states *before* demanding the most complex cognitive work.** The delight of an insight in movement two creates the broadened cognitive state that enables the complex integration required in movement three. Positive emotions are not just motivational — they are cognitive infrastructure.

### Attention Restoration and Cognitive Recovery

The current prompt handles the "passive slide" — extended stretches without constructive engagement. But it does not address **cognitive fatigue** as a resource depletion problem that requires recovery intervals.

Research on directed attention fatigue shows that sustained effortful processing depletes a renewable but finite cognitive resource. Performance on tasks requiring these resources declines predictably over time. The micro-break effect demonstrates that even brief pauses during continuous cognitive activity yield significant performance gains.

For long-form audio, the listener cannot take a break. But the explanation can provide **cognitive recovery intervals** — passages of lower processing demand that allow partial restoration:

- A vivid, concrete narrative passage after a demanding abstract passage (the concrete requires less effortful processing while still engaging the listener)
- A moment of humor through content (not a joke — the absurdity of a situation, the strangeness of a fact) that shifts processing mode
- A brief revisitation of something already understood, applied to a new context (retrieval rather than encoding — less demanding but still productive)
- An explicit emotional resolution after a confusion arc (the relief itself serves as cognitive recovery)

The key principle: **recovery intervals are not wasted time — they are investments in the listener's capacity for the next demanding passage.** An explanation that maintains maximum cognitive demand throughout will produce declining returns as the listener's resources deplete.

### Engineering the Emotional Arc

Combining these frameworks, the emotional trajectory of a 30–60 minute piece should follow a specific pattern:

**1. Opening: Engagement and Trust (minutes 0–5)**
- Emotional target: interest (positive activating) + moderate surprise
- The listener should feel: "this is going to be worth my time"
- Mechanism: a compelling opening narrative that surfaces a surprising gap or contradiction, creating curiosity without demanding much background knowledge
- This is where the narrative mode is most important — transportation begins here or not at all

**2. First Investment: Productive Challenge (minutes 5–15)**
- Emotional target: curiosity → confusion → resolution (the micro-cycle the prompt already describes)
- The first threshold concept approach happens here, when primacy effects are strongest
- End this section with a clear insight moment — the first "aha" — which delivers reward and establishes the emotional contract: effort is rewarded

**3. Deepening: Escalating Challenge with Recovery (minutes 15–30)**
- This is the serial position danger zone — where attention is most fragile and recall is weakest
- Emotional target: alternating between challenge and resolution, with each cycle slightly more demanding
- Place the most vivid concrete narrative here (the attention re-earner)
- Include a relief beat after the hardest passage — a moment where the listener feels the reward of understanding before the next challenge
- At least one productive failure moment — the listener's model is tested and found wanting, creating the motivational energy to rebuild

**4. Synthesis and Peak: The Transformative Insight (final 10–15 minutes)**
- Emotional target: building tension → peak insight → delight → synthesis
- The peak-end rule means this section disproportionately determines the listener's overall evaluation
- The final insight should not just resolve the last question — it should reframe the opening, creating the experience of transformation
- The closing should leave the listener in a positive activating state (not relief/deactivation) — they should feel energized by the new understanding, not merely finished with the piece

### Specific Emotional Engineering Techniques

**The Reward Cycle.** Every 8–12 minutes, the listener should experience a complete emotional cycle: challenge → struggle → insight → delight. This is not the same as the prompt's constructive engagement turn (every 4–5 minutes) — the reward cycle is longer and encompasses multiple constructive turns. The constructive turns keep the listener active; the reward cycles keep them motivated.

**The Relief Beat.** After a particularly demanding passage — a threshold concept approach, a complex analogy, a productive failure moment — include a brief passage (30–60 seconds) of lower cognitive demand that acknowledges the difficulty implicitly. This is not a break from the content — it is a narrative passage that applies or extends what was just learned, using concrete, imageable language that requires less effortful processing. The function is dual: it provides cognitive recovery *and* it reinforces the just-learned content through a different encoding pathway.

**The Escalation Pattern.** The overall arc should escalate — each challenge slightly more demanding than the last, each insight slightly more powerful. This mirrors the flow state pattern: challenge and skill increasing in tandem. If the difficulty stays flat, boredom accumulates (the listener's model-building capacity exceeds the demand). If it jumps too sharply, anxiety and frustration overwhelm.

**The Emotional Foreshadow.** Before a demanding passage, create the emotional conditions for success: a small positive experience (a vivid image, a satisfying connection, a moment of delight) that broadens the listener's cognitive scope and creates the attentional flexibility needed for the upcoming challenge. This is the broaden-and-build theory operationalized as an explanation technique.

**Preventing Boredom Through Prediction Error Pacing.** Map the explanation's prediction error profile: where are the surprises, contradictions, and novel connections? If any stretch of more than 3–4 minutes has no prediction error — no surprise, no complication, no perspective shift — the listener's brain will signal disengagement. Fill these stretches with: unexpected connections to other domains, surprising applications of the concept, historical anecdotes that challenge assumptions, or constructive engagement turns that force the listener to discover something.

### Integration with Existing Prompt Architecture

The emotional trajectory framework does not replace the prompt's existing micro-level emotional engineering — it provides the macro-level container. The specific integration points:

- **The Audit** should include an emotional mapping step: where are the natural high-emotion moments in this topic? Where is the content most likely to be emotionally flat? Where will the listener need recovery?
- **The Architecture** should specify the emotional arc across movements, not just the conceptual sequence. Each movement should have a planned emotional state (challenge, recovery, insight, transition) in addition to its planned conceptual content.
- **The Writing** should include emotional pacing as a quality criterion: is this passage demanding enough to prevent boredom? Is it followed by sufficient recovery to prevent fatigue? Does this section deliver a reward that justifies the effort invested?
- **The Failure Modes** should include two new entries: "The Emotional Flatline" (extended passages with no emotional variation — neither challenge nor delight, just steady information delivery) and "The Exhaustion Spiral" (escalating difficulty without recovery beats, depleting the listener's regulatory resources until they disengage).

---

## Key Sources

### Narrative Transportation
- Green, M. C., & Brock, T. C. (2000). The role of transportation in the persuasiveness of public narratives. *Journal of Personality and Social Psychology*, 79(5), 701–721.
- Green, M. C., & Appel, M. (2024). Narrative transportation: How stories shape how we see ourselves and the world. *Advances in Experimental Social Psychology*, 69.
- Mar, R. A., Li, J., Nguyen, A. T., & Ta, C. P. (2021). Memory and comprehension of narrative versus expository texts: A meta-analysis. *Psychonomic Bulletin & Review*, 28, 732–749.
- Dahlstrom, M. F. (2014). Using narratives and storytelling to communicate science with nonexpert audiences. *PNAS*, 111(Suppl 4), 13614–13620.
- Bruner, J. (1985). Narrative and paradigmatic modes of thought. In E. Eisner (Ed.), *Learning and Teaching the Ways of Knowing*. University of Chicago Press.
- Norris, S. P., Guilbert, S. M., Smith, M. L., Hakimelahi, S., & Phillips, L. M. (2005). A theoretical framework for narrative explanation in science. *Science Education*, 89(4), 535–563.
- Soares, A. et al. (2023). Narrating science: Can it benefit science learning, and how? A theoretical review. *Journal of Research in Science Teaching*.

### Threshold Concepts
- Meyer, J. H. F., & Land, R. (2003). Threshold concepts and troublesome knowledge: Linkages to ways of thinking and practising within the disciplines. ETL Project, Occasional Report 4. University of Edinburgh.
- Meyer, J. H. F., & Land, R. (2005). Threshold concepts and troublesome knowledge (2): Epistemological considerations and a conceptual framework for teaching and learning. *Higher Education*, 49, 373–388.
- Land, R., Meyer, J. H. F., & Smith, J. (2008). *Threshold Concepts within the Disciplines*. Sense Publishers.
- Perkins, D. (1999). The many faces of constructivism. *Educational Leadership*, 57(3), 6–11.
- Kent, S. (2016). Threshold Concepts. Taylor Institute Guide Series #1. University of Calgary.

### Emotional Trajectory
- Pekrun, R. (2006). The control-value theory of achievement emotions: Assumptions, corollaries, and implications for educational research and practice. *Educational Psychology Review*, 18, 315–341.
- Pekrun, R. (2024). Control-value theory: From achievement emotion to a general theory of human emotions. *Educational Psychology Review*, 36, Article 109.
- Fredrickson, B. L. (2001). The role of positive emotions in positive psychology: The broaden-and-build theory of positive emotions. *American Psychologist*, 56(3), 218–226.
- Kizilirmak, J. M. et al. (2025). The neural basis of the insight memory advantage. *Trends in Cognitive Sciences*, 29(2).
- Gomez-Lavin, J. (2025). Boredom signals deviation from a cognitive homeostatic set point. *Communications Psychology*.
- Elpidorou, A. (2023). Synthesising boredom: A predictive processing approach. *Synthese*, 202, Article 166.
