# Requirements and Specification

## Readiness Gate

Before technical design, distinguish:

- confirmed user outcomes and observable behavior;
- constraints from repository policy, compatibility, runtime, data, security, and delivery;
- decisions already made;
- assumptions that are safe and reversible;
- open questions that materially change behavior, authority, architecture, or acceptance;
- contradictions between requirement, docs, code, and runtime evidence.

Ask a question only when a reasonable assumption could materially diverge from user intent. Continue with labeled assumptions for smaller reversible details.

Use `domain-modeling` when the unresolved question is about canonical language, entity identity, ownership, lifecycle, invariants, business rules, or bounded contexts. Keep technical modules, interfaces, files, and validation in `code-planner`.

## Specification Contract

Use the applicable sections:

```markdown
## Requirements
## Constraints and Non-Goals
## Open Questions
## Decisions
## Domain Model
## Technical Design
## Acceptance Criteria
## Validation Plan
## Task Slices and Blocking Edges
```

Omit empty ceremony, but never omit unresolved material risk.

## Technical Design

Name only decisions that implementation needs:

- owning modules and interfaces;
- data/control flow and failure behavior;
- compatibility, migration, and rollback boundaries;
- authorization and external-action boundaries;
- test seams and validation sources;
- affected consumers, manifests, docs, generated artifacts, and delivery gates.

Do not freeze incidental file paths or code shapes that the implementer can discover safely unless path ownership is part of the task contract.

## Acceptance Criteria

Write observable pass/fail statements. Cover expected behavior, meaningful error states, compatibility, accessibility/security/performance constraints when relevant, and explicit exclusions. Avoid criteria such as `code is clean` or `works correctly` without an observable check.

## Vertical Slices

Prefer tracer bullets that cross the minimum required layers and remain independently demonstrable or testable. Declare `Blocked by` edges only for real prerequisites.

Use expand-migrate-contract for wide mechanical changes that cannot remain green as end-to-end slices:

1. expand with a compatible new form;
2. migrate consumers in bounded batches;
3. contract only after stale-consumer proof;
4. keep rollback and integration checks explicit.
