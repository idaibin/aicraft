# Frontend Implementation Checklist

Use this checklist when implementing or reviewing frontend changes.

## Required Context

- Read relevant repo guidance first.
- Run `git status --short` before edits.
- Identify actual package manager, scripts, frontend app boundary, target screen, route, component, framework, UI type, visual source, style system, and runtime proof requirement.
- Identify the frontend project class, pinned runtime/package manager, lockfile, dependency policy, script contract, directory/naming standard, and documented exceptions.
- Inspect only target page, component, route, service, hook, type, style, shared UI, and layout owner files needed for the request.
- Check existing imports and nearby patterns before adding libraries, aliases, icons, helpers, or components.

## Reuse-First Gate

- Start from a current `code-context` directory/file inventory, or reproduce the same targeted search when it is unavailable or stale.
- Search relevant routes, pages, layouts, components, hooks, services, shared UI, tests, exports, and symbols before creating anything.
- Classify candidates as:
  - direct reuse: behavior and ownership already match
  - reference-only: adapt the nearest structure, naming, props, state, styling, and tests
  - unrelated: similar name but different ownership or behavior
  - `Not found`: no relevant implementation exists
- Prefer direct reuse, then adaptation. Create new only when both are insufficient, and record the ownership/behavior reason.
- Place new files in the existing directory and naming convention; do not create parallel `components`, `shared`, `common`, `ui`, `hooks`, or service layers.
- After implementation, search again for accidental duplicates, obsolete predecessors, competing exports, and stale references.

## Stack And Structure

- Confirm whether the project uses React, Vue, Next.js, Vite, TanStack Router, TypeScript, Tailwind, Ant Design, shadcn/ui, CSS modules, Less/Sass, desktop webviews, project-local components, or a deliberate mix.
- Keep page files consistent with existing thickness. Move logic only when the local pattern already uses hooks, services, helpers, or feature components.
- Put new files in the established layer. Use framework-native and repository-defined names such as React Router `routes`, Next.js `app`, Astro `pages`, or project-specific equivalents; do not mix `pages`, `views`, and `routes` casually.
- When repository standards define canonical names, use their plural directories and file-case rules for new work. Do not mass-rename existing paths during an unrelated feature.
- Reuse existing request helpers, response unwrap helpers, route builders, permission checks, form wrappers, table wrappers, modal/drawer patterns, icons, and interaction helpers.
- Extract a shared component or package only after identifying real consumers, named ownership, stable props/API, shared tests, and consumer validation.
- Preserve path aliases and import ordering conventions.
- Keep local UI state local unless the app already uses a global store or route/query layer for the same responsibility.

## DOM And Layout Ownership

- Identify the owners before editing nested layouts:
  - app/window shell: global chrome, toolbar, app background, global clipping, modal host
  - content container: shared page inset and broad viewport bounds
  - page root: page-level grid/flex layout and transition root
  - panels/regions: local bounds and spacing
  - inner content: the one intended scroll or overflow owner
- Choose the shortest valid DOM path before adding a wrapper. Each element must own semantics, layout, state, accessibility, animation, or reuse.
- Remove wrappers that only forward classes, group a single child, repeat page-stage or layout boundaries, or duplicate a local component boundary.
- Merge animation-only wrappers into semantic roots when possible; prefer an animated `main`, `section`, or existing component root over a separate animation wrapper plus an identical inner container.
- Prefer Flexbox for one-dimensional row or column composition. Use the owning parent for `justify-*` and `items-*` alignment; do not add a child wrapper only to center content.
- Use Grid only when rows and columns form a real two-dimensional relationship.
- Keep children adaptive with the project's grow, shrink, basis, wrapping, `min-w-0`, and `min-h-0` conventions. Avoid fixed widths/heights when the available space should determine size.
- Assign page-edge margin, padding, and inset to one owner. If the shell or content container already owns outer spacing, page roots and reusable components must not repeat it; components own internal spacing only.
- Do not stack repeated `h-full`, `min-h-0`, `overflow-*`, padding, inset, or width rules across shell, content, page, and panel layers.
- Keep one main scroll owner where practical. Fixed headers, sidebars, inspectors, and footers should not compete with the list or content region for overflow control.
- Avoid broad `overflow-visible` patches that hide unclear ownership. If overflow must be visible, name the owning region and keep scrolling somewhere else explicit.

