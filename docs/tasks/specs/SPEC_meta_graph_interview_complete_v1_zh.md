# SPEC · meta 图谱一次性补齐 + 本地 CI 门禁（面试加速 · v1）

> **状态**：`spec-signed`（初版 + 思考轮 R0–R6 + 20-spec-audit **conditional_pass** · **HG-SPEC-SIGNOFF approved 2026-06-26** · 待 00 拆 task）  
> **track**：`epic`  
> **域**：Track C · `Cyning12/kimi-code` @ **`cyning/meta`** · 本地目录 **`kimi-code-meta/`**  
> **关联图谱**：`docs/_tech_graph/` · [`01_struct.md`](../../_tech_graph/01_struct.md) · [`graph_module_flow_map.yaml`](../../_tech_graph/graph_module_flow_map.yaml)  
> **下游**：SPEC 签收 → 00 拆 task 链 + 并行 30 派工 → 维护者签收成品  
> **非主线**：**不**阻塞 Ops Desk P3+ 业务；Ops Desk `graph_analyst` 读边属后继消费 task

---

## Harness 元信息

| 字段 | 值 |
| --- | --- |
| **spec_slug** | `meta-graph-interview-complete` |
| **freeze_id** | `META-GRAPH-INTERVIEW-COMPLETE` |
| **test_strategy** | `required` |
| **test_strategy_note** | 本地 CI 须可失败 · 红→绿关账 |
| **orchestration** | **00 @ `Projects/` 自编排** · 维护者仅签收 SPEC / 思考轮 / 成品 |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **human_gate（维护者）** | `HG-SPEC-SIGNOFF`（初版 §1–§6 + 思考轮 R0–R6 + 20-spec-audit · **approved 2026-06-26**）· `HG-GRAPH-INTERVIEW-CLOSE`（pending） |
| **10-spec rounds** | [`Projects/docs/harness/invokes/by-task/meta-graph-interview-complete/rounds/`](../../../../docs/harness/invokes/by-task/meta-graph-interview-complete/rounds/) |
| **entry_invoke_10_spec** | [`Projects/docs/harness/invokes/by-task/meta-graph-interview-complete/PROMPT_10_spec_rethink_R1_R5.md`](../../../../docs/harness/invokes/by-task/meta-graph-interview-complete/PROMPT_10_spec_rethink_R1_R5.md) |
| **handoff_prompt** | [`PROMPT_START_handoff_new_agent_v1_zh.md`](../../../../docs/harness/invokes/by-task/meta-graph-interview-complete/PROMPT_START_handoff_new_agent_v1_zh.md) · **已移交新 Agent** |
| **工作区索引** | [`Projects/docs/harness/tasks/active/task_meta_graph_interview_complete_v1.md`](../../../../docs/harness/tasks/active/task_meta_graph_interview_complete_v1.md) |

---

## 1. 背景与目标

**背景**

- Ops Desk P3-3a 人验暴露：`graph_analyst` 读到的 snapshot **模块节点不全 / 依赖边不可用**，无法回答「模块依赖图」类问题。
- 既有 Track C 路径以 **单 Issue → `graph:issue-sync` → 单 flow YAML** 增量补齐；对 **面试演示** 节奏过慢。
- 本地 `graph.json` 已有 compile/export 工具链（`pnpm graph:*`），但 **GHA `ci.yml` 未跑图谱门禁**；完整性无单一「本地 CI 一键红绿」。

**目标（完成态）**

1. **`cyning/meta` 图谱 Inform 层一次性补齐**：`01_struct` 模块表 · 各模块 default flow · `00_main` 索引边 · **`graph.json` 含可消费的 module 依赖边**（非空 `edges` · 覆盖 P0 模块）。
2. **本地 CI 门禁脚本**（可 `pnpm graph:ci` 或等价）：compile check · export check · equivalence · **完整性 lint**（模块覆盖率 / 必填 flow / 边非空阈值）— **失败即非零退出**。
3. **00 编排并行 30**：按模块/flow 切 workstream · 独立 worktree/分支 · **不混 PR**；维护者 **不** 介入派工细节，只签收 SPEC、10-spec 思考轮文档、最终 CLOSE。

---

## 2. 范围

### 2.1 Inform 补齐（kimi-code-meta）

- [ ] 对照 [`01_struct.md`](../../_tech_graph/01_struct.md) 与 [`graph_module_flow_map.yaml`](../../_tech_graph/graph_module_flow_map.yaml)，列出 **缺口清单**（缺 flow / 缺 module 节点 / 缺跨模块边）。
- [ ] **批量** 补 `*.graph.yaml`（允许 skeleton→充实两阶段，但 export 前须过 compile）。
- [ ] 更新 `00_main.graph.yaml`：**模块级依赖边**（`depends_on` / `calls` 等 schema 内合法 type）连到各 `10_flow_*` 与子模块。
- [ ] `pnpm graph:export` 产出 **`graph.json`**：`edge_count > 0` · 覆盖 §2.2 模块白名单。
- [ ] `02_version.md` 追加本 Epic 关账行。

