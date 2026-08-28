---
graph_id: 10_flow_mcp_tool
version: 2026-08-28
generated_at: 2026-08-28T08:27:10Z
source: docs/_tech_graph/10_flow_mcp_tool.graph.yaml
---

# Flow：MCP 连接 · 发现 tool · 挂到 ToolManager（skeleton）

connectAll → connectOne/createClient（stdio/sse/http 折叠）→ status → attachMcpTools

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
    MCP_AUTH[createMcpAuthTool]
    MCP_LOOP[loopTools 合并 mcp]
    MCP_CALL[callTool → mcpResultToExecutableOutput]

    MCP_IDX --> MCP_CONN
    // → packages/agent-core/src/mcp/index.ts#L1
    // → packages/agent-core/src/mcp/connection-manager.ts#L72
    MCP_CONN --"~>"--> MCP_ONE
    // → packages/agent-core/src/mcp/connection-manager.ts#L156
    MCP_ONE --"~>"--> MCP_DISC
    // → packages/agent-core/src/mcp/connection-manager.ts#L258
    // → packages/agent-core/src/mcp/connection-manager.ts#L332
    MCP_DISC --"?>"--> MCP_ST
    // → packages/agent-core/src/mcp/connection-manager.ts#L379
    MCP_ST --"[ok]"--> MCP_OK
    // → packages/agent-core/src/mcp/connection-manager.ts#L280
    MCP_ST --"?>"--> MCP_NA
    // → packages/agent-core/src/mcp/connection-manager.ts#L289
    MCP_ST --"[err]"--> MCP_FAIL
    // → packages/agent-core/src/mcp/connection-manager.ts#L293
    MCP_SKILL --"::triggers"--> MCP_NA
    // → packages/agent-core/src/skill/builtin/mcp-config.ts#L14
    MCP_OK --"::triggers"--> MCP_ATT
    // → packages/agent-core/src/agent/tool/index.ts#L68
    MCP_NA --"::triggers"--> MCP_ATT
    // → packages/agent-core/src/agent/tool/index.ts#L75
    MCP_ATT --"[ok]"--> MCP_REG
    // → packages/agent-core/src/agent/tool/index.ts#L367
    MCP_ATT --"?>"--> MCP_AUTH
    // → packages/agent-core/src/agent/tool/index.ts#L336
    MCP_REG --> MCP_LOOP
    // → packages/agent-core/src/agent/tool/index.ts#L236
    MCP_AUTH --> MCP_LOOP
    // → packages/agent-core/src/agent/tool/index.ts#L348
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
| MCP_AUTH | createMcpAuthTool |  |
| MCP_LOOP | loopTools 合并 mcp |  |
| MCP_CALL | callTool → mcpResultToExecutableOutput |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| MCP_IDX | MCP_CONN | -> | depends_on |  | 2 anchor(s) |
| MCP_CONN | MCP_ONE | ~> | async_calls |  | 1 anchor(s) |
| MCP_ONE | MCP_DISC | ~> | async_calls |  | 2 anchor(s) |
| MCP_DISC | MCP_ST | ?> | condition |  | 1 anchor(s) |
| MCP_ST | MCP_OK | [ok] | depends_on |  | 1 anchor(s) |
| MCP_ST | MCP_NA | ?> | condition |  | 1 anchor(s) |
| MCP_ST | MCP_FAIL | [err] | depends_on |  | 1 anchor(s) |
| MCP_SKILL | MCP_NA | ::triggers | triggers |  | 1 anchor(s) |
| MCP_OK | MCP_ATT | ::triggers | triggers |  | 1 anchor(s) |
| MCP_NA | MCP_ATT | ::triggers | triggers |  | 1 anchor(s) |
| MCP_ATT | MCP_REG | [ok] | depends_on |  | 1 anchor(s) |
| MCP_ATT | MCP_AUTH | ?> | condition |  | 1 anchor(s) |
| MCP_REG | MCP_LOOP | -> | depends_on |  | 1 anchor(s) |
| MCP_AUTH | MCP_LOOP | -> | depends_on |  | 1 anchor(s) |
| MCP_LOOP | MCP_CALL | ::yields | yields |  | 2 anchor(s) |

## Notes

**切片 skeleton/partial**：stdio / sse / http 折叠进 `createClient`，不为每个 transport 另开图。
daemon `IMcpService`（`packages/agent-core/src/services/mcp/mcp.ts` · `mcpService.ts`）不另开图；本图只注协议适配。
`00_main` 索引边 `FLOW_MCP` 留给 W-close，本波不改 `00_main.graph.yaml`。


