---
graph_id: 00_main
version: 2026-06-18
generated_at: 2026-06-18T14:26:55Z
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
    FLOW_TURN[>10_flow_agent_turn.md]
    FLOW_READ[>10_flow_read_tool.md]
    FLOW_CTX[>10_flow_context_tool_exchange.md]
    FLOW_CLI[CLI 会话主循环]
    FLOW_DOC[>10_flow_cli_session.md]
    TELEM[telemetry]
    AUTH[oauth]

    U --> CLI
    CLI --> SDK
    // → apps/kimi-code
    SDK --> AC
    // → packages/node-sdk
    AC --> KS
    AC --> KA
    AC --"::triggers"--> TOOLS
    TOOLS --"加载"--> FLOW_SKILL
    CLI --"::triggers"--> FLOW_CLI
    FLOW_CLI --"加载"--> FLOW_DOC
    AC --"加载"--> FLOW_TURN
    AC --"加载"--> FLOW_READ
    AC --"加载"--> FLOW_CTX
    AC --> TELEM
    AC --> AUTH

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
| U | 用户终端 |  |
| CLI | kimi CLI / TUI<br/>apps/kimi-code |  |
| SDK | @moonshot-ai/kimi-code-sdk<br/>packages/node-sdk |  |
| AC | agent-core<br/>Agent / Session / tools |  |
| KS | kosong · LLM 调用 |  |
| KA | kaos · shell / 文件 |  |
| TOOLS | skills · MCP · subagents |  |
| FLOW_SKILL | >10_flow_skill_load.md |  |
| FLOW_TURN | >10_flow_agent_turn.md |  |
| FLOW_READ | >10_flow_read_tool.md |  |
| FLOW_CTX | >10_flow_context_tool_exchange.md |  |
| FLOW_CLI | CLI 会话主循环 |  |
| FLOW_DOC | >10_flow_cli_session.md |  |
| TELEM | telemetry |  |
| AUTH | oauth |  |

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
| CLI | FLOW_CLI | ::triggers | triggers |  |  |
| FLOW_CLI | FLOW_DOC | -> | depends_on | 加载 |  |
| AC | FLOW_TURN | -> | depends_on | 加载 |  |
| AC | FLOW_READ | -> | depends_on | 加载 |  |
| AC | FLOW_CTX | -> | depends_on | 加载 |  |
| AC | TELEM | -> | depends_on |  |  |
| AC | AUTH | -> | depends_on |  |  |

## Notes

**分步规则**：改 agent 轮次/tool 开 `10_flow_agent_turn`；改 context/tool 配对/resume 开 `10_flow_context_tool_exchange`；改 skill 解析/加载开 `10_flow_skill_load`；改 Read 截断/status 开 `10_flow_read_tool`；改 MCP 开 `10_flow_mcp_tool`（待补）；每张 flow 随业务 task 增量维护。



## 待补 flow 清单（分步增量 · 非 bootstrap 一次画完）

| flow 文件 | 状态 | 说明 |
|-----------|------|------|
| `10_flow_cli_session.md` | **骨架** | 编辑源：[10_flow_cli_session.graph.yaml](10_flow_cli_session.graph.yaml) · #437 主落点 |
| `10_flow_agent_turn.md` | **partial** | 编辑源：[10_flow_agent_turn.graph.yaml](10_flow_agent_turn.graph.yaml) · C2 #583 |
| `10_flow_read_tool.md` | **partial** | 编辑源：[10_flow_read_tool.graph.yaml](10_flow_read_tool.graph.yaml) · C3 #94 |
| `10_flow_context_tool_exchange.md` | **skeleton** | 编辑源：[10_flow_context_tool_exchange.graph.yaml](10_flow_context_tool_exchange.graph.yaml) · C3 #705 |
| `10_flow_skill_load.md` | **partial · fork** | 编辑源：[10_flow_skill_load.graph.yaml](10_flow_skill_load.graph.yaml) · C3 #580 |
| `10_flow_mcp_tool.md` | 待补 | 仅本清单 · 首个触达 Issue 再建 `.graph.yaml` |
| `10_flow_subagent.md` | 待补 | 仅本清单 · 首个触达 Issue 再建 `.graph.yaml` |

## Sub-graph Links

- `Struct`: [`01_struct.md`](01_struct.md)（规范层 · 手写 Markdown）
- `Version`: [`02_version.md`](02_version.md)（timeline · 手写 Markdown）
- `Mermaid Protocol`: [`99_mermaid_protocol.md`](99_mermaid_protocol.md)
- 模块表：[`01_struct.md`](01_struct.md) · 上游代码地图：[`AGENTS.md`](../../AGENTS.md)

