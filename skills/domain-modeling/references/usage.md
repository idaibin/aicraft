# Domain Modeling Usage

## Summary

Use `domain-modeling` to make business language, identity, lifecycle, rules, and context boundaries explicit before technical design or implementation.

## Triggers

- `Model the Node, Metric, Observation, Alert, Report, and Policy domain before we redesign the screens.`
- `Clarify what account, tenant, member, and user mean here.`
- `Draw the order lifecycle and identify invalid transitions.`
- `Separate the billing and entitlement bounded contexts.`
- `Turn these business rules into an explicit domain model, but do not plan code yet.`

## Non-Triggers

- Map repository roots, startup commands, or reusable code: use `repo-map`.
- Produce technical design, tasks, owners, and validation: use the host's built-in planning.
- Diagnose a failing transition in current code: use the host's built-in diagnosis under effective instructions.
- Implement the modeled behavior: use the matching `implement-*` skill.

## Composition

For complex product work, use the smallest necessary chain:

```text
repo-map (only when repository truth is unknown)
  -> domain-modeling (when business language or lifecycle is unclear)
  -> host planning
  -> implement-*
  -> repo-review
  -> repo-delivery
```

Do not invoke every step ceremonially. A clear, small technical change may start at implementation; a pure terminology request stops after the domain model.

## Output

Return a concise model with confirmed facts, inference, contradictions, decisions, open questions, and unverified gaps. Prefer tables for term definitions and relationships, and a state diagram only when transitions are meaningful.
