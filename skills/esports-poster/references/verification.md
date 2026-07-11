# Verification

Verify facts before visual generation. Current results and schedules are time-sensitive.

## Source Priority

1. Official tournament schedule, bracket, standings, announcement, or broadcast.
2. Official league or organizer social post.
3. Established tournament database with a clear match page.
4. Reputable esports reporting that identifies the event and completed series.
5. Community discussion only as a discovery lead, never as the sole final authority when a better source exists.

Use at least one authoritative source for routine facts. Use a second source when official pages are incomplete, dynamic, region-redirected, or internally inconsistent.

## Result Verification

Confirm:

- match is complete
- tournament and year
- official stage
- final series score
- winner and loser
- bracket consequence
- whether `sweep`, `eliminated`, or `advances` language is accurate

Do not infer a final score from game discussion threads, live streams, partial scoreboards, or search snippets that may be stale.

## Preview Verification

Confirm:

- both teams are fixed rather than `TBD`
- official date
- official start time
- source time zone
- requested audience time zone
- stage
- format
- advancement consequence

If the official page still shows `TBD`, do not substitute a predicted team.

## Time-Zone Conversion

Record both source and output values:

```text
source_datetime:
source_timezone:
output_datetime:
output_timezone:
conversion_checked:
```

Use an IANA time zone when possible, for example:

- `Asia/Shanghai`
- `Asia/Seoul`
- `Europe/Berlin`
- `America/Los_Angeles`

Do not label KST as Beijing time or reuse a time from an earlier fixture.

## Team and Logo Verification

- Match the logo to the exact organization and current competitive team.
- Prefer transparent official assets or verified tournament assets.
- Do not use academy, legacy, fan-made, or geographic-city marks.
- Preserve logo proportions and clear space.
- If a usable logo cannot be verified, report it as unresolved instead of drawing an approximation.

## Conflict Handling

When sources disagree:

1. compare publication and event timestamps
2. prefer completed official bracket data over previews
3. identify whether one page is cached or region-shifted
4. state the conflict
5. do not generate until the match record is resolved

## Verification Record

```text
Status: verified | unresolved
Official source:
Secondary source:
Checked at:
Tournament:
Stage:
Mode:
Teams:
Score:
Date and time:
Timezone:
Format:
Advancement:
Logo assets:
Unresolved fields:
```
