---
name: audit-frontend
description: "Use when auditing complex or cross-cutting frontend architecture across React, TypeScript, Vite, TanStack Router, shadcn/ui or local component systems, high-density consoles, and Tauri desktops, especially for component reuse, file ownership, state/data boundaries, layout consistency, accessibility, performance, and documentation alignment."
---

# Frontend Audit

## Overview

Audit complex frontend work from repository evidence rather than a universal
folder template. This skill is read-only by default and reports findings; use
`implement-frontend` when the requested outcome includes code changes.

## Rule Priority

Resolve conflicts in this order:

1. The user's current explicit request.
2. The nearest applicable `AGENTS.md` or repository guidance.
3. Existing project code, components, and design system.
4. Project documentation and interface contracts.
5. This skill.
6. External reference repositories.

Never rewrite a working local structure merely to match this skill or an
external repository.

## Workflow

```text
discover
→ classify
→ inspect existing patterns
→ map ownership, boundaries, and contracts
→ test audit hypotheses
→ rank evidence-backed findings
→ report evidence and residual risks
```

1. Read repository guidance, run `git status --short`, and identify the target
   app, project class, package manager, scripts, and documented architecture.
2. Consume current `code-context` output or perform a targeted inventory of the
   route/page entry, owning feature, analogous screens, UI primitives, layout
   and tokens, data/cache, forms/schema, state, tests, and docs.
3. Classify the task as Web, high-density Console, or Tauri Desktop, then map
   each responsibility to its page, feature, primitive, hook, service, store,
   schema, or local type owner.
4. Compare the target with direct reuse candidates, the nearest analogous
   feature, documented contracts, and the existing component and layout system.
5. Trace routing, data, state, styling, accessibility, performance, and native
   boundaries without changing the repository.
6. Audit loading, empty, error, partial, retry, optimistic, stale, cancellation,
   keyboard, focus, and long-task behavior that applies to the feature.
7. Use non-mutating repository checks and collect browser or real-client
   evidence when behavior cannot be proven statically.
8. Report findings first with severity, impact, exact location, evidence,
   recommended owner, remediation direction, and validation gaps.

## Modes

- **Architecture and ownership audit:** review routes, features, shared layers,
  reuse decisions, dependency direction, docs, and structural lifecycle.
- **Component and layout audit:** review component-system consistency, minimal
  DOM/CSS, spacing and scroll ownership, responsiveness, and duplicate rules.
- **State and contract audit:** review server, URL, form, shared business, and
  local UI state plus request, schema, error, and native IPC boundaries.
- **Accessibility and performance audit:** review keyboard/focus behavior,
  semantics, feedback states, render/data paths, evidence, and validation gaps.

## Hard Rules

- Do not recommend a shared component, hook, store, service, schema, or layout
  system before searching existing implementations and recording why reuse or
  adaptation is insufficient.
- Keep route and page files primarily compositional. Move remote access,
  reusable behavior, business workflows, and cross-screen state to the existing
  owning boundary; do not create empty layers for visual neatness.
- Keep `components/ui` or its local equivalent business-neutral. Keep business
  components, types, and state with their feature until a stable cross-feature
  contract and real consumers justify promotion.
- Use hooks only for real state, effects, subscriptions, or reusable behavior.
  Use services for remote/native boundaries, schemas for input and contract
  validation, and global stores only for genuinely cross-tree business state.
- Distinguish server/cache, URL/route, form, shared business, and local UI state.
  Do not mirror one source of truth into another without a synchronization
  contract.
- Reuse existing tokens, primitives, variants, layout owners, breakpoints,
  request/cache mechanisms, forms, toasts, and feedback states. Do not add a
  parallel system for a local feature.
- Keep DOM and CSS minimal: one owner for page-edge spacing and scrolling,
  Flexbox for one-dimensional layout, Grid for real two-dimensional layout,
  adaptive children, no empty wrappers, and no duplicate declarations or
  margin patches.
- Do not recommend `memo`, `useMemo`, or `useCallback` by default. Optimize only from
  a traced render/data path, measurement, or explicit complexity evidence.
- Keep Tauri pages behind a typed frontend adapter or service. Commands expose
  stable transport DTOs and errors, delegate business logic to Rust domain
  owners, and stream progress with cancellation for long work.
- Preserve keyboard operation, visible focus, accessible names, dialog/popover
  focus behavior, form labels/errors, and non-color status communication.
- Do not refactor unrelated legacy code. No file-length threshold alone can
  justify splitting; split only when ownership or behavior becomes clearer.
- Do not edit, stage, commit, or deliver code in audit mode. If the user asks to
  apply a finding, hand the scoped remediation to `implement-frontend`, then use
  `code-review` for the resulting Git changes.

## Do Not Use For

- Repository orientation without a frontend task; use `code-context`.
- Frontend implementation, modification, or refactoring; use
  `implement-frontend`.
- Root-cause diagnosis before a fix is known; use `diagnose`.
- Any existing frontend Git change set, even when the requested checks are
  component reuse, state, layout, accessibility, or performance; use
  `code-review`.
- Browser or real desktop runtime operation; use `ops-browser` or `ops-client`.
- A backend-only Rust implementation or audit; use `implement-rust` or
  `audit-rust`.

## Output Contract

Start with severity-ranked findings. For each finding, report impact, exact
location, evidence, recommended owner and remediation direction, and validation
gap. Then summarize the project class, rules and files inspected, existing
candidates, ownership map, state/data and native boundaries, layout and token
owners, applicable feedback/accessibility/performance states, documentation
drift, validation evidence, and `Not verified` residual risks.

## Skill Maintenance

Keep this entry concise. When triggers or rules change, update references,
`agents/openai.yaml`, eval cases, README/install indexes, and run
`python3 scripts/validate-skills.py`.

## References

- Read [architecture-and-ownership.md](references/architecture-and-ownership.md) for discovery, directories, routes, pages, and file responsibility.
- Read [component-system.md](references/component-system.md) for primitives, feature components, composition, variants, and reuse decisions.
- Read [state-data-and-forms.md](references/state-data-and-forms.md) for state classes, requests, caching, feedback states, services, schemas, and forms.
- Read [styling-and-layout.md](references/styling-and-layout.md) for tokens, spacing, responsive layout, Console density, DOM, and CSS ownership.
- Read [desktop-tauri.md](references/desktop-tauri.md) for frontend adapters, commands, Rust boundaries, windows, shortcuts, progress, and cancellation.
- Read [accessibility-and-performance.md](references/accessibility-and-performance.md) for keyboard/focus checks and evidence-based performance review.
- Read [review-checklist.md](references/review-checklist.md) for the systematic audit sequence.
- Read [anti-patterns.md](references/anti-patterns.md) for detectable failure patterns and corrective decisions.
- Read [reference-corpus.md](references/reference-corpus.md) for official source evidence, adopted rules, and rejected cargo-cult choices.
- Read [usage.md](references/usage.md) for trigger and routing examples.
- Read [eval-cases.md](references/eval-cases.md) for trigger, non-trigger, scenario, quality, and scoring evals.
