# Deep Module Design

Use this guidance only when the requested technical design creates, splits, merges, or materially changes a module boundary.

## Design Tests

- Define the interface as everything callers must know: operations, types, invariants, ordering, errors, configuration, and relevant performance behavior.
- Prefer a narrow stable interface that hides meaningful policy, coordination, or complexity.
- Place the seam where callers can vary behavior without learning internal workflow or storage/transport details.
- Keep dependency direction toward stable domain and contract owners; isolate framework, persistence, network, and platform adapters at the edges.
- Make the public interface the primary behavior-test seam. Use internal seams only for complexity that must vary inside the module.
- Require a real second implementation, environment, or consumer pressure before adding polymorphic abstraction. Do not create hypothetical adapters solely for tests.

## Shallow-Module Signals

- The wrapper repeats nearly every parameter and error from its dependency.
- Callers still coordinate ordering, retries, validation, or state transitions themselves.
- Deleting the module removes little complexity and mostly deletes forwarding code.
- Tests must bypass the interface to reach the behavior that matters.
- A new layer increases navigation without creating one clear owner for policy or invariants.

When a shallow boundary is proven, prefer replacing it with a deeper owner or removing it. Do not stack another wrapper on top. Record affected callers, compatibility, migration, tests, docs, and rollback in the plan.
