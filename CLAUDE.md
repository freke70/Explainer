# CLAUDE.md — Workflow & Approach for Future Sessions

## What This Project Is

AI-powered study tool pipeline: take raw study material (textbook chapters, lecture notes) and produce cognitively engineered study summaries, TTS audio scripts, and educational diagrams. The target user is a Flemish university student (orthopedagogy / social sciences).

## The Approach That Works

### 1. Read the System Prompt First

The summary system prompt lives at `prompts/samenvatting.md`. It's not a template — it's a cognitive science framework. Read it before generating anything. The key paradigms:
- Cognitive Load Theory (manage working memory, eliminate extraneous load)
- Generative Learning (force the learner to DO cognitive work, not just read)
- Schema Theory (chunk, hierarchize, connect — not flat bullet lists)
- Transfer-Appropriate Processing (design for the EXAM, not for coverage)
- Retrieval Practice Design (the summary is a testing interface, not a reading document)

### 2. Read ALL Source Material Before Writing Anything

Read the entire source text in chunks. Don't start writing after the first page. You need the full picture to identify:
- **Threshold concepts** (the 2-3 ideas that unlock everything else)
- **The expert's organization** (which may differ from the textbook's chapter order)
- **Knowledge structures** (causal, comparative, hierarchical, procedural — different structures need different formats)

### 3. Multi-File Structure, Not One Monolith

Split the summary into files by **cognitive function**, not by chapter section:

| File type | Purpose | Example |
|-----------|---------|---------|
| Leerarchitectuur | Meta-document: diagnosis, study instructions, file map | `00_Leerarchitectuur.md` |
| Kernkader | Conceptual skeleton: the organizing framework the student should internalize first | `01_Kernkader.md` |
| Historisch/Inhoudelijk overzicht | Detailed content with cue-columns for self-testing | `02_Historisch_Overzicht.md` |
| Vergelijkingsmatrix | Discrimination instrument for distinguishing similar concepts | `03_Vergelijkingsmatrix.md` |
| Transfer/Toepassing | Connecting theory to practice, past to present, abstract to concrete | `04_Verleden_is_Heden.md` |
| Zelftoets | Active retrieval: fill-in-the-blank, matching, open questions, flashcards | `05_Zelftoets.md` |

This structure works because each file serves a different study mode (overview vs. deep study vs. discrimination practice vs. self-test). A single document can't optimize for all of these simultaneously.

### 4. Generate Educational Diagrams with Gemini

The Gemini image model (`tools/google_generate.py`) is excellent at structured educational visuals. Use it for:
- **Conceptual diagrams** (the sedimentenmodel, causal chains)
- **Timelines** (historical overviews with labeled periods)
- **Flowcharts** (decision trees, process flows)
- **Comparison visuals** (when a table isn't enough)

**Prompting approach that works:**
- Be extremely specific: name every element, label, subtitle, and annotation
- Specify language (Dutch/Flemish)
- Specify style ("clean, academic style, readable fonts, good contrast")
- Specify orientation ("landscape")
- Describe the spatial layout ("horizontal layers stacked on top of each other", "horizontal timeline from left to right")
- The model handles text-in-images well — don't shy away from detailed labels

**Edit mode:** Pass `--input existing.png` to fix issues without regenerating from scratch. Be surgical: "Change 'SOCIAIL' to 'SOCIAAL'. Keep everything else exactly the same." This makes Tier 2 diagrams (concept maps, fishbone) reliable — generate → inspect → fix.

**API key env var:** `GOOGLE_AI_API_KEY`
**Default model:** `gemini-3.1-flash-image-preview`

After generating, embed directly in the markdown: `![Alt text](img/filename.png)`

### 5. Build DOCX for Offline Use

`tools/build_docx.py` (and a copy in each summary folder as `build_docx.py`) converts the markdown files into a single .docx. Key decisions:
- **No page breaks between sections** — it should flow as one continuous document
- Title page with page break, then continuous flow
- Tables with shaded headers
- Blockquotes with left border (via XML)
- Images embedded inline at ~5.5 inches width
- `<details>` tags converted to visible text (since docx has no collapsible sections)
- Navigation tables stripped (not useful in a single doc)
- Code blocks in Consolas on grey background

### 6. Everything in Flemish Dutch

All output content (summaries, diagrams, self-tests) should be in Flemish Dutch. System prompts and research docs stay in English.

## Repo Structure

```
prompts/          System prompts (the engines)
research/         Cognitive science background
tools/            Scripts (image gen, docx builder)
source/           Raw input material
output/           Generated content, per chapter:
  output/ortho1/
    samenvatting/   Multi-file summary + images + docx
    tts_claude.txt  TTS audio script
    tts_gemini.txt  TTS audio script (Gemini version)
```

## Key Mistakes to Avoid

- **Don't compress, extract.** The summary's hierarchy should reflect the expert's conceptual organization, not mirror the textbook's chapter structure.
- **Don't make a comfort document.** If it's pleasant to re-read, it's probably not forcing retrieval. Embed cue-columns, blanks, `<details>` blocks, self-test prompts.
- **Don't spread effort evenly.** Invest disproportionately in threshold concepts. Even coverage is the enemy of strategic learning.
- **Don't skip the diagnosis phase.** Identify discipline, knowledge type, exam format, learner level, and threshold concepts BEFORE writing.
- **Don't use one format for everything.** Different knowledge structures need different formats within the same summary (tables for comparison, causal chains for mechanisms, cue-columns for recall).
