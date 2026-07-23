# UI Documentation Boundaries

## Location Order

1. Use the repository's existing authoritative UI or design-system source.
2. Use the repository's established design/spec convention.
3. Only when neither exists and the user explicitly authorizes durable publication,
   use `docs/ui/` directly:
   - `docs/ui/<slice-id>/spec.md` for one page domain or connected flow contract;
   - `docs/ui/index.md` only for several independent UI slices;
   - `docs/ui/DESIGN.md` only when creating or changing the accepted shared visual
     authority through Design System Spec;
   - `docs/ui/design-system/manifest.yaml` only when verified repository automation
     consumes it.

Do not create an index for one slice, add a `docs/specs/` wrapper, or create a parallel
UI tree when an existing design, RFC, feature, or component-system location already
owns the contract. Reusing an accepted theme never creates `DESIGN.md` or a manifest.

`DESIGN.md` is the human-readable semantic authority for shared visual decisions.
`design-system/manifest.yaml` is only the machine-readable automation contract for a
named real consumer and declared asset bindings. It must bind the consumer, semantic
authority, and every declared asset by path and SHA-256, must reject any mismatch, and must not
contain independent visual decisions. Validate it with the package's design-system
manifest validator before acceptance or automation use.

## PRD Relationship

Use the same stable `<slice-id>` as the related `docs/prd/<slice-id>/spec.md` when both
artifacts exist. Cross-link them instead of copying facts. PRD owns user behavior,
business rules, permissions, failure semantics, and product acceptance. UI owns the
selected source, layout, component/token mapping, states and interaction,
responsive/accessibility rules, and UI acceptance.

## Consumer Read Contract

To implement one UI slice, read only:

1. `docs/ui/DESIGN.md` when it exists and applies;
2. `docs/ui/index.md` when the request has several UI slices;
3. the related `docs/prd/<slice-id>/spec.md`;
4. `docs/ui/<slice-id>/spec.md`.

Do not require sibling PRD or UI contracts. Keep unfinished task-local work under the
repository's ignored task workspace, such as `.codex/artifacts/<task-id>/`, until
durable publication is explicitly approved.
