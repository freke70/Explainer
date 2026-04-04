#!/usr/bin/env python3
"""Direct Google Gemini image generation with safety_settings=BLOCK_NONE.

Usage:
    python google-generate.py --prompt "your prompt" --output output.png [--aspect-ratio 9:16]
"""

import argparse
import base64
import os
import sys

# Route through SOCKS5 proxy if available
try:
    import socks
    import socket
    if os.environ.get("SOCKS_PROXY_PORT"):
        _port = int(os.environ["SOCKS_PROXY_PORT"])
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", _port)
        socket.socket = socks.socksocket
except ImportError:
    pass

from google import genai
from google.genai import types

def main():
    parser = argparse.ArgumentParser(description="Google Gemini direct image generation")
    parser.add_argument("--prompt", required=True, help="Image prompt")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--aspect-ratio", default=None, help="Aspect ratio (e.g. 9:16, 16:9, 1:1)")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview", help="Model name")
    args = parser.parse_args()

    api_key = os.environ.get("GOOGLE_AI_API_KEY")
    if not api_key:
        print("Error: GOOGLE_AI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # All configurable safety categories set to BLOCK_NONE
    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]

    config = types.GenerateContentConfig(
        safety_settings=safety_settings,
        response_modalities=["TEXT", "IMAGE"],
    )

    print(f"Calling {args.model} (safety=BLOCK_NONE)...", file=sys.stderr)

    response = client.models.generate_content(
        model=args.model,
        contents=args.prompt,
        config=config,
    )

    # Create output directory
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    saved = False
    candidate = response.candidates[0] if response.candidates else None
    if not candidate or not candidate.content or not candidate.content.parts:
        finish = candidate.finish_reason if candidate else "no_candidate"
        print(f"Warning: No image generated. Finish reason: {finish}", file=sys.stderr)
        sys.exit(0)
    for part in candidate.content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            ext_map = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}
            ext = ext_map.get(part.inline_data.mime_type, ".png")
            out_path = args.output
            if not out_path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                out_path = os.path.splitext(out_path)[0] + ext
            with open(out_path, "wb") as f:
                f.write(part.inline_data.data)
            print(f"Image saved to: {out_path} ({len(part.inline_data.data)} bytes)", file=sys.stderr)
            saved = True
        elif part.text:
            print(f"Model text: {part.text[:300]}", file=sys.stderr)

    if not saved:
        finish = response.candidates[0].finish_reason if response.candidates else "unknown"
        print(f"Warning: No image generated. Finish reason: {finish}", file=sys.stderr)

    # Print usage
    if response.usage_metadata:
        u = response.usage_metadata
        print(f"Tokens — prompt: {u.prompt_token_count}, completion: {u.candidates_token_count}, total: {u.total_token_count}", file=sys.stderr)

    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
