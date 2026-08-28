# Task · W3b 10_flow_subagent（有锚才建）

> **状态**：`done` · 2026-08-28  
> **Epic SPEC**：[`SPEC_meta_graph_full_coverage_v1_zh.md`](../specs/SPEC_meta_graph_full_coverage_v1_zh.md)  
> **代签授权**：[`NOTE_00_process_signoff_auth_20260828.md`](../../harness/invokes/by-task/meta-graph-full-coverage/NOTE_00_process_signoff_auth_20260828.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-full-coverage-w3-subagent` |
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
| **module_id** | `agent_core` |
| **graph_delta** | `docs/_tech_graph/10_flow_subagent.graph.yaml` |
| **graph_delta_note** | 新建 subagent flow；不改 00_main |
| **graph_gate** | `close_partial_or_final` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 本 Epic 改 `docs/_tech_graph` Inform 层，不写 `docs/coding_wiki/` |
| **wiki_promotion** | `none` |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | 过程轨 `cyning/meta` 图谱补全 · 无强制上游 PR |
| **experience_capture** | `not_applicable` |
| **experience_capture_note** | 图谱登记/索引，不沉淀 coding_wiki 条目 |
| **kpi_aggregator** | `CLOSE` |
| **entry_invoke_30** | `docs/harness/invokes/by-task/meta-graph-full-coverage/PROMPT_30_meta-graph-full-coverage-w3-subagent.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved 2026-08-28 | 20-R1, 30 | 00 代签 · 维护者授权过程文档 |
| HG-AUDIT-R1 | approved 2026-08-28 | 30 | 审查文 `docs/harness/reviews/task_meta_graph_full_coverage_w3_subagent_audit_R1_20260828.md` · 00 代签 |
| HG-GRAPH-MODULES | 见 `01_struct.md` | 30 业务码 | 本 task 只动 Inform；W1 扩表后 00 回写 approved |

### 依赖

- 前序：W1 done。可与 W3-mcp 并行。**禁止**改 `00_main.graph.yaml`。

---

## 1. 背景与目标

Epic 已 spec-signed。本 task 只交付本波增量，**不**单独承担全图谱。完整性由 W0→W1→W2→W3-mcp→W3-subagent→W-close 链保证。

## 2. 范围

- [x] 新建 `docs/_tech_graph/10_flow_subagent.graph.yaml`
- [x] 锚：`packages/agent-core/src/session/subagent-host.ts`（`SessionSubagentHost`）· `subagent-batch.ts` · `session/index.ts` subagentHost 装配；测试 `test/session/subagent-host.test.ts` 可作佐证锚
- [x] TUI `apps/kimi-code/src/tui/controllers/subagent-event-handler.ts` **可选**消费锚，不单独成图
- [x] `graph_id` = `10_flow_subagent`；compile `.md`
- [x] 锚消失则 defer，不建空 yaml

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
| 为 TUI 另建第二张 flow | 退回 | 是 | 合并到本图注释 |

## 验收标准

- [x] yaml 存在且可 compile
- [x] 至少 1 条边含 host/batch 路径 anchors
- [x] 未改 `00_main.graph.yaml`

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
| **residual_risks** | swarm 调度细节保持切片，不追求生产完备。 |

## 7. 给 30 必读

- `docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md` 附录 A
- `docs/_tech_graph/01_struct.md`
- `docs/_tech_graph/graph_module_flow_map.yaml`
- `docs/_tech_graph/00_main.graph.yaml`
- `docs/harness/prompts/30-execute-code.md` · GATE_VERIFY 首输出

### 自检结论

30 已落地。`graph_id=10_flow_subagent`。12 节点 / 15 边；全部边含 `anchors.path`。

锚路径：`packages/agent-core/src/session/index.ts`（L732 装配）· `subagent-host.ts` · `subagent-batch.ts` · 可选消费 `apps/kimi-code/src/tui/controllers/subagent-event-handler.ts`。佐证测试未画节点。

验证：`python3 tools/tech_graph/graph_yaml_compile.py --graph-id 10_flow_subagent` → `10_flow_subagent.md`。未 `--all --check`、未 export `graph.json`（避 W3a 抢文件）。

未改：`00_main.graph.yaml` · `01_struct.md` · `graph_module_flow_map.yaml` · `packages/**` · `apps/**`。未 git commit。未迁 l0/l1/l2。无第二张 TUI 图。

`dsh-coding-kit verify` 误判 `approved 2026-08-28` 为 pending；以 task 表为准，闸一致可 30。
