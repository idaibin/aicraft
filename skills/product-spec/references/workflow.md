# Product Specification Workflow

## Evidence First

1. Read effective guidance and product-document conventions.
2. Search named requirements, current product facts, UI states, and representative
   consumers only as far as needed to resolve product choices.
3. Separate confirmed current behavior from proposals and assumptions.
4. Ask only questions whose answers can change the selected slice.

## Internal Clarification

Ask one key question at a time. Include a recommended answer, the reason, and the
trade-off. Prefer a bounded choice over a broad interview. Checkpoint a coherent
decision group before moving to another boundary. Do not write after every answer.

Use these statement states:

- **Confirmed**: supported by user decision or current authoritative evidence.
- **Assumption**: proposed to keep progress possible but not yet authoritative.
- **Open Question**: unresolved and potentially material.
- **Rejected**: considered and explicitly excluded.
- **Deferred**: intentionally outside the current slice.

## Ready for an Implementation Slice

Name the slice, then verify only applicable gates:

- user and problem outcome;
- scope and non-goals;
- main, empty/loading, permission, validation, business-error, and recovery flows
  that can affect the slice;
- business rules and user-visible semantics;
- user-visible UI and data effects only where the slice touches them;
- dependency edges and executable acceptance results.

Block only when a missing decision can change user behavior, business rules,
permission/security boundaries, failure semantics, or
acceptance results. Otherwise record the question as Assumption or Deferred and
declare `Ready for <slice>`.

## Stop Conditions

- Stop clarification when the slice passes the Ready gate.
- Stop Artifact Update if the requested source is absent or write authorization is
  missing; return a preview or `Not found` instead of creating a replacement.
- Stop and route deep domain or ui-design ownership to the proper Skill.
- Stop before implementation, Git mutation, runtime verification, or technical
  interface definition. Route current interface mapping separately to `repo-map`.
