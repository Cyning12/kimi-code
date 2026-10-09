# invoke · meta-graph-glayer

| 项 | 内容 |
|----|------|
| **task** | `docs/tasks/active/task_meta_graph_glayer_v1.md` |
| **Open Folder** | `kimi-code-meta/` |
| **规格** | 工作区 `docs/harness/spec/graph_skill_layering_v1/`（IMPLEMENTATION §1 + SPEC G-L） |

## 帽序

1. **10**（本目录 · 已起草 task）→ **20** 审短范围  
2. **30**（`HG-AUDIT-R1=approved` 后）：先工具递归 → 再 `git mv` → `pnpm graph:ci`  
3. **40** 自检 · CLOSE  

## 现状→目标（对照摘要）

| 现路径 | 目标 |
|--------|------|
| `00_main.*` | `l0/00_main.*` · `layer: G-L0` |
| `01_struct.md` | `l1/01_modules.md` + 根 stub POINTER |
| `10_flow_*.{graph.yaml,md}` | `l1/` · `layer: G-L1` |
| `99_*` · schema · `graph.json` | `shared/`（或根 POINTER） |
| （无） | `l2/indexes/{by_path,by_symbol}.yaml` 壳 |
| （无） | `LAYER_README.md` |

## 禁止

- 改产品 `apps/` `packages/`  
- 重画 flow 业务边  
- 七图全量 G-L2  
