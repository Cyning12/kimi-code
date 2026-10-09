# Task · meta graph · 对齐 G-L 三层物理落地方案

> **状态**：`done`  
> **分支**：`cyning/meta` **only** · **无** Moonshot upstream PR  
> **真值规格**：工作区 [`docs/harness/spec/graph_skill_layering_v1/`](../../../../docs/harness/spec/graph_skill_layering_v1/README.md)  
> · 目录实施 [`IMPLEMENTATION_directory_schema_v1_zh.md`](../../../../docs/harness/spec/graph_skill_layering_v1/IMPLEMENTATION_directory_schema_v1_zh.md)  
> · 拍板 [`DECISIONS_maintainer_20260727_v1_zh.md`](../../../../docs/harness/spec/graph_skill_layering_v1/DECISIONS_maintainer_20260727_v1_zh.md)（**Q2=物理分层**）  
> **对照**：本仓现状 = 语义三层已齐、物理仍平铺；**非** Ink 对照仓同期搬家

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-glayer` |
| **test_strategy** | `required` |
| **test_strategy_note** | 必须 `pnpm graph:ci` 绿；工具递归子目录有 pytest 或等价夹具 |
| **code_quality_bar** | `strict` |
| **track** | `engineering`（meta 过程轨 · Inform 目录） |
| **orchestration** | **10-task**（短 · R0–R3 可 early_stop）→ **20** → **30** → **40** → CLOSE |
| **audit_profile** | `human_only` |
| **invoke_retention_profile** | `default` |
| **required_invoke_hats** | `10,30,40` |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **module_id** | `monorepo_root` |
| **graph_delta** | `docs/_tech_graph/`（目录重排 + yaml `layer` 头字段 · 不改业务边语义） |
| **graph_delta_note** | 物理迁入 `l0/l1/l2/shared`；flow 拓扑保持；工具改递归发现 |
| **graph_change_layer** | `mixed`（G-L0 索引路径 + G-L1 搬家 + G-L2 索引壳） |
| **review_hat** | `20` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 本单只动 `_tech_graph` / `tools/tech_graph`；无可晋升 coding_wiki 条目 |
| **experience_capture** | `recommended` |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | 仅 `cyning/meta` fork 过程轨 · 无上游 PR |
| **entry_invoke_10_task** | `docs/harness/invokes/by-task/meta-graph-glayer/README.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved | 22-R1, 30 | 2026-10-09 维护者签收（会话授权） |
| HG-AUDIT-R1 | approved | 30 | 2026-10-09 维护者签收 · R1 审查通过 |
| HG-GRAPH-MODULES | approved | — | 阶段 B 已签；本单不重签模块表语义，仅迁路径 |

---

## 1. 背景与目标

### 1.1 现状快照（起 task 时）

| 维度 | 现状 | 相对最新方案 |
|------|------|--------------|
| L0 顶层 | 根目录 `00_main.graph.yaml` + `.md` | 应入 `l0/` |
| L1 模块 | 根目录 `01_struct.md`（实为模块表） | 应升格/迁入 `l1/01_modules.md`；根留 stub |
| L1 流程 | 7× `10_flow_*.graph.yaml` 全 **deep**（平铺） | 应入 `l1/` |
| L2 方法倒排 | **无** `indexes/` | 至少落 **空壳/抽样壳**（本短单不深挖全量 implementedBy） |
| 元数据 | yaml **无** `layer:` 头字段 | 须补 `G-L0` / `G-L1` |
| 工具 | `graph_yaml_compile.py` 等仅 `TECH_GRAPH_DIR.glob("*.graph.yaml")` | **必须**改递归，否则搬家后 CI 红 |
| 协议/导出 | `99_*` · `graph.json` · schema 在根 | 建议入 `shared/`（或根留 POINTER） |

### 1.2 目标（一句话）

把 `docs/_tech_graph` **物理对齐** G-L0/G-L1/G-L2 落地方案（`l0/l1/l2/shared` + `LAYER_README` + yaml `layer`），并让 `pnpm graph:ci` 在子目录布局下全绿；**不**改 7 张 flow 的业务拓扑。

### 1.3 完成态

- [x] `docs/_tech_graph/LAYER_README.md`（声明目录缩写 ≡ G-L*）
- [x] 物理树：`l0/` · `l1/` · `l2/indexes/`（壳）· `shared/`
- [x] `00_main.*` → `l0/`；`10_flow_*` → `l1/`；模块表 → `l1/01_modules.md`（可由 `01_struct.md` 迁入并改标题）
- [x] 根过渡 stub：`01_struct.md`（及必要时 `00_main.md`）→ POINTER 新路径，兼容旧引用
- [x] 全部 `*.graph.yaml` 补 `layer: G-L0|G-L1`
- [x] `tools/tech_graph/*` 发现/读写路径支持子目录；`graph_module_flow_map.yaml` 路径更新
- [x] `docs/_tech_graph/README.md` · `02_version.md` 一行关账
- [x] `pnpm graph:ci` PASS

---

## 2. 范围

1. **分析落盘**：本 task §1.1 + invoke 内 ≤40 行对照表（现状→目标路径）即可，不另开长 SPEC  
2. **目录搬家** + `LAYER_README` + yaml `layer`  
3. **工具链**：compile / export / equivalence / completeness / issue-sync 相关路径解析  
4. **G-L2 壳**：`l2/indexes/by_path.yaml` · `by_symbol.yaml` 可为空映射或仅 1 个试点条目（推荐 `10_flow_read_tool` 1～3 锚点），**禁止**七图全量方法化  
5. 更新仓内引用（README · flow_map · 必要 stub）

## 3. 非范围

