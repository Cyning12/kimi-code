---
graph_id: 00_main
version: 2026-08-28
generated_at: 2026-08-28T08:27:10Z
source: docs/_tech_graph/00_main.graph.yaml
---

# 顶层流程总图（kimi-code · 人类友好版）

CLI Agent 主干与子流程路由

## Mermaid

```mermaid
flowchart TD
    U[用户终端]
    CLI[kimi CLI / TUI<br/>apps/kimi-code]
    SDK[@moonshot-ai/kimi-code-sdk<br/>packages/node-sdk]
    AC[agent-core<br/>Agent / Session / tools]
    KS[kosong · LLM 调用]
    KA[kaos · shell / 文件]
    TOOLS[skills · MCP · subagents]
    FLOW_SKILL[>10_flow_skill_load.md]
    FLOW_MCP[>10_flow_mcp_tool.md]
    FLOW_SUB[>10_flow_subagent.md]
    FLOW_TURN[>10_flow_agent_turn.md]
    FLOW_READ[>10_flow_read_tool.md]
    FLOW_CTX[>10_flow_context_tool_exchange.md]
    FLOW_CLI[CLI 会话主循环]
    FLOW_DOC[>10_flow_cli_session.md]
    TELEM[telemetry]
    AUTH[oauth]
    MONO[monorepo · docs/tools/harness]
    VIS[vis · Session 可视化<br/>apps/vis]
    ACP[acp-adapter<br/>packages/acp-adapter]
    MIG[migration-legacy<br/>packages/migration-legacy]
    WEB[kimi-web<br/>apps/kimi-web]
    PROTO[protocol · REST+WS schema<br/>packages/protocol]
    SRV[server · REST+WS<br/>packages/server]
    E2E[server-e2e<br/>packages/server-e2e]

    U --> CLI
    CLI --> SDK
    // → apps/kimi-code
    SDK --> AC
    // → packages/node-sdk
    AC --> KS
    AC --> KA
    AC --"::triggers"--> TOOLS
    TOOLS --"加载"--> FLOW_SKILL
    TOOLS --"加载"--> FLOW_MCP
    TOOLS --"加载"--> FLOW_SUB
    CLI --"::triggers"--> FLOW_CLI
    FLOW_CLI --"加载"--> FLOW_DOC
    AC --"加载"--> FLOW_TURN
    AC --"加载"--> FLOW_READ
    AC --"加载"--> FLOW_CTX
    AC --> TELEM
    AC --> AUTH
    AC --> PROTO
    // → packages/agent-core/package.json
    SRV --> AC
    // → packages/server/package.json
    SRV --> PROTO
    // → packages/server/package.json
    E2E --> PROTO
    // → packages/server-e2e/package.json
    WEB --"::triggers"--> SRV
    // → apps/kimi-web
    ACP --> AC
    // → packages/acp-adapter/package.json
    ACP --> KA
    // → packages/acp-adapter/package.json
    ACP --> SDK
    // → packages/acp-adapter/package.json
    VIS --> AC
    // → apps/vis/server/package.json
    VIS --> KS
    // → apps/vis/server/package.json
    MIG --> AC
    // → packages/migration-legacy/package.json
    CLI --"devDep / bundle (kimi server run)"--> SRV
    // → apps/kimi-code/package.json
    CLI --"devDep / bundle"--> WEB
    // → apps/kimi-code/package.json

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
    class FLOW_DOC doc
    class AUTH infra
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| U | 用户终端 | external |
| CLI | kimi CLI / TUI<br/>apps/kimi-code | struct |
| SDK | @moonshot-ai/kimi-code-sdk<br/>packages/node-sdk | struct |
| AC | agent-core<br/>Agent / Session / tools | struct |
| KS | kosong · LLM 调用 | struct |
| KA | kaos · shell / 文件 | struct |
| TOOLS | skills · MCP · subagents | flow |
| FLOW_SKILL | >10_flow_skill_load.md | flow |
| FLOW_MCP | >10_flow_mcp_tool.md | flow |
| FLOW_SUB | >10_flow_subagent.md | flow |
| FLOW_TURN | >10_flow_agent_turn.md | flow |
| FLOW_READ | >10_flow_read_tool.md | flow |
| FLOW_CTX | >10_flow_context_tool_exchange.md | flow |
| FLOW_CLI | CLI 会话主循环 | flow |
| FLOW_DOC | >10_flow_cli_session.md | flow |
| TELEM | telemetry | struct |
| AUTH | oauth | struct |
| MONO | monorepo · docs/tools/harness | struct |
| VIS | vis · Session 可视化<br/>apps/vis | struct |
| ACP | acp-adapter<br/>packages/acp-adapter | struct |
| MIG | migration-legacy<br/>packages/migration-legacy | struct |
| WEB | kimi-web<br/>apps/kimi-web | struct |
| PROTO | protocol · REST+WS schema<br/>packages/protocol | struct |
| SRV | server · REST+WS<br/>packages/server | struct |
| E2E | server-e2e<br/>packages/server-e2e | struct |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| U | CLI | -> | depends_on |  |  |
| CLI | SDK | -> | depends_on |  | 1 anchor(s) |
| SDK | AC | -> | depends_on |  | 1 anchor(s) |
| AC | KS | -> | depends_on |  |  |
| AC | KA | -> | depends_on |  |  |
| AC | TOOLS | ::triggers | triggers |  |  |
| TOOLS | FLOW_SKILL | -> | depends_on | 加载 |  |
| TOOLS | FLOW_MCP | -> | depends_on | 加载 |  |
| TOOLS | FLOW_SUB | -> | depends_on | 加载 |  |
| CLI | FLOW_CLI | ::triggers | triggers |  |  |
| FLOW_CLI | FLOW_DOC | -> | depends_on | 加载 |  |
| AC | FLOW_TURN | -> | depends_on | 加载 |  |
| AC | FLOW_READ | -> | depends_on | 加载 |  |
| AC | FLOW_CTX | -> | depends_on | 加载 |  |
| AC | TELEM | -> | depends_on |  |  |
| AC | AUTH | -> | depends_on |  |  |
| AC | PROTO | -> | depends_on |  | 1 anchor(s) |
| SRV | AC | -> | depends_on |  | 1 anchor(s) |
| SRV | PROTO | -> | depends_on |  | 1 anchor(s) |
| E2E | PROTO | -> | depends_on |  | 1 anchor(s) |
| WEB | SRV | ::triggers | calls |  | 1 anchor(s) |
| ACP | AC | -> | depends_on |  | 1 anchor(s) |
| ACP | KA | -> | depends_on |  | 1 anchor(s) |
| ACP | SDK | -> | depends_on |  | 1 anchor(s) |
| VIS | AC | -> | depends_on |  | 1 anchor(s) |
| VIS | KS | -> | depends_on |  | 1 anchor(s) |
| MIG | AC | -> | depends_on |  | 1 anchor(s) |
| CLI | SRV | -> | depends_on | devDep / bundle (kimi server run) | 1 anchor(s) |
| CLI | WEB | -> | depends_on | devDep / bundle | 1 anchor(s) |

## Notes

**分步规则**：改 agent 轮次/tool 开 `10_flow_agent_turn`；改 context/tool 配对/resume 开 `10_flow_context_tool_exchange`；改 skill 解析/加载开 `10_flow_skill_load`；改 Read 截断/status 开 `10_flow_read_tool`；改 MCP 开 `10_flow_mcp_tool`；改 subagent 开 `10_flow_subagent`；每张 flow 随业务 task 增量维护。



## 待补 flow 清单（分步增量 · 非 bootstrap 一次画完）

| flow 文件 | 状态 | 说明 |
|-----------|------|------|
| `10_flow_cli_session.md` | **骨架** | 编辑源：[10_flow_cli_session.graph.yaml](10_flow_cli_session.graph.yaml) · #437 主落点 |
| `10_flow_agent_turn.md` | **partial** | 编辑源：[10_flow_agent_turn.graph.yaml](10_flow_agent_turn.graph.yaml) · C2 #583 |
| `10_flow_read_tool.md` | **partial** | 编辑源：[10_flow_read_tool.graph.yaml](10_flow_read_tool.graph.yaml) · C3 #94 |
| `10_flow_context_tool_exchange.md` | **skeleton** | 编辑源：[10_flow_context_tool_exchange.graph.yaml](10_flow_context_tool_exchange.graph.yaml) · C3 #705 |
| `10_flow_skill_load.md` | **partial · fork** | 编辑源：[10_flow_skill_load.graph.yaml](10_flow_skill_load.graph.yaml) · C3 #580 |
| `10_flow_mcp_tool.md` | **skeleton** | 编辑源：[10_flow_mcp_tool.graph.yaml](10_flow_mcp_tool.graph.yaml) · MCP connect/discover |
| `10_flow_subagent.md` | **skeleton** | 编辑源：[10_flow_subagent.graph.yaml](10_flow_subagent.graph.yaml) · spawn/batch/lifecycle |

## Sub-graph Links

- `Struct`: [`01_struct.md`](01_struct.md)（规范层 · 手写 Markdown）
- `Version`: [`02_version.md`](02_version.md)（timeline · 手写 Markdown）
- `Mermaid Protocol`: [`99_mermaid_protocol.md`](99_mermaid_protocol.md)
- 模块表：[`01_struct.md`](01_struct.md) · 上游代码地图：[`AGENTS.md`](../../AGENTS.md)

