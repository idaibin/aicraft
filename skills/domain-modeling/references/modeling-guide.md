# Domain Modeling Guide

## Contents

- [Evidence](#evidence)
- [Term and Concept Tests](#term-and-concept-tests)
- [State and Rule Tests](#state-and-rule-tests)
- [Boundary Tests](#boundary-tests)
- [Scenario Stress Test](#scenario-stress-test)
- [Output Template](#output-template)

## Evidence

Prefer, in order, explicit user decisions, accepted requirements, current business contracts, domain documentation, representative tests, and current code behavior. Code proves what the system does, not automatically what the business intends.

Label each material statement:

- **Confirmed:** directly supported by an authoritative source.
- **Inferred:** best explanation of available evidence, awaiting confirmation.
- **Conflict:** authoritative sources disagree.
- **Not verified:** required evidence was not inspected or is unavailable.

## Term and Concept Tests

- Give one canonical term one meaning inside a bounded context.
- Separate identity-bearing entities from descriptive value objects.
- Name commands as requested intent and events as completed facts.
- Distinguish observations from alerts, reports, and policies.
- Reject concepts that exist only because of one screen, table, endpoint, or framework.
- Ask whether two concepts have different identity, lifecycle, invariants, ownership, or permissions before merging them.

## State and Rule Tests

For each stateful entity, identify:

- initial, active, suspended, failed, cancelled, expired, and terminal states when applicable;
- allowed transitions and the command or event that causes each;
- guards, permissions, invariants, side effects, idempotency, retries, and compensation;
- whether concurrent commands can race and which outcome wins;
- what historical facts must remain true after later transitions.

Write rules as observable statements, for example: `An acknowledged Alert cannot return to New; a new Observation may create a new Alert.`

## Boundary Tests

Create separate bounded contexts only when at least one differs materially:

- canonical language;
- identity or lifecycle owner;
- consistency and transaction rules;
- permission authority;
- source of truth;
- change cadence or external integration contract.

Record context relationships as upstream/downstream, shared kernel, published language, anti-corruption layer, or an equivalent repository-native relationship only when the distinction changes design decisions.

## Scenario Stress Test

Probe only relevant cases:

1. normal creation and completion;
2. invalid transition or missing prerequisite;
3. retry, duplicate command, or out-of-order event;
4. cancellation, expiry, rollback, or compensation;
5. concurrent owners or conflicting updates;
6. partial failure across context boundaries;
7. permission or tenant change during the lifecycle;
8. historical data created under an older rule.

## Output Template

```markdown
# Domain Model

## Scope and Evidence
## Ubiquitous Language
## Entities and Value Objects
## Relationships
## State Machine
## Business Rules and Invariants
## Bounded Contexts
## Scenarios Tested
## Contradictions and Decisions
## Open Questions
## Not Verified
```
