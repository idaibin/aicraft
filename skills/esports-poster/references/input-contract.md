# Input Contract

Normalize user wording into this record before generating a poster.

## Shared Fields

| Field | Required | Rules |
| --- | --- | --- |
| `mode` | yes | `result`, `preview`, or `style-calibration` |
| `tournament` | yes | official event name and year |
| `stage` | yes | official or accurately translated stage name |
| `team_a` | yes | canonical display name and abbreviation |
| `team_b` | yes | canonical display name and abbreviation |
| `format` | usually | `BO1`, `BO3`, `BO5`, or sport-specific equivalent |
| `language` | yes | primary poster language |
| `style_pack` | yes | named reusable visual system or explicitly supplied reference |
| `logo_a` | yes for generation | supplied or verified asset |
| `logo_b` | yes for generation | supplied or verified asset |

## Result-Only Fields

| Field | Required | Rules |
| --- | --- | --- |
| `winner` | yes | must equal `team_a` or `team_b` |
| `score_a` | yes | belongs to `team_a` |
| `score_b` | yes | belongs to `team_b` |
| `advancement` | optional | verified next step only |
| `elimination` | optional | use only when the format confirms elimination |

Normalize result order before layout:

```text
display_left = winner
display_right = loser
display_left_score = winner_score
display_right_score = loser_score
```

A user-supplied order does not override this rule unless the user explicitly requires a fixed bracket orientation.

## Preview-Only Fields

| Field | Required | Rules |
| --- | --- | --- |
| `date` | yes | absolute date |
| `time` | yes | exact local clock time |
| `timezone` | yes | IANA zone or explicit audience label |
| `advancement` | optional | verified implication only |

Preview mode must not retain result-only fields. Remove stale score or winner data copied from a previous poster.

## Style Calibration Fields

| Field | Required | Rules |
| --- | --- | --- |
| `approved_references` | yes | user-approved images or official key art |
| `stable_tokens` | derived | colors, typography, texture, spacing, motifs |
| `layout_contracts` | derived | separate result and preview hierarchy |
| `forbidden_elements` | derived | rejected styles and recurring model errors |

## Normalization Rules

- Use absolute dates, not only `today` or `tomorrow`, in the internal record.
- Preserve the requested audience time zone. Convert from the official schedule time and record the conversion.
- Keep canonical team abbreviations consistent across text and logo labels.
- Distinguish `LYON` the esports team from unrelated geographic or academy entities.
- Treat `3-1`, `3:1`, and `3–1` as the same score, then render with the style pack's separator.
- Do not convert a scheduled matchup into a result record until completion is verified.
- If the user asks for two posters, create two normalized records and two independent outputs.
