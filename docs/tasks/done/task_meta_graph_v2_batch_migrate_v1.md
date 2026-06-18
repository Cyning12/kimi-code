# Task · meta graph_v2 · 流程轨 YAML 批量迁移（#437 前清债）

> **状态**：`done` · HG-GRAPH-YAML-CLOSE **approved**（2026-06-18）  
> **分支**：`cyning/meta` **only** · **无** Moonshot upstream PR  
> **安排真值**：工作区 `[PLAN_kimi_code_meta_harness_2x_v1_zh.md](../../../../docs/harness/guides/PLAN_kimi_code_meta_harness_2x_v1_zh.md)` §4′  
> **试点纪律**：`[PILOT_kimi_code_fork_adoption_v1_zh.md](../../../../docs/harness/guides/PILOT_kimi_code_fork_adoption_v1_zh.md)` §5.2（关账后 `graph_delta` 改指 `.graph.yaml`）  
> **后继 Issue**：[#437 Approve once vs session](https://github.com/MoonshotAI/kimi-code/issues/437) — **本 task CLOSE 后再开业务 task**

---

## Harness 元信息


| 字段                       | 值                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| **task_slug**            | `meta-graph-v2-batch-migrate`                                                             |
| **test_strategy**        | `required`                                                                                |
| **test_strategy_note**   | compile `--check` · export 等价 · 每图 ≥1 pytest（或 vitest 包装脚本冒烟）· `graph axioms check`       |
| **code_quality_bar**     | `strict`                                                                                  |
| **track**                | `engineering`（meta 过程轨 · 非上游 Issue）                                                       |
| **orchestration**        | **10-task**（R0–R5）→ **20** → **30** → **40** → CLOSE                                      |
| **audit_profile**        | `human_only`                                                                              |
| **git_branch**           | `cyning/meta`                                                                             |
| **worktree_root**        | `kimi-code-meta/`（Open Folder）                                                            |
| **meta_worktree**        | 同 `worktree_root`                                                                         |
| **freeze_id**            | `KIMI-META-GRAPH-V2-BATCH@0fa2d54f` |
| **module_id**            | `monorepo_root`（`01_struct` · 图谱基础设施）                                                     |
| **graph_delta**          | `flow_track_batch`（见 §4 迁移清单）                                                             |
| **graph_delta_note**     | 本 task **即**流程轨迁移；非单 Issue 切片                                                             |
| **graph_gate**           | `yaml_source_before_close` · `compile_check_green` · `02_version_on_close`                |
| **entry_invoke_10_task** | `docs/harness/invokes/by-task/meta-graph-v2-batch-migrate/PROMPT_START_10_v1.md`          |
| **entry_invoke_30**      | `Projects/docs/harness/invokes/by-task/meta-graph-v2-batch-migrate/PROMPT_START_30_v1.md` |


### 人工闸


| human_gate_id           | status       | blocks_hats | 说明                        |
| ----------------------- | ------------ | ----------- | ------------------------- |
| **HG-TASK-DRAFT**       | approved     | 20-R1, 30   | §4 交接物 + F0 参照清单人扫        |
| **HG-GRAPH-MODULES**    | approved     | —           | 阶段 B 已签；本 task 不重复签模块表    |
| **HG-AUDIT-R1**         | **approved** | 30          | 20 思考审查 + F0–F1 方案人签      |
| **HG-GRAPH-YAML-CLOSE** | **approved** | done        | F5 全量 compile/export 绿后人签 |


> **禁止**：与 #437 或其它 `feature/fix-*` **同 PR** · 向 Moonshot 上游 PR 任何 harness / `_tech_graph` 工具路径。

---

## 1. 背景与目标

meta `docs/_tech_graph/` 当前为 **手写 Mermaid `.md` / `.ai.md` 双轨**（阶段 B bootstrap + C2/C3 partial）。若继续在 #437 及后续 Issue 上增量手改 Mermaid，flow 数量上升后将触发 **二次大批量 YAML 迁移**，与 Ink 后端已验证路径重复踩坑。

**本 task 目标**：在 **#437 开工前**，一次性把 **流程轨** 迁为 `***.graph.yaml` 唯一编辑源**，复用 Ink 后端试点工具链与验收口径；关账后 C 轨 Issue task 的 `graph_delta` **只指 YAML**，不再手改 `.md` / `.ai.md`。

### 完成态（关账后 #437 无图谱债）

- [ ] 清单内 **6 图**均有 `*.graph.yaml` 编辑源 + compile 生成 `.md`
- [ ] 含 flowchart 的图：**删除或 `@deprecated` 手写 `.ai.md`**（export 改读 YAML，对齐 Ink G0）
- [ ] `graph.json`（`schema_version: graph_v2`）export + 等价检查 CI / 本地 `--check` 绿
- [ ] `graph_v2.schema.json`（或等价校验入口）落盘 meta `docs/_tech_graph/`
- [ ] PILOT §5.2 · task 模板 · `FRAGMENT_30`：`graph_delta` 默认 `**.graph.yaml` 路径**
- [ ] `02_version.md` 一行关账 · invoke CLOSE · task → `done/`
- [ ] **可立即**起草 `task_fix_approve_once_437_v1.md`，`graph_delta: 10_flow_cli_session.graph.yaml`

### 不在本 task 范围（保持 Markdown）


| 文件                       | 理由                                                                                                                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `01_struct.md`           | 规范层 · classDiagram · `[GUIDE_inform_spec_layer_format_selection_v1_zh.md](../../../../ai_coding_governance/methodology/graph/GUIDE_inform_spec_layer_format_selection_v1_zh.md)` §2 |
| `02_version.md`          | timeline 叙述 · 关账时增一行即可                                                                                                                                                              |
| `99_mermaid_protocol.md` | 拓扑协议 prose · compile 内枚举即可                                                                                                                                                          |
| `graph_query` CLI 产品化    | Ink P2-3 已做 · meta **v1 仅 export + 等价** · query 进 backlog                                                                                                                           |
| HGM ingest / Neo4j       | Track G · 正交                                                                                                                                                                        |


---

## 2. 后端参照链（只读 · 禁止改 Ink 仓）

> Agent **须 @ 读**下列真值；实现 **复制/适配到 `kimi-code-meta/tools/` 或 `scripts/`**，不 fork 业务代码。

### 2.1 方法论


| 文档                                                                                                                                                                              | 用途                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `[GUIDE_inform_spec_layer_format_selection_v1_zh.md](../../../../ai_coding_governance/methodology/graph/GUIDE_inform_spec_layer_format_selection_v1_zh.md)`                     | 流程轨 vs 规范层分工                |
| `[REPORT_inform_yaml_migration_before_after_benefits_v1_zh.md](../../../../ai_coding_governance/methodology/graph/REPORT_inform_yaml_migration_before_after_benefits_v1_zh.md)` | 迁移前后架构 · ROI · 禁止项          |
| 工作区 `[pointer_task_engineering_tech_graph_v2_graph_query_v1](../../../../docs/harness/reviews/pointer_task_engineering_tech_graph_v2_graph_query_v1_audit_R1_20260517.md)`      | graph_v2 + query 子仓 task 索引 |


### 2.2 子仓 task（done · 按序参照）


| 序   | task                                                                                       | 借什么                                                |
| --- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| 1   | `ai-ink-brain-api-python/docs/tasks/done/task_engineering_tech_graph_v2_graph_query_v1.md` | P2-0 最小 v2 字段 · 等价阈值 · G-END 决议                    |
| 2   | `…/task_engineering_graph_v2_schema_dual_track_v1.md`                                      | `graph_v2.schema.json` 双轨（若存在 · deferred 亦读 MD 摘要） |
| 3   | `…/task_engineering_graph_yaml_migration_epic_v1.md`                                       | **F2–F3 批量节奏** · P0 `00_main` 先行 · 子阶段表            |
| 4   | `…/done/task_engineering_graph_yaml_p0_00_main_v1.md`                                      | 单图迁移验收模板                                           |


### 2.3 工具脚本（复制源 · 路径以子仓为准）


| 脚本                                                                    | 职责                               |
| --------------------------------------------------------------------- | -------------------------------- |
| `scripts/graph_yaml_compile.py` 或 `tools/tech_graph_graph_v2_yaml.py` | YAML → `.md`（+ 必要时 `.ai.md` 过渡期） |
| `tools/tech_graph_graph_export.py`                                    | 导出 `graph.json` · **关账改读 YAML**  |
| `tools/tech_graph_graph_equivalence_check.py`                         | 参考拓扑 vs export · 95%/90% 阈值      |
| `tools/tech_graph_graph_v2_schema.py`                                 | schema 校验                        |
| `.github/workflows/tech-graph.yml`（片段）                                | CI `--check` 步骤参照                |


**meta 适配说明**：kimi-code-meta 为 TS monorepo · 工具可 **Python 脚本落 `tools/tech_graph/`**（与 Ink 同语言降低移植成本）· 或 pnpm script 包装 `python3 tools/...` · **不在** `apps/` `packages/` 加运行时依赖。

---

## 3. 任务链 · F0–F5（流程轨迁移）

```text
F0 参照只读 + 选型 mini
  → F1 工具链 bootstrap（compile / export / equivalence / schema）
  → F2 00_main.graph.yaml（P0 试点 · 单图验收）
  → F3 10_flow_* batch（5 图 · 可分子 commit F3a–F3e）
  → F4 纪律更新（PILOT · template · gate-check 钩子）
  → F5 关账（graph.json · 02_version · axioms · invoke · done/）
  → 后继：task_fix_approve_once_437_v1（YAML-first skeleton）
```

### F0 · 选型 mini（10-task R1–R2 回填）


| 交付                                                                 | 验收                   |
| ------------------------------------------------------------------ | -------------------- |
| 读本 task §2 全部参照 · 列出 meta 现有 `.md`/`.ai.md` 与目标 YAML 映射表           | §4 清单与仓库 glob **一致** |
| 确认 **不**做规范层 YAML 化                                                | §1 非范围勾选             |
| 选定工具落点：`kimi-code-meta/tools/tech_graph/` + `package.json` scripts | 路径写入 §10             |
| 定义 `freeze_id` 前缀与 `graph.json` 落盘策略（同路径 v2 · 对齐 Ink 默认）           | §10 备忘               |


**出口**：HG-TASK-DRAFT 可签 · 可进入 F1 30。

### F1 · 工具链 bootstrap


| 交付                                                                      | 验收                           |
| ----------------------------------------------------------------------- | ---------------------------- |
| 从 Ink 后端 **复制/adapt** compile · export · equivalence · schema 四件套       | 本地 `--help` 可跑               |
| `docs/_tech_graph/graph_v2.schema.json` + 人读 `graph_v2_schema.md`（可选薄页） | schema validate 样例 PASS      |
| `pnpm graph:compile:check` 或等价 script（命名可调整）                            | README / task §8 可复现         |
| pytest 或 smoke：`tests/tech_graph/` ≥1 夹具                                | `test_strategy: required` 满足 |


**出口**：F2 可迁移 `00_main` · **禁止**未 F1 绿就 batch 改图。

### F2 · P0 · `00_main.graph.yaml`


| 交付                                                   | 验收                     |
| ---------------------------------------------------- | ---------------------- |
| `00_main.graph.yaml` 为 **唯一编辑源**                     | 手改 `.md` 视为 drift      |
| compile 生成 `00_main.md` · 语义与迁移前 Mermaid **等价**      | equivalence check PASS |
| 处理 `00_main.ai.md`：删除或顶栏 `@deprecated · 源迁 YAML`     | 与 Ink G0 一致            |
| `00_main` 待补 flow 清单表 **保留**在生成 `.md` 或 YAML `notes` | #437 仍可读清单             |


**参照**：Ink `task_engineering_graph_yaml_p0_00_main_v1.md`。

### F3 · batch · `10_flow_`*（流程轨核心）


| 子步      | 源文件（当前）                                       | 目标 YAML                                    | 当前状态                    |
| ------- | --------------------------------------------- | ------------------------------------------ | ----------------------- |
| **F3a** | `10_flow_cli_session.md`                      | `10_flow_cli_session.graph.yaml`           | skeleton · **#437 主落点** |
| **F3b** | `10_flow_agent_turn.md` + `.ai.md`            | `10_flow_agent_turn.graph.yaml`            | partial · C2 #583       |
| **F3c** | `10_flow_read_tool.md` + `.ai.md`             | `10_flow_read_tool.graph.yaml`             | partial · C3 #94        |
| **F3d** | `10_flow_context_tool_exchange.md` + `.ai.md` | `10_flow_context_tool_exchange.graph.yaml` | skeleton · C3 #705      |
| **F3e** | `10_flow_skill_load.md` + `.ai.md`            | `10_flow_skill_load.graph.yaml`            | partial · C3 #580       |


**每子步验收（与 Ink Epic 对齐）**：

- [ ] `.graph.yaml` 存在且为唯一编辑源
- [ ] compile 生成 `.md` · 与迁移前拓扑等价
- [ ] 原 `.ai.md` deprecated 或删除（export **不再**以 `.ai.md` 为源）
- [ ] 单图 pytest/smoke ≥1
- [ ] 独立 meta commit（建议 `graph(yaml): migrate 10_flow_`*）便于回滚

**禁止**：F3 期间开 #437 产品 `feature/`* 分支改码。

### F4 · 纪律更新（meta + 工作区指针）


| 交付                                                                                             | 验收          |
| ---------------------------------------------------------------------------------------------- | ----------- |
| 更新 fork `docs/tasks/TASK_TEMPLATE_upstream_pr_v1.md`：`graph_delta` 示例改为 `10_flow_*.graph.yaml` | 模板可读        |
| 更新 `docs/harness/prompts/FRAGMENT_30_invoke_block_v1_zh.md`：`@…/graph_delta.graph.yaml`        | 30 帽一致      |
| 工作区 PILOT §5.2：`skeleton_before_30` = **YAML skeleton** + compile 出 `.md`                      | 维护者扫一眼      |
| `gate-check` 或 pre-commit **可选**钩子文档化（对齐 G1.1 optional ingest）                                 | PLAN §4 表更新 |


### F5 · 关账


| 交付                                                                      | 验收                  |
| ----------------------------------------------------------------------- | ------------------- |
| 全量 `graph_yaml_compile --all --check` exit 0                            | CI 或本地记录            |
| `graph.json` export · v2 schema 校验 · 等价全图 PASS                          | §8 命令绿              |
| `graph axioms check` PASS                                               | Track C 纪律延续        |
| `02_version.md` 一行 · invoke `meta-graph-v2-batch-migrate/CLOSE`         | Projects 工作区可链      |
| `HG-GRAPH-YAML-CLOSE` → approved                                        | 人签                  |
| 起草 **后继 task 占位**（不必本 PR 写完 §5）：`task_fix_approve_once_437_v1.md` draft | graph_delta 已指 YAML |


---

## 4. 迁移清单（graph_delta 真值）


| graph_id                        | 编辑源（关账后）                                   | 生成物                                | 备注         |
| ------------------------------- | ------------------------------------------ | ---------------------------------- | ---------- |
| `00_main`                       | `00_main.graph.yaml`                       | `00_main.md`                       | F2         |
| `10_flow_cli_session`           | `10_flow_cli_session.graph.yaml`           | `10_flow_cli_session.md`           | F3a · #437 |
| `10_flow_agent_turn`            | `10_flow_agent_turn.graph.yaml`            | `10_flow_agent_turn.md`            | F3b        |
| `10_flow_read_tool`             | `10_flow_read_tool.graph.yaml`             | `10_flow_read_tool.md`             | F3c        |
| `10_flow_context_tool_exchange` | `10_flow_context_tool_exchange.graph.yaml` | `10_flow_context_tool_exchange.md` | F3d        |
| `10_flow_skill_load`            | `10_flow_skill_load.graph.yaml`            | `10_flow_skill_load.md`            | F3e        |


**待补 flow**（`10_flow_mcp_tool` · `10_flow_subagent`）：仍只在 `00_main` 清单 · **本 task 不建 YAML** · 首个触达 Issue 再按新纪律建 `.graph.yaml`。

---

## 5. 非范围

- Moonshot upstream PR（`apps/` · `packages/`）
- #437 产品 bugfix（**后继 task**）
- #580 / #705 等业务 Issue 关账
- Ink / ai-ink-brain 子仓任何修改
- Track E B9 shell 实验
- `graph_query` 产品 CLI · HGM ingest 全量
- Ops Desk SPEC / HG-SPEC-SIGNOFF

---

## 6. 失败路径


| 触发条件                  | 系统行为                          | 可重试 |
| --------------------- | ----------------------------- | --- |
| F1 未绿即 F3 batch       | **拒执行 F3**                    | 是   |
| compile `--check` 失败  | **不得** `HG-GRAPH-YAML-CLOSE`  | 是   |
| 等价检查低于阈值              | 拒关账 · 回到对应 F2/F3 子步           | 是   |
| 手改生成 `.md` 未回写 YAML   | CI/check 失败 · 维护者拒 merge meta | 是   |
| 与 #437 同分支 / 同 PR     | **拒** · 双分支纪律                 | 否   |
| `HG-AUDIT-R1` pending | 30 **拒开工**                    | 是   |
| 关账无 `02_version` 行    | 不得 `done/`                    | 是   |


---

## 7. 给 10-task 交接物


| 字段              | 值                                                             |
| --------------- | ------------------------------------------------------------- |
| **帽子**          | 10-task                                                       |
| **Open Folder** | `kimi-code-meta/`                                             |
| **必读**          | 本 task §1–§4 · §2 后端 task 链 · `docs/_tech_graph/01_struct.md` |
| **禁止**          | 改 `../kimi-code/apps` · `../kimi-code/packages` · Ink 子仓      |
| **产出**          | §5 思考轮（下节）回填 · F0 映射表                                         |


---

## 8. Kimi Code Agent · 思考轮次（§5 占位）


| 字段                    | 值                                                                     |
| --------------------- | --------------------------------------------------------------------- |
| **actual_last_round** | R5                                                                    |
| **early_stop**        | false                                                                 |
| **early_stop_reason** | —                                                                     |
| **residual_risks**    | F1 工具移植路径差异 · cli_session 无 `.ai.md` · partial 图 prose 入 YAML `notes` |


### R0 · 读 task

- 已读 task 全文 §1–§4 · §7 · invoke README · PLAN §4′；确认 **HG-TASK-DRAFT approved** · 分支 `cyning/meta` · Open Folder `kimi-code-meta/`。
- 交付边界：**F0 选型 + R0–R5 回填**；禁止 F1–F5 实现 · 禁止改 `*.graph.yaml` · 禁止 commit/push。
- 关账目标：6 图 YAML 单源 → compile `.md` → export `graph.json` v2 → PILOT §5.2 YAML-first → 后继 #437 `graph_delta: 10_flow_cli_session.graph.yaml`。
- 人工闸：`HG-AUDIT-R1` pending → **30 拒开工**；`HG-GRAPH-YAML-CLOSE` 待 F5 人签。

### R1 · Ink 后端参照 + meta 现状

- **Epic 对应**：Ink P0→P5（7 flow）≈ meta F2（`00_main`）+ F3a–F3e（5 flow）；meta **无** RAG 专链（`10_flow_rag` 等 7 图中的 6 张不在 scope）。
- **四件套路径（Ink 只读）**：`scripts/graph_yaml_compile.py` · `tools/tech_graph_graph_export.py` · `tools/tech_graph_graph_equivalence_check.py` · `tools/tech_graph_graph_v2_schema.py` · CI 片段 `.github/workflows/tech-graph.yml`。
- **meta 现状 glob**：`docs/_tech_graph/` 共 15 文件 · **0× `*.graph.yaml`** · **0× `tools/tech_graph/`** · root `package.json` 无 graph script。
- **§4 六图 glob 一致**：5× `10_flow_*.md` 与 task §4 完全匹配；`00_main.md` + `00_main.ai.md` 存在。
- `**.ai.md` 分布**：`00_main` · `agent_turn` · `read_tool` · `context_tool_exchange` · `skill_load` 共 5 份；`**10_flow_cli_session` 无 `.ai.md`**（skeleton · 待 F3a 从 `.md` 直迁 YAML）。
- **成熟度**：skeleton — `cli_session` · `context_tool_exchange`；partial — `agent_turn` · `read_tool` · `skill_load`。
- **确认不 YAML 化**：`01_struct.md` · `02_version.md` · `99_mermaid_protocol.md`（GUIDE §2 规范层 · task §1 非范围）。

### R2 · 方案对比

- **A 全 batch 一次 PR** vs **B 分阶段 commit（推荐 B）**：F2 单 commit `00_main` → F3a–F3e 各独立 commit（`graph(yaml): migrate 10_flow_*`），对齐 Ink Epic #163–#171 回滚粒度。
- **export 源切换时机**：F3 各子步可 `@deprecated` 对应 `.ai.md`；**export 改读 YAML 统一在 F5**（对齐 Ink Inform P1 · 避免 F3 中途 export 双源）。
- **工具落点**：`kimi-code-meta/tools/tech_graph/`（Python · 从 Ink copy/adapt）+ root `package.json` 包装 `pnpm graph:compile:check` 等；**不在** `apps/` · `packages/` 加运行时依赖。
- **风险**：hand-edited `.md` drift → `compile --check` 挡；partial 图内 prose/表格 → YAML `notes` 字段保留（Ink P2 `notes` 渲染先例）。

### R3 · 边界 / 测试

- **test_strategy required**：F1 起 `tests/tech_graph/` ≥1 smoke/图 · 全量 `graph_yaml_compile --all --check` · export 等价（95%/90% 阈值 · Ink P2-0）· `graph axioms check`。
- **非范围**：`graph_query` CLI 产品化 · HGM ingest · #437 产品码 · Moonshot upstream · Ink/ai-ink-brain 修改。
- **F3 纪律**：**不得** 开 `feature/fix-437-*` 或其它产品分支；与 #437 同 PR/同分支 → STOP（task §6）。
- **待补 flow**（`10_flow_mcp_tool` · `10_flow_subagent`）：仅 `00_main` 清单 · 本 task 不建 YAML。

### R4 · PR / commit 策略

- **仅 `cyning/meta`** · 无 Moonshot upstream PR；产品 diff 留在后继 `feature/fix-*`。
- **commit 消息**：`graph(yaml): migrate 00_main` · `graph(yaml): migrate 10_flow_`* · `chore(tech_graph): bootstrap compile/export toolchain` · `chore(tech_graph): F4 discipline · PILOT §5.2`。
- **30 invoke 快照**：落 `Projects/docs/harness/invokes/by-task/meta-graph-v2-batch-migrate/`（30 帽纪律 · 本 10 帽不写 invoke 正文）。
- **关账 push**：F5 后 meta commit push `origin/cyning/meta` · 工作区 task pointer → `done/`（若启用双仓索引）。

### R5 · 图谱增量 + 关账判断

- **graph_delta**：`flow_track_batch`（§4 六图）；关账后 PILOT §5.2 · task 模板 · `FRAGMENT_30` 默认 `graph_delta` → `**.graph.yaml` 路径。
- **后继 #437**：CLOSE 后起草 `task_fix_approve_once_437_v1.md` · `graph_delta: 10_flow_cli_session.graph.yaml` · YAML 增量 → compile → `feature/fix-437-`* 产品码。
- `**.ai.md` 处置**：F2/F3 顶栏 `@deprecated · 源迁 YAML`；**物理删除** 留 F5 + `HG-GRAPH-YAML-CLOSE` 维护者决策（对齐 Ink G0）。
- **关账 checklist**：§9 全绿 · `02_version.md` 一行 · `freeze_id` 填 F1 commit 短 SHA · invoke CLOSE。

---

## 9. 验收标准（关账 checklist）

- [x] F0–F5 全部子交付完成
- [x] §4 六图 YAML 单源 + compile 生成 `.md`
- [x] export `graph.json` v2 + 等价 + schema 绿
- [x] `graph axioms check` PASS
- [x] PILOT / template / FRAGMENT_30 已更新
- [x] §5 思考轮闭合 · `HG-AUDIT-R1` · `HG-GRAPH-YAML-CLOSE` approved
- [x] invoke CLOSE 落盘 · meta commit push `cyning/meta`（commit `0fa2d54f` · push 待维护者）
- [ ] 工作区 pointer task → `done/`（若启用双仓索引）

---

## 10. 验证命令（30 后回填真路径）

```bash
cd /path/to/kimi-code-meta
git checkout cyning/meta

# F1+ · 按落盘脚本名为准
python3 tools/tech_graph/graph_yaml_compile.py --all --check
python3 tools/tech_graph/tech_graph_graph_export.py --check
python3 tools/tech_graph/tech_graph_graph_equivalence_check.py

pnpm graph:compile:check   # 若已包装
npx @cyning/harness@2.0.1 graph axioms check --root .

git diff --name-only HEAD~1 -- docs/_tech_graph/
# 期望：*.graph.yaml 新增/更新 · *.md 为生成物 · 无 apps/ packages/
```

---

## 11. 后继 · #437 无债开工条件

本 task **CLOSE** 后，维护者起草（或 Agent 00 相位起草）：


| 字段              | 建议值                                                                                 |
| --------------- | ----------------------------------------------------------------------------------- |
| **task**        | `task_fix_approve_once_437_v1.md`                                                   |
| **graph_delta** | `10_flow_cli_session.graph.yaml`                                                    |
| **graph_gate**  | `yaml_edit_before_30` · compile skeleton · `close_partial_or_final`                 |
| **30 前**        | 在 YAML 上补 approve-once / session 分支 → `graph_yaml_compile` → 再开 `feature/fix-437-`* |
| **上游 PR**       | 仅产品 diff                                                                            |


```text
meta-graph-v2-batch-migrate CLOSE
  → task_fix_approve_once_437_v1 draft
  → 10_flow_cli_session.graph.yaml 增量
  → HG-AUDIT-R1
  → feature/fix-437-* · 上游 PR
```

---

## 12. 实现备忘（30 后回填）


| 项               | 状态  | 备注                                                                |
| --------------- | --- | ----------------------------------------------------------------- |
| F0 映射表          | ✅   | §12.1                                                             |
| F1 工具路径         | ✅   | `tools/tech_graph/` · `tests/tech_graph/test_graph_yaml_smoke.py` |
| F2 00_main      | ✅   | `00_main.graph.yaml`                                              |
| F3a–F3e         | ✅   | 5× `10_flow_*.graph.yaml` · 子图节点 ID 全局唯一前缀                        |
| F4 纪律           | ✅   | `TASK_TEMPLATE` · `FRAGMENT_30_invoke_block`                      |
| F5 graph.json   | ✅   | export + equivalence + axioms PASS · `02_version` 一行              |
| meta commit SHA | ✅   | `0fa2d54f` · `chore(tech_graph): graph_v2 batch migrate` |
| invoke CLOSE    | ✅   | Projects `invoke_20260618_CLOSE_meta-graph-v2-batch-migrate.md` |


### 12.1 · F0 映射表（md → 目标 `.graph.yaml`）


| graph_id                        | 当前源                                           | `.ai.md` | 成熟度                          | 目标 YAML                                    | 阶段  | 备注                                     |
| ------------------------------- | --------------------------------------------- | -------- | ---------------------------- | ------------------------------------------ | --- | -------------------------------------- |
| `00_main`                       | `00_main.md` + `00_main.ai.md`                | ✅        | bootstrap                    | `00_main.graph.yaml`                       | F2  | 待补 flow 清单保留在 YAML `notes` 或生成 `.md`   |
| `10_flow_cli_session`           | `10_flow_cli_session.md`                      | ❌        | **skeleton**                 | `10_flow_cli_session.graph.yaml`           | F3a | **#437 主落点** · 无 `.ai.md` · 从 `.md` 直迁 |
| `10_flow_agent_turn`            | `10_flow_agent_turn.md` + `.ai.md`            | ✅        | **partial** · C2 #583        | `10_flow_agent_turn.graph.yaml`            | F3b | telemetry outcome 切片                   |
| `10_flow_read_tool`             | `10_flow_read_tool.md` + `.ai.md`             | ✅        | **partial** · C3 #94         | `10_flow_read_tool.graph.yaml`             | F3c | PR #708 OPEN                           |
| `10_flow_context_tool_exchange` | `10_flow_context_tool_exchange.md` + `.ai.md` | ✅        | **skeleton** · C3 #705       | `10_flow_context_tool_exchange.graph.yaml` | F3d | task #705 active                       |
| `10_flow_skill_load`            | `10_flow_skill_load.md` + `.ai.md`            | ✅        | **partial · fork** · C3 #580 | `10_flow_skill_load.graph.yaml`            | F3e | upstream 未合并                           |


**不 YAML 化（规范层 · 保持 Markdown）**：`01_struct.md` · `02_version.md` · `99_mermaid_protocol.md`

**待补 flow（本 task 不建 YAML）**：`10_flow_mcp_tool` · `10_flow_subagent` — 仅 `00_main` 清单引用

**仓库核对（2026-06-18 · 30 后）**：6× `*.graph.yaml` · compile 生成 `.md` · `graph.json` v2 export 绿

### 12.2 · F0 工具落点 · freeze_id · graph.json 草案


| 项                                | 建议值                                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **工具目录**                         | `kimi-code-meta/tools/tech_graph/`                                                                                                                                                   |
| **复制源（Ink 只读）**                  | `ai-ink-brain-api-python/scripts/graph_yaml_compile.py` · `tools/tech_graph_graph_export.py` · `tools/tech_graph_graph_equivalence_check.py` · `tools/tech_graph_graph_v2_schema.py` |
| **pnpm 包装（root `package.json`）** | `graph:compile` · `graph:compile:check` · `graph:export:check` · `graph:equivalence`（F1 定稿脚本名）                                                                                       |
| **schema 落盘**                    | `docs/_tech_graph/graph_v2.schema.json` + 可选薄页 `graph_v2_schema.md`                                                                                                                  |
| **graph.json**                   | `docs/_tech_graph/graph.json` · `schema_version: graph_v2` · 对齐 Ink 默认路径                                                                                                             |
| **freeze_id 前缀**                 | `KIMI-META-GRAPH-V2-BATCH@` + F1 bootstrap commit 短 SHA（当前 task 元信息 `TBD`）                                                                                                           |
| **CI 参照**                        | Ink `.github/workflows/tech-graph.yml` 片段 · meta 新增或扩展现有 workflow（F1/F5 · 30 帽）                                                                                                      |
| **测试目录**                         | `tests/tech_graph/` · 每图 ≥1 smoke · 全量 `--check`                                                                                                                                     |


---

## 13. 修订记录


| 日期         | 说明                                        |
| ---------- | ----------------------------------------- |
| 2026-06-18 | CLOSE · HG-GRAPH-YAML-CLOSE approved · 6 图 YAML-first · #437 draft 就绪 |


