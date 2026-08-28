# Task · W2 00_main 模块节点与有证据依赖边

> **状态**：`done` · 2026-08-28  
> **Epic SPEC**：[`SPEC_meta_graph_full_coverage_v1_zh.md`](../specs/SPEC_meta_graph_full_coverage_v1_zh.md)  
> **代签授权**：[`NOTE_00_process_signoff_auth_20260828.md`](../../harness/invokes/by-task/meta-graph-full-coverage/NOTE_00_process_signoff_auth_20260828.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-full-coverage-w2` |
| **test_strategy** | `required` |
| **test_strategy_note** | 关账回归 `python3 tools/tech_graph/graph_yaml_compile.py --all --check` 等四段；环境允许时 `pnpm graph:ci`。覆盖完成看 SPEC §4.2，不以面试阈值为唯一验收。 |
| **code_quality_bar** | `strict` |
| **freeze_id** | `META-GRAPH-FULL-COVERAGE` |
| **track** | `engineering` |
| **orchestration** | 00 编排 · 本 task **30 subagent** 落地 · 完成后 00 自动派下一波 |
| **semi_auto** | `false` |
| **audit_profile** | `human_only` |
| **invoke_retention_profile** | `default` |
| **required_invoke_hats** | `10,30,40` |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **meta_worktree** | 同 `worktree_root` |
| **module_id** | `monorepo_root` |
| **graph_delta** | `docs/_tech_graph/00_main.graph.yaml` |
| **graph_delta_note** | 仅 00_main 索引/模块边；不建 W3 flow yaml |
| **graph_gate** | `close_partial_or_final` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 本 Epic 改 `docs/_tech_graph` Inform 层，不写 `docs/coding_wiki/` |
| **wiki_promotion** | `none` |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | 过程轨 `cyning/meta` 图谱补全 · 无强制上游 PR |
| **experience_capture** | `not_applicable` |
| **experience_capture_note** | 图谱登记/索引，不沉淀 coding_wiki 条目 |
| **kpi_aggregator** | `CLOSE` |
| **entry_invoke_30** | `docs/harness/invokes/by-task/meta-graph-full-coverage/PROMPT_30_meta-graph-full-coverage-w2.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved 2026-08-28 | 20-R1, 30 | 00 代签 · 维护者授权过程文档 |
| HG-AUDIT-R1 | approved 2026-08-28 | 30 | 审查文 `docs/harness/reviews/task_meta_graph_full_coverage_w2_audit_R1_20260828.md` · 00 代签 |
| HG-GRAPH-MODULES | 见 `01_struct.md` | 30 业务码 | 本 task 只动 Inform；W1 扩表后 00 回写 approved |

### 依赖

- 前序：W1 done · `01_struct` HG-GRAPH-MODULES approved

---

## 1. 背景与目标

Epic 已 spec-signed。本 task 只交付本波增量，**不**单独承担全图谱。完整性由 W0→W1→W2→W3-mcp→W3-subagent→W-close 链保证。

## 2. 范围

- [x] `00_main.graph.yaml` 为已登记模块补 struct 节点：`vis` `acp_adapter` `migration_legacy` `kimi_web` `protocol` `server` `server_e2e`
- [x] 边仅附录 A.3 证据：含 `agent_core→protocol`、`server→agent_core/protocol`、`server_e2e→protocol`、`kimi_web` 对 `server` 用 `calls`/`::triggers`（禁止 web→agent_core depends_on）、`acp_adapter` 实有出边、`vis→agent_core/kosong`
- [x] **不发明** vis→node_sdk；不为 stub 包加节点
- [x] **不**加 FLOW_MCP / FLOW_SUB 索引（W-close）
- [x] compile 生成 `00_main.md`；`python3 tools/tech_graph/tech_graph_graph_export.py` 保持 graph.json 同步

## 非范围

- 不迁 `l0/l1/l2`；不改 dsh-coding-kit / Ops-desk
- 不改 `packages/**` `apps/**` 生产逻辑（AGENTS.md Project Map 文档行除外，仅 W1）
- 不画全部 builtin tool 独立 flow；不把现有 5 张 flow 充实到生产完备
- 无代码锚不预建空 yaml
- 不 git commit / push（除非维护者另说）


## 失败路径

| 触发条件 | 系统行为 | 可重试 | 用户可见 |
|----------|----------|--------|----------|
| HG-AUDIT-R1 表为 pending 仍 30 | **拒开工** | 是 | 以 task 表为准 |
| 无代码锚预建空 yaml | 审查退回 | 是 | 补锚或 defer |
| 迁目录未改 glob | graph:ci 假绿/漏图 | 是 | 回滚扁平 |
| 发明 package.json 没有的依赖边 | 退回 | 是 | 删边 |
| 给 kimi-web 画 protocol/agent_core 包依赖 | 退回 | 是 | 改为 calls→server |

## 验收标准

- [x] 已登记模块均有 `module_id` struct 节点
- [x] 新边均可指回 package.json 或 SPEC A.3
- [x] compile + export check 绿（或记录 Node engines 后直跑 python）

- [x] 未改 dsh-coding-kit / Ops-desk / 业务生产逻辑
- [x] 落盘 30 invoke 快照于 `docs/harness/invokes/by-task/meta-graph-full-coverage/`

## 6. 思考轮（10-task 预填 · 继承 SPEC R0–R5）

### R0
Open Folder = 本仓根。读 SPEC 附录 A 与本 task 范围。维持扁平 glob。

### R1
本波只做上表范围；完整性靠后续波，不在本 30 一次画完。

### R2
维持扁平；禁 l0/l1/l2；有锚才建 yaml。

### R3
依赖边必须有 package.json 或源码证据。`kimi-web` 只允许 runtime `calls` 到 `server`。

### R4
`test_strategy=required`。本波验证命令见验收。全链关账才跑齐 graph:ci。

### R5
闸已 00 代签。可 30。

### 思考轮控制

| 字段 | 值 |
|------|-----|
| **actual_last_round** | `R5` |
| **early_stop** | `no` |
| **early_stop_reason** | — |
| **residual_risks** | MCP/subagent 索引边留 W-close，避免与 W3 yaml 并行冲突。 |

## 7. 给 30 必读

- `docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md` 附录 A
- `docs/_tech_graph/01_struct.md`
- `docs/_tech_graph/graph_module_flow_map.yaml`
- `docs/_tech_graph/00_main.graph.yaml`
- `docs/harness/prompts/30-execute-code.md` · GATE_VERIFY 首输出

### 自检结论

**帽**：30 · **日期**：2026-08-28 · **结论**：W2 Inform 落地 · 15 个已登记 `module_id` 均有 `00_main` struct 节点 · **可派 W3**

**GATE_VERIFY（task 表真值）**

| human_gate_id | task表status | 用户/invoke声称 | 一致？ | blocks_30 | 30可开工？ |
|---------------|--------------|-----------------|--------|-----------|------------|
| HG-TASK-DRAFT | approved 2026-08-28 | approved 2026-08-28 | Y | Y（本波仅 Inform） | ✅ |
| HG-AUDIT-R1 | approved 2026-08-28 | approved 2026-08-28 | Y | Y | ✅ |
| HG-GRAPH-MODULES | 见 `01_struct.md` approved 2026-08-28 | W1 扩表后 00 代签 | Y | 仅 30 业务码 | ✅ Inform only |

reviews：`docs/harness/reviews/task_meta-graph-full-coverage-w2_audit_R1_20260828.md` 存在。

`npx dsh-coding-kit verify` 把 `approved 2026-08-28` 误解析为 pending → 机械 BLOCKED。**以 task 表为准**，声称与表一致，可开工。未把闸改成 pending。未改 `01_struct` / `flow_map`（无 W1 笔误）。

**新增节点 id**：`VIS` `ACP` `MIG` `WEB` `PROTO` `SRV` `E2E`（module_id：`vis` `acp_adapter` `migration_legacy` `kimi_web` `protocol` `server` `server_e2e`）。未加 stub `kimi-migration-legacy`。未加 `FLOW_MCP` / `FLOW_SUB`。

**新增边**：`AC→PROTO` · `SRV→AC` · `SRV→PROTO` · `E2E→PROTO` · `WEB→SRV`（`::triggers` / `type: calls`）· `ACP→AC,KA,SDK` · `VIS→AC,KS` · `MIG→AC` · 可选 `CLI→SRV` / `CLI→WEB`（label `devDep / bundle`）。禁止项：无 `WEB depends_on AC/PROTO`、无 `VIS→SDK`。

**验证**：`graph_yaml_compile.py --all --check` · export `--check` · equivalence · completeness 均 exit 0。`graph_id` 仍为 `00_main`。freeze_id 未改。未新建 `10_flow_*.graph.yaml`；未改 `packages/**` `apps/**`；未 git commit。compile `--all` 曾改 5 张 flow md 的 `generated_at`，已 checkout 还原。

**交付**：`invoke_20260828_30_w2.md`。
