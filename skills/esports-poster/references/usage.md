# Usage

Use `esports-poster` when the user wants an esports result or preview poster and accuracy depends on current fixture data, team ordering, logos, time zones, or a reusable event visual system.

## Trigger Examples

- `查一下今天 MSI 的比赛结果，生成一张赛果海报。`
- `按明天 HLE 对 LYON 的赛程生成一张 4:5 预告图。`
- `胜者放前，比分和左右战队必须一致。`
- `使用刚才确认的 MSI 2026 风格重新生成结果图和预告图。`
- `把这几张已经通过的海报整理成可维护的赛事风格包。`
- `Generate a verified Worlds result poster and keep the winner, logo, and score order aligned.`

## Non-Trigger Examples

- `今天 MSI 比分是多少？`
- `分析一下 BLG 为什么赢 HLE。`
- `给我一个英雄联盟赛事新闻摘要。`
- `生成一个没有具体比赛信息的电竞背景图。`
- `制作直播 OBS 实时比分覆盖层。`

These requests may use search, writing, image generation, or broadcast tooling, but they do not require the full poster workflow.

## Mode Selection

### Result

Use when the series is complete and the final score is verified.

Required:

- tournament
- stage
- winner
- loser
- ordered final score
- optional advancement or elimination line
- verified team logos
- selected style pack

The winner appears first and defaults to the left. `LYON 3:0 G2` means LYON, LYON logo, and `3` occupy the same side.

### Preview

Use when the series is scheduled but not complete.

Required:

- tournament
- stage
- Team A
- Team B
- date
- exact local time
- time zone
- series format
- optional advancement implication
- verified team logos
- selected style pack

Do not show a score, winner marker, or language that implies a predetermined winner.

### Style Calibration

Use when the user approves a reference direction and wants it maintained across later posters.

Extract:

- canvas and safe area
- background and texture
- typography hierarchy
- primary and secondary accents
- logo treatment
- repeated geometric marks
- content density
- result layout
- preview layout
- forbidden motifs

Do not treat incidental text, one-off team colors, or accidental model artifacts as stable style tokens.

## Recommended Interaction

1. Verify the match record.
2. State the normalized record briefly.
3. Generate one poster per mode.
4. Correct factual or layout defects without changing the approved style pack.
5. After approval, synchronize the prompt source and skill references in the repository.

## Example Result Input

```text
Mode: result
Tournament: MSI 2026
Stage: Lower Bracket Round 3
Winner: LYON
Loser: G2
Score: 3:0
Primary language: Chinese
Style pack: MSI 2026
```

## Example Preview Input

```text
Mode: preview
Tournament: MSI 2026
Stage: Lower Bracket Final
Team A: HLE
Team B: LYON
Date: 2026-07-11
Time: 16:00
Timezone: Asia/Shanghai
Format: BO5
Next step: winner advances to the Grand Final against BLG
Primary language: Chinese
Style pack: MSI 2026
```
