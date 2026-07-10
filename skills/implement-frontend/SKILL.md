---
name: implement-frontend
description: Use when implementing or modifying frontend UI, routes, components, forms, tables, dashboards, responsive behavior, DOM/CSS structure, layout ownership, scroll boundaries, or frontend architecture while preserving the existing stack, design system, state, API contracts, and verification flow.
---

# Frontend Implementation

## Overview

Implement frontend changes with existing-stack alignment, minimal DOM/CSS, clear layout ownership, and explicit verification. Use this after repository context is clear; route browser evidence to `ops-browser` and real desktop-window proof to `ops-client`.

## Workflow

1. Read repo guidance first: root `AGENTS.md`, nearest subproject `AGENTS.md`, `AGENT.md`, or chat-supplied rules.
2. Identify the frontend project class, app boundary, package manager, runtime pin, script contract, directory/naming standard, and documented exceptions.
3. Identify the target page, route, screen, component, framework, UI type, visual source, and required states before editing.
4. Consume a current `code-context` inventory or perform the same targeted search for existing routes, pages, layouts, components, hooks, services, shared UI, tests, and analogous implementations.
5. Decide in order: directly reuse, adapt the nearest reference, or create new. Record why existing candidates are insufficient before adding a file or abstraction.
6. Inspect only the selected target and reference page, route, component, service, hook, style, shared UI, and layout owner files needed for the requested change.
7. Classify the existing UI system and layout model: component library, utility/CSS strategy, shell/content/page boundaries, panels, and scroll regions.
8. Preserve typography, spacing, density, routing, state, API contracts, accessibility, and visual system unless the task explicitly asks to change them.
9. Implement with the smallest component, DOM, CSS, and ownership surface that matches existing patterns.
10. Update manifests, scripts, routes, tests, docs, indexes, and stale references when adding, reusing, moving, renaming, or deleting structural frontend code.
11. Remove stale wrappers, duplicate declarations, late overrides, and temporary layout patches made obsolete by the change.
12. Run matching project-defined checks, then use `ops-browser` or `ops-client` when runtime UI evidence is required.

## Modes

- **Targeted implementation:** make a requested frontend change without broad layout or stack changes.
- **Structure and style simplification:** reduce wrapper DOM, repeated utilities, duplicated CSS, unclear layout ownership, and competing scroll/overflow rules.
- **Implementation self-check:** verify the edited frontend surface for component-system, import, style, layout, ownership, and route drift.
- **Stack alignment:** decide how to use React, Vue, Next.js, Vite, TanStack Router, Tailwind, Ant Design, shadcn/ui, desktop webviews, or local components based on the existing app.

## Do Not Use For

- First-pass repository discovery, real commands, or entry points; use `code-context`.
- Future task decomposition or multi-agent implementation planning; use `code-planner`.
- Dirty-tree ownership, mixed-hunk review, staging, or commit planning; use `code-review`.
- Systematic frontend architecture, reuse, state/data, accessibility,
  performance, or Tauri-boundary audit without requested edits; use
  `audit-frontend`.
- Browser operation, screenshots, console, network, downloads, uploads, or runtime evidence collection; use `ops-browser`.
- Desktop-client launch review, CGWindowID proof, real-window screenshots, or native runtime operation; use `ops-client`.
- Root-cause diagnosis before a frontend fix is known; use `diagnose`.

## Hard Rules

