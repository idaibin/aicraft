# Eval Cases

Use these cases when changing `ops-client` triggers, modes, window evidence rules, Accessibility guidance, AI-operable UI guidance, or metadata.

## Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `验证真实 Tauri 客户端窗口，不要用浏览器预览。` | Should trigger `ops-client`. | Real client-window verification. |
| `操作这个指定客户端，先确认启动命令和运行来源。` | Should trigger `ops-client`. | Specified client and launch review. |
| `看当前仓库里有没有 Tauri 客户端，以及应该怎么启动。` | Should trigger `ops-client`. | Repository-contained client discovery. |
| `用 CGWindowID 截一下 app 窗口。` | Should trigger `ops-client`. | Window-level screenshot evidence. |
| `这个 Tauri/客户端按钮让 AI 更容易识别和点击。` | Should trigger `ops-client`. | AI-operable DOM/Accessibility guidance for client UI. |

## Non-Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `复用浏览器标签页填写网页表单。` | Should prefer `ops-browser`. | Browser operation workflow. |
| `这个网页按钮让 AI 更容易识别和点击。` | Should prefer `ops-browser` or frontend work, not `ops-client`. | Browser UI is not desktop-client operation. |
| `审查当前 git 改动，分类提交。` | Should prefer `code-review`. | Dirty-tree review. |
| `先了解这个仓库的目录和命令。` | Should prefer `code-context`. | Repository context task. |

## Quality Eval

| Case | Expected evidence | Reject if |
| --- | --- | --- |
| Real window evidence | Confirms process/runtime/window identity and captures by `CGWindowID`. | Uses browser preview or region screenshot as client proof. |
| Runtime source | Distinguishes `pnpm tauri dev`, debug bundle, release app, or reports `Not verified`. | Assumes runtime source without evidence. |
| Launch command | Identifies the client app location and startup command from manifests/docs/scripts or reports `Not found`. | Starts or verifies a client without checking the owning command. |
| Startup safety | Confirms whether starting or restarting the client could disturb an existing instance, active window, or user workflow. | Restarts the client without checking impact. |
| Background-safe interaction | Uses Accessibility/control-tree paths and avoids stealing mouse/focus where possible. | Coordinate-clicks without checking stable control paths. |
| AI-operable UI | Recommends semantic controls, accessible names, labels, and stable selectors for critical controls. | Leaves icon-only or generic controls unidentified. |
| Restart/rebuild | Re-verifies after relevant UI, bundle, or Accessibility changes. | Claims fix against stale client instance. |

## Scoring

Score each quality case from 0 to 10. Minimum pass: all trigger/non-trigger expectations are correct and every quality case scores at least 7.
