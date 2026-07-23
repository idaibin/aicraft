---
name: ui-spec
description: "Use when a selected visual source or accepted UI surface must become an implementation-ready specification covering layout, states, interaction, responsive/accessibility behavior, component/token mappings, shared visual contracts, and acceptance; do not use for visual exploration, image generation, or frontend source edits."
compatibility: "Python 3.10+; PyYAML 6.0.2; jsonschema 4.25.1 with Draft 2020-12 support."
---

# UI Specification

## Overview

Turn a selected visual source and verified product facts into an implementation-ready UI contract, then hand it to `dev-frontend`. This Skill specifies an accepted direction; it does not explore visual directions, generate images, build prototypes, or edit product source.

## Workflow

1. Read effective repository guidance and run `git status --short` before planning an authorized artifact write.
2. Fix the selected visual source: a user-selected Product Design result, supplied screenshot/mockup/frame, accepted current surface, or accepted shared design-system revision. Record its identity, revision, approval, rights, `use`, and `ignore` boundaries. If no visual source has been selected and the user wants exploration, redesign, images, or a prototype, stop and route that work to the host's Product Design capability when available.
3. Fix the target surfaces, flows, and business domains, then count each independent
   implementation slice. For one page or flow, keep one Feature Spec. For multiple
   independent domains that share visual rules, create one short shared UI index and
   one independently loadable contract per confirmed domain; load
   [references/multi-surface.md](references/multi-surface.md). Route unresolved
   behavior, permissions, failure semantics, or product acceptance to `product-spec`.
4. Select one profile:
   - **Feature Spec (default):** specify one selected page or flow without changing shared semantics.
   - **Design System Spec (conditional):** specify an accepted revision only when shared tokens, component semantics, variants, state vocabulary, or product-wide visual rules must change.
5. Inspect only the selected visual source, live routes/components/tokens, DTO-shaped facts, accepted product artifacts, and scoped references needed for the profile. Treat pending, rejected, or stale artifacts as leads only; revalidate live owners and do not promote them implicitly.
6. Challenge only residual UI-contract ambiguity after product facts and the visual
   source are fixed. Resolve source and repository facts first; ask one material UI
   question at a time with a recommendation, trade-off, and affected slice, then stop
   when that slice's contract gates pass. Route product decisions back to
   `product-spec` and unselected visual direction to Product Design.
7. Translate the selected direction into explicit hierarchy, regions, layout ownership, density, semantic colors, typography roles, spacing and geometry, material, assets, copy, component/token mappings, required states and transitions, feedback ownership, responsive rules, focus, reduced motion, overflow, and acceptance checks. Mark every value as verified, extracted, proposed, or `Not verified`; an image does not prove exact tokens, behavior, accessibility, or runtime state.
8. Reuse current owners before declaring `adapt` or `new`. Keep Feature Spec changes local unless shared meaning actually changes; preserve one accepted shared-system owner and rollback path.
9. Apply deterministic truth, rights, required-state, mapping, responsive, accessibility, overflow, approval, and implementation-budget gates. Human rejection cannot be averaged away.
10. Produce the smallest specification artifacts that remove implementation ambiguity.
    Generate a structured change/evaluation manifest when an accepted Design System
    Spec revision changes. Create the durable
    `docs/ui/design-system/manifest.yaml` automation contract only when a verified
    repository consumer requires it. Ordinary Feature Specs that reuse current
    themes/components remain prose contracts.
11. For a durable design-system automation manifest, bind the human-readable design
    authority and declared machine assets by path and SHA-256, declare the real
    automation consumer, and fail validation on any mismatch. The manifest registers
    bindings only; it never introduces an independent design decision.
12. Validate authored artifacts with applicable local checks, then hand source work to `dev-frontend` and runtime evidence to `ops-browser` or `ops-client` without claiming implementation or runtime verification.

## Profiles

- **Feature Spec (default):** one selected page or flow contract; a multi-surface
  request may use a shared index plus independently loadable Feature Spec contracts,
  each with its own layout, mapping, states, interaction, responsive/accessibility
  rules, assets, acceptance, and readiness verdict.
- **Design System Spec (conditional):** accepted shared tokens, semantic components, variants, state vocabulary, or visual rules; may create, extract, maintain, or evaluate the repository-owned contract.

## Do Not Use For

- Visual exploration, image generation, redesign alternatives, UX research/critique, or shareable prototypes; use the host's Product Design capability when available.
- Unresolved product behavior, permissions, failure semantics, or acceptance; use `product-spec`.
- Frontend source changes or refactors; use `dev-frontend` with the accepted specification.
- Read-only frontend implementation audits; use `audit-frontend`.
- Browser screenshots, console/network evidence, or desktop-window operation; use `ops-browser` or `ops-client`.
- Git staging, commits, pushes, or branch cleanup; use `repo-delivery` after review.

## Hard Rules

- Require a selected visual source or accepted existing UI/design-system baseline before authoring a visual implementation contract.
- Do not generate or edit images, build prototype code, or edit product source.
- Do not invent metrics, features, routes, permissions, states, backend behavior, or runtime evidence.
- Do not treat pixels as proof of exact tokens, component ownership, behavior, accessibility, or implementation feasibility.
- Do not activate Design System Spec merely because a feature reuses existing tokens or components.
- Do not create a parallel component library or token system when the project already has an owner.
- Do not promote a present manifest when approval is absent, pending, rejected, or stale.
- Treat the accepted `DESIGN.md` or repository-native equivalent as the human-readable
  semantic authority. Treat `design-system/manifest.yaml` only as its machine-readable
  automation contract; reject stale authority hashes, stale binding hashes, undeclared
  consumers, independent decision fields, or a conflict policy other than failure.
- Require applicable loading, empty, error, populated, permission, focus, responsive, overflow, localization, and reduced-motion rules; justify exclusions.
- Do not merge independent business domains into one omnibus contract. Author only
  confirmed slice contracts, keep unconfirmed slices visible in the shared index,
  and mark the overall multi-surface result `Partial` until every requested slice has
  its own complete state, interaction, responsive/accessibility, mapping, and
  acceptance contract.
- Do not stage, commit, push, publish, or approve a shared baseline.

## Output Contract

Report the selected profile, source identity and approval, evidence basis, target
surfaces and slice boundaries, shared index and slice artifacts, verified/extracted/
proposed decisions, layout and state contract, component/token mappings, responsive/
accessibility rules, assets and copy, shared-system changes or `None`, structured
artifact reason or `Skipped`, evaluation gates, one `Ready for dev-frontend <slice>`
or blocker verdict per slice, overall `Complete` or `Partial`, handoff, validation,
and every `Not found` or `Not verified` gap. Never present a source image or
specification as implemented or runtime-verified UI.

## References

- See [references/usage.md](references/usage.md) for routing and artifact examples.
- See [references/workflow.md](references/workflow.md) for profile-specific specification and handoff details.
- See [references/visual-source.md](references/visual-source.md) when qualifying and translating the selected visual source.
- See [references/multi-surface.md](references/multi-surface.md) when a request covers more than one page, flow, or business domain.
- See [references/documentation-boundaries.md](references/documentation-boundaries.md) for durable UI locations, PRD links, and consumer reads.
- See [references/artifact-contract.md](references/artifact-contract.md) only for a shared Design System Spec package or accepted revision.
- See [references/evaluation-rubric.md](references/evaluation-rubric.md) for blockers and scoring.
- See [references/eval-cases.md](references/eval-cases.md) for trigger and quality evals.