- 改 `apps/**` · `packages/**` 产品码  
- 重画 flow 边 / 降级 deep→shallow  
- 全量 G-L2 `implementedBy`  
- `docs/skills` S-L0/S-L1/S-L2（另 task）  
- Ops-desk / Ink / SpecWave 产品仓搬家  
- 上游 PR · 改 Moonshot CI  

---

## 4. 失败路径

| 触发条件 | 系统行为 | 可重试 | 用户可见 |
|----------|----------|--------|----------|
| HG-AUDIT-R1 pending 即 30 | 拒开工 | 是 | 须 20 + 人签 |
| 只搬家不改工具 glob | `graph:ci` 红 / 漏图 | 是 | CI |
| 断根路径无 stub 且旧文档仍链根文件 | Agent/人读断链 | 是 | 补 stub |
| 改写 flow 业务边「顺手重构」 | 20 退回 / 维护者拒收 | 是 | diff 审查 |
| 七图全量 G-L2 膨胀 | 超非范围 · 拒合 | 否 | 拆后续 task |

---

## 验收标准

- [x] `test -d docs/_tech_graph/l0 && test -d docs/_tech_graph/l1 && test -d docs/_tech_graph/l2/indexes && test -d docs/_tech_graph/shared`
- [x] `test -f docs/_tech_graph/LAYER_README.md`
- [x] 根无「唯一真值」平铺 `10_flow_*.graph.yaml`（已迁入 `l1/`）
- [x] `rg -n '^layer:' docs/_tech_graph --glob '*.graph.yaml'` 覆盖全部 yaml
- [x] `pnpm graph:ci` exit 0
- [x] `npx --yes spec-wave task lint --file docs/tasks/active/task_meta_graph_glayer_v1.md` PASS（起草期）
- [x] invoke `30`/`40` 留档；`02_version.md` 有本 slug 一行

---

## 依赖与必读

| 路径 | 用途 |
|------|------|
| `docs/_tech_graph/README.md` · `01_struct.md` · `00_main.graph.yaml` | 现状 |
| `tools/tech_graph/graph_yaml_compile.py`（及 export/equivalence/completeness） | 硬改点 |
| 工作区 `docs/harness/spec/graph_skill_layering_v1/IMPLEMENTATION_directory_schema_v1_zh.md` §1 | 目标树 |
| 工作区同包 `SPEC_graph_layering_GL0_GL1_GL2_v1_zh.md` §1 | 层定义 |
| `docs/_tech_graph/graph_module_flow_map.yaml` | 路径同步 |

---

## 思考轮控制

| 轮 | 结论 | early_stop | reason（early_stop） | residual_risks |
|----|------|------------|----------------------|----------------|
| R0 | done | no | — | none |
| R1 | done | no | — | 漏改某一脚本 |
| R2 | done | yes | 短单包络已定：物理树+layer+壳索引；不做全量 G-L2 | stub 过渡期双路径维护 |
| R3 | skip | yes | 随 R2 early_stop | none |
| R4 | skip | yes | 随 R2 early_stop | none |
| R5 | skip | yes | 随 R2 early_stop | none |

### R0 · 问题框定

本仓语义三层（00/01/10_flow）已在 2026-08-28 deepen Epic 收口；缺口是 **物理分层与 layer 元数据**，以及工具对子目录的发现能力。

### R1 · 代码/工具事实

`graph_yaml_compile.list_graph_ids` 使用 `TECH_GRAPH_DIR.glob("*.graph.yaml")`；export 同类。物理搬家前不改工具 = 必红。

### R2 · 包络冻结

采用 Ops-desk 同构目录（IMPLEMENTATION §1）；G-L2 仅 indexes 壳（可选 1 试点条目）；根 stub 保 `HG-GRAPH-MODULES` / 旧链可读。

---

### R3 · （early_stop · 跳过）

随 R2 停 · 无增量。

### R4 · （early_stop · 跳过）

随 R2 停 · 无增量。

### R5 · （early_stop · 跳过）

随 R2 停 · 无增量。

## 给 30 的执行顺序（建议）

1. 改 `tools/tech_graph` 为递归发现（先测后搬）  
2. `git mv` 入 `l0/l1/shared`；建 `l2/indexes` 壳  
3. 写 `LAYER_README` · yaml `layer` · 根 stub · 更新 flow_map / README  
4. `pnpm graph:ci`  
5. `02_version` + invoke 关账  

---


### KPI

Task_KPI%: 92

| 维 | 分 | 说明 |
|----|----|------|
| 完整度 | 5 | 物理树+工具+layer+L2壳齐 |
| 验证 | 5 | graph CI + pytest 16 |
| 范围纪律 | 4 | 未做全量 G-L2 |
| 文档 | 5 | LAYER_README + stub |

### 经验总结

- 搬家前必须先改 `rglob` 发现，否则 CI 必红
- 审查文文件名须与 `task_<slug>` 下划线基名对齐（勿用 hyphen slug）
- 根 `01_struct.md` stub + `l1/01_modules.md` 真值可兼顾旧链与 completeness

### 自检结论（执行者）

- `npx spec-wave verify --task docs/tasks/active/task_meta_graph_glayer_v1.md` → **PASS**（闸 approved · R1 审查命中）
- `python3 tools/tech_graph/graph_yaml_compile.py --all --check` · export --check · equivalence · completeness → **PASS**
- `pytest tests/tech_graph -q` → **16 passed**
- 目录：`l0/` `l1/` `l2/indexes/` `shared/` + `LAYER_README.md`；8/8 yaml 含 `layer:`

---

## 修订记录

| 日期 | 摘要 |
|------|------|
| 2026-10-09 | 10-task 短单初稿 · 对齐 G-L 物理三层落地 |
