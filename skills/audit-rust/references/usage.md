# Usage

## Trigger Examples

- `Audit crate ownership for a local-first CLI and Tauri backend without imposing empty layers.`
- `Compare our Rust toolchain and directory baseline with this existing repository without forcing a migration.`
- `Audit our crate move/delete lifecycle policy across manifests, registrations, tests, migrations, deployment paths, and docs; there is no current Git change set.`
- `Audit this Tokio service for unbounded tasks, channels, locks, cancellation, panic propagation, and shutdown.`
- `Profile this Rust hot path and prove whether clones, allocations, mmap, or a custom allocator matter.`
- `Review SQLite migrations, WAL growth, query plans, indexes, backup, and recovery in this desktop app.`
- `Check unsafe FFI ownership and run the supported Rust quality gates.`
- `Compare rusqlite and SQLx for this existing runtime and deployment model.`
- `Verify Rust architecture docs against crates, commands, migrations, and real code.`

## Routing Examples

- Use `code-context` first when the task is only repository orientation or when
  no Rust target is known.
- Use `implement-rust` for a change whose module,
  contracts, and validation are already established.
- Use `diagnose` when the root cause of a failure or regression is unknown.
- Use `code-security` for a security-only audit after the relevant Rust boundary
  is mapped.
- Use `code-review` for dirty-tree ownership, staging, and commit grouping; use
  `code-delivery` for commit, push, squash, or remote proof.
- Use `code-review` for any existing Rust/SQLite diff, including crate moves or
  deletions; domain depth does not bypass Git ownership and staging review.

## Expected Investigation Summary

```text
Project class:
Repository guidance and status:
Applicable baseline class and legacy exceptions:
Workspace/crates/entries/features/MSRV/edition:
Runtime, tasks, threads, channels, locks, cancellation, shutdown:
Errors, tracing, public invariants:
SQLite crate/linkage/runtime/connections/migrations/WAL:
Unsafe/FFI/native dependencies:
Existing analogous code and reuse candidates:
Structural lifecycle dependencies:
Tests, benchmarks, CI, and docs:
Baseline or missing evidence:
```

## Expected Final Report

```text
Decision and scope:
Adopted, adapted, and rejected baseline rules:
Owners and invariants:
Add/reuse/move/rename/delete lifecycle updates:
Required changes and documentation updates:
Performance/memory evidence:
SQLite evidence and query plans:
Concurrency and shutdown evidence:
Unsafe/FFI and dependency evidence:
Validation commands and results:
Findings with impact and location:
Not found / Not verified:
Residual risks:
```

Lead with findings ordered by impact. Never claim a benchmark,
migration path, runtime version, release build, Miri/Loom run, or recovery test
that was not actually executed.
