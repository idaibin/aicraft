# Usage

## Use `repo-review` When

Use this skill for an independent read-only review whose primary object is a committed repository state or comparison:

- an entire repository or bounded subsystem at one commit;
- `base..head` or two branches resolved to immutable SHAs;
- a pull request or release candidate;
- a complete review package with verifiable manifest and hashes;
- a second-opinion review that consolidates frontend, Rust, security, test, CI, documentation, and structural findings.

## Nearest Skill Boundaries

| Request | Owner | Reason |
| --- | --- | --- |
| Map commands, entry points, project class, reuse candidates, or docs/code drift | `repo-context` | The output is repository understanding, not judgment. |
| Review local uncommitted changes, classify dirty files, split commits, or prepare exact staging | `code-review` | The object is the current worktree and commit readiness. |
| Review a repository snapshot, branch range, PR, release candidate, or review package | `repo-review` | The object is an immutable repository basis and consolidated findings. |
| Audit a known auth, authorization, data, config, dependency, IPC, or release security surface | `audit-security` | The output is a bounded security specialist assessment. |
| Find why a test, build, runtime, or performance symptom fails | `diagnose` | The output is a confirmed root cause and regression seam. |
| Apply accepted findings | matching `implement-*` | Review remains read-only. |
| Stage, commit, push, squash, or clean branches | `code-delivery` | Git mutation is a separate authorization boundary. |

Do not merge these skills merely because they all read repository files. They have different primary objects, authorization boundaries, stop conditions, and output contracts.

## Examples

### Commit range

```text
Review 23d30ccd..d1c5f0d8 independently. Check all changed skills for routing, safety, workflow executability, metadata synchronization, and eval quality. Return P0-P3 findings with exact file/line, impact, fix, and verification.
```

Resolve both endpoints to SHAs, inspect the complete range and required contract files, and select specialists only for the changed domains.

### Whole repository

```text
Review this repository at the current main commit for structural drift, frontend architecture, Rust risks, security-sensitive configuration, tests, CI, and documentation consistency. Do not modify anything.
```

Select profiles from the actual project classes. Do not claim directories or runtime surfaces were reviewed when they were not.

### Pull request

```text
Perform an independent review of PR 42. Do not post comments. Consolidate duplicate findings and state No actionable findings when applicable.
```

Read PR metadata and all changed files, resolve the base/head SHAs, and treat comment posting as a separate unauthorized action.

### Review package

```text
Review the supplied multipart package only after validating its manifest, order, hashes, and final marker.
```

Report whether each claim is supported by package evidence or directly verified against the repository.

## Report Shape

```text
Review basis
Selected profiles and exclusions

P0
P1
P2
P3

Cross-domain integration
Validation and evidence
Not found / Not verified
```

Every actionable finding includes location, evidence, impact, remediation, and verification. Empty groups explicitly say `No actionable findings` when a complete P0-P3 report was requested.
