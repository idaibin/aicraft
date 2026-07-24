# Rust Best Practices

Apply repository guidance first. Use these rules when the repository does not
define a stricter or intentionally different contract.

## Contents

- [Interfaces And Ownership](#interfaces-and-ownership)
- [Option, Result, And Errors](#option-result-and-errors)
- [Control Flow And Allocation](#control-flow-and-allocation)
- [Traits, Dispatch, And State](#traits-dispatch-and-state)
- [Code Quality And Abstraction](#code-quality-and-abstraction)
- [Concurrency And Unsafe](#concurrency-and-unsafe)
- [Axum And Tauri Boundaries](#axum-and-tauri-boundaries)
- [FFI And Native Resources](#ffi-and-native-resources)
- [Ports And Large Rewrites](#ports-and-large-rewrites)
- [Tests, Documentation, And Lints](#tests-documentation-and-lints)

## Interfaces And Ownership

- Read architecture/API docs and the nearest complete feature before designing
  a public interface.
- Reuse or extend existing route, handler, service, repository, trait, DTO/type,
  error, and test families before creating parallel contracts.
- Accept `&str`, `&[T]`, or `&T` for read-only inputs when ownership is not
  required. Pass small `Copy` values by value.
- Clone only when an owned copy is required by the contract, concurrency model,
  cache, or state transition. Avoid clones in loops and large structures.
- Keep visibility as narrow as possible. Expose public items only when callers
  outside the owning module or crate require them.

## Option, Result, And Errors

- Return `Result<T, E>` for fallible operations and propagate with `?`.
- Use typed crate/library errors and the repository's existing error hierarchy.
  Prefer `thiserror` for reusable library errors and reserve `anyhow` for binary
  boundaries when the repository already accepts it.
- Avoid production `unwrap`, `expect`, and `panic!`. Use explicit invariants only
  when failure is truly impossible, and document the reason.
- Use lazy `_else` variants when fallback construction allocates or performs work.
- Test error variants, messages, mapping, and transport responses.

## Control Flow And Allocation

- Use `match` for real variant handling, `let ... else` for early exits, and
  iterator chains for clear transformations.
- Prefer readable loops when early exit or side effects make iterator chains
  harder to understand.
- Avoid intermediate collections, redundant allocation, premature boxing, and
  unnecessary ownership transfer.
- Measure release builds before optimizing. Do not add `#[inline]`, custom
  allocation, or complex caching from intuition alone.

## Traits, Dispatch, And State

- Prefer generics or `impl Trait` when concrete types are known and static
  dispatch keeps the API clear.
- Use `dyn Trait` only for real runtime polymorphism, heterogeneous collections,
  plugins, or a deliberate stable boundary. Box at the boundary, not internally.
- Use type-state only when it removes meaningful invalid states without making
  the API harder to understand.
- Do not introduce a trait for a single implementation unless it defines a real
  boundary, test seam, or extension contract already required by the design.

## Code Quality And Abstraction

- Prefer one owner for a business rule, schema, configuration fact, error
  mapping, or state transition. Similar syntax is acceptable when sharing would
  couple independent change reasons; duplicate authorities are not.
- Account for public API, features, targets, `cfg`, macros, derives, generated
  code, build scripts, examples/benches, FFI exports, and downstream crates
  before removing apparently unused code.
- A trait, newtype, adapter, or module earns its cost when it enforces an
  invariant, stabilizes a public/third-party/platform boundary, owns lifecycle
  or policy, or creates a necessary test or observability seam. One current
  implementation does not disprove that role.
- Reject pass-through service/manager/repository layers only when they add no
  validation, transformation, policy, error mapping, lifecycle, transaction,
  caching, instrumentation, compatibility, or stable boundary and create a
  demonstrated change/debug cost.
- Treat `clone`, `Arc`, `Mutex`, generics, dynamic dispatch, and lint suggestions
  as investigation signals. Decide from ownership, size/frequency, contention,
  async boundaries, public compatibility, and representative measurement.

## Concurrency And Unsafe

- Match pointer and synchronization types to the ownership model: `Rc` for
  single-thread sharing, `Arc` for cross-thread sharing, and locks only for real
  shared mutation.
- Preserve `Send`, `Sync`, cancellation, cleanup, and task-lifetime behavior
  across async boundaries. Do not block the async runtime.
- Avoid global mutable state and unbounded tasks, channels, queues, or retries.
- Use `unsafe` only when no safe design satisfies the requirement. Keep the
  block minimal and document invariants with `# Safety` or `// SAFETY:`.
- For `tokio::select!`, preserve state across cancellation when a losing branch
  is not safe to restart. Give spawned work an explicit lifecycle/outcome
  policy. Join, cancel, and observe output/error/panic when correctness, durable
  work, resources, shutdown, or caller-visible outcomes depend on it.
  Intentional detachment is acceptable only for bounded non-critical work that
  retains no uncontrolled resources and whose failure is irrelevant or
  independently observable; do not add a task-set or token mechanically.

## Axum And Tauri Boundaries

- In Axum, keep request extraction/validation and response translation at the
  transport edge, preserve the repository's typed `State`/`FromRef` model, and
  keep domain workflows independent of handler signatures. Respect the
  one-body-consumer extractor boundary and map rejections/errors deliberately.
- Compose Tower middleware in the smallest router scope that owns the policy.
  Do not add permissive CORS, a universal timeout, or generic tracing/body-limit
  layers without a workload and trust-boundary requirement. Test the router as
  a service when the repository exposes that seam.
- In Tauri, keep commands thin and validate frontend-controlled inputs in Rust.
  Use capabilities and permissions for core/plugin invocation authorization.
  Custom commands registered through `invoke_handler` are application-wide by
  default; use `tauri_build::AppManifest::commands` and the generated
  `allow-<command>`/`deny-<command>` permissions before relying on capability
  assignments for per-window/webview command ACL. Enforce configured scopes in
  the command or plugin implementation, and enforce user/domain authorization
  at its Rust owner when business identity or policy applies. Update
  registration, `build.rs`, generated permissions, typed caller/DTO/error
  contracts, capability/permission/scope, CSP, tests, and real-client
  validation when affected. Never duplicate platform ACL mechanically in every
  command or authorize arbitrary paths, URLs, shell/process operations, or
  remote content merely because the frontend can type the call.

## FFI And Native Resources

- Put foreign calls, raw pointers, callbacks, and layout assumptions behind a
  small adapter whose safe API expresses the validated contract.
- Use `#[repr(C)]` or `#[repr(transparent)]` only where an ABI or layout
  contract requires it. Do not model an open foreign integer enum as an
  exhaustive Rust enum when unknown values can cross the boundary.
- State who allocates, owns, borrows, transfers, and frees each resource. Keep
  allocation/free APIs paired and reclaim callback-owned resources exactly once.
- Bind returned references to a real owner lifetime. Validate nullability,
  alignment, lengths, initialization, aliasing, thread affinity, and callback
  re-entry before constructing references from pointers.
- Define panic behavior at every FFI boundary. Do not allow unwinding across an
  ABI that does not explicitly support it.
- Generate repetitive ABI glue when generation reduces hand-maintained drift,
  and verify generated declarations against both sides of the boundary.

## Ports And Large Rewrites

- Write down source-language-to-Rust type, ownership, error, and cleanup
  mappings before bulk work. Record complex field lifetimes separately.
- Prove the mapping on a small representative slice before scaling it.
- Preserve architecture and observable behavior during a mechanical port;
  separate parity work from later idiomatic refactoring and `unsafe` reduction.
- Treat semantic differences as review targets: assertion evaluation, eager
  versus lazy fallback, integer conversion and rounding, slice alignment and
  trailing bytes, bounds checks, destructor timing, callback re-entry, and
  debug-versus-release behavior.
- Never put required side effects inside `debug_assert!`; its expression is
  removed from optimized builds. Use lazy fallback variants when evaluation
  must be conditional.
- A big-bang rewrite is exceptional. Require a stable language-independent
  behavior suite, a mechanical mapping, a short compatibility window, and
  enough capacity to reach all supported platforms without freezing essential
  product work; otherwise migrate behind stable boundaries incrementally.

## Tests, Documentation, And Lints

- Give tests behavior-focused names and keep each test focused on one behavior.
- Use unit tests for private edge cases, integration tests for public contracts,
  and doc tests for public happy-path usage.
- Document public functions, structs, enums, traits, constants, and modules.
  Include examples and `# Errors`, `# Panics`, and `# Safety` when relevant.
- Write comments for rationale, constraints, safety, and non-obvious tradeoffs,
  not for code narration. Link TODOs to an owned issue.
- Run repository-defined rustfmt, check, test, doc-test/rustdoc, and Clippy
  commands. Treat warnings as errors when the repository does.
- Fix lints instead of silencing them. Use narrow justified `#[expect(...)]`
  rather than broad `#[allow(...)]`.
- Treat `cargo check` as a compile gate, not proof of behavior. Start from the
  repository Baseline and combine the overlays actually selected by the change.
  Add release-mode tests for configuration-sensitive code, cross-target checks
  for affected `cfg`, Miri for supported unsafe-sensitive code, sanitizers and
  leak tests for native ownership, and fuzzing for parsers or adversarial bytes
  only when each tool is both supported and relevant to the changed invariant.
  Target-specific code alone does not justify Miri, sanitizers, fuzzing, stress,
  leak, or repeated-operation checks.
- Verify tests actually ran and were not silently skipped. Repeated-operation
  tests should prove memory plateaus when leaks are part of the risk model.
