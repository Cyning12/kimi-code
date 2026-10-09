# LAYER_README · G-L 目录约定（kimi-code-meta）

| 目录缩写 | 正文层 | 内容 |
|----------|--------|------|
| `l0/` | **G-L0** | 顶层索引 / 骨架 · `00_main.*` |
| `l1/` | **G-L1** | 模块表 `01_modules.md` + 域流程 `10_flow_*` |
| `l2/` | **G-L2** | 方法倒排 `indexes/`（本仓短单仅壳 / 试点） |
| `shared/` | meta | 协议 · schema ·（可选）axioms |

根目录保留：`README.md` · `LAYER_README.md` · `02_version.md` · `graph.json`（export）· `graph_module_flow_map.yaml` · `01_struct.md`（stub）。

`*.graph.yaml` 须带头字段 `layer: G-L0|G-L1`。编辑源 = yaml；`.md` 由 `pnpm graph:compile` 生成。

真值规格：工作区 `docs/harness/spec/graph_skill_layering_v1/`。
