# Prompt Templates

Replace every bracketed field before generation. Remove mode-inapplicable lines.

## Result Poster

```text
Generate one independent 4:5 vertical esports result poster at 1080 x 1350.

Verified match record:
Tournament: [tournament]
Stage: [stage]
Winner: [winner]
Loser: [loser]
Final score: [winner score] : [loser score]
Format: [format]
Advancement or elimination: [verified consequence]
Primary language: [language]
Style pack: [style pack]
Logo references: [winner logo], [loser logo]
Visual references: [approved style references]

Result contract:
- Put the winner first and, by default, on the left.
- Keep winner name, winner logo, and winner score on the same side.
- Keep loser name, loser logo, and loser score on the same side.
- Display the score as winner score : loser score.
- Mark the poster as a completed result.
- Use one short factual headline.
- Use advancement, elimination, or sweep language only when verified.
- Do not include preview time, a future score, or unrelated footer content.

Apply the selected style pack without changing the verified match record.
Use real supplied or verified logos; do not redesign them.
Keep all primary text readable and free of duplicated or malformed characters.
```

## Preview Poster

```text
Generate one independent 4:5 vertical esports match-preview poster at 1080 x 1350.

Verified fixture record:
Tournament: [tournament]
Stage: [stage]
Team A: [team A]
Team B: [team B]
Date: [absolute date]
Time: [exact local time]
Timezone: [timezone]
Format: [format]
Advancement implication: [verified consequence]
Primary language: [language]
Style pack: [style pack]
Logo references: [team A logo], [team B logo]
Visual references: [approved style references]

Preview contract:
- Give both teams equal visual status.
- Keep each team name and logo on the same side.
- Use VS as the only central matchup separator.
- Show the absolute date, exact time, time zone, stage, and format.
- Do not show a score.
- Do not use WINNER, SERIES RESULT, eliminated, advances, or any predetermined outcome.
- Do not include unrelated footer content.

Apply the selected style pack without changing the verified fixture record.
Use real supplied or verified logos; do not redesign them.
Keep all primary text readable and free of duplicated or malformed characters.
```

## MSI 2026 Style Addition

Append this block when `style_pack = MSI 2026`:

```text
Use a warm gray-white printed-paper background, near-black oversized extra-condensed typography, a signal-red or red-orange rough brush bar, and very sparse acid-lime accents. Add only subtle paper grain, restrained print noise, thin technical lines, target marks, or small coordinate-like details. Keep the composition flat, editorial, asymmetric but controlled, and low to medium density with strong whitespace.

Do not use black-gold luxury styling, beige-gold templates, purple sci-fi styling, blue-orange split backgrounds, cinematic fire or lightning, fantasy animals, dense HUD overlays, metallic 3D lettering, glass panels, player collages, or the phrase 近两日焦点.
```

## Negative Prompt

```text
wrong tournament
wrong year
wrong stage
wrong team logo
approximate or redrawn logo
academy or legacy logo
team and score side mismatch
loser shown first in result mode
score in preview mode
winner marker in preview mode
result and preview combined
fabricated player
fabricated uniform
fabricated sponsor
unverified advancement claim
duplicated text
garbled Chinese
long paragraph
engagement bait
hashtag footer
近两日焦点
```
