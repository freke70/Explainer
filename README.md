# Explainer

AI-powered study tools: system prompts, research, and generated study materials.

## Structure

```
prompts/          System prompts (the "engines")
research/         Background research & cognitive science theory
tools/            Scripts & utilities (image generation, docx builder)
source/           Raw source material (textbook chapters, lecture notes)
output/           Generated content, organized per chapter/topic
```

## Tools

### Image Generation (`tools/google_generate.py`)

Generates educational diagrams via Google Gemini.

```bash
GOOGLE_AI_API_KEY=... python tools/google_generate.py \
  --prompt "your prompt" --output output/path.png
```

### DOCX Builder (`tools/build_docx.py`)

Converts a set of markdown summary files into a single .docx document.

```bash
cd output/ortho1/samenvatting && python build_docx.py
```

## System Prompts

| Prompt | Purpose |
|--------|---------|
| `prompts/samenvatting.md` | Cognitive learning architect — generates study summaries |
| `prompts/tts_explainer.md` | Long-form TTS explainer — 20-30 min audio scripts |
| `prompts/narrative_dilation.md` | Literary stylist — fiction/narrative writing |
