---
graph_id: 10_flow_cli_session
version: 2026-06-18
generated_at: 2026-06-26T07:36:26Z
source: docs/_tech_graph/10_flow_cli_session.graph.yaml
---

# Flow：CLI 会话主循环 · approve-once vs session（#437 skeleton）

CLI 启动 → TUI 审批 → agent-core 权限 ·

## Mermaid

```mermaid
flowchart TD
    CS_START[进程启动 main]
    CS_PARSE[解析 argv / 配置]
    CS_TUI[TUI 或 ACP 模式]
    CS_LOOP[用户输入 / 事件]
    CS_SDK_CALL[经 node-sdk 创建/恢复 Session]
    CS_AGENT[agent-core 处理轮次]
    CS_PERM[PermissionManager 策略链]
    CS_PERM_ASK[需用户审批 · policy ask]
    CS_APPROVE_PANEL[ApprovalPanel · 四选项]
    CS_APPROVE_ONCE[Approve once · 无 scope]
    CS_APPROVE_SESSION[Approve for session · scope=session]
    CS_CONTROLLER[ApprovalController 队列 autoResolve]
    CS_SESSION_CACHE[sessionApprovalRulePatterns 缓存]
    CS_SESSION_HIST[session-approval-history 复用]
    CS_TOOLS[工具 / 子 agent 执行]
    CS_EXIT[退出 / 保存 checkpoint]

    CS_START --> CS_PARSE
    CS_PARSE --> CS_TUI
    CS_TUI --> CS_LOOP
    CS_LOOP --> CS_SDK_CALL
    // → packages/node-sdk/src
    CS_SDK_CALL --> CS_AGENT
    CS_AGENT --> CS_PERM
    // → packages/agent-core/src/agent/permission/index.ts#L96
    CS_PERM --"[ok]"--> CS_PERM_ASK
    CS_PERM --"[err]"--> CS_TOOLS
    CS_PERM_ASK --> CS_APPROVE_PANEL
    // → apps/kimi-code/src/tui/kimi-tui.ts#L1136
    CS_APPROVE_PANEL --"[ok]"--> CS_APPROVE_ONCE
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L7
    CS_APPROVE_PANEL --"[err]"--> CS_APPROVE_SESSION
    // → apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts#L155
    CS_APPROVE_ONCE --> CS_CONTROLLER
    // → apps/kimi-code/src/tui/reverse-rpc/approval/controller.ts#L19
    CS_APPROVE_SESSION --> CS_CONTROLLER
    CS_CONTROLLER --> CS_SESSION_CACHE
    // → packages/agent-core/src/agent/permission/index.ts#L192
    CS_SESSION_CACHE --> CS_SESSION_HIST
    // → packages/agent-core/src/agent/permission/policies/session-approval-history.ts#L17
    CS_SESSION_HIST --> CS_TOOLS
    CS_TOOLS --> CS_LOOP
    CS_LOOP --> CS_EXIT

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| CS_START | 进程启动 main | flow |
| CS_PARSE | 解析 argv / 配置 |  |
| CS_TUI | TUI 或 ACP 模式 |  |
| CS_LOOP | 用户输入 / 事件 |  |
| CS_SDK_CALL | 经 node-sdk 创建/恢复 Session | flow |
| CS_AGENT | agent-core 处理轮次 | flow |
| CS_PERM | PermissionManager 策略链 |  |
| CS_PERM_ASK | 需用户审批 · policy ask |  |
| CS_APPROVE_PANEL | ApprovalPanel · 四选项 |  |
| CS_APPROVE_ONCE | Approve once · 无 scope |  |
| CS_APPROVE_SESSION | Approve for session · scope=session |  |
| CS_CONTROLLER | ApprovalController 队列 autoResolve |  |
| CS_SESSION_CACHE | sessionApprovalRulePatterns 缓存 |  |
| CS_SESSION_HIST | session-approval-history 复用 |  |
| CS_TOOLS | 工具 / 子 agent 执行 |  |
| CS_EXIT | 退出 / 保存 checkpoint |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| CS_START | CS_PARSE | -> | depends_on |  |  |
| CS_PARSE | CS_TUI | -> | depends_on |  |  |
| CS_TUI | CS_LOOP | -> | depends_on |  |  |
| CS_LOOP | CS_SDK_CALL | -> | depends_on |  | 1 anchor(s) |
| CS_SDK_CALL | CS_AGENT | -> | depends_on |  |  |
| CS_AGENT | CS_PERM | -> | depends_on |  | 1 anchor(s) |
| CS_PERM | CS_PERM_ASK | [ok] | condition |  |  |
| CS_PERM | CS_TOOLS | [err] | condition |  |  |
| CS_PERM_ASK | CS_APPROVE_PANEL | -> | depends_on |  | 1 anchor(s) |
| CS_APPROVE_PANEL | CS_APPROVE_ONCE | [ok] | condition |  | 1 anchor(s) |
| CS_APPROVE_PANEL | CS_APPROVE_SESSION | [err] | condition |  | 1 anchor(s) |
| CS_APPROVE_ONCE | CS_CONTROLLER | -> | depends_on |  | 1 anchor(s) |
| CS_APPROVE_SESSION | CS_CONTROLLER | -> | depends_on |  |  |
| CS_CONTROLLER | CS_SESSION_CACHE | -> | depends_on |  | 1 anchor(s) |
| CS_SESSION_CACHE | CS_SESSION_HIST | -> | depends_on |  | 1 anchor(s) |
| CS_SESSION_HIST | CS_TOOLS | -> | depends_on |  |  |
| CS_TOOLS | CS_LOOP | -> | depends_on |  |  |
| CS_LOOP | CS_EXIT | -> | depends_on |  |  |

## Notes

**#437 骨架（2026-06-18）**：Approve once 仅当次 · Approve for session 写入
`sessionApprovalRule` + `localSessionApprovalRulePatterns` · TUI 队列同 action
在 scope=session 时可 autoResolve（controller.autoResolveFor）。

**产品修复面（待 30）**：
- Write/Edit 等同目录多文件 · session 规则粒度（#437 comment）
- Bash 等同命令复用 · 已有 permission 测试覆盖

**锚点入口**：
- `apps/kimi-code/src/main.ts`
- `apps/kimi-code/src/tui/reverse-rpc/approval/handler.ts`


