---
graph_id: 10_flow_mcp_tool
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_mcp_tool.graph.yaml
---

# Flow：MCP 连接 · 发现 tool · needs-auth / reconnect

connectAll → connectOne/createClient（stdio/sse/http 折叠）→ status → attachMcpTools；needs-auth 走 createMcpAuthTool → reconnect 侧链

## Mermaid

```mermaid
flowchart TD
    MCP_SKILL[MCP_CONFIG_SKILL builtin]
    MCP_IDX[mcp/index re-export]
    MCP_CONN[McpConnectionManager.connectAll]
    MCP_ONE[connectOne · createClient 折叠 transport]
    MCP_DISC[connectAndDiscoverTools]
    MCP_ST[status 分支]
    MCP_OK[connected]
    MCP_NA[needs-auth]
    MCP_FAIL[failed]
    MCP_ATT[attachMcpTools]
    MCP_REG[registerMcpServer · qualify]
    MCP_AUTH[createMcpAuthTool · OAuth 折叠]
    MCP_RECONN[reconnect]
    MCP_LOOP[loopTools 合并 mcp]
    MCP_CALL[callTool → mcpResultToExecutableOutput]

    MCP_IDX --> MCP_CONN
    // → packages/agent-core/src/mcp/index.ts#L1
    // → packages/agent-core/src/mcp/connection-manager.ts#L72
    MCP_CONN --"~>"--> MCP_ONE
    // → packages/agent-core/src/mcp/connection-manager.ts#L156
    // → packages/agent-core/src/mcp/connection-manager.ts#L213
    // → packages/agent-core/src/mcp/connection-manager.ts#L226
    MCP_ONE --"~>"--> MCP_DISC
    // → packages/agent-core/src/mcp/connection-manager.ts#L258
    // → packages/agent-core/src/mcp/connection-manager.ts#L332
    // → packages/agent-core/src/mcp/connection-manager.ts#L334
    // → packages/agent-core/src/mcp/connection-manager.ts#L337
    // → packages/agent-core/src/mcp/connection-manager.ts#L344
    MCP_DISC --"?>"--> MCP_ST
    // → packages/agent-core/src/mcp/connection-manager.ts#L379
    MCP_DISC --"[timeout]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/connection-manager.ts#L267
    // → packages/agent-core/src/mcp/connection-manager.ts#L495
    MCP_ST --"[ok]"--> MCP_OK
    // → packages/agent-core/src/mcp/connection-manager.ts#L280
    MCP_ST --"?>"--> MCP_NA
    // → packages/agent-core/src/mcp/connection-manager.ts#L289
    // → packages/agent-core/src/mcp/connection-manager.ts#L367
    MCP_ST --"[err]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/connection-manager.ts#L293
    MCP_OK --"[err]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/connection-manager.ts#L305
    // → packages/agent-core/src/mcp/connection-manager.ts#L315
    MCP_SKILL --"::triggers"--> MCP_NA
    // → packages/agent-core/src/skill/builtin/mcp-config.ts#L14
    MCP_OK --"::triggers"--> MCP_ATT
    // → packages/agent-core/src/agent/tool/index.ts#L68
    // → packages/agent-core/src/agent/tool/index.ts#L307
    MCP_NA --"::triggers"--> MCP_ATT
    // → packages/agent-core/src/agent/tool/index.ts#L75
    // → packages/agent-core/src/agent/tool/index.ts#L311
    MCP_ATT --"[ok]"--> MCP_REG
    // → packages/agent-core/src/agent/tool/index.ts#L367
    // → packages/agent-core/src/agent/tool/index.ts#L236
    MCP_ATT --"?>"--> MCP_AUTH
    // → packages/agent-core/src/agent/tool/index.ts#L336
    MCP_REG --> MCP_LOOP
    // → packages/agent-core/src/agent/tool/index.ts#L544
    MCP_AUTH --> MCP_LOOP
    // → packages/agent-core/src/agent/tool/index.ts#L348
    // → packages/agent-core/src/agent/tool/index.ts#L544
    MCP_AUTH --"~>"--> MCP_RECONN
    // → packages/agent-core/src/mcp/auth-tool.ts#L83
    // → packages/agent-core/src/mcp/auth-tool.ts#L102
    // → packages/agent-core/src/mcp/auth-tool.ts#L142
    // → packages/agent-core/src/agent/tool/index.ts#L352
    // → packages/agent-core/src/mcp/oauth/service.ts#L102
    MCP_RECONN --"~>"--> MCP_ONE
    // → packages/agent-core/src/mcp/connection-manager.ts#L232
    // → packages/agent-core/src/mcp/connection-manager.ts#L248
    MCP_AUTH --"[err]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/auth-tool.ts#L112
    // → packages/agent-core/src/mcp/auth-tool.ts#L168
    MCP_AUTH --"[timeout]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/auth-tool.ts#L135
    MCP_RECONN --"[err]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/connection-manager.ts#L234
    // → packages/agent-core/src/mcp/connection-manager.ts#L238
    MCP_LOOP --"::yields"--> MCP_CALL
    // → packages/agent-core/src/agent/tool/index.ts#L279
    // → packages/agent-core/src/agent/tool/index.ts#L544

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| MCP_SKILL | MCP_CONFIG_SKILL builtin | flow |
| MCP_IDX | mcp/index re-export |  |
| MCP_CONN | McpConnectionManager.connectAll |  |
| MCP_ONE | connectOne · createClient 折叠 transport |  |
| MCP_DISC | connectAndDiscoverTools |  |
| MCP_ST | status 分支 |  |
| MCP_OK | connected |  |
| MCP_NA | needs-auth |  |
| MCP_FAIL | failed |  |
| MCP_ATT | attachMcpTools |  |
| MCP_REG | registerMcpServer · qualify |  |
| MCP_AUTH | createMcpAuthTool · OAuth 折叠 |  |
| MCP_RECONN | reconnect |  |
| MCP_LOOP | loopTools 合并 mcp |  |
| MCP_CALL | callTool → mcpResultToExecutableOutput |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| MCP_IDX | MCP_CONN | -> | depends_on |  | 2 anchor(s) |
| MCP_CONN | MCP_ONE | ~> | async_calls |  | 3 anchor(s) |
| MCP_ONE | MCP_DISC | ~> | async_calls |  | 5 anchor(s) |
| MCP_DISC | MCP_ST | ?> | condition |  | 1 anchor(s) |
| MCP_DISC | MCP_FAIL | [timeout] | depends_on |  | 2 anchor(s) |
| MCP_ST | MCP_OK | [ok] | depends_on |  | 1 anchor(s) |
| MCP_ST | MCP_NA | ?> | condition |  | 2 anchor(s) |
| MCP_ST | MCP_FAIL | [err] | depends_on |  | 1 anchor(s) |
| MCP_OK | MCP_FAIL | [err] | depends_on |  | 2 anchor(s) |
| MCP_SKILL | MCP_NA | ::triggers | triggers |  | 1 anchor(s) |
| MCP_OK | MCP_ATT | ::triggers | triggers |  | 2 anchor(s) |
| MCP_NA | MCP_ATT | ::triggers | triggers |  | 2 anchor(s) |
| MCP_ATT | MCP_REG | [ok] | depends_on |  | 2 anchor(s) |
| MCP_ATT | MCP_AUTH | ?> | condition |  | 1 anchor(s) |
| MCP_REG | MCP_LOOP | -> | depends_on |  | 1 anchor(s) |
| MCP_AUTH | MCP_LOOP | -> | depends_on |  | 2 anchor(s) |
| MCP_AUTH | MCP_RECONN | ~> | async_calls |  | 5 anchor(s) |
| MCP_RECONN | MCP_ONE | ~> | async_calls |  | 2 anchor(s) |
| MCP_AUTH | MCP_FAIL | [err] | depends_on |  | 2 anchor(s) |
| MCP_AUTH | MCP_FAIL | [timeout] | depends_on |  | 1 anchor(s) |
| MCP_RECONN | MCP_FAIL | [err] | depends_on |  | 2 anchor(s) |
| MCP_LOOP | MCP_CALL | ::yields | yields |  | 2 anchor(s) |

## Notes

**deep**：needs-auth → `createMcpAuthTool`（OAuth beginAuthorization/complete 折叠）→ `reconnect` → `connectOne` 侧链已补；connected 后 unexpected close 挂 `[err]`。
stdio / sse / http 仍折叠进 `createClient`（connection-manager L334/L337/L344），不为每个 transport 另开图。
daemon `IMcpService`（`packages/agent-core/src/services/mcp/mcp.ts` · `mcpService.ts`）不另开图。
`00_main` 索引边 `FLOW_MCP` 留给 W-close，本波不改 `00_main.graph.yaml`。


