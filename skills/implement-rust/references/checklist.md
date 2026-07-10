# Rust Implementation Checklist

## Required Context

- Read the nearest repository guidance and run `git status --short`.
- Identify the project class and current directory contract.
- Read relevant `Cargo.toml`, `Cargo.lock`, `rust-toolchain*`, `rustfmt.toml`,
  Clippy/lint config, `justfile` or other command source, architecture docs, and
  directly related code/tests.
- Record exact edition, resolver, minimum Rust version, feature flags, workspace
  membership, dependency inheritance, and validation commands when present.
- Say `Not found` for missing contracts and `Not verified` for unchecked runtime behavior.

## Interface Reuse Gate

- Start from a current `code-context` inventory, or reproduce the same targeted
  search when it is unavailable or stale.
- Read architecture/API docs and trace the nearest analogous route registration,
  handler, service, repository, trait/impl, types/DTOs, errors, migrations,
  callers/consumers, tests, examples, and module exports.
- Classify candidates as direct reuse, extensible contract, reference-only,
  unrelated, or `Not found`.
- Prefer direct reuse, then extension, then adaptation. Create a new interface
  only when existing contracts cannot own the behavior safely or clearly.
- For a new endpoint or public API, record method/path or function/trait shape,
  auth/permission, input/output, serialization, error mapping, persistence,
  callers, compatibility, docs, and tests.
- Follow the nearest feature's directory, module, naming, visibility, type,
  error, and test conventions; do not create parallel interface families.

## Project Class And Structure

- Library workspace: keep product-neutral crates under the repository's crate convention.
- Application workspace: keep deployable apps and shared crates in their documented owners.
- HTTP service: keep transport, workflow, domain, persistence, and runtime-engine responsibilities separate.
- CLI: keep argument/output handling thin and move reusable behavior behind library modules when the repository already supports it.
- Tauri/native: keep UI-facing commands and platform integration at the shell boundary; keep business rules in owned Rust modules or crates.
- Compact service: do not manufacture an apps/crates monorepo when one package is the correct boundary.
- Legacy or multi-process project: preserve protected runtime and deployment paths until a dedicated migration approves changes.

## Implementation

- Follow existing module names, visibility, type conventions, feature gates, and dependency direction.
- Keep entry handlers and commands thin.
- Keep deterministic business rules independent of IO where practical.
- Keep SQL, filesystem, network, process, and platform behavior in their existing infrastructure boundary.
- Use typed inputs and outputs at boundaries.
- Preserve public API and serialization shapes unless the task changes the contract.
- Propagate errors with the local error model; add context at ownership boundaries.
- Avoid runtime panics, silent fallback, needless cloning, blocking async calls, unbounded tasks/channels, and hidden global state.
- Add tests for branching behavior, bug regressions, parsing, boundary conversion, and reusable helpers.
- Prefer borrowed inputs and slices when ownership is unnecessary; avoid
  redundant clones and intermediate collections.
- Prefer static dispatch; use trait objects only for real runtime polymorphism.
- Keep async work non-blocking and bounded; preserve cancellation and cleanup.
- Keep FFI/raw-pointer code in narrow adapters. Check ABI/layout, pointer
  validity, aliasing, lifetime, thread affinity, ownership transfer, cleanup,
  callback re-entry, allocator symmetry, and panic behavior.
- Document public APIs and invariants with rustdoc, examples, and applicable
  `# Errors`, `# Panics`, and `# Safety` sections.
- Use comments for rationale rather than narration; link TODOs to owned issues.

## Ports And Rewrites

- Record source-language-to-Rust mappings for types, ownership, errors,
  cleanup, callbacks, and complex field lifetimes before bulk changes.
- Prove the mapping on a small representative slice.
- Preserve observable behavior and architecture before idiomatic cleanup.
- Compare source and Rust semantics for assertions, eager/lazy fallback,
  rounding/casts, slices/alignment, bounds/overflow, destruction, re-entry, and
  debug/release behavior.
- Never place required side effects inside `debug_assert!`.
- Reject stubs, placeholder constants, skipped/deleted tests, and compile-only
  claims of parity.
- Use a big-bang rewrite only when its compatibility suite, mechanical mapping,
  supported-platform path, capacity, and product-risk case are explicit.

## Reuse And Extraction

- Search for the nearest existing helper, crate, service, or engine before adding code.
- Prefer local reuse when only one product or feature needs the behavior.
- Before shared extraction, identify at least two real consumers or a stricter repository rule.
- Confirm product neutrality, stable API, named owner, dependency direction, shared tests, and consumer validation.
- Update adoption or execution records when repository governance requires them.

## Structural Lifecycle

When adding, reusing, moving, renaming, or deleting a crate, module, feature,
binary, migration, or shared surface, check:

- Cargo workspace membership and dependency declarations
- `mod.rs`, `lib.rs`, `main.rs`, binary targets, feature flags, and public exports
- call sites, tests, examples, benchmarks, fixtures, and generated sources
- command files, CI, packaging, release, deploy, service, updater, and runtime paths
- architecture docs, project maps, indexes, ownership records, and migration notes
- stale references with targeted search after the change

## Validation

- Use repository-defined commands first.
- Run matching format, check, test, and Clippy gates when present.
- Run doc tests or rustdoc checks when public APIs or documentation change.
- Fix Clippy findings instead of silencing them; use narrow justified
  `#[expect(...)]` when suppression is necessary.
- Keep validation commands non-mutating; use an explicit formatting/fix command when writes are intended.
- Verify feature combinations or platform targets only when the changed contract requires them.
- Add release-mode, cross-target, Miri, sanitizer/leak, fuzz, stress, or
  repeated-operation gates when unsafe, FFI, parsers, platform code, concurrency,
  or resource ownership makes them relevant.
- Confirm selected tests actually ran and were not silently skipped.
- Classify failures as environment, configuration, existing project, or introduced code issues.
- Do not claim runtime, deployment, platform, or cross-consumer behavior without evidence.

## Review

- Confirm every changed line belongs to the task.
- Confirm no unrelated dependency, toolchain, edition, resolver, or formatting migration slipped in.
- Confirm code, manifests, commands, tests, and docs agree.
- Confirm every new endpoint, trait, type/DTO family, error model, or module has
  an explicit reuse/extension/reference search result and new-interface reason.
- Confirm ownership/borrowing, errors, allocation, dispatch, async/concurrency,
  tests, rustdoc, comments, and lints follow `references/best-practices.md`.
- For FFI, unsafe, native resources, or language ports, confirm the applicable
  source-backed checks in `references/bun-production-patterns.md` without
  copying Bun-specific toolchain or architecture choices.
- Route final dirty-tree ownership and commit grouping to `code-review`.
