# Skills

Independent Agent Skills for real software-engineering work.

Each published Skill is a self-contained package with its own trigger, workflow,
authority boundary, output contract, supporting references, and evaluation
cases. Skills can be installed separately and composed when a task crosses
owners; none requires another package or a repository-root runtime file to do
its basic job.

[![skills.sh](https://skills.sh/b/idaibin/skills)](https://skills.sh/idaibin/skills)

## Install

Browse and select Skills interactively:

```bash
npx skills@latest add idaibin/skills
```

List the catalog without installing:

```bash
npx skills@latest add idaibin/skills --list
```

Install selected Skills globally for Codex:

```bash
npx skills@latest add idaibin/skills \
  --skill repo-map domain-modeling repo-review \
  --global --agent codex
```

Install one Skill:

```bash
npx skills@latest add idaibin/skills \
  --skill design-system \
  --global --agent codex
```

See [INSTALL.md](INSTALL.md) for project/global scope, updates, removal, and the
`design-ui` to `design-system` migration.

## Catalog

### Repository Engineering

| Skill | Use when |
| --- | --- |
| `repo-map` | Current repository boundaries, commands, task routes, or reusable owners need a verified map. |
| `domain-modeling` | Business language, identity, lifecycle, invariants, scenarios, or bounded contexts are unresolved. |
| `repo-review` | Local changes or an immutable commit/range/PR/release basis need an independent read-only review. |
| `repo-delivery` | Reviewed changes need authorized staging, commit, push, synchronization, or branch cleanup. |

### Design and Implementation

| Skill | Use when |
| --- | --- |
| `design-system` | A repository-owned design system must be created, extracted, maintained, or evaluated before source implementation. |
| `implement-frontend` | A requested frontend feature, component, page, or design-system contract must be implemented and validated. |
| `implement-rust` | A requested Rust feature, refactor, or port must be implemented with ownership and behavior evidence. |

### Audit and Operations

| Skill | Use when |
| --- | --- |
| `audit-frontend` | A known frontend surface needs a bounded read-only architecture, accessibility, performance, state, or design audit. |
| `audit-rust` | A Rust workspace or surface needs a bounded ownership, concurrency, SQLite, unsafe/FFI, performance, or memory audit. |
| `audit-security` | A known security-sensitive code or configuration surface needs a bounded read-only assessment. |
| `ops-browser` | A browser page must be operated or verified with screenshot, console, network, form, or download evidence. |
| `ops-client` | A Tauri, Electron, or native desktop client must be verified against its real process and window. |

### Review and Writing Extensions

| Skill | Use when |
| --- | --- |
| `chatgpt-review` | A local review package or explicitly authorized external ChatGPT review round is required. |
| `human-writing` | Source-grounded prose must be drafted or revised while preserving facts, voice, and disclosure boundaries. |

## Composition

Skills are composable owners, not a mandatory framework:

```text
unknown repository -> repo-map
unclear domain      -> domain-modeling
complex change      -> host planning and repository instructions
known failure       -> evidence-driven diagnosis under effective instructions
source work         -> implement-frontend / implement-rust
design contract     -> design-system -> implement-frontend
review              -> repo-review (with bounded audit-* specialists when needed)
delivery            -> repo-delivery
```

The nearest applicable owner may start directly. Cross-Skill handoffs transfer
bounded evidence, never implicit authorization.

## Package Contract

Every public package lives at `skills/<name>/` and contains:

```text
skills/<name>/
├── SKILL.md
├── agents/openai.yaml
└── references/
```

Packages add `assets/` or `scripts/` only when the capability needs them. A
published package may reference files inside its own directory; it must not
require `docs/`, `contracts/`, `evals/`, `protocols/`, another Skill, or an
absolute local path at runtime.

The repository-level `docs/`, `contracts/`, `evals/`, `protocols/`, and
`scripts/` directories are maintainer-facing validation infrastructure. They
do not ship as hidden runtime dependencies.

## Validate

```bash
python3 scripts/sync-shared-protocols.py --check
python3 scripts/validate-skills.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/eval-skill-contracts.py --validate-only
python3 scripts/measure-skill-footprint.py --baseline-ref HEAD
git diff --check
```

The validator checks package structure, local references, catalog consistency,
nearest-neighbor routing coverage, and static evaluation contracts. Passing
these checks proves repository structure, not live model behavior or end-to-end
workflow success; current evidence is recorded in
[docs/quality/status.md](docs/quality/status.md).

## Design Principles

- Small, intent-based, and composable, following the useful catalog qualities
  demonstrated by `mattpocock/skills`.
- One public Skill per stable user intent and authority boundary; technology
  variants remain profiles when their owner and output contract are the same.
- Progressive disclosure: concise discovery metadata and `SKILL.md`, with
  detailed workflows and examples in package-local references.
- Repository truth and explicit authorization take priority over generic
  conventions.

## Contributing and License

Read [AGENTS.md](AGENTS.md), [skills/AGENTS.md](skills/AGENTS.md), and
[docs/skills/skill-standard.md](docs/skills/skill-standard.md) before changing a
package. Unless a file states otherwise, the collection is available under the
[Apache License, Version 2.0](LICENSE).
