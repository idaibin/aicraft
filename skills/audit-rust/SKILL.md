---
name: audit-rust
description: "Use when auditing or profiling complex Rust CLIs, libraries, Tokio services, Tauri backends, Cargo workspaces, local-first single binaries, or SQLite-backed applications, especially for toolchain baselines, crate boundaries, structural lifecycle, ownership, errors, concurrency, CPU and memory evidence, database migrations and query plans, unsafe or FFI safety, quality gates, and architecture-document alignment."
---

# Rust Audit

## Overview

Audit complex Rust engineering from repository evidence. Use this read-only
workflow for architecture, performance, memory, concurrency, SQLite, unsafe,
and FFI review; use `implement-rust` when the requested outcome includes code
changes.

## Rule Priority

Resolve conflicts in this order:

1. The user's current explicit request.
2. The nearest applicable `AGENTS.md` or repository guidance.
3. Existing project code, toolchain, and architecture.
4. Project documentation and interface contracts.
5. This skill.
6. External reference repositories.

Do not rewrite a working local design merely to resemble an external project.

## Workflow

```text
discover
→ classify
→ inspect analogous code and evidence
→ map ownership, lifecycle, and invariants
→ establish correctness or performance baseline
→ test audit hypotheses
→ rank evidence-backed findings
→ report evidence and residual risks
```

1. Read repository guidance, run `git status --short`, and inspect only the
   relevant manifests, entry points, modules, docs, tests, benches, migrations,
   CI, and runtime configuration.
2. Determine workspace and crate boundaries, library and binary entry points,
   feature flags, MSRV, edition, runtime/thread model, error and tracing style,
   database crate and SQLite linkage, migration strategy, quality commands, and
   unsafe, FFI, mmap, or native dependencies.
3. Classify applicable standards as portable governance, organization baseline,
   new-project template, repository contract, or documented legacy exception.
   Never turn a version snapshot or example directory tree into a universal rule.
4. Consume current `code-context` output or build a targeted inventory of
   analogous APIs, traits, modules, database access, background tasks, tests,
   benchmarks, migrations, callers, and architecture docs before creating a new
   boundary.
5. Classify the task as architecture/API, ownership/resource, errors,
   async/concurrency, performance, memory, SQLite, unsafe/FFI, or combined.
6. Map governing invariants, resource owners, shutdown/cancellation paths,
   error boundaries, workload, baseline, and validation gaps.
7. For add, reuse, move, rename, or delete operations already present, audit
   every affected manifest, registration, import/re-export, feature flag, test,
   migration, generated file, deployment path, architecture document, and index;
   search for stale references.
8. Validate hypotheses with non-mutating repository-defined commands and
   representative data. Do not
   substitute `cargo check` for release, benchmark, concurrency, migration, or
   runtime evidence.
9. Report findings first with severity, impact, exact location, evidence,
   remediation direction, and `Not verified` gaps.

## Modes

- **Architecture and baseline audit:** review crate/module/API ownership,
  lifecycle, invariants, dependencies, toolchain policy, docs, and exceptions.
- **Baseline audit:** compare toolchain, workspace, directory, naming,
  validation, documentation, and legacy-exception policy against real projects.
- **Performance and memory analysis:** define workload, measure, profile, specify
  a one-factor experiment, and verify comparable time, allocation, RSS, I/O,
  binary, and compile-cost evidence. Route experiment edits to `implement-rust`.
- **SQLite review:** inspect runtime/linkage, connections, transactions, WAL,
  migrations, schema, indexes, query plans, maintenance, backup, and recovery.
- **Architecture and safety audit:** report evidence-backed findings across
  ownership, errors, concurrency, unsafe/FFI, dependencies, tests, and docs.

## Hard Rules

- Do not add a public trait, global state, runtime, thread pool, cache,
  connection pool, repository/service/manager layer, or database abstraction
  before proving the consumer, replacement, test, lifecycle, or deployment need.
- Do not hard-code the latest stable Rust release or a universal MSRV in this
  skill. Read the repository's pinned toolchain and support policy; treat edition
  2024 and resolver 3 as valid current choices for new work, not forced migrations.
- Do not impose one `apps/`, `crates/`, `domain/`, `application/`,
  `infrastructure/`, or frontend-mirrored directory tree. Record feature and
  interface ownership in the project's existing architecture map instead.
- Split crates by stable responsibility or deployment boundary, not file count.
  Keep binary entry points focused on composition, configuration, startup, and
  shutdown. Keep domain logic independent of CLI, HTTP, Tauri, and database
  implementations.
- Give every file, socket, mmap, connection, transaction, statement, rows
  iterator, task, subscription, lock, channel, buffer, cache, and index reader or
  writer a clear owner and bounded lifetime.
- Do not label every `clone` as a problem. Report copying only with evidence for
  value size, frequency, hot-path position, retention, and observable impact.
- Keep expected failures recoverable and typed. Libraries do not exit the
  process; expected input or business errors do not panic; boundary layers turn
  internal errors into useful CLI, API, or UI messages without duplicate logs.
- Do not make synchronous code async merely because Tokio exists. Keep blocking
  file, CPU, native, and SQLite work off async executor threads; bound tasks and
  channels; define backpressure, timeout scope, panic propagation, cancellation,
  and graceful shutdown; do not hold locks across `.await` without proof.