- Verify the actual stack before using Tailwind, Ant Design, shadcn/ui, React Router, Zustand, Redux, React Query, form libraries, icon libraries, or routing helpers.
- Follow repository-pinned Node/package-manager versions, lockfile, dependency policy, script names, directory names, and file naming. Do not upgrade or normalize them during unrelated UI work.
- Keep framework-native structure: use the repository's React Router `routes`, Next.js `app`, Astro `pages`, Vue routing, or documented equivalent. Apply canonical plural directories or kebab-case only when repository standards require them; otherwise preserve existing naming until alignment is explicit.
- Do not introduce a parallel UI kit, CSS system, routing pattern, state layer, API helper, icon library, or form library when an existing one covers the need.
- Do not create a page, component, hook, helper, service, wrapper, or shared abstraction before checking the `code-context` inventory and performing a targeted file/symbol search. Reuse directly when behavior matches; otherwise follow the nearest reference's placement, naming, props, state, styling, and tests.
- Create a new implementation only when reuse or adaptation would violate ownership or behavior. State the reason and place it in the existing directory and naming convention.
- Keep layout ownership explicit: app/window shell owns chrome and global clipping; content containers own the page's outer inset; page roots own page layout; components own only their internal spacing; panels own panel bounds; inner regions own scrolling or overflow.
- Keep the shortest valid layout path. Every wrapper must own semantics, layout, state, accessibility, animation, or reuse; flatten nested `div`s that do not.
- Prefer Flexbox for one-dimensional row/column layout and parent-owned horizontal or vertical alignment. Use Grid for genuinely two-dimensional layout, not as an extra wrapper around a simple flex flow.
- Center content only when the design calls for it, using the owning parent's alignment. Let children adapt with the project's flex/grow/shrink/basis and minimum-size conventions instead of duplicate wrappers or fixed dimensions.
- Do not repeat page-edge margin, padding, inset, height, width, or overflow rules across shell/content/page/component layers. If an outer owner provides the spacing, inner components must not provide it again.
- Collapse wrappers that only pass classes, hold one child, duplicate a component boundary, or exist only for animation. When safe, make the animated node the semantic page root.
- Prefer semantic HTML, existing components, component props, natural document flow, cascade, and inheritance over redundant wrappers, repeated declarations, and one-off overrides.
- Use project scale utilities for ordinary Tailwind sizing and spacing, such as `h-1`, `h-12`, or `w-22` when available; do not use arbitrary pixel utilities such as `h-[22px]` for routine dimensions.
- Use one named layout class or CSS variable for business-specific geometry such as split-pane widths; keep utility classes for ordinary spacing and icon sizing only when they match the local scale.
- Keep each CSS responsibility at one owning selector, component prop, token, or variant. Consolidate duplicate declarations at that owner, then delete stale copies, patch rules, and late overrides.
- Preserve route paths, query parameters, payload shapes, response unwrapping, loading states, permission-hidden entries, and accessibility behavior unless the task requires changes.
- Prefer local component reuse. Extract a shared component or package only when real consumers, ownership, API stability, and consumer validation are established.
- Keep `lint`, `typecheck`, `test`, `check`, and formatting validation non-mutating; use an explicit fix/write command when source rewrites are intended.
- When adding, reusing, moving, renaming, or deleting routes, components, features, packages, or shared directories, update manifests, exports, route generation, scripts, tests, CI/build/deploy paths, docs, indexes, and stale references in the same task.
- Mark unchecked visual, responsive, console, network, runtime, or accessibility behavior as `Not verified`.

## Output Contract

Report the branch, frontend project class, detected stack/toolchain, existing implementations checked, direct reuse or reference candidate, new-file justification when applicable, touched UI surface, structural lifecycle updates, layout and outer-spacing owners, Flex/Grid decision, adaptive-child behavior, DOM/CSS simplification choices, preserved contracts, commands run, failed commands, browser/client evidence or `Not verified` gaps, and any intentionally excluded layout or stack changes.

## Skill Maintenance

When maintaining this package, keep `SKILL.md` concise, move detailed examples to `references/`, update `agents/openai.yaml`, and run `python3 scripts/validate-skills.py`.

## References

- See [references/usage.md](references/usage.md) for trigger guidance and examples.
- See [references/checklist.md](references/checklist.md) for implementation and review checks.
- See [references/stack-guidelines.md](references/stack-guidelines.md) for Vite, React, Tailwind, Ant Design, and shadcn/ui boundaries.
- See [references/eval-cases.md](references/eval-cases.md) for trigger and quality evals.
