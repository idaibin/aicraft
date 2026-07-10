# Frontend Audit Checklist

## Grounding

- Read all applicable guidance and status.
- Identify Web, Console, or Tauri Desktop.
- Trace route/page, layout, feature owner, analogous implementation, UI
  primitives, tokens, request/cache, forms/schema, state, tests, docs, and
  desktop adapter.
- Record direct-reuse, composition/variant, reference-only, unrelated, and
  `Not found` candidates.
- Check whether new files and abstractions have evidence-backed justification.

## Ownership

- Page/route composes rather than owning unrelated workflow and transports.
- Business components stay in the feature; UI primitives stay business-neutral.
- Hooks, services, stores, schemas, and types each own a real responsibility.
- Local UI state remains local; URL and server state keep their source of truth.
- Tauri pages use an adapter; commands delegate to Rust domain/API owners.

## UI And Data

- Existing primitives, variants, tokens, page layouts, tables, dialogs, empty
  states, forms, requests, cache, toasts, and errors are reused.
- Loading, empty, error, partial, retry, optimistic, stale, and cancellation
  paths are explicit where applicable.
- Page-edge spacing, scrolling, breakpoints, and CSS declarations have one owner.
- No meaningless wrappers, copied components, or competing systems exist in the
  audited scope.

## Accessibility And Performance

- Keyboard, focus, dialogs/popovers/menus, form associations, icon names,
  non-color status, and async announcements are covered.
- Lists are bounded; requests deduplicate; global state and contexts are scoped.
- Memoization and bundle/IPC conclusions have measurement or path evidence.
- Desktop long tasks expose progress, cancellation, error, cleanup, and listener
  lifecycle.

## Structural And Documentation Lifecycle

- Identify required updates across routes, exports, manifests, aliases,
  generated files, tests, stories, fixtures, CI/build/deploy, architecture
  docs, project maps, and indexes that describe the boundary.
- Search for stale names, copies, imports, styles, docs, and command identifiers.

## Validation

- Run repository-defined formatting check, lint, typecheck, focused tests, and
  build/route generation that match the change.
- Validate browser behavior when layout, interaction, responsiveness, network,
  accessibility, or performance claims require it.
- Validate the real desktop client for native commands, menus, shortcuts,
  windows, progress, cancellation, and platform behavior.
- Report exact failures and `Not verified` gaps; never convert an unchecked
  assumption into a pass.