## Styling

- Preserve existing layout, spacing, breakpoints, typography, palette, copy, navigation, component hierarchy, table density, and form density unless requested.
- Prefer existing tokens, class utilities, component props, variants, and style files over one-off inline styles.
- Prefer browser inheritance and cascade for font, color, line-height, and spacing context when the parent or design system already defines them.
- Consolidate repeated CSS declarations into the nearest owning class, component prop, token, variant, or shared style only when that does not broaden side effects.
- Keep one declaration source for each visual responsibility. Do not repeat the same spacing, sizing, alignment, typography, color, border, or overflow declaration in base styles, component styles, utilities, and late overrides.
- Remove duplicate class definitions and late CSS overrides after moving responsibility to the correct owner; do not leave stale patch rules that shadow design-system declarations.
- Use project scale utilities for ordinary Tailwind spacing and dimensions, such as `h-1`, `h-12`, or `w-22` when available.
- Do not use arbitrary pixel utilities such as `h-[22px]`, `w-[88px]`, `mt-[7px]`, or `rounded-[13px]` for routine UI sizing; move real product/layout constants into a named class, token, or CSS variable.
- Use one named layout class or CSS variable for business-specific geometry such as split-pane widths, toolbar offsets, or complex loader anatomy.
- Do not introduce a new UI kit, theme provider, global CSS reset, Tailwind config, token system, icon library, radius scale, shadow style, or button style for a local change.
- Avoid mixing Ant Design and shadcn/ui inside one feature unless that mix already exists and is intentional.
- Avoid decorative UI, landing-page patterns, or marketing-style composition on operational/admin pages unless requested.

## Behavior And Contracts

- Preserve routes, query params, hash behavior, permission-hidden entries, payload fields, response shapes, loading states, and error handling unless the task targets them.
- Trace API changes through request helper, service, type, caller, and page state.
- Keep form validation, controlled state, table pagination, sorting, filtering, modal lifecycle, and drawer lifecycle aligned with existing local patterns.
- Use semantic controls: buttons for actions, links for navigation, labels for fields, and visible focus states.
- Do not silently change date, currency, locale, enum, or status-display semantics.
- For Tauri/Electron UI, keep shell, file, platform, and native API access behind existing IPC/command wrappers and surface command errors in the UI.

## Validation

- Run project-defined type, lint, test, build, formatter, or route checks that match the change.
- Keep validation commands non-mutating. Use explicit fix/write commands only when rewrites are in scope.
- Use `ops-browser` when visual layout, interaction, responsive behavior, console errors, network payloads, or route behavior need web evidence.
- Use `ops-client` when the task requires proof from a real Tauri, Electron, or native desktop window.
- Mark unchecked runtime, visual, responsive, console, network, accessibility, or permission behavior as `Not verified`.

## Review

- Check for duplicate imports, unused imports, dead components, parallel helper layers, inconsistent aliases, uncontrolled layout changes, stale override rules, and accidental global style impact.
- Check that every new page/component/helper has an explicit reuse/reference search result and new-file justification.
- Check wrapper necessity, Flex/Grid choice, parent-owned alignment, adaptive child sizing, and single-owner page-edge spacing.
- For added, reused, moved, renamed, or deleted routes, components, features, packages, or shared directories, verify manifests, exports, route generation, scripts, tests, CI/build/deploy paths, architecture/project-map docs, indexes, and stale references.
- Compare before/after DOM and CSS ownership: if a wrapper or rule disappeared, confirm its old responsibility moved to the correct owner or was truly unnecessary.
- Check that every changed line belongs to the requested frontend change.
- Route final dirty-tree review and staging to `code-review`; route push or squash delivery to `code-delivery`.
