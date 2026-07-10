# Usage

## Trigger Examples

- `Use ChatGPT Pro to review this branch, save review.md, then fix it.`
- `Use my ChatGPT Project to review this branch for three rounds, then let Codex verify and fix each round.`
- `Use Chat for a one-off independent review and save review.md.`
- `Use my Chrome profile and ChatGPT project for this repo review.`
- `Default to the Codex in-app Browser and open the ChatGPT project for this repo review.`
- `After ChatGPT review, run local Codex CLI to fix the findings, but ask which approval mode to use first.`
- `Reset the ChatGPT review bridge defaults for this repo.`

## Non-Triggers

- Local-only code review without ChatGPT Pro.
- Browser verification without a repository review loop.
- GitHub-native PR review only.
- Security-only audit without ChatGPT as reviewer.

## Local Collection

Before any external action, collect only local read-only context:

- repository path, branch, and dirty state
- review package scope and approximate size
- validation commands already run and results
- bridge default record status
- local Chrome profile directory candidates
- cached ChatGPT tab candidates only if already available

Do not attach to Chrome, claim tabs, open browser profiles, create ChatGPT sessions, send content, start Codex CLI, or change defaults during this phase. Explicit send authorization removes a later duplicate route prompt; it does not skip package preparation, scope checks, or redaction.

## External Action Gate

Use the gate in `SKILL.md` only when external sending or route selection is not already authorized. An explicit request such as `use GPT to review`, `send this for review`, or `互审 3 轮` authorizes sending on the safely resolved route for the stated scope and round count; do not ask the same route question again.

Option handling:

- `1`: authorizes resolving and opening the Codex in-app Browser route; stop again before sending unless sending was also explicitly requested.
- `2`: ask before connecting to current Chrome; enumerate ChatGPT tabs; stop before claiming a tab or sending.
- `3`: generate/update the local package only.
- `4`: resolve the user-provided ChatGPT URL or surface; do not persist it unless separately requested.
- `0`: stop.

## Local Codex Gate

Use the exact Local Codex Gate in `SKILL.md` before `codex exec`.

Mode mapping:

- `1`: return review findings and recommendations only.
- `2`: output a copyable HEREDOC command; do not execute it.
- `3`: execute with `--sandbox workspace-write --ask-for-approval on-request`.
- `4`: execute with `--sandbox workspace-write --ask-for-approval never` only after explicit session-level approval plus confirmed repo path, branch, allowed files, validation commands, and forbidden actions.

The screenshot-style permission prompt is produced by the local execution permission layer. This skill controls the choice gate and command parameters, not the system prompt UI.

## Standard Chat, Project, And Codex

- Use a standard chat for an isolated, one-off reviewer conversation.
- Use a Project for repository-bound durable context or repeated review rounds
  when its URL can be verified. Verify the account workspace separately.
- Use Codex to collect evidence, apply fixes, run tests, and challenge ChatGPT findings locally.
- For mutual review, alternate `standard chat or Project review -> Codex verification/fix -> next external round`. Count only completed, attributed ChatGPT responses as external review rounds.

## Review Package

Include only in-scope evidence:

- task summary and review focus
- repo path, branch, base, commit, and remote when available
- `git diff --stat`, `git diff --name-status`, and selected diffs
- relevant files or excerpts
- validation output summaries
- explicit exclusions

Prefer text input under 20,000 characters, file/pasted attachment for 20,000-80,000 characters, and split packages above 80,000 characters, 20 files, or 1 MB.

When ChatGPT turns pasted text into an attachment, verify that exactly one intended attachment exists before sending. Do not paste the same package again unless the first attachment is removed or the upload clearly failed.

## Review Artifact

Write `review.md` unless the user names another path. Preserve previous useful passes by appending a dated pass.

Each pass should record:

- repository, branch, base, and commit/diff basis
- ChatGPT URL or `Not verified`
- browser/profile route
- input and output method
- reviewer findings
- Codex verification notes
- fix plan and validation
- attribution gaps
