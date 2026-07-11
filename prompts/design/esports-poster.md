# Esports Poster Generation Prompt

Use this standalone prompt for verified esports match-result or match-preview posters. It is the source-prompt counterpart of `skills/esports-poster`, but it must remain directly executable without installing the skill.

## Inputs

```text
Mode: result | preview
Tournament:
Stage:
Team A:
Team B:
Winner: result only
Score: result only
Date: preview only
Time: preview only
Timezone: preview only
Format:
Advancement or elimination:
Primary language:
Style pack:
Team logo references:
Approved visual references:
```

## Verification Gate

Before generating:

1. verify current results or schedules against an official tournament source
2. confirm the event year, stage, teams, format, and bracket consequence
3. convert the official schedule time to the requested audience time zone
4. verify that each logo belongs to the exact team
5. stop if the score, fixture, time, opponent, or logo cannot be resolved

Do not infer a final score from a live match.

## Shared Contract

```text
Canvas: 1080 x 1350
Aspect ratio: 4:5 vertical
One poster per image
Primary text: concise and readable
Team name, logo, and score side: always consistent
```

Do not combine a result and preview poster on the same canvas. Do not fabricate players, uniforms, sponsors, logos, rivalries, or advancement paths.

## Direct Prompt

```text
Generate one independent 4:5 vertical esports poster at 1080 x 1350 from the verified record below.

Mode: [result or preview]
Tournament: [tournament]
Stage: [stage]
Team A: [team A]
Team B: [team B]
Winner: [result only]
Score: [result only]
Date and time: [preview only]
Timezone: [preview only]
Format: [format]
Advancement or elimination: [verified consequence]
Primary language: [language]
Style pack: [style pack]
Team logo references: [assets]
Approved visual references: [assets]

For result mode:
- the completed winner must appear first and, by default, on the left
- winner name, logo, and score must stay on one side
- loser name, logo, and score must stay on the other side
- render the score as winner score : loser score
- use only verified sweep, advancement, or elimination language
- do not include preview time

For preview mode:
- both teams must have equal visual status
- use VS as the central separator
- show absolute date, exact time, time zone, stage, and format
- do not show a score, winner label, result label, or predetermined outcome

Apply the selected style pack without changing the verified facts.
Use real supplied or verified logos and preserve their proportions.
Keep the composition low to medium density with a clear one-glance hierarchy.
Keep the bottom area free of hashtags, follow prompts, generic slogans, and unrelated labels such as 近两日焦点.
```

## Negative Prompt

```text
wrong event or year
wrong stage
wrong score
wrong or approximate logo
team/logo/score side mismatch
loser first in result mode
score or winner marker in preview mode
result and preview combined
fabricated player or uniform
unverified advancement claim
garbled or duplicated text
long paragraphs
engagement footer
```

## Validation

- match record is verified
- mode is pure result or preview
- result winner is first
- result score order matches team order
- preview has no score or winner marker
- date, time, time zone, and format are exact
- logos match team names
- primary text is readable
- one poster occupies one `4:5` image
