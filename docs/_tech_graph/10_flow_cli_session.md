---
graph_id: 10_flow_cli_session
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_cli_session.graph.yaml
---

# Flow：CLI 会话主循环 · TUI/ACP · approve-once vs session

main 启动 → uiMode/ACP 分叉 → SDK createSession → TUI ApprovalPanel 四选项 · once vs session

## Mermaid

```mermaid
flowchart TD
    CS_START[进程启动 main]
    CS_PARSE[解析 argv / uiMode]
    CS_PROMPT[[print 子流程 · runPrompt]]
    CS_TUI[shell · KimiTUI.start]
    CS_ACP[[ACP 子流程 · runAcpServer]]
    CS_SDK_CALL[harness.createSession]
    CS_LOOP[用户输入 / session.prompt]
    CS_AGENT[[agent-core 轮次 子流程]]
    CS_PERM[PermissionManager.beforeToolCall]
    CS_PERM_ASK[policy kind=ask · requestToolApproval]
    CS_PERM_DENY[policy kind=deny 阻断]
    CS_APPROVE_PANEL[ApprovalPanel · 四选项]
    CS_APPROVE_ONCE[Approve once · 无 scope]
    CS_APPROVE_SESSION[Approve for session · scope=session]
    CS_REJECT[Reject / cancel]
    CS_CONTROLLER[ApprovalController.autoResolveFor]
    CS_SESSION_CACHE[sessionApprovalRulePatterns 缓存]
    CS_SESSION_HIST[session-approval-history 复用]
    CS_TOOLS[工具执行（允许）]
    CS_EXIT[退出 / shutdown]

    CS_START --> CS_PARSE
    // → apps/kimi-code/src/main.ts#L118
    // → apps/kimi-code/src/main.ts#L179
    CS_PARSE --"?>"--> CS_PROMPT
    // → apps/kimi-code/src/main.ts#L61
    // → apps/kimi-code/src/cli/run-prompt.ts#L57
    CS_PARSE --"?>"--> CS_TUI
    // → apps/kimi-code/src/main.ts#L66
    // → apps/kimi-code/src/cli/run-shell.ts#L33
    CS_PARSE --"?>"--> CS_ACP
    // → apps/kimi-code/src/cli/commands.ts#L91
    // → apps/kimi-code/src/cli/sub/acp.ts#L40
    CS_PROMPT --"~>"--> CS_SDK_CALL
    // → apps/kimi-code/src/cli/run-prompt.ts#L293
    CS_TUI --"~>"--> CS_SDK_CALL
    // → apps/kimi-code/src/cli/run-shell.ts#L163
    // → apps/kimi-code/src/tui/kimi-tui.ts#L698
    CS_ACP --"~>"--> CS_SDK_CALL
    // → packages/acp-adapter/src/server.ts#L286
    // → apps/kimi-code/src/cli/sub/acp.ts#L112
    CS_PROMPT --"[err]"--> CS_EXIT
    // → apps/kimi-code/src/cli/run-prompt.ts#L227
    CS_ACP --"[err]"--> CS_EXIT
    // → apps/kimi-code/src/cli/sub/acp.ts#L121
    CS_SDK_CALL --> CS_LOOP
    // → packages/node-sdk/src/kimi-harness.ts#L92
    CS_LOOP --"~>"--> CS_AGENT
    // → apps/kimi-code/src/tui/kimi-tui.ts#L1162
    // → apps/kimi-code/src/cli/run-prompt.ts#L151
    CS_AGENT --> CS_PERM
    // → packages/agent-core/src/agent/permission/index.ts#L96
    CS_PERM --"?>"--> CS_PERM_ASK
    // → packages/agent-core/src/agent/permission/index.ts#L281
    // → packages/agent-core/src/agent/permission/index.ts#L116
    CS_PERM --"[ok]"--> CS_TOOLS
    // → packages/agent-core/src/agent/permission/index.ts#L272
    CS_PERM --"[err]"--> CS_PERM_DENY
    // → packages/agent-core/src/agent/permission/index.ts#L276
    CS_PERM_ASK --"~>"--> CS_APPROVE_PANEL
    // → apps/kimi-code/src/tui/reverse-rpc/approval/handler.ts#L12
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L19
    // → apps/kimi-code/src/tui/kimi-tui.ts#L2434
    CS_APPROVE_PANEL --"?>"--> CS_APPROVE_ONCE
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L7
    CS_APPROVE_PANEL --"?>"--> CS_APPROVE_SESSION
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L155
    CS_APPROVE_PANEL --"[err]"--> CS_REJECT
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L10
    // → apps/kimi-code/src/tui/reverse-rpc/approval/handler.ts#L16
    CS_APPROVE_ONCE --> CS_CONTROLLER
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L164
    // → apps/kimi-code/src/tui/kimi-tui.ts#L2443
    CS_APPROVE_SESSION --> CS_CONTROLLER
    // → apps/kimi-code/src/tui/reverse-rpc/approval/controller.ts#L14
    CS_CONTROLLER --"[ok]"--> CS_TOOLS
    // → apps/kimi-code/src/tui/reverse-rpc/approval/controller.ts#L19
    CS_CONTROLLER --"?>"--> CS_SESSION_CACHE
    // → packages/agent-core/src/agent/permission/index.ts#L86
    // → apps/kimi-code/src/tui/reverse-rpc/approval/controller.ts#L20
    CS_SESSION_CACHE --> CS_SESSION_HIST
    // → packages/agent-core/src/agent/permission/policies/session-approval-history.ts#L17
    CS_SESSION_HIST --> CS_TOOLS
    // → packages/agent-core/src/agent/permission/policies/session-approval-history.ts#L22
    CS_TOOLS --> CS_LOOP
    // → apps/kimi-code/src/tui/kimi-tui.ts#L1162
    CS_LOOP --> CS_EXIT
    // → apps/kimi-code/src/cli/run-shell.ts#L136
    // → apps/kimi-code/src/cli/run-prompt.ts#L158

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| CS_START | 进程启动 main | flow |
| CS_PARSE | 解析 argv / uiMode |  |
| CS_PROMPT | print 子流程 · runPrompt |  |
| CS_TUI | shell · KimiTUI.start |  |
| CS_ACP | ACP 子流程 · runAcpServer |  |
| CS_SDK_CALL | harness.createSession | flow |
| CS_LOOP | 用户输入 / session.prompt |  |
| CS_AGENT | agent-core 轮次 子流程 | flow |
| CS_PERM | PermissionManager.beforeToolCall |  |
| CS_PERM_ASK | policy kind=ask · requestToolApproval |  |
| CS_PERM_DENY | policy kind=deny 阻断 |  |
| CS_APPROVE_PANEL | ApprovalPanel · 四选项 |  |
| CS_APPROVE_ONCE | Approve once · 无 scope |  |
| CS_APPROVE_SESSION | Approve for session · scope=session |  |
| CS_REJECT | Reject / cancel |  |
| CS_CONTROLLER | ApprovalController.autoResolveFor |  |
| CS_SESSION_CACHE | sessionApprovalRulePatterns 缓存 |  |
| CS_SESSION_HIST | session-approval-history 复用 |  |
| CS_TOOLS | 工具执行（允许） |  |
| CS_EXIT | 退出 / shutdown |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| CS_START | CS_PARSE | -> | depends_on |  | 2 anchor(s) |
| CS_PARSE | CS_PROMPT | ?> | condition |  | 2 anchor(s) |
| CS_PARSE | CS_TUI | ?> | condition |  | 2 anchor(s) |
| CS_PARSE | CS_ACP | ?> | condition |  | 2 anchor(s) |
| CS_PROMPT | CS_SDK_CALL | ~> | async_calls |  | 1 anchor(s) |
| CS_TUI | CS_SDK_CALL | ~> | async_calls |  | 2 anchor(s) |
| CS_ACP | CS_SDK_CALL | ~> | async_calls |  | 2 anchor(s) |
| CS_PROMPT | CS_EXIT | [err] | condition |  | 1 anchor(s) |
| CS_ACP | CS_EXIT | [err] | condition |  | 1 anchor(s) |
| CS_SDK_CALL | CS_LOOP | -> | depends_on |  | 1 anchor(s) |
| CS_LOOP | CS_AGENT | ~> | async_calls |  | 2 anchor(s) |
| CS_AGENT | CS_PERM | -> | depends_on |  | 1 anchor(s) |
| CS_PERM | CS_PERM_ASK | ?> | condition |  | 2 anchor(s) |
| CS_PERM | CS_TOOLS | [ok] | condition |  | 1 anchor(s) |
| CS_PERM | CS_PERM_DENY | [err] | condition |  | 1 anchor(s) |
| CS_PERM_ASK | CS_APPROVE_PANEL | ~> | async_calls |  | 3 anchor(s) |
| CS_APPROVE_PANEL | CS_APPROVE_ONCE | ?> | condition |  | 1 anchor(s) |
| CS_APPROVE_PANEL | CS_APPROVE_SESSION | ?> | condition |  | 1 anchor(s) |
| CS_APPROVE_PANEL | CS_REJECT | [err] | condition |  | 2 anchor(s) |
| CS_APPROVE_ONCE | CS_CONTROLLER | -> | depends_on |  | 2 anchor(s) |
| CS_APPROVE_SESSION | CS_CONTROLLER | -> | depends_on |  | 1 anchor(s) |
| CS_CONTROLLER | CS_TOOLS | [ok] | condition |  | 1 anchor(s) |
| CS_CONTROLLER | CS_SESSION_CACHE | ?> | condition |  | 2 anchor(s) |
| CS_SESSION_CACHE | CS_SESSION_HIST | -> | depends_on |  | 1 anchor(s) |
| CS_SESSION_HIST | CS_TOOLS | -> | depends_on |  | 1 anchor(s) |
| CS_TOOLS | CS_LOOP | -> | depends_on |  | 1 anchor(s) |
| CS_LOOP | CS_EXIT | -> | depends_on |  | 2 anchor(s) |

## Notes

**主干（TUI）**：`main` → `runShell` → `KimiTUI.init` `createSession` → `session.prompt`
→ `PermissionManager` ask → `adaptApprovalRequest` / `showApprovalPanel` →
Approve once（无 scope）vs Approve for session（`scope=session` + `autoResolveFor`）
→ `sessionApprovalRulePatterns` / `session-approval-history` → 工具执行。

**分叉**：`uiMode==='print'` → `runPrompt`（`createSession` L293 · headless
`setApprovalHandler` 自动 approved，不经 TUI 面板）。`kimi acp` →
`runAcpServer`（`acp-adapter` `createSession` L286 · 审批桥 `session.ts`
`setApprovalHandler` L220，折叠不展开 ACP UI）。

**#437**：Approve once 仅当次；Approve for session 写入
`localSessionApprovalRulePatterns`；同 action 队列可 `autoResolveFor`。

**折叠**：agent-core 轮次细节见 `10_flow_agent_turn`（本图不展开）。
ACP transport / print JSON 输出不画。

**纠正**：旧骨架把 allow 标成 `[err]`、把 session 选项标成 `[err]`；现码
allow=`approve`、session 为合法 `?>` 分支，deny/reject 才是 `[err]`。


