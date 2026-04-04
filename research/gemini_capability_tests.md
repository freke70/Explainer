# Gemini Image Generation — Capability Test Results

**Model:** `gemini-3.1-flash-image-preview`
**Date:** 2026-04-04
**Test context:** Educational diagrams in Dutch for orthopedagogy study summaries

---

## Test Results Summary

| # | Diagram Type | Rating | Content Accuracy | Layout Quality | Text Readability | Notes |
|---|---|---|---|---|---|---|
| 1 | Tree diagram | **A** | All nodes correct | Clean hierarchy, proper parent-child lines | Excellent | Perfect for taxonomies/classifications |
| 2 | Venn diagram (3 circles) | **A** | All regions correct, overlap content placed correctly | Good circle overlap, colored regions | Good | Handles 3-circle Venn well — impressive overlap placement |
| 3 | Pro/con T-chart | **A** | All items correct both columns | Clean table with colored headers | Good | Simple but effective, green/red headers work |
| 4 | Decision tree | **A+** | All questions, branches, and outcomes correct | Perfect diamond→rectangle flow, color-coded outcomes | Excellent | YES/NO branching handled flawlessly. Best test result. |
| 5 | Concept map (8 nodes) | **B+** | All nodes and labels present, dashed feedback arrow works | Minor issue: "SOCIAIL" typo, duplicate "tolerantie varieert" label | Good | Workable but needs proofreading. Spatial layout is good but arrow labels get cramped at 8+ nodes |
| 6 | Fishbone/Ishikawa | **B+** | All categories and sub-items present | Correct fishbone structure, head on right | Good | Minor: added "matisering" (not in prompt — hallucinated sub-item under Cultuur). Structure is sound. |
| 7 | Feedback loop (5 nodes) | **A** | All nodes and labels correct, clockwise flow | Clean circular layout, numbered nodes, center label | Excellent | Circular arrow metaphor works perfectly |

### Plus 3 earlier production tests (from the Ortho1 summary):

| # | Diagram Type | Rating | Notes |
|---|---|---|---|
| 8 | Layer/tier diagram | **A+** | Sedimentenmodel. Flawless — correct gradient, labels, subtitle, annotation |
| 9 | Timeline (7 events) | **A+** | Historical timeline. Icons, color-coded tags, dates all correct |
| 10 | Causal flowchart (3 boxes + feedback) | **A** | Causale keten. Clean boxes, arrows, bullet lists inside boxes, feedback arrow |

---

## Tier Classification (Confirmed)

### Tier 1 — Reliable (generate confidently)

| Type | Confidence | Sweet spot | Prompting notes |
|---|---|---|---|
| **Layer/tier diagram** | Very high | 3-5 layers | Specify order (bottom=oldest), color gradient, labels + subtitles |
| **Timeline** | Very high | 5-10 events | Specify direction (left=earliest), name every event + date, describe annotation placement |
| **Decision tree** | Very high | 3-4 levels | Specify diamond=question, rectangle=answer, color-code outcomes, label branches JA/NEE |
| **Tree diagram** | Very high | Up to ~12 nodes | Specify top-to-bottom, name every node, describe branch structure |
| **Flowchart** | High | 3-8 nodes | Specify orientation, name every node and arrow label, use labeled arrows |
| **Feedback loop** | High | 3-6 nodes | Specify clockwise/CCW, name every node and arrow label, number the nodes |
| **Pro/con T-chart** | High | 5-7 items per side | Simple — just specify headers, items, and colors |
| **Venn diagram** | High | 2-3 circles max | Name every region explicitly including overlaps |

### Tier 2 — Usable with caution

| Type | Confidence | Risk | Mitigation |
|---|---|---|---|
| **Concept map** (8+ nodes) | Medium | Typos in labels, cramped arrow text, possible hallucinated connections | Limit to 6-8 nodes. Keep labels to 2-3 words. Proofread output. |
| **Fishbone diagram** | Medium | May hallucinate extra sub-items, diagonal text can be hard to read | Limit to 4 categories × 2-3 sub-items. Verify output against prompt. |

