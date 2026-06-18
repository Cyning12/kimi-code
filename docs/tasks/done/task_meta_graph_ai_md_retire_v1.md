# Task · meta graph · 退役 `.ai.md` 双轨（graph_v2 收口）

> **状态**：`done`  
> **分支**：`cyning/meta`  
> **前序**：[`task_meta_graph_v2_batch_migrate_v1.md`](./task_meta_graph_v2_batch_migrate_v1.md) CLOSE  
> **关账**：2026-06-18

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-ai-md-retire` |
| **test_strategy** | `required` |
| **module_id** | `monorepo_root` |
| **graph_delta** | `none` |
| **graph_delta_note** | 文档与 export 收口 · 不增量 flow 语义 |

### 人工闸

| human_gate_id | status | 说明 |
|---------------|--------|------|
| HG-TASK-DRAFT | approved | 本单执行授权 |

---

## 目标

删除 `docs/_tech_graph/*.ai.md`（6× flow + main），编辑源仅 **`*.graph.yaml` → compile → `.md`**。

## 验收

- [x] 6× `.ai.md` 已删
- [x] `README` · `99_mermaid_protocol` · `01_struct` 已更新
- [x] `graph:export` 不再写入无效 `source_ai_path`
- [x] `pnpm graph:compile:check` · `graph:export:check` · `pytest tests/tech_graph` 绿

## 变更摘要

- 删除：`00_main.ai.md` · 5× `10_flow_*.ai.md`
- `tech_graph_graph_v2_yaml.py`：`source_ai_path` 仅当文件存在时写入
- `TASK_TEMPLATE_upstream_pr_v1.md`：关账 checklist 改 YAML 口径
- `graph.json`：`graphs[]` 仅 `source_yaml_path`
