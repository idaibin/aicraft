---
name: ui-design
description: "Use when a concrete page or flow needs evidence-grounded visual and interaction design before frontend implementation, or shared tokens, component semantics, variants, or the product-wide visual system must change."
---

# UI Design

## Overview

Design a concrete product surface from verified facts and hand it to `dev-frontend`. Default to the smallest **Feature UI** profile for one page or flow. Activate the **Design System** profile only when shared tokens, component semantics, variants, or the product-wide visual language must change.

## Workflow

1. Read effective repository guidance and run `git status --short` before planning an authorized artifact write.
2. Fix the target page or flow, audience, user job, facts, available actions, required states, platform, existing UI owners, evidence gaps, and forbidden inventions.
3. Select one profile:
   - **Feature UI (default):** produce the visual and interaction solution for one page or flow, including relevant wireframes, high-fidelity views, interaction states, responsive behavior, and a bounded `dev-frontend` handoff.
   - **Design System (conditional):** load shared-system artifacts only when the requested surface changes reusable tokens, component semantics, variants, or the overall visual language. Keep one accepted owner and preserve rollback when changing it.
4. Inspect only the current screenshots, routes, components, tokens, DTO-shaped product facts, and scoped references needed for the selected profile. Mark missing evidence `Not found` or `Not verified`.
5. Give every external reference explicit source, rights status, `use`, and `ignore` constraints. A reference never authorizes copying brand, content, or functionality.
6. Define one coherent direction grounded in the product subject: hierarchy, layout, density, palette, typography roles, material, interaction tone, required states, and one justified signature element.
7. Produce the smallest artifact set that makes the design comparable and implementable. Use the package schema and manifest only for a shared Design System revision, not for every Feature UI task.
8. Apply deterministic truth, rights, state, overflow, accessibility, and implementation-budget gates before visual judgment. Human rejection cannot be averaged away.
9. When image generation or editing is needed, ask the host's image tool to render the constrained concept. This Skill owns facts, direction, prompts, comparison, and handoff—not the image runtime or its success claim.
10. Validate authored artifacts with applicable local checks, then hand source/runtime work to `dev-frontend`, `ops-browser`, or `ops-client` without claiming implementation or runtime verification.

## Profiles

- **Feature UI (default):** one page or flow; concrete visuals, states, responsive and interaction rules, and implementation handoff.
- **Design System (conditional):** shared tokens, semantic components, variants, or overall visual-system change; may create, extract, maintain, or evaluate the accepted shared package.

## Do Not Use For

- Unresolved product behavior, permissions, failure semantics, or acceptance; use `product-spec`.
- Frontend source changes or refactors; use `dev-frontend` with the accepted design artifacts.
- Read-only frontend implementation audits; use `audit-frontend`.
- Browser screenshots, console/network evidence, or desktop-window operation; use `ops-browser` or `ops-client`.
- Git staging, commits, pushes, or branch cleanup; use `repo-delivery` after review.

## Hard Rules

- Do not invent metrics, features, routes, permissions, states, backend behavior, or runtime evidence.
- Do not activate the Design System profile merely because a page uses existing tokens or components.
- Do not create a parallel component library or token system when the project already has an owner.
- Keep product colors, geometry, copy, and brand rules in project artifacts, not this reusable Skill.
- Require applicable loading, empty, error, populated, permission, focus, responsive, and reduced-motion states; justify exclusions.
- Keep image, prototype, browser, time, cost, and storage budgets finite.
- Do not edit product source, operate runtime tools directly, stage, commit, push, publish, or approve a shared baseline.

## Output Contract

Report the selected profile, evidence basis, target page/flow, visual direction, primary artifacts, required states and interactions, shared-system changes or `None`, evaluation gates, `dev-frontend` handoff, validation, and every `Not found` or `Not verified` gap. Never present a mockup, generated image, or prototype as implemented or runtime-verified UI. An explicitly requested independent external challenge/research may hand one fixed question to `ask-chatgpt`; it never implies sending.

## References

- See [references/usage.md](references/usage.md) for routing and artifact examples.
- See [references/workflow.md](references/workflow.md) for profile-specific design and handoff details.
- See [references/visual-direction.md](references/visual-direction.md) for distinctive direction and self-critique.
- See [references/artifact-contract.md](references/artifact-contract.md) only for a shared Design System package or accepted revision.
- See [references/evaluation-rubric.md](references/evaluation-rubric.md) for blockers and scoring.
- See [references/eval-cases.md](references/eval-cases.md) for trigger and quality evals.
