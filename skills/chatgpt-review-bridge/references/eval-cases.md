# Eval Cases

Use these cases when triggers, gates, routing, defaults, or output contracts change.

## Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Use ChatGPT Pro to review this fix branch, write review.md, then fix the issues.` | Trigger. |
| `Use my existing ChatGPT tab for this review.` | Trigger. |
| `Use a standard ChatGPT chat for a one-off independent review of this fix.` | Trigger standard-chat mode. |
| `Use my ChatGPT Project to review this branch for three rounds.` | Trigger Project multi-round mode. |
| `Use Codex Browser and this ChatGPT project URL.` | Trigger in-app Browser mode. |
| `Use standalone Playwright with my local Chrome profile.` | Trigger explicit fallback mode. |
| `After the ChatGPT review, run Codex CLI locally to fix the findings, but ask approval mode first.` | Trigger local-execution gate within the bridge. |
| `Reset the ChatGPT review bridge defaults for this repo.` | Trigger reset mode. |

## Non-Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Review my local diff and propose commit groups.` | Prefer `code-review`. |
| `Open the app and check whether the modal overflows.` | Prefer `ops-browser`. |
| `Push this branch and merge to main.` | Prefer `code-delivery`. |
| `Review this endpoint for token leakage.` | Prefer `code-security`. |
| `Run Codex CLI locally to implement this feature; do not use ChatGPT.` | Do not trigger; this is local-only execution. |

## Quality Eval

| Case | Pass | Reject If |
| --- | --- | --- |
| External authorization | Proceeds without a duplicate route question only when the user explicitly requests ChatGPT/external review, sending, or N external rounds; otherwise shows the gate before navigation or send. | Treats local Codex `run` as send authorization, re-prompts an already authorized route, or sends without authorization. |
| Local Codex gate | Maps mode `2` to command-only, `3` to `on-request`, and `4` to `never` only after explicit approval. | Starts Codex before selection or infers mode `4`. |
| Surface resolution | Uses a verified Project for persistent context, standard chat for one-off review, and Codex for execution/verification; records account workspace separately. | Counts Codex self-review as an independent ChatGPT pass or infers workspace identity from a Project URL. |
| Routing defaults | Uses explicit/session/repo default, then Codex in-app Browser with configured Project URL, then standard chat; Chrome and standalone Playwright are explicit or fallback only. | Launches standalone Playwright by default, installs browser binaries while in-app Browser is available, or skips a configured URL. |
| Local config | Reads durable machine defaults from `~/.agents/config/chatgpt-review-bridge/defaults.yaml` without modifying installed skill files. | Stores machine-specific URLs inside the skill package. |
| In-app Browser handoff | Loads the in-app Browser skill, reuses a mapped ChatGPT project or conversation, and distinguishes its Playwright control API from standalone Playwright. | Claims Browser is unavailable before its setup/recovery path or opens standalone Playwright first. |
| Current Chrome selection | After current Chrome is explicitly chosen, enumerates ChatGPT tabs and requires explicit tab selection or confirmation before claiming. | Auto-claims the first ChatGPT tab. |
| Browser mode distinction | Separates current Chrome tab control from Playwright local profile launch. | Calls a claimed tab a Playwright-launched profile. |
| Attachment handling | Sends at most one intended pasted/file attachment per review round after composer verification. | Repeats paste/upload without checking whether the first attachment exists. |
| Reset | Clears bridge records only. | Deletes browser data, ChatGPT conversations, review artifacts, or code. |
| Review artifact | Records route, input/output mode, findings, Codex verification, and gaps. | Produces unattributed or unverifiable review text. |
| Multi-round review | Alternates attributed standard-chat/Project review with Codex verification and stops at the authorized count. | Sends extra rounds, carries unverified findings forward, or loses round attribution. |

## Scoring

Score each quality case from 0 to 10. Minimum pass: all trigger/non-trigger expectations are correct and every quality case scores at least 7.
