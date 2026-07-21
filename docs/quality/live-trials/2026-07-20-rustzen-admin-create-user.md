# Rustzen Admin Create-User Product Spec And OpenAPI Trial

## Basis

- Observed: `2026-07-20`; completed and independently rechecked: `2026-07-21`
- Source Codex tasks: `019f7eb5-e722-7900-adea-c851486f327a` and
  `019f83b9-3a1b-7a10-987c-2ad0aac86a64`
- Target repository: `rustzen-admin`
- Trial branch: `feat/create-user-openapi-trial`
- Trial state: two local commits; clean worktree; not pushed or merged
- Initial Git basis: `07a3317d88c062abda1ea2f59b3790a1e889a1c0`
- Final target commit: `63f0d275508f5cd9b1ff07606bbf5c7e312c26e2`
- Review basis: fixed range
  `07a3317d88c062abda1ea2f59b3790a1e889a1c0..63f0d275508f5cd9b1ff07606bbf5c7e312c26e2`
- Candidate Skill basis: the uncommitted AICraft `product-spec` / OpenAPI workflow
  candidate in `feat/product-spec-contract-workflow`; its exact revision was not
  frozen and cannot serve as a formal campaign revision

## Selected Slice

- Service: Admin
- Feature: create user
- Operation: `POST /api/system/users`
- Authentication/authorization: bearer authentication plus `system:user:create`
- Real consumer: the create-user dialog on the React `/system/user` route
- Product artifact: `docs/reference/create-user-openapi-trial.md`
- Ready result: `Ready for create-user OpenAPI and generated-client slice`

## API Contract Map Snapshot

This is a trial evidence snapshot, not a substitute for a current target-repository
repo map. Recheck source before reuse.

| Field | Observed current-source evidence |
| --- | --- |
| Service/owner root | Admin; `apps/admin` |
| Authority | Code-first declarations in `apps/admin/src/features/system/user/handler.rs`, `types.rs`, `apps/admin/src/common/api.rs`, and `common/error.rs` |
| Registration | `POST /api/system/users`; operation ID `createAdminUser` |
| Exchange artifact | Derived `openapi/admin-create-user.json`; Utoipa `5.5.0`; `just openapi-generate` |
| Generated consumer | Orval `8.22.0` Fetch client under `apps/web/src/api/generated/admin/`; `just openapi-client-generate` |
| Real consumer | `apps/web/src/api/system/user/api.ts` and `apps/web/src/routes/system/user.tsx` |
| DTO boundary | Handwritten `User.CreateRequest` removed; generated `CreateUserRequest` owns the touched frontend contract |
| Validation entries | `just openapi-validate`, `just openapi-compat`, `just verify-create-user-contract`, `just check` |
| Baseline character | First bootstrap reconstruction from fixed behavior; no historical OpenAPI artifact or generator existed at the Git basis |

## Retained Results

The normalized candidate and bootstrap baseline were observed byte-identical. Two
client generations were also byte-identical:

```text
OpenAPI:          7db8e5a77c244b9827edcd80c71393ab59d26db19b80fe050ceee7b793f69ae2
Generated client: b0a596e86ca5cbeec6a734bf23488a2e2004bcabaf783ac84546c041dd8a9522
```

| Gate | Observed result |
| --- | --- |
| OpenAPI reconstruction/validation | Passed for the bounded operation |
| Two isolated generations | Passed; repeated OpenAPI outputs matched the OpenAPI SHA, and repeated generated-client outputs matched the client SHA |
| Compatibility | Passed only against the newly frozen bootstrap reconstruction; not historical compatibility evidence |
| TypeScript client regeneration | Passed without unexplained tracked drift |
| DTO ownership | Passed for the touched create-user request |
| Backend runtime contract | In-process Router/SQLite contract tests passed 200 success, 400 invalid status/code `10007`, 401 unauthenticated, 403 unauthorized, 404 missing role, 409 duplicate username/email, and simulated persistence 500; error responses retained `data: null` |
| Frontend | Generated-client test, TypeScript check, and Vite build passed |
| Browser | The original source task reported loading, close/list refresh, duplicate error toast, and console observations; the completion pass did not reproduce them or retain durable browser evidence |
| Clean checks | `just check` passed independently on the final commit: format, typecheck, frontend test/build, Cargo check, Clippy, workspace tests, and Admin 69 tests passed; one generated-code lint warning remained non-blocking |
| Independent review | The original review found and fixed error `data: null` requiredness, status `1..4` bounds, and missing trial-basis documentation; final fixed-range review found no P0-P3 issue |

## Reproduction Commands

The completion pass ran these commands successfully against the final target commit:

```text
just openapi-generate
just openapi-validate
just openapi-compat
just openapi-client-generate
just verify-create-user-contract
cargo test -p rustzen-admin features::system::user
cargo test -p rustzen-admin create_user_contract
cd apps/web && bun run vp test run src/api/system/user/api.test.ts
env TMPDIR=/private/tmp/rustzen-main-review-tmp just check
git diff --check 07a3317d88c062abda1ea2f59b3790a1e889a1c0..63f0d275508f5cd9b1ff07606bbf5c7e312c26e2
```

The first sandboxed `just check` attempt failed before code checks because Bun could
not write its temporary directory. Repeating it with a writable task-owned
`TMPDIR` passed. This was an execution-environment failure, not a source fix.

## Gaps And Honest Status

- The target changes are locally committed but remain unpushed and unmerged; remote
  availability, branch protection, and CI are not verified.
- Browser loading, success toast, dialog close, list refresh, and 409/404/500 error
  presentation were not independently reproduced against the final commit.
- The completion pass did not retain browser network, screenshot, or console evidence.
- Deployment and production behavior were not tested.
- Orval `8.22.0` still generates one non-blocking `no-misused-spread` lint warning for
  optional request headers. TypeScript checking, the frontend build, and the current
  consumer pass; the generated file was not edited manually.
- A bootstrap artifact cannot prove compatibility with a historical executable
  contract that did not exist.
- The historical AICraft candidate revision was not frozen. A formal repeat must use
  a committed Skill revision rather than retroactively assigning the current version.
- This candidate-only run has no matched previous-Skill and no-Skill controls and no
  independent semantic verifier. AICraft `behavior` and `workflow` remain
  `not_verified`.

## Catalog Decision

Retain `product-spec` as an experimental candidate. Accept the trial as useful
workflow evidence for:

- the progressive single Feature Spec and `Ready for <slice>` gate;
- single code-first authority and normalized OpenAPI/client handoff;
- explicit bootstrap-versus-historical compatibility labeling;
- generated DTO ownership and real-consumer tracing;
- a standardized Live Trial handback plus `repo-map` API Contract Map profile.

Before any broader claim, repeat the trial from a committed Skill revision, preserve
durable target and browser evidence, add an independent semantic verifier, and run
controlled repeated trials.
