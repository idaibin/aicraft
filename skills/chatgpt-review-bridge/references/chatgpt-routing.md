# ChatGPT Routing And IO

## Terminology Basis

- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
  documents Projects across free and paid plan types; use `project` for durable
  project context rather than inventing another product surface.
- [ChatGPT Enterprise workspaces](https://help.openai.com/en/articles/8265430-what-is-a-workspace-how-can-i-switch-workspaces)
  documents account environments with separate conversations and files. Verify
  and record workspace identity independently from Project identity.

## Routing Order

1. Explicit user surface, URL, or browser mode.
2. Session surface and `chatgpt_default_url`.
3. Repository or user surface and `chatgpt_default_url`.
4. A Project through Codex's in-app Browser when a configured Project URL exists.
5. A standard chat through Codex's in-app Browser at `https://chatgpt.com/`.
6. Current Chrome or standalone Playwright only when explicitly selected or the in-app Browser is unavailable.

If generic ChatGPT is used, report that the review is not project-bound.

## Surface Resolution

- Resolve `project` for repository-bound, persistent, or multi-round review when a verified Project URL exists.
- Resolve `standard-chat` for one-off review or when no durable Project route exists.
- Resolve `codex` only as the executor or as an explicitly requested separate-agent review. Never count self-review as an independent ChatGPT pass.
- Treat UI labels as presentation details. Route by verified capability and URL so a label change does not silently change behavior.
- Verify and record the active account workspace independently. A Project is
  available across plan types, and its URL does not establish personal or
  organization workspace membership.

## Default Configuration

Default to Codex's in-app Browser for new bridge records.

Runtime defaults may come from a durable local config file:

```text
~/.agents/config/chatgpt-review-bridge/defaults.yaml
```

Read that file after explicit per-request and session settings, and before falling back to the generic ChatGPT URL. Do not store machine-specific defaults inside the installed skill package because package updates may overwrite them.

Supported fields:

- `default_browser_mode`: `codex-in-app-browser`, `current-chrome-explicit`, `standalone-playwright-explicit`, or `manual`
- `chatgpt_surface`: `standard-chat` or `project`
- `account_workspace_note`
- `chatgpt_default_url`
- `profile_record_name`
- `profile_path`
- `repo_path`
- `branch_scope`

Example:

```yaml
default_browser_mode: codex-in-app-browser
chatgpt_surface: project
account_workspace_note: Not verified
chatgpt_default_url: https://chatgpt.com/g/<project-id>/project
```

Changing defaults is a persistent bridge-default change and requires explicit instruction.

## Current Chrome Routing

After the user chooses current Chrome mode:

1. Enumerate open ChatGPT tabs.
2. Present candidate tabs and require an explicit tab selection or confirmation.
3. Claim only the confirmed tab.
4. Stop before sending the review package.

Do not save a selected tab or URL as a default unless separately requested.

## Codex In-App Browser Routing

After the route is explicitly authorized or resolved from an explicitly requested review:

1. Load and follow `browser:control-in-app-browser` before browser work.
2. Reuse the mapped ChatGPT project or conversation when available.
3. Open the configured Project URL; otherwise open a standard chat.
4. Ask the user to sign in inside Browser if authentication is required.
5. Mark Project identity and account workspace `Not verified` unless each is inspected.
6. Stop before sending content.

Step 6 does not apply when the current user request already explicitly authorizes sending or a fixed number of review rounds. That authorization covers only the resolved route, scope, and round count.

## Standalone Playwright Routing

Use only when explicitly selected or when the in-app Browser is unavailable after following its setup and recovery instructions. Ask for a profile only when profile mode is explicit or a profile record exists. Do not install browser binaries merely because the in-app Browser route is available.

If no browser session, tab identity, account state, upload state, or response completion signal can be verified, stop or mark the affected field `Not verified`.

## Text And File Input

Use text input for compact packages and file/pasted attachments when size or structure matters. If pasted content becomes an attachment, treat it as the single intended upload for that round, verify the composer state, and do not paste or upload again unless the first attempt is removed or clearly failed. Never upload secrets, `.env`, private registry tokens, local keychains, browser profile data, or unrelated dirty files.

## Output Capture

Capture ChatGPT output into `review.md` by direct page extraction, download, or selected response text. Screenshots are supporting evidence only.

Accept a response only when it can be tied to:

- intended and final URL
- branch/commit/diff basis
- submitted input or attachment names/counts
- completion signal or `Not verified`
- latest assistant response extraction method

Reject or mark `Not verified` if the tab is ambiguous, generation is still streaming, output is empty/truncated, or the response predates the submitted prompt.

For multiple rounds, append one attributed pass per round and verify Codex's
changes before sending the next package. Reuse the same Project conversation by
default; use separate conversations only when independence is requested.

## Prompt Template

```text
You are the reviewer. Codex is the executor.

Review the supplied branch/diff/files for concrete defects, regressions, missing tests, and unsafe assumptions. Prioritize actionable findings with file/path references when possible.

Return:
1. Findings ordered by severity
2. False-positive risks or assumptions
3. Suggested verification
4. Verdict: pass, needs changes, or blocked
```
