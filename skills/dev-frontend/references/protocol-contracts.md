# Frontend Protocol Contracts

## Activation Gate

Use this profile only when the repository already owns an OpenAPI/generated-client
pipeline or the task explicitly requests establishing one. Ordinary HTTP callers may
keep the repository's native client/types and focused contract tests; do not add
OpenAPI merely because REST is present.
When inactive, report generated-contract checks `Not applicable`.

## Consumer Boundary

When active, consume repository-owned TypeScript client/types generated from the
normalized OpenAPI artifact. Frontend code must not depend on backend language or
framework annotations.

Record:

- service and bounded feature;
- code-first or contract-first authority selected upstream;
- baseline OpenAPI artifact and operation reference;
- generator name/version and exact clean-generation command;
- generated client/type paths and representative consumers;
- manual DTOs in the touched chain and their disposition.

## Implementation Rules

- Use generated request, response, error, and operation shapes through the existing
  client abstraction.
- Preserve optional versus nullable fields, enums, IDs, date/time, money, pagination,
  headers/auth, status codes, validation errors, business errors, and compatibility.
- Do not copy an endpoint path, DTO, or error union into frontend source when the
  generated client owns it.
- Keep loading, success, empty, unauthenticated/unauthorized, validation/business
  error, and retry states aligned with the approved product behavior.

## Verification

1. Clean-regenerate the client and verify no unexplained drift.
2. Run frontend typecheck, build, and focused tests from repository commands.
3. Exercise one real consumer through loading, success, and error with `ops-browser`
   when live web evidence is required.
4. Require clean-state CI reproduction for generation, contract validation,
   compatibility, client, backend tests, and frontend gates when in scope.

Mark unavailable profile gates `Not verified`. When the profile does not apply,
report `Not applicable` and validate the repository-native client boundary instead.