### 2.2 模块白名单（P0 · 面试演示最小集）

| tier | module_id | 说明 | completeness |
| --- | --- | --- | --- |
| **P0** | `cli` | apps/kimi-code | 节点 + module 边 **fail** |
| **P0** | `agent_core` | packages/agent-core | 同上 |
| **P0** | `node_sdk` | packages/node-sdk | 同上 |
| **P0** | `monorepo_root` | docs/tools/harness | **索引 struct 节点** · 0 出边可验收 |
| **P1 warn** | `kosong`, `kaos`, `oauth`, `telemetry` | 子系统 · `00_main` 物化 | 缺则 **warn** |
| **P2 defer** | `vis`, `acp_adapter`, `migration_legacy` | 本 Epic 不阻塞 | flow_map skeleton · 后继 issue-sync |

> **不得**缩至仅 `cli` 单模块（R1 签收）。

### 2.3 本地 CI 门禁（本仓）

- [ ] 新增 **`pnpm graph:ci`**（或 `scripts/graph-ci.sh`）串联：
  - `pnpm graph:compile:check`
  - `pnpm graph:export:check`
  - `pnpm graph:equivalence`（现有阈值）
  - **新增** `graph_completeness_check`（路径 `tools/tech_graph/graph_completeness_check.py`）：  
    - P0 四模块 **100%** 有 `module_id` struct 节点（**exit 4**）  
    - P0 各 module 在 **module 级 `depends_on` 边** 中 ≥1 次（**exit 4**）  
    - module 级 `depends_on` 边计数 **`≥ 8`**（B4 签收 · **exit 4**）  
    - 全图 `edges.length` **≥ 100** 回归下限（**exit 4**）  
    - P1 缺节点 **stderr warn · exit 0**；P2 defer 不 fail
- [ ] 文档：[`docs/_tech_graph/README.md`](../../_tech_graph/README.md) §常用命令 增补 `graph:ci`。
- [ ] **可选**（非本 SPEC 阻塞）：`.github/workflows/ci.yml` 增加 `graph` job @ `cyning/meta` — 00 在 task 链评估。

### 2.4 00 编排（工作区 · 不写本 SPEC 细节）

- [ ] 00 读签收后 SPEC → 产出 **task 母单 + 子 task 切片**（按 module/flow 并行）。
- [ ] 每子 task：`worktree_root` · `git_branch` · `graph_delta` · 40-self-check 命令含 **`pnpm graph:ci`**。
- [ ] 并行纪律：见 [`Projects/docs/harness/README.md`](../../../../docs/harness/README.md) **并行分支与 Git worktree**。
- [ ] 10-spec 思考轮落盘：`Projects/docs/harness/invokes/by-task/meta-graph-interview-complete/rounds/`。

---

## 3. 非范围

- Ops Desk **`graph_analyst` 读 `edges`**（api-python · 后继 task）
- MoonshotAI **上游 PR**（过程轨仅 `cyning/meta`）
- **Issue-by-issue** 作为主补齐路径（`graph:issue-sync` 仍可用于后继维护，非本 Epic 主策略）
- P3-3b asyncio fan-out · LangGraph 替换
- 强改 Kimi Code **产品代码**（除图谱锚点注释/路径引用外）

---

## 4. 验收标准

- [ ] **`pnpm graph:ci` 本地全绿**（维护者可在 `kimi-code-meta/` 一键复现）
- [ ] `graph.json`：`nodes` 覆盖 P0 模块 · `edges` 非空且 module 级依赖可追踪
- [ ] `01_struct` · `graph_module_flow_map.yaml` · YAML 源 **三者一致**（无孤儿 module_id）
- [ ] 10-spec **R0–R5** 回填完成 · `20-spec-audit` conditional_pass 或 pass
- [ ] 维护者 **HG-SPEC-SIGNOFF** → **HG-GRAPH-INTERVIEW-CLOSE**
- [ ] Ops Desk sync 后新 snapshot ingest（**人验可选** · 非本 SPEC 阻塞项）

---

## 5. failure_paths

| 触发条件 | 系统行为 | 可重试 |
| --- | --- | --- |
| YAML compile 失败 | `graph:ci` exit ≠0 · 禁止 merge graph.json | 是 · 修 YAML |
| export 与 committed graph.json 漂移 | `graph:export:check` fail | 是 · re-export |
| equivalence 阈值未达 | exit 3 · 列出 missing anchor/label | 是 · 补 YAML 边标签 |
| completeness 模块未覆盖 | exit 4 · 打印缺 module 列表 | 是 · 补 flow/节点 |
| 并行 PR 混交 discipline 文件 | 20-task-audit reject | 是 · 拆 PR |

---

## 6. 依赖与引用

