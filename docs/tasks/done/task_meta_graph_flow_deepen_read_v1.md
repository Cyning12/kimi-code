# Task · 加深 10_flow_read_tool

> **状态**：`done` · 2026-08-28  
> **Epic SPEC**：[`SPEC_meta_graph_flow_deepen_v1_zh.md`](../specs/SPEC_meta_graph_flow_deepen_v1_zh.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-flow-deepen-read` |
| **test_strategy** | `required` |
| **test_strategy_note** | `python3 tools/tech_graph/graph_yaml_compile.py --graph-id 10_flow_read_tool` 必须成功。关账 graph:ci 归 W-close。 |
| **code_quality_bar** | `strict` |
| **freeze_id** | `META-GRAPH-FLOW-DEEPEN` |
| **track** | `engineering` |
| **orchestration** | 00 编排 · 30 subagent 只改本图 |
| **semi_auto** | `false` |
| **audit_profile** | `human_only` |
| **invoke_retention_profile** | `default` |
| **required_invoke_hats** | `10,30,40` |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **module_id** | `agent_core` |
| **graph_delta** | `docs/_tech_graph/10_flow_read_tool.graph.yaml` |
| **graph_delta_note** | 原地加深 |
| **graph_gate** | `close_partial_or_final` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 改技术图谱非 coding_wiki |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | cyning/meta 过程轨 |
| **experience_capture** | `not_applicable` |
| **experience_capture_note** | 图谱加深不沉淀 wiki |
| **entry_invoke_30** | `docs/harness/invokes/by-task/meta-graph-flow-deepen/PROMPT_30_meta-graph-flow-deepen-read.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved 2026-08-28 | 20-R1, 30 | 00 代签 |
| HG-AUDIT-R1 | approved 2026-08-28 | 30 | 审查文 R1 · 00 代签 |
| HG-GRAPH-MODULES | approved（不重开） | 30 业务码 | 本 task 只改 yaml |

---

## 1. 背景与目标

把 `10_flow_read_tool` 从骨架/partial/skeleton 提升到 SPEC §4.2 **deep**。

加深重点：拓扑可留；给几乎所有硬边补 read.ts line。补 schema/文件失败 [err]（若代码有）。

## 2. 范围

- [ ] 只编辑 `docs/_tech_graph/10_flow_read_tool.graph.yaml`（可 compile 生成同名 `.md`）
- [ ] 达到 D1–D8；自检写明锚覆盖率（path%、line%）
- [ ] `graph_id` 保持 `10_flow_read_tool`

## 非范围

- 不新建 10_flow_*；不改 00_main.graph.yaml / 01_struct / flow_map / compile.py / graph.json
- 不改 packages/** apps/** 生产逻辑
- 不迁 l0/l1/l2；不 git commit/push
- 只 `python3 tools/tech_graph/graph_yaml_compile.py --graph-id <本图>`，禁止 `--all`


## 失败路径

| 触发条件 | 系统行为 | 可重试 | 用户可见 |
|----------|----------|--------|----------|
| HG-AUDIT-R1 pending | 拒开工 | 是 | 以 task 表为准 |
| 改生产 TS | 退回 | 是 | 回退 |
| D3 未达标称 deep | W-close 拒收 | 是 | 补锚 |
| `--all` 或改 graph.json | 退回 | 是 | 只 compile 本 graph-id |

## 验收标准

- [ ] D1–D8 自检表填齐
- [ ] `compile --graph-id 10_flow_read_tool` exit 0
- [ ] 未改其它 yaml / 生产码

## 6. 思考轮

### R0
读 SPEC §2.1 本行 + 现 yaml + 源码。

### R1
只加深本图。

### R2
原地加深，不推倒 graph_id。

### R3
禁止虚构 path。

### R4
D3 百分比为硬验收。

### R5
可 30。

### 思考轮控制

| 字段 | 值 |
|------|-----|
| **actual_last_round** | `R5` |
| **early_stop** | `no` |
| **early_stop_reason** | — |
| **residual_risks** | line 随代码漂移 |

## 7. 给 30 必读

- `docs/tasks/specs/SPEC_meta_graph_flow_deepen_v1_zh.md`
- `docs/_tech_graph/10_flow_read_tool.graph.yaml`
- `docs/_tech_graph/99_mermaid_protocol.md`

### 自检结论

（30 回填 D1–D8）
