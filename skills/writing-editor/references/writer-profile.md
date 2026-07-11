# Writer Profile

## Default Voice

Use this profile only when the user has not supplied a stronger writing sample.

- Chinese personal technical writing.
- Direct, calm, specific, and experience-based.
- Willing to make a judgment, but only as strong as the evidence allows.
- Practical rather than literary.
- Interested in boundaries, maintenance cost, failure modes, and why one option was rejected.
- Comfortable saying `我后来改了判断`, `这个方案能跑，但我不想继续扩大它`, or `这里我还没有验证`.
- Uses first person when the material is genuinely personal; does not force first person into neutral documentation.
- Prefers a clear verb and concrete noun over abstract management vocabulary.
- Ends on a decision, unresolved question, limitation, or next concrete step rather than inspiration.

## Voice Fingerprint

When the user provides previous writing, infer a local fingerprint before editing:

1. **Sentence rhythm:** short/long distribution, use of pauses, parentheticals, and fragments.
2. **Paragraph behavior:** direct opening, scene-first opening, or context-first opening.
3. **Judgment style:** firm, exploratory, skeptical, explanatory, or understated.
4. **Technical density:** how much code, naming, and implementation detail appears in prose.
5. **Transitions:** explicit connectors, implicit topic shifts, or question-led transitions.
6. **Lexicon:** habitual terms, preferred Chinese/English mixing, and words the author avoids.
7. **Emotional range:** neutral, frustrated, amused, uncertain, or reflective.
8. **Ending pattern:** decision, open issue, practical next step, or concise summary.

Match these patterns without copying errors or reproducing confidential details.

## Preferred Moves

- Start where the author actually encountered the problem.
- Name the constraint before praising the solution.
- Use `because`, `so`, and direct causality when the evidence supports it.
- Preserve rejected alternatives when they explain the choice.
- Keep specific project names, directory names, commands, and operational details.
- Allow an uneven but intentional rhythm: a short sentence can follow a dense technical paragraph.
- Compress repeated summaries into one final judgment.
- Turn abstract value claims into an observable change in work.

## Avoid

- Corporate-report voice.
- Public-account uplift.
- Fake vulnerability or staged confession.
- Generic confidence.
- Decorative metaphors.
- Uniform three-part structures.
- Stronger certainty than the author expressed.
- Rewriting every sentence into the same polished register.
- Treating casual phrasing as an error when it belongs to the author's voice.

## Project Context

For AICraft, Feeds Hub, Rustzen, and small developer tools, preserve:

- why the project exists
- what boundary was deliberately kept small
- what the author tried or rejected
- operational constraints
- current verification status
- maintenance and deployment costs
- the distinction between an experiment, an engineering reference, and a product
