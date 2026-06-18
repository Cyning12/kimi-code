---
graph_id: 10_flow_agent_turn
version: 2026-06-18
generated_at: 2026-06-18T14:26:55Z
source: docs/_tech_graph/10_flow_agent_turn.graph.yaml
---

# Flow：Agent 轮次 · tool 结果与 telemetry（C2 #583 切片）

tool 中止 → tool.result → tool_call telemetry outcome

## Mermaid

```mermaid
flowchart TD
    AT_EXEC[tool 执行]
    AT_SETTLE[abort settle / 正常返回]
    AT_UC[isUserCancellation?]
    AT_MARK[cancelledByUser=true]
    AT_ERR[isError output 无 user 标记]
    AT_OK[isError false]
    AT_RESULT[ExecutableToolResult]
    AT_EVENT[LoopEvent tool.result]
    AT_TRACK[trackToolLifecycle]
    AT_OUTCOME[telemetryToolOutcome]
    AT_OC[outcome 分支]
    AT_TRACK_OK[properties outcome success]
    AT_TRACK_CANCEL[properties outcome cancelled]
    AT_TRACK_ERR[properties outcome error]
    AT_ERRTYPE[telemetryToolErrorType]
    AT_TELEM[telemetry.track tool_call]

    AT_EXEC --> AT_SETTLE
    // → packages/agent-core/src/loop/tool-call.ts
    AT_SETTLE --"?>"--> AT_UC
    // → packages/agent-core/src/utils/abort.ts
    AT_UC --"[ok]"--> AT_MARK
    AT_UC --"[err]"--> AT_ERR
    AT_MARK --> AT_RESULT
    AT_ERR --> AT_RESULT
    AT_SETTLE --"[ok]"--> AT_OK
    AT_OK --> AT_RESULT
    AT_RESULT --> AT_EVENT
    AT_EVENT --> AT_TRACK
    // → packages/agent-core/src/agent/turn/index.ts#L787
    AT_TRACK --> AT_OUTCOME
    // → packages/agent-core/src/agent/turn/tool-telemetry.ts
    AT_OUTCOME --"?>"--> AT_OC
    AT_OC --"success"--> AT_TRACK_OK
    AT_OC --"cancelled"--> AT_TRACK_CANCEL
    AT_OC --"error"--> AT_TRACK_ERR
    AT_TRACK_ERR --> AT_ERRTYPE
    AT_ERRTYPE --> AT_TRACK_ERR
    AT_TRACK_OK --"::archives"--> AT_TELEM
    AT_TRACK_CANCEL --"::archives"--> AT_TELEM
    AT_TRACK_ERR --"::archives"--> AT_TELEM
    // → packages/telemetry

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| AT_EXEC | tool 执行 |  |
| AT_SETTLE | abort settle / 正常返回 |  |
| AT_UC | isUserCancellation? |  |
| AT_MARK | cancelledByUser=true |  |
| AT_ERR | isError output 无 user 标记 |  |
| AT_OK | isError false |  |
| AT_RESULT | ExecutableToolResult |  |
| AT_EVENT | LoopEvent tool.result |  |
| AT_TRACK | trackToolLifecycle |  |
| AT_OUTCOME | telemetryToolOutcome |  |
| AT_OC | outcome 分支 |  |
| AT_TRACK_OK | properties outcome success |  |
| AT_TRACK_CANCEL | properties outcome cancelled |  |
| AT_TRACK_ERR | properties outcome error |  |
| AT_ERRTYPE | telemetryToolErrorType |  |
| AT_TELEM | telemetry.track tool_call |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| AT_EXEC | AT_SETTLE | -> | depends_on |  | 1 anchor(s) |
| AT_SETTLE | AT_UC | ?> | condition |  | 1 anchor(s) |
| AT_UC | AT_MARK | [ok] | depends_on |  |  |
| AT_UC | AT_ERR | [err] | depends_on |  |  |
| AT_MARK | AT_RESULT | -> | depends_on |  |  |
| AT_ERR | AT_RESULT | -> | depends_on |  |  |
| AT_SETTLE | AT_OK | [ok] | depends_on |  |  |
| AT_OK | AT_RESULT | -> | depends_on |  |  |
| AT_RESULT | AT_EVENT | -> | depends_on |  |  |
| AT_EVENT | AT_TRACK | -> | depends_on |  | 1 anchor(s) |
| AT_TRACK | AT_OUTCOME | -> | depends_on |  | 1 anchor(s) |
| AT_OUTCOME | AT_OC | ?> | condition |  |  |
| AT_OC | AT_TRACK_OK | -> | depends_on | success |  |
| AT_OC | AT_TRACK_CANCEL | -> | depends_on | cancelled |  |
| AT_OC | AT_TRACK_ERR | -> | depends_on | error |  |
| AT_TRACK_ERR | AT_ERRTYPE | -> | depends_on |  |  |
| AT_ERRTYPE | AT_TRACK_ERR | -> | depends_on |  |  |
| AT_TRACK_OK | AT_TELEM | ::archives | archives |  |  |
| AT_TRACK_CANCEL | AT_TELEM | ::archives | archives |  |  |
| AT_TRACK_ERR | AT_TELEM | ::archives | archives |  | 1 anchor(s) |

## Notes

**#437 关联（permission · 非本图节点增量）**：Write/Edit approve-for-session
按工具名缓存 session 规则 · `packages/agent-core/src/agent/permission/index.ts`


