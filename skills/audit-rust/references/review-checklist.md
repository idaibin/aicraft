# Review Checklist

## 1. Grounding

- [ ] Read nearest repository guidance and current `git status --short`.
- [ ] Inspect root/member manifests, toolchain, features, profiles, entry points,
      relevant code, tests, benches, CI, docs, migrations, and runtime config.
- [ ] Classify CLI, library, Tokio service, Tauri backend, SQLite-first app,
      single binary, workspace, or combined project.
- [ ] Record MSRV, edition, resolver, targets, native dependencies, unsafe/FFI,
      database crate/linkage, and repository-defined commands.
- [ ] Classify proposed rules as portable governance, organization baseline,
      new-project template, repository contract, or legacy exception.
- [ ] Verify workspace fields, dependencies, and lints are actually inherited by
      members; do not infer adoption from root declarations alone.
- [ ] Find analogous modules, APIs, traits, tasks, queries, migrations, tests,
      and docs before creating anything.

## 2. Architecture And API

- [ ] Assign every responsibility to a stable crate/module/boundary owner.
- [ ] Keep binary/command/transport entry points thin and domain independent.
- [ ] Justify every new trait, common type, crate, manager, service, repository,
      runtime, pool, cache, and global state.
- [ ] State public invariants, feature and compatibility impact, and caller map.
- [ ] Replace ambiguous booleans only when semantic types improve the contract.

## 3. Ownership And Errors

- [ ] Trace creation, sharing, mutation, close/wait, and drop for all resources.
- [ ] Quantify clone/allocation/retention impact before making a finding.
- [ ] Bound collections, channels, tasks, caches, buffers, and input-driven growth.
- [ ] Classify user, business, dependency, corruption, retryable, and invariant
      errors; trace conversion, logging, retry, and user-visible mapping.
- [ ] Keep expected failures recoverable and sensitive data out of logs.

## 4. Async And Concurrency

- [ ] Prove async is needed and locate blocking file, CPU, SQLite, and native work.
- [ ] Record task owner, join/panic path, cancellation point, shutdown wait, and
      cleanup for every background task.
- [ ] Record channel capacity/backpressure, concurrency limit, timeout scope,
      retry amplification, lock scope/order, and `.await` interaction.
- [ ] Identify missing deterministic lifecycle tests and a focused Loom model
      only when useful.

## 5. Performance And Memory

- [ ] Define representative workload, release-equivalent profile, environment,
      repetitions, variance, and baseline.
- [ ] Profile the claimed CPU, allocation, RSS, I/O, lock, task, binary, compile,
      or cold-start cost before optimization.
- [ ] Define one factor to test, route requested experiment edits to
      `implement-rust`, and verify comparable rerun evidence.
- [ ] Distinguish leak, live owner, cache, allocator retention, mmap, SQLite page
      cache, OS cache, and index reader/writer retention.
- [ ] Identify missing regression benchmarks/tests and record trade-offs.

## 6. SQLite

- [ ] Verify runtime version, compile options, linkage, connection/thread model,
      busy policy, foreign keys, journal/synchronous mode, and async boundary.
- [ ] Check transaction batching, duration, rollback, reader lifetime, writer
      coordination, busy/locked handling, and network/CPU work inside transactions.
- [ ] Check WAL checkpoint policy, starvation, file growth, backup/shutdown, and
      filesystem assumptions.
- [ ] Review migration upgrade/failure/recovery; schema constraints and index
      order; representative `EXPLAIN QUERY PLAN` and timing for critical queries.
- [ ] Assess freelist, optimize, vacuum, backup restore, and integrity evidence.

## 7. Unsafe, Dependencies, And Validation

- [ ] Verify each unsafe/FFI invariant, ABI, ownership, alignment, lifetime,
      thread affinity, panic containment, and cleanup.
- [ ] Review new dependency features, advisories, native/build code, MSRV,
      license, binary size, and compile cost.
- [ ] Run repository-defined format, check, lint, test, docs, release, migration,
      benchmark, Miri, Loom, audit, or coverage gates that match the change.
- [ ] For add/reuse/move/rename/delete operations, verify alignment across manifests,
      registrations, imports/re-exports, features, tests, migrations, generated
      files, deployment paths, docs, and indexes; search for stale references.
- [ ] Verify code, manifests, registrations, migrations, tests, architecture,
      performance, and operational docs agree; report the required remediation
      scope when they do not.
- [ ] Report exact evidence and mark gaps `Not found` or `Not verified`.
