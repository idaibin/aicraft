# Eval Cases

Use these cases when changing `esports-poster` triggers, modes, verification, style packs, prompts, or output contracts.

## Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `查一下今天 MSI 的结果，按官方风格生成赛果海报。` | Should trigger `esports-poster` in Result mode and verify the completed series before generation. | Current result research plus poster generation. |
| `明天 HLE 对 LYON，做一张 4:5 预告图，时间用北京时间。` | Should trigger Preview mode, verify the fixture, and convert the time zone. | Scheduled fixture with exact poster contract. |
| `胜者放前，左右战队、Logo 和比分必须一致。` | Should trigger or continue Result mode and enforce ordered mapping. | Core result-layout contract. |
| `把这套 MSI 海报风格整理成以后能复用的规范。` | Should trigger Style Calibration mode. | Reusable event visual-system maintenance. |
| `Generate a Worlds result poster after checking the official bracket.` | Should trigger Result mode. | Generic esports fixture and poster workflow. |

## Non-Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `MSI 今天谁赢了？` | Should not require `esports-poster`; answer the score query. | No poster requested. |
| `分析 BLG 这场团战为什么赢。` | Should not trigger `esports-poster`. | Match analysis, not visual generation. |
| `生成一个赛博朋克电竞背景。` | Should not trigger `esports-poster`. | No fixture, result, preview, or reusable event contract. |
| `给 OBS 做一个实时比分插件。` | Should not trigger `esports-poster`. | Broadcast software implementation. |
| `把官方 MSI 海报一比一复制。` | Should not execute as requested. | Exact reproduction boundary. |

## Quality Eval

| Case | Expected evidence | Reject if |
| --- | --- | --- |
| Current-data verification | Uses an official source, records absolute date/time, and resolves stage, teams, format, and consequence before generation. | Relies on memory, treats live data as final, or invents a bracket path. |
| Result ordering | Winner is first; winner name, logo, and score occupy one side; loser fields occupy the other. | Loser appears first or any name/logo/score mapping is crossed. |
| Preview purity | Shows `VS`, date, time, time zone, stage, and format with equal team status. | Contains any score, winner label, result copy, or implied outcome. |
| Multi-output request | Produces independent result and preview images with separate normalized records. | Combines both posters on one canvas. |
| Logo integrity | Uses supplied or verified team assets with preserved proportions. | Draws an approximate logo or uses an academy, legacy, or unrelated mark. |
| MSI 2026 style | Uses gray-white paper, near-black condensed type, red-orange brush marks, sparse acid-lime, low density, and strong whitespace. | Uses black-gold, purple sci-fi, split team-color backgrounds, fantasy action scenes, or dense HUD effects. |
| Text integrity | Chinese and numeric information are readable, short, and non-duplicated. | Contains malformed Chinese, repeated labels, long copy, or unrelated footer text. |
| Missing data | Stops and reports unresolved fields and checked sources. | Generates plausible but unverified content. |
| Style calibration | Extracts repeatable tokens, separates team identity from event identity, and adds failure cases. | Treats incidental composition or model artifacts as fixed rules. |

## Scoring

Score each quality case from 0 to 10.

Minimum pass:

- every trigger and non-trigger expectation is correct
- no factual hallucination
- result-order and preview-purity cases score 10
- every other quality case scores at least 7
