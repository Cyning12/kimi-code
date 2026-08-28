# docs/_tech_graph（kimi-code-meta）

本仓技术图谱目录。**流程图编辑源**为 `*.graph.yaml`；人类可读 `.md` 由 compile 生成。

## 文件角色

| 模式 | 维护者 | 说明 |
|------|--------|------|
| `*.graph.yaml` | 30 / 图谱 task | **唯一编辑源**（flowchart） |
| `*.md` | compile | `pnpm graph:compile` 产出 · 审阅用 |
| `01_struct.md` | 维护者 | 模块边界 · **HG-GRAPH-MODULES** |
| `02_version.md` | task 关账 | 版本时间线一行 |
| `99_mermaid_protocol.md` | 维护者 | 边标记与 compile 约定 |
| `graph.json` | export | `pnpm graph:export` · CI 校验 |

## 常用命令

```bash
pnpm graph:compile          # YAML → .md
pnpm graph:compile:check    # CI：.md 须与 YAML 一致
pnpm graph:export           # 写 graph.json
pnpm graph:export:check     # CI：graph.json 须与 export 一致
pnpm graph:equivalence      # YAML 与 graph.json 拓扑等价
pnpm graph:completeness     # 模块覆盖率 · P0 边 · N_min
pnpm graph:ci               # 一键：compile + export + equivalence + completeness
pnpm graph:issue-sync --task docs/tasks/active/<task>.md
```

## 已交付图（本仓）

| graph_id | YAML | 状态 | 说明 |
|----------|------|------|------|
| `00_main` | `00_main.graph.yaml` | 索引 | 顶层索引 |
| `10_flow_cli_session` | `10_flow_cli_session.graph.yaml` | **deep** | CLI 会话 · #437 |
| `10_flow_agent_turn` | `10_flow_agent_turn.graph.yaml` | **deep** | Agent turn · #583 |
| `10_flow_read_tool` | `10_flow_read_tool.graph.yaml` | **deep** | Read tool · #94 |
| `10_flow_context_tool_exchange` | `10_flow_context_tool_exchange.graph.yaml` | **deep** | Context · #705 |
| `10_flow_skill_load` | `10_flow_skill_load.graph.yaml` | **deep** | Skill load · #580 |
| `10_flow_mcp_tool` | `10_flow_mcp_tool.graph.yaml` | **deep** | MCP connect/discover · W3 |
| `10_flow_subagent` | `10_flow_subagent.graph.yaml` | **deep** | Subagent spawn/batch · W3 |

## 关联

- 模块表：[`01_struct.md`](./01_struct.md)
- Schema：[`graph_v2_schema.md`](./graph_v2_schema.md)
