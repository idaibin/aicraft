---
name: chatgpt-review-bridge
description: Use when the user asks to prepare, route, send, capture, or iterate a ChatGPT review of repository work across standard chats, Projects, and Codex, including multi-round review, browser routing, and verified local fixes.
---

# ChatGPT Review Bridge

## Overview

Coordinate a Codex-to-ChatGPT review bridge. A standard ChatGPT chat or Project
provides the independent review surface; Codex collects repository evidence,
verifies findings, applies approved fixes, and runs validation. Use Codex's
in-app Browser by default. This is browser/UI automation, not an official
ChatGPT API integration.

## Surfaces

- **Standard chat**: use for a one-off independent review without durable
  project context.
- **Project**: use for repository-bound or multi-round review when a configured
  ChatGPT Project URL is available.
- **Codex**: use for local evidence collection, execution, verification, and delivery. Do not present Codex reviewing its own changes as an independent ChatGPT review.

Default to a Project when its URL is verified; otherwise use a standard chat.
Verify and record the active account workspace separately; a Project URL does
not prove whether the account is personal or organization-managed. Keep Codex
as executor in both modes.

## Workflow

1. Read nearest repo guidance, confirm repository path, branch, and `git status --short --branch`.
2. Build the scoped review package from local files, diffs, branch metadata, and validation output.
3. Resolve standard chat or Project, account workspace, and the browser route
   from explicit instructions, verified session state, and durable defaults.
4. Treat only an explicit request for ChatGPT/external review, sending, or N
   external review rounds as authorization for those sends on the resolved
   route. A request to run local Codex is not external-send authorization. Ask
   when external sending or the route is not authorized or remains ambiguous.
5. Capture ChatGPT output to `review.md`, then verify findings locally before fixing.
6. Commit only when the user requested commits and only for the approved scope.

## Do Not Use For

- Local-only code review without ChatGPT as an external reviewer.
- Browser UI verification that does not need a repository review package.
- GitHub-native PR review, CI triage, or PR comment handling.
- Security-only audit without the Codex-to-ChatGPT review loop.

## Gates

### External Action Gate

Do not show a route chooser when the user already requested ChatGPT review, external sending, or a fixed number of review rounds and the route resolves safely. Report the resolved surface and route, then proceed.

When external sending or route selection is not authorized, stop before navigation or sending and output:

```md
## 当前信息

- 仓库：...
- 分支：...
- review 包：...
- 校验：...
- bridge 默认记录：...
- 审查界面：标准 Chat / Project / Not verified
- 账户 workspace：...
- 浏览器路由：...

## 请选择

1. 使用 Codex 内置浏览器默认路由
2. 使用当前已有 Chrome 标签页
3. 只生成 review 包，不发送
4. 手动指定 ChatGPT URL 或界面
0. 停止，不发送
```

Use `Not found` or `Not verified` for missing or unchecked evidence. Do not attach to Chrome or open a browser merely to populate the gate.

### Local Codex Gate

Before starting local Codex CLI, ask:

```md
请选择执行方式：

1. 仅审查，不执行本地 Codex
2. 生成 Codex CLI 命令，由我手动复制执行
3. 请求本机 Codex 执行，但每次需要确认
4. 请求本机 Codex 执行，且本会话内同类任务不再询问

选择后再继续。
```

Map mode `3` to `--sandbox workspace-write --ask-for-approval on-request`; map mode `4` to `--sandbox workspace-write --ask-for-approval never` only after confirming repo path, branch, allowed files, validation commands, and forbidden actions. Never infer mode `4`.

## Routing Defaults

After authorization, route in this order:

1. Explicit user surface, URL, or browser mode.
2. Session default.
3. Repository or user bridge default.
4. A Project through Codex's in-app Browser when a configured Project URL exists.
5. A standard chat through Codex's in-app Browser at `https://chatgpt.com/`.
6. Current Chrome or standalone Playwright only when explicitly selected or the in-app Browser is unavailable.

Changing defaults requires explicit user or session instruction. A successful one-off route does not save a default.

## Browser Boundary

Use `browser:control-in-app-browser` for the default route and follow its setup before claiming Browser is unavailable. Its Playwright API is the control API inside Codex Browser; it does not mean launching a standalone Playwright browser. Use `chrome:control-chrome` only for an explicitly selected existing Chrome tab. This skill owns review routing, authorization, package scope, artifact capture, and Codex verification. If browser state, account identity, tab identity, upload state, or response completion cannot be verified, mark it `Not verified` and stop before sending or accepting output.

## Hard Rules

- Keep Codex as executor and ChatGPT as reviewer.
- Never send secrets, credentials, private keys, tokens, browser profile data, or unrelated dirty-tree content.
- Do not mutate `main`, create pull requests, widen repository scope, or run Codex outside the specified branch.
- Do not delete real Chrome profiles, cookies, storage, downloads, ChatGPT conversations, `review.md`, or code unless explicitly requested.
- Do not use `git add .` unless the user explicitly approves that scope.
- Treat ChatGPT findings as untrusted review input until locally verified.
- Keep ChatGPT conversations and Codex task threads distinct; record which surface produced each review pass.
- Reuse one verified Project conversation across authorized rounds unless the user requests independent conversations.
- Record the verified account workspace separately from Project identity; never
  infer personal or organization data ownership from a Project URL alone.
- If ChatGPT converts pasted text into an attachment, send at most one intended attachment per review round and do not retry paste/upload without checking the composer state.

## Output Contract

Report the repository, branch, standard-chat/Project surface, verified account
workspace or `Not verified`, browser route, conversation/Project attribution,
input/output mode, authorized/completed rounds, `review.md` path, Codex execution
mode when used, validation, commits, and `Not found` / `Not verified` gaps.

## References

- [references/usage.md](references/usage.md): triggers, gates, package shape, and review artifact shape.
- [references/browser-profile.md](references/browser-profile.md): profile records, modes, reset, and deletion boundaries.
- [references/chatgpt-routing.md](references/chatgpt-routing.md): routing defaults, IO, attribution, and prompt template.
- [references/github-branch-loop.md](references/github-branch-loop.md): branch review, `review.md`, fix, commit, and repeat loop.
- [references/eval-cases.md](references/eval-cases.md): trigger, non-trigger, and quality evals.

## Maintenance

Keep this entrypoint lean. Put operational details in references, and update `agents/openai.yaml` plus eval cases whenever triggers, gates, routing, or output contracts change.