### Tier 3 — Use text/markdown instead

| Type | Why |
|---|---|
| **Complex concept map** (12+ nodes) | Crossing arrows, unreadable labels, unpredictable layout |
| **Argument map** (multi-level) | Requires precise opposing branches — too nuanced for image gen |
| **Multi-loop causal diagram** | Overlapping cycles become spaghetti |
| **Large comparison matrix** (>6 cols) | Text too small, better as markdown table |
| **Parallel timelines** | Vertical alignment across tracks is unreliable |

---

## Edit Mode — Fix Instead of Regenerate

The tool supports `--input image.png` to send an existing image back to Gemini with an edit prompt. Tested:

| Test | Edit instruction | Result |
|---|---|---|
| Fix typo | "Change SOCIAIL to SOCIAAL, remove duplicate node" | **Clean fix.** Both corrections applied, rest of diagram preserved exactly. |
| Translate labels | "Change YES/NO to JA/NEE" | **Perfect.** Only the labels changed, layout/colors/content identical. |

**Implications for the pipeline:**
- Tier 2 diagrams (concept maps, fishbone) become Tier 1 with one edit pass
- Workflow: generate → inspect → fix specific issues → done
- Much cheaper than regenerating from scratch (preserves the good parts)
- Can also be used for style changes (add color, change font emphasis) without re-prompting the full diagram

**Edit prompting tips:**
- Be surgical: name exactly what to change and say "keep everything else exactly the same"
- Reference specific text strings: "change 'SOCIAIL' to 'SOCIAAL'" not "fix the typo"
- One edit pass is reliable; chaining multiple edits may drift

---

## Key Findings

### What Gemini Does Exceptionally Well
1. **Geometric structure** — anything with boxes, arrows, circles, lines in a predictable layout
2. **Text-in-image** — Dutch text rendered clearly and accurately in most cases
3. **Color coding** — semantic use of color (green=positive, red=negative, gradient=chronological) handled well
4. **Following spatial instructions** — "top-to-bottom", "left-to-right", "clockwise" are reliably interpreted
5. **Convention recognition** — diamonds=decisions, rectangles=processes, circles=states are understood without explanation

### Where It Struggles
1. **Spelling at scale** — with 8+ labeled nodes, occasional typos appear ("SOCIAIL" instead of "SOCIAAL")
2. **Hallucinated content** — fishbone added a sub-item not in the prompt. Always verify output matches prompt.
3. **Dense arrow labels** — when many arrows converge on one node, labels overlap or get cramped
4. **Nuanced relationships** — "correlates with" vs. "causes" distinctions are hard to convey visually

### Prompting Patterns That Produce Best Results

1. **Name everything explicitly** — don't say "add some examples", say "sub-items: 'Ziekenhuis', 'Instelling', 'Psychiatrie'"
2. **Specify spatial layout** — "top-to-bottom", "horizontal, left to right", "clockwise circle"
3. **Specify shape semantics** — "diamond shapes for questions, rectangular boxes for answers"
4. **Specify color semantics** — "green header for voordelen, red header for nadelen"
5. **End with style instructions** — "Clean academic style, readable fonts, good contrast"
6. **Keep node count under 12** — quality drops noticeably above this threshold
7. **Keep labels to 1-5 words** — longer text gets cramped or truncated

---

## Production Recommendation

For the study summary pipeline, generate images for:
- **Every threshold concept** that has a spatial/structural component (sedimentenmodel, causale keten)
- **Every timeline** in historical chapters
- **Decision trees** for discrimination practice (which mensbeeld? which zorgvorm?)
- **Feedback loops** for systemic concepts (vicieuze cirkels)
- **Tree diagrams** for classifications/taxonomies

Do NOT generate images for:
- Comparison matrices (markdown tables are better — searchable, editable, no typo risk)
- Argument structures (too nuanced — use structured text)
- Content that is primarily textual (definitions, lists of characteristics)
