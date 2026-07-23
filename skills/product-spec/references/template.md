# Product Specification Templates

Use repository conventions before these shapes. Omit inapplicable sections.

## Feature Spec

```markdown
# <Feature>

## Goal and implementation slice
## Users and scenarios
## Confirmed decisions
## Scope and non-goals
## Main and failure flows
## Business rules and permissions
## UI states and evidence (if applicable)
## User-visible data effects (if applicable)
## Affected product surfaces and dependencies (if applicable)
## Acceptance criteria
## Assumptions, open questions, rejected and deferred decisions
## Ready for <implementation slice>
```

For several independent features, add a short index before the slice documents:

```markdown
# <Request> Product Index

## Shared confirmed facts
## Slice inventory, links, and status
## Shared dependencies and exclusions
## Slice-specific blockers
## Consumer read contract
```

Each linked slice uses the Feature Spec template. Do not repeat UI colors, typography,
components, tokens, or page geometry; link the target UI contract instead.

## Foundation Spec

```markdown
# <Product or Product Line>

## Product boundary and positioning
## Target users and problems
## Core journeys and failure expectations
## Shared capabilities and exclusions
## Product language required for this boundary
## MVP and non-goals
## Success signals
## Confirmed, assumed, open, rejected, and deferred decisions
## Ready for <first implementation slice>
```

Move multi-context language, lifecycle, invariants, and complex state modeling to
`domain-modeling`; link the result instead of duplicating it.

## Artifact Update

Preview the smallest patch to the named artifact. Preserve its structure and
authority, identify the confirmed source for each changed fact, and do not create
fallback files merely because the named path is missing.
