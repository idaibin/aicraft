---
name: esports-poster
description: Use when researching or generating esports match-result or match-preview posters that require verified scores, schedules, time zones, team order, logos, and a reusable event visual system.
---

# Esports Poster

## Overview

Research, normalize, and generate accurate esports result or preview posters. Keep match facts separate from visual styling, use verified team assets, and apply a reusable event style pack without mixing result and preview contracts.

## Workflow

1. Classify the request as **Result**, **Preview**, or **Style Calibration**.
2. Normalize the required fields with [references/input-contract.md](references/input-contract.md).
3. Verify current scores, schedules, stages, formats, time zones, and advancement paths with [references/verification.md](references/verification.md).
4. Select the event style pack and layout contract from [references/visual-system.md](references/visual-system.md).
5. Build the generation instruction from [references/prompt-templates.md](references/prompt-templates.md).
6. Generate one independent `4:5` poster per requested output.
7. Validate team order, logo mapping, score mapping, time, mode purity, typography, and forbidden elements before delivery.

## Modes

- **Result:** completed series only. Put the verified winner first and, by default, on the left. Keep team name, logo, and score order identical.
- **Preview:** upcoming series only. Show equal team status, `VS`, date, time, time zone, stage, and format. Do not show a score or winner marker.
- **Style Calibration:** derive or revise a style pack from approved references. Separate stable visual tokens from one-off composition details, then update quality evals before treating the style as reusable.

## Do Not Use For

- General image generation unrelated to esports fixtures.
- Plain score lookup, standings, news summaries, or match analysis when no poster is requested.
- Live-match graphics that require frame-by-frame score updates or broadcast overlays.
- Exact reproduction of copyrighted official artwork, sponsor lockups, or player photography without supplied rights-cleared assets.

## Hard Rules

- For current or recent fixtures, verify facts before generation; do not rely on memory.
- Prefer official tournament schedules, brackets, announcements, and broadcasts. Use authoritative secondary sources only when official pages are incomplete.
- Do not infer a final score from an in-progress match.
- Stop and report unresolved facts instead of generating a misleading poster.
- Use real supplied or verified team logos. Do not redraw approximate logos.
- Do not fabricate players, uniforms, sponsors, venues, rivalries, or advancement paths.
- Generate result and preview posters as separate images.
- Default canvas is `1080 x 1350`, `4:5` vertical.
- Result mode: winner first; score order must exactly match team order.
- Preview mode: no score, `WINNER`, `SERIES RESULT`, or implied winner.
- Keep the bottom area free of unrelated engagement copy such as `近两日焦点`, hashtags, follow prompts, or generic slogans.
- A published skill must remain self-contained. Repository-level prompts may be maintained as source assets but are not runtime dependencies.

## Output Contract

Before generation, establish a compact verified match record:

```text
Mode:
Tournament:
Stage:
Team order:
Score: result only
Date and time: preview only
Time zone:
Format:
Advancement path:
Style pack:
Verification status:
```

Generate the requested poster only after required fields are verified. If the image tool requires image-only completion, provide the verification record before the tool call.

For unresolved data, output the missing or conflicting field and the sources checked. Do not generate the poster.

## Skill Maintenance

When triggers, modes, verification rules, style packs, or output contracts change, update `references/usage.md`, `references/input-contract.md`, `references/verification.md`, `references/visual-system.md`, `references/prompt-templates.md`, `references/eval-cases.md`, and `agents/openai.yaml`. Keep the repository-level prompt synchronized as a standalone source asset, but do not make this skill depend on it.

## References

- See [references/usage.md](references/usage.md) for triggers, mode selection, and operating examples.
- See [references/input-contract.md](references/input-contract.md) for required fields and normalization rules.
- See [references/verification.md](references/verification.md) for result, schedule, time-zone, and asset verification.
- See [references/visual-system.md](references/visual-system.md) for shared layout rules and the MSI 2026 style pack.
- See [references/prompt-templates.md](references/prompt-templates.md) for result, preview, and negative prompt templates.
- See [references/eval-cases.md](references/eval-cases.md) for trigger, non-trigger, quality, and scoring evals.