- Optimize only from a representative workload and comparable baseline. Do not
  introduce `#[inline]`, unsafe, SIMD, allocator changes, mmap, object pools,
  `SmallVec`, interning, caches, or parallel iteration on intuition alone.
- Distinguish true leaks from live references, caches, allocator retention,
  mmap, SQLite page cache, and OS file cache. Without measurement, report a
  hypothesis or `Not verified`, not a leak conclusion.
- Inspect the actual SQLite runtime and linkage. Verify critical queries with
  representative data and `EXPLAIN QUERY PLAN`; treat WAL as one-writer
  concurrency, handle busy/locked outcomes, and never delete `-wal` or `-shm`
  files manually.
- Do not default to `auto_vacuum=FULL`, run `VACUUM` without free-space and
  outage analysis, or raise cache/mmap settings without measurement. Keep
  network calls and long computation outside transactions.
- Choose `rusqlite` or SQLx from the existing runtime, connection, transaction,
  compile-time query, and deployment needs; never migrate because one is newer
  or because synchronous SQLite is assumed slow.
- Keep every unsafe block minimal and document its safety invariant. Verify FFI
  ownership, length, alignment, lifetime, ABI, panic containment, and native
  handle cleanup; use Miri, Loom, sanitizers, or focused tests only when the
  repository and target support them.
- Do not refactor unrelated code. A large file, `Arc<Mutex<_>>`, `unwrap`, or
  full table scan is a review signal, not an automatic finding; prove impact and
  context before prescribing a change.
- Apply stricter templates to new projects only when the organization has adopted
  them. Migrate established projects incrementally at real change boundaries;
  never perform mechanical renames merely to make layouts visually identical.
- Do not edit, stage, commit, or deliver code in audit mode. If the user asks to
  apply a finding, hand the scoped remediation to `implement-rust`, then use
  `code-review` for the resulting Git changes.

## Do Not Use For

- Repository orientation without a Rust task; use `code-context`.
- Rust implementation, modification, refactoring, or porting; use
  `implement-rust`.
- Root-cause diagnosis before a fix is known; use `diagnose`.
- Any existing Git change set, including a Rust/SQLite crate move, deletion, or
  domain-specific diff; use `code-review`, then `code-delivery` for delivery.
- Security-only review after the Rust surface is mapped; use `code-security`.
- A frontend-only change with no Rust or SQLite boundary.

## Output Contract

Start with severity-ranked findings. For each finding, report impact, exact
location, evidence, remediation direction, and validation gap. Then summarize
the project class; guidance, manifests, code, migrations, docs, tests, and
commands inspected; existing candidates; crate/module and resource owners;
applicable baseline class and documented exceptions; structural lifecycle map;
invariants and error boundaries; async/thread/channel/lock/cancellation model;
SQLite runtime, linkage, connection, transaction, WAL, schema, migration, and
query-plan evidence; workload and before/after performance or memory evidence;
unsafe/FFI and dependency risks; documentation drift; validation results; and
`Not found` or `Not verified` gaps.

## Skill Maintenance

Keep this entry procedural. When triggers, modes, or rules change, update the
references, `agents/openai.yaml`, eval cases, README/install indexes, and run
`python3 scripts/validate-skills.py`.

## References

- Read [architecture-and-modules.md](references/architecture-and-modules.md) for workspace, crate, module, binary, domain, trait, and dependency boundaries.
- Read [project-baseline-and-lifecycle.md](references/project-baseline-and-lifecycle.md) for baseline classification, new versus legacy projects, reuse-first discovery, feature maps, and add/move/delete synchronization.
- Read [ownership-and-resources.md](references/ownership-and-resources.md) for ownership, clone, `Arc`, resource, buffer, cache, and lifecycle review.
- Read [errors-and-api-design.md](references/errors-and-api-design.md) for public invariants, API types, errors, panic, retry, logging, and boundary translation.
- Read [async-and-concurrency.md](references/async-and-concurrency.md) for runtime, blocking work, tasks, channels, locks, timeouts, cancellation, shutdown, and Loom.
- Read [performance.md](references/performance.md) for workloads, baselines, CPU, allocation, I/O, binary, compile-time, and benchmark decisions.
- Read [memory.md](references/memory.md) for RSS, allocation, retention, caches, mmap, SQLite pages, and leak classification.
- Read [sqlite.md](references/sqlite.md) for linkage, connections, transactions, WAL, migrations, schema, indexes, plans, maintenance, backup, and recovery.
- Read [testing-and-quality.md](references/testing-and-quality.md) for risk-based tests, Cargo gates, Clippy, docs, release builds, Miri, audit, coverage, and benchmarks.
- Read [unsafe-and-security.md](references/unsafe-and-security.md) for unsafe invariants, FFI, native resources, dependencies, secrets, and security checks.
- Read [review-checklist.md](references/review-checklist.md) for a full pre-change and post-change audit sequence.
- Read [anti-patterns.md](references/anti-patterns.md) for detectable failure patterns and corrective decisions.
- Read [reference-corpus.md](references/reference-corpus.md) for official source evidence, adopted rules, and rejected cargo-cult choices.
- Read [usage.md](references/usage.md) for trigger, routing, and reporting examples.
- Read [eval-cases.md](references/eval-cases.md) for trigger, non-trigger, scenario, quality, and scoring evals.
