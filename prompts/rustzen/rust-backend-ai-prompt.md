# Rustzen Backend Prompt

Use this prompt when implementing, reviewing, or planning Rust backend work for `rustzen-admin` or a closely related Rustzen backend.

## Task

[Describe the backend task, feature, bug fix, refactor, or API change here.]

## Language

- Respond in the user's language unless the user explicitly requests another language.
- Keep code, commands, paths, API names, type names, capability strings, SQL fields, and error text unchanged.

## Start Here

Before editing:

1. Read:
   - `README.md`
   - root `AGENTS.md`
   - `apps/server/AGENTS.md`
   - `docs/architecture.md`
   - `docs/guides/backend.md`
   - `docs/guides/permission.md`
   - `docs/guides/ai-coding-rules.md`
2. Inspect the owning source files under `apps/server/src/`.
3. Inspect any matching frontend API module under `apps/web/src/api/` if the backend contract changes.
4. Inspect the root `justfile` before choosing verification commands.
5. Check `git status` and protect unrelated local changes.

Use current source code as the final source of truth. Do not rely on this prompt if the repository has moved on.

## Current Backend Shape

For `rustzen-admin`, the backend is currently organized as:

```txt
apps/server/src/
  features/
    <feature>/
      mod.rs
      handler.rs
      service.rs
      repo.rs
      types.rs
  infra/
  common/
  middleware/
apps/server/migrations/
  sqlite/
```

Shared Rust capability crates live under:

```txt
crates/auth/
crates/config/
crates/runtime/
crates/storage/
```

PostgreSQL-first behavior is historical or legacy context. SQLite is the active default storage backend unless current repository docs say otherwise.

## Layer Rules

### `mod.rs`

- Assemble routes only.
- Keep route paths and HTTP methods explicit.
- Use the current permission routing helpers.
- Use `PermissionsCheck::Require(...)` as the default for protected routes.

### `handler.rs`

- Extract HTTP path/query/body/state/current-user inputs.
- Call service methods.
- Return `AppResult<T>` / `ApiResponse<T>` according to existing code.
- Do not write SQL.
- Do not put complex business logic here.

### `service.rs`

- Handle orchestration, validation, transactions, and permission-aware behavior.
- Services may coordinate feature behavior, but must not bypass repositories.
- Do not call another feature's repo directly.
- Keep state and permission checks explicit.

### `repo.rs`

- Own SQL and persistence only.
- Do not put business rules here.
- Do not cross feature boundaries.
- Use explicit SQL fields; do not use `SELECT *`.

### `types.rs`

- Keep row/entity types, request types, response types, query types, and command types together.
- Use `snake_case` for Rust and database fields.
- Use `camelCase` for JSON and frontend-facing fields.
- Prefer `#[serde(rename_all = "camelCase")]` on HTTP request and response structs.

## API Contract Rules

When a backend API changes, verify the full chain:

- backend route nesting and final path under `/api`
- HTTP method
- path/query/body parameters
- success response structure
- error response structure
- frontend API module under `apps/web/src/api/`
- frontend TypeScript types
- page or component field usage
- data conversion before submit
- loading, empty, error, and notification behavior

For `rustzen-admin`, the current envelope is:

```txt
code
message
data
total?   # only when pagination/list metadata is needed
```

Frontend `apiRequest` unwraps `data` by default. Use `raw: true` only when callers need envelope metadata such as `total`. List methods should return the shape expected by the table component, usually:

```txt
{ data, total, success }
```

## Database And Migration Rules

- SQLite is the active default.
- Schema changes require migrations.
- SQLite migrations live under `apps/server/migrations/sqlite/`.
- New migration filenames should follow the current sequence and naming style already present in that directory.
- Runtime config uses `RUSTZEN_SQLITE_PATH` and other `RUSTZEN_*` variables.
- Use `crates/storage/` helpers for SQLite connection and migration behavior.
- Use `crates/config/` and `crates/runtime/` for runtime path behavior.
- SQL must list fields explicitly.
- Soft-delete filters such as `deleted_at IS NULL` only belong on tables that actually use soft delete.

## Audit Field Rules

Do not mechanically add audit fields to every table.

Current convention:

- Mutable primary tables commonly use `created_at` and `updated_at`.
- Soft-deletable tables may use `deleted_at` when the business behavior requires soft delete.
- Relation tables commonly use `created_at`.
- Log or event tables are append-only and usually use `created_at` or an event-specific timestamp.
- Actor fields such as `created_by`, `updated_by`, or `deleted_by` should be added only when the feature explicitly needs operator attribution. If added, keep the actor field type consistent across the schema.

Do not use `deleted_at` to model disabled, frozen, unpublished, closed, or inactive states. Use a dedicated `status` or `state` field for business state.

## Prohibited

- SQL in handlers.
- Services bypassing repos.
- Repos calling across features.
- Generated-file edits unless the project workflow explicitly requires them.
- Compatibility fallbacks without explicit migration need.
- Speculative abstraction.
- Backend contract changes without matching frontend API/type/page updates.

## Verification

Choose verification from the current `justfile` and task scope. Typical checks include:

- `cargo check -p server`
- `just check`
- `just build`
- API call or runtime log verification for contract or startup behavior
- `git diff --check`

If verification cannot be completed, explain exactly why and list remaining risk.

## Output

Return:

1. What changed
2. Files changed
3. API, schema, permission, or runtime contract impact
4. Verification commands and results
5. Remaining risks or follow-up items
