# invoke · hat 30+40 · meta-graph-glayer

| 字段 | 值 |
|------|-----|
| hat_id | 30+40 |
| task_slug | meta-graph-glayer |
| date | 2026-10-09 |
| outcome | PASS · 物理三层落地 · graph CI 绿 |

## 变更摘要

1. `tools/tech_graph`：`iter_graph_yaml` / `resolve_graph_yaml` / `resolve_flow_rel`；compile/export/completeness/schema 路径对齐
2. `docs/_tech_graph`：`l0/` `l1/` `l2/indexes/` `shared/` + `LAYER_README.md`；`01_struct.md` stub → `l1/01_modules.md`
3. yaml 补 `layer: G-L0|G-L1`；L2 indexes 壳 + read_tool 试点
4. `tests/tech_graph/test_graph_yaml_smoke.py` 递归解析

## 验证

- verify --task PASS
- compile/export/equivalence/completeness PASS
- pytest tests/tech_graph 16 passed
