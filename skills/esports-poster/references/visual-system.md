# Visual System

Separate match facts from visual styling. A style pack may change color, typography, texture, and motifs, but it must not change result or preview semantics.

## Shared Poster Contract

```text
Canvas: 1080 x 1350
Aspect ratio: 4:5 vertical
Safe margin: approximately 60 to 80 px
Primary language: user-selected
Output: one independent poster per image
Density: low to medium
```

Shared hierarchy:

1. tournament
2. stage and mode
3. teams
4. score or `VS`
5. result headline or preview time
6. optional verified consequence

Keep logo areas balanced. Never assign a logo, name, or score to different sides.

## Result Layout Contract

```text
Tournament header
Stage · 赛果
Winner/series label
Winner logo and name | loser logo and name
Winner score : loser score
Short factual headline
Optional advancement or elimination line
```

The winner appears first and defaults to the left. Visual emphasis may favor the winner, but the loser must remain readable.

## Preview Layout Contract

```text
Tournament header
Stage · 预告
Stage label · format
Team A logo and name | VS | Team B logo and name
Short matchup headline
Absolute date · exact time
Time zone · format
Optional verified advancement implication
```

Both teams have equal visual status. Do not use result labels.

## MSI 2026 Style Pack

Use for the approved MSI 2026 direction.

```text
Background: warm gray-white or off-white printed paper
Primary text: near-black
Primary accent: signal red or red-orange rough brush bar
Secondary accent: sparse acid-lime detail
Typography: oversized extra-condensed heavy sans-serif
Texture: subtle paper grain, restrained print noise, light scratches
Motifs: thin technical lines, target marks, small coordinate-like details
Composition: flat editorial sports graphic, asymmetric but controlled
Whitespace: strong
```

Required character:

- modern international tournament editorial design
- crisp hierarchy
- limited palette
- restrained rough-print energy
- no separate full-color background for each team

Forbidden for this style pack:

- black-gold luxury treatment
- beige-gold premium template
- purple sci-fi template
- blue-orange split battlefield
- cinematic fire, lightning, explosions, dragons, phoenixes, or lions
- dense HUD overlays
- metallic 3D typography
- glassmorphism cards
- player head collages
- `近两日焦点`
- result and preview combined on one canvas

## Style Calibration Rules

When the user approves a generated poster:

1. record only repeatable visual tokens
2. separate event identity from team identity
3. capture result and preview layouts independently
4. add rejected visual directions to the forbidden list
5. add an eval case for every repeated failure
6. test the pack with at least one different matchup before declaring it stable

Official artwork is a reference system, not a tracing target. Do not reproduce a source poster pixel-for-pixel.