- 远程映射：[`Projects/docs/harness/guides/POINTER_kimi_code_meta_git_mapping_v1_zh.md`](../../../../docs/harness/guides/POINTER_kimi_code_meta_git_mapping_v1_zh.md)
- 图谱工具真值：`kimi-code-meta/tools/tech_graph/` · `package.json` scripts `graph:*`
- 已完成 precedents：[`task_meta_graph_v2_batch_migrate_v1`](../../done/task_meta_graph_v2_batch_migrate_v1.md) · [`task_meta_graph_issue_sync_gate_v1`](../../done/task_meta_graph_issue_sync_gate_v1.md)
- Ops 消费契约：[`Projects/docs/harness/guides/ONTOLOGY_ops_desk_kimi_code_v1_zh.md`](../../../../docs/harness/guides/ONTOLOGY_ops_desk_kimi_code_v1_zh.md) · GraphSnapshot
- 00 编排图：[`Projects/docs/harness/guides/DIAGRAM_00_orchestrator_agents_human_v1_zh.md`](../../../../docs/harness/guides/DIAGRAM_00_orchestrator_agents_human_v1_zh.md)

---

## 7. 思考轮（10-spec 回填 · R0–R6）

> 落盘摘要：[`Projects/.../rounds/`](../../../../docs/harness/invokes/by-task/meta-graph-interview-complete/rounds/README.md)

### R0 · 读入与约束

- **基线**：graph.json **99 nodes · 103 edges · 6 graphs** · 无 `module_id`/`kind` · 无 `graph:ci`
- **Ops 缺口**：P3-3a snapshot **12 模块节点 · 0 依赖边**
- **拍板**：B1 export 扩 `module_id`+`kind` · B2 monorepo 索引节点 · B3 P0 fail/P1 warn · B4 module_dep≥8 · total≥100

### R1 · 范围 / 非范围 / 场景

- **面试问句 Q1–Q4 + Q6 必达**；Q5（vis/acp）建议级
- **§2.2 扩表**：P0/P1 warn/P2 defer 三层
- **Ops graph_analyst 改 api-python**：后继 task · 本 Epic 只补 Inform

### R2 · 方案对比

- **推荐 A**：YAML 显式 `module_id` + export 透传 + `graph_completeness_check.py`
- **弃选**：符号硬编码映射 · post-export 脚本写边 · 仅 lint 不扩 schema

### R3 · 边界 / 失败语义 / 安全

- **Merge 序**：WS-0 → WS-1 → WS-2/3 并行 → WS-5
- **worktree** 每 stream 独立分支 · 禁止混 PR
- **exit 4** = completeness · 图谱 YAML 无 secret

### R4 · 验收 / 可测性 / test_strategy

- **`pnpm graph:ci`** = compile + export + equivalence + completeness
- **T1–T5** 可失败用例（见 `ROUND_05_R4`）
- **GHA graph job**：本 Epic **非阻塞** · 可选 follow-up

### R5 · SPEC 签收就绪 · 是否可交 00 出 task

- **就绪**：可交 **00 拆 task 母单 + 6 workstream 子 task**
- **待**：20-spec-audit · 维护者 **HG-SPEC-SIGNOFF**（思考轮）

### R6 · 并行切片 · 子 Agent 思考轮（扩展）

- **6 workstream**：WS-0 foundation … WS-5 flow-map（见 `ROUND_07_R6`）
- **子 Agent 强制**：每 stream `rounds/by-stream/<id>/` 最少 **R0+R1** 后 30 改码
- **模板**：`TEMPLATE_subagent_rethink_v1_zh.md`

### 思考轮控制

| 字段 | 值 |
| --- | --- |
| `actual_last_round` | `R6` |
| `early_stop` | `no` |
| `early_stop_reason` | — |
| `residual_risks` | WS-0/WS-1 串行依赖 · P2 三模块 defer · Ops ingest 非阻塞 |
| `round_extension_note` | R6：Epic 跨工具+6 并行 YAML · 子 30 Agent 须独立思考轮落盘 |

---

## 8. 维护者签收点（仅三项）

| 序 | 节点 | 维护者动作 |
| --- | --- | --- |
| 1 | **初版 SPEC** | 读 §1–§6 · **approved 2026-06-26** |
| 2 | **多轮思考文档** | 读 `rounds/` R0–R6 + 20-spec-audit（conditional_pass）· **HG-SPEC-SIGNOFF approved 2026-06-26** |
| 3 | **成品** | `pnpm graph:ci` 绿 · 图谱 PR 合并 · `HG-GRAPH-INTERVIEW-CLOSE` |

---

## 修订记录

| 日期 | 摘要 |
| --- | --- |
| 2026-06-21 | 00 起草 · 面试加速 · 批量补齐 + 本地 CI · 00 自编排并行 |
| 2026-06-26 | 维护者初版签收 + B1–B4 · 10-spec R0–R6 回填 · 子 Agent 思考轮纪律 |
| 2026-06-26 | 20-spec-audit R1 **conditional_pass**（4 非阻塞移交 WS-0/WS-1/WS-5）· 维护者 **HG-SPEC-SIGNOFF approved** · 状态 → `spec-signed` · 待 00 拆 task |
