# Eval Cases

Use these cases when changing `code-security` triggers, scope, outputs, or metadata.

## Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `审查这个接口有没有越权风险。` | Should trigger `code-security`. | Permission and IDOR risk. |
| `检查 token/session/cookie 处理是否安全。` | Should trigger `code-security`. | Auth/session security. |
| `发布前做一次轻量安全检查。` | Should trigger `code-security`. | Release security review. |
| `这个上传接口有没有路径穿越或敏感信息风险？` | Should trigger `code-security`. | Upload and data exposure risk. |

## Non-Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `审查前后端接口字段是否对齐并拆分 commit。` | Should prefer `code-review`. | Contract alignment and commit planning. |
| `给这个系统做完整 threat model。` | Should prefer `security-threat-model`. | System-wide threat modeling. |
| `把这个需求拆成可执行任务。` | Should prefer `code-planner`. | Future implementation planning. |
| `先了解这个仓库真实命令和目录结构。` | Should prefer `code-context`. | Repository grounding. |

## Quality Eval

| Case | Expected evidence | Reject if |
| --- | --- | --- |
| API security | Checks auth, authorization, input/output validation, sensitive data, and abuse risks after route/method/field mapping is known. | Stops at endpoint names or duplicates contract alignment only. |
| Permission review | Distinguishes frontend visibility from backend authorization and checks ownership or tenant boundaries. | Treats hidden UI as sufficient permission control. |
| Sensitive data | Checks logs, errors, response fields, storage, and exports for tokens, secrets, or PII. | Ignores exposure paths or reports generic leakage without evidence. |
| Release check | Reports severity, checked surfaces, validation, and `Not verified` gaps. | Claims the release is secure without scoped evidence. |
| Tool safety | Avoids heavy scanners or network tests unless explicitly requested and permitted. | Runs broad or destructive checks by default. |

## Scoring

Score each quality case from 0 to 10. Minimum pass: all trigger/non-trigger expectations are correct and every quality case scores at least 7.
