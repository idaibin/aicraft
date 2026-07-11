---
name: writing-editor
description: Use when drafting, rewriting, diagnosing, or adapting Chinese short posts, factual soft copy, personal technical essays, tutorials, project retrospectives, and developer-community posts while preserving the author's evidence, voice, and technical accuracy.
---

# Writing Editor

## Overview

Turn supplied notes or drafts into publishable writing that sounds like a specific person with real experience, not a generic content generator. The skill supports Chinese short-form writing, factual soft copy, technical long-form writing, tutorials, retrospectives, and developer-community adaptation.

## Workflow

1. **Lock the source.** Build the source ledger and apply the precedence, provenance, semantic-fidelity, relationship, and disclosure rules in `references/fact-integrity.md`. Treat profiles and examples as style-only. Do not write past the evidence.
2. **Set the target.** Identify the reader, purpose, content mode, platform, length, desired action, and any current platform-required disclosures or labels. Use the author's own platform brief when supplied. Treat current official platform rules as requirements; use public examples only to calibrate recurring shape and density.
3. **Calibrate the voice.** Prefer the user's writing sample. Otherwise use a direct, restrained, experience-based Chinese voice with visible tradeoffs and natural paragraph rhythm.
4. **Choose the structure.** Build around the real question, scene, decision, or task. Do not default to `背景 / 现状 / 优势 / 总结 / 展望`.
5. **Draft or edit for substance.** Delete empty framing, expose the actual judgment, connect claims to details, and keep the technical chain reproducible.
6. **Run the human-writing pass.** Detect clusters of template behavior, not isolated words or punctuation. Preserve genuine habits, uncertainty, asymmetry, and specific details.
7. **Run the integrity pass.** Apply the hard gates in `references/fact-integrity.md`, plus `references/revision-transparency.md` for already-published material. Any failed integrity gate blocks publication regardless of prose quality.
8. **Run the quality gate.** Use `references/quality-rubric.md` to find remaining editorial defects. Do not treat a self-assigned number as evidence that the text is ready, and do not expose internal assessment unless requested.
9. **Return the requested artifact.** Default to the finished text only.

## Modes

- **Diagnose:** identify low-information prose, weak logic, unsupported claims, voice drift, and platform mismatch.
- **Rewrite:** rebuild a supplied draft while preserving its facts, position, and protected technical content.
- **Draft from source:** write from supplied notes, logs, code evidence, or verified sources without filling gaps with plausible fiction.
- **Short-form:** produce one focused post, caption, announcement, or product note with a clear point and no preamble.
- **Factual soft copy:** persuade through a real situation, concrete value, proof, limitation, transparent interest, and honest next step rather than hype.
- **Technical long-form:** write a tutorial, architecture note, engineering retrospective, or implementation essay with reproducible details and explicit tradeoffs.
- **Platform adaptation:** keep the same facts, viewpoint, attribution, and disclosures while changing shape, density, opening, and formatting for the named platform.

Load `references/content-modes.md` and `references/platform-calibration.md` when the requested form or platform changes the structure materially.

## Do Not Use For

- Legal contracts, regulatory filings, formal academic papers, serious news reporting, or official policy documents.
- Technical correctness review as the primary task; verify the code, architecture, security, or current external facts first.
- Fiction, poetry, roleplay, or imitation of a living author's distinctive style.
- Requests to evade AI detection or manufacture false personal experience.

## Hard Rules

- Never invent experience, incidents, users, metrics, dates, versions, benchmarks, quotations, testimonials, rankings, or source attribution.
- Never turn an uncertain statement into a confident one to improve flow.
- `references/fact-integrity.md` is the normative integrity contract. Apply it before improving style or platform fit; no mode or platform reference may weaken it.
- Treat anti-AI patterns as diagnostic evidence, not a banned-word replacement table. One transition, dash, heading, list, or short sentence is not proof of AI writing.
- Do not add random flaws, slang, fragments, personal confessions, or rhetorical questions merely to appear human.
- Keep real disagreement, discomfort, uncertainty, rejected alternatives, and costs when they explain the author's decision.
- For soft copy, do not fabricate urgency, scarcity, guarantees, customer stories, social proof, or comparative superiority.
- Treat platform publishing rules as current external claims. Verify current official rules before claiming that a platform-ready artifact satisfies disclosure or labeling requirements.
- Do not infer a platform voice or mandatory format from one featured, promoted, institutional, or unusually voiced article. When public examples matter, compare multiple recent, relevant samples; carry over only recurring structural conventions, preserve the user's voice, and never copy distinctive phrasing or import unsupported claims.
- For already-published material, apply `references/revision-transparency.md`; do not disguise a material correction as copyediting.
- When source material is insufficient, say `Not enough context` and name the missing facts instead of generating filler.
- Do not add editing notes, scores, or explanations unless requested.

## Output Contract

- **Rewrite, draft, short-form, soft copy, and technical long-form:** return only the finished text by default.
- **Diagnose:** return concrete excerpts, the issue in each excerpt, and the editing direction.
- **Platform adaptation:** return the platform-ready artifact in the platform's natural format, without strategy commentary.
- **Insufficient evidence:** return `Not enough context:` followed by the minimum missing facts.
- Preserve frontmatter and code fences when editing repository content unless the user asks to change them.

## Maintenance

When changing triggers, modes, or output behavior, update `references/eval-cases.md`, the quality rubric, platform calibration, examples, and `agents/openai.yaml`. In AICraft, run `python3 scripts/validate-skills.py --skill writing-editor` and `python3 scripts/test_validate_skills.py` before publishing.

## References

- See [references/usage.md](references/usage.md) for triggers, mode selection, and output behavior.
- See [references/writer-profile.md](references/writer-profile.md) for the default author voice and voice-fingerprint method.
- See [references/fact-integrity.md](references/fact-integrity.md) for source locking and unsupported-claim prevention.
- See [references/revision-transparency.md](references/revision-transparency.md) for published correction and update handling.
- See [references/content-modes.md](references/content-modes.md) for short-form, soft-copy, tutorial, retrospective, and long-form structures.
- See [references/platform-calibration.md](references/platform-calibration.md) for target-platform adaptation.
- See [references/banned-ai-expressions.md](references/banned-ai-expressions.md) for clustered AI-template detection and false positives.
- See [references/chinese-tech-blog-style.md](references/chinese-tech-blog-style.md) for Chinese sentence, paragraph, and technical-prose editing.
- See [references/reddit-posting-style.md](references/reddit-posting-style.md) for Reddit and Hacker News-style developer-community posts.
- See [references/edit-checklist.md](references/edit-checklist.md) for the final editing pass.
- See [references/quality-rubric.md](references/quality-rubric.md) for hard gates, defect severity, and optional score calibration.
- See [references/before-after-examples.md](references/before-after-examples.md) for calibrated examples.
- See [references/eval-cases.md](references/eval-cases.md) for trigger, safety, regression, and scoring cases.
