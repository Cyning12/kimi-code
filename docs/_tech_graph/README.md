# docs/_tech_graph（kimi-code-meta）

本仓技术图谱目录。**物理分层**：`l0/` · `l1/` · `l2/` · `shared/`（见 [`LAYER_README.md`](./LAYER_README.md)）。  
**流程图编辑源**为 `*.graph.yaml`；人类可读 `.md` 由 compile 生成。

## 文件角色

| 模式 | 维护者 | 说明 |
|------|--------|------|
| `l0|l1/*.graph.yaml` | 30 / 图谱 task | **唯一编辑源**（flowchart）· 须含 `layer:` |
| `l0|l1/*.md` | compile | `pnpm graph:compile` 产出 · 审阅用 |
| `l1/01_modules.md` | 维护者 | 模块边界 · **HG-GRAPH-MODULES**（根 `01_struct.md` 为 stub） |
| `l2/indexes/` | 维护者 | G-L2 倒排（壳 / 试点） |
| `shared/` | 维护者 | 协议 · schema |
| `02_version.md` | task 关账 | 版本时间线一行 |
| `graph.json` | export | `pnpm graph:export` · CI 校验 |

## 常用命令

```bash
pnpm graph:compile          # YAML → .md（递归子目录）
pnpm graph:compile:check    # CI：.md 须与 YAML 一致
pnpm graph:export           # 写 graph.json
pnpm graph:export:check     # CI：graph.json 须与 export 一致
pnpm graph:equivalence      # YAML 与 graph.json 拓扑等价
pnpm graph:completeness     # 模块覆盖率 · P0 边 · N_min
pnpm graph:ci               # 一键：compile + export + equivalence + completeness
pnpm graph:issue-sync --task docs/tasks/active/task_*.md
```

## 已交付图（本仓）

| graph_id | 路径 | layer | 状态 |
|----------|------|-------|------|
| `00_main` | `l0/` | G-L0 | 索引 |
| `10_flow_cli_session` | `l1/` | G-L1 | deep |
| `10_flow_agent_turn` | `l1/` | G-L1 | deep |
| `10_flow_read_tool` | `l1/` | G-L1 | deep |
| `10_flow_context_tool_exchange` | `l1/` | G-L1 | deep |
| `10_flow_skill_load` | `l1/` | G-L1 | deep |
| `10_flow_mcp_tool` | `l1/` | G-L1 | deep |
| `10_flow_subagent` | `l1/` | G-L1 | deep |

## 关联

- 模块表：[`l1/01_modules.md`](./l1/01_modules.md)
- Schema：[`shared/graph_v2_schema.md`](./shared/graph_v2_schema.md)
- 分层约定：[`LAYER_README.md`](./LAYER_README.md)
