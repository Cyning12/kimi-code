# Task · W0 缺口清单定稿（冻结附录 A）

> **状态**：`done` · W0 freeze 2026-08-28  
> **Epic SPEC**：[`SPEC_meta_graph_full_coverage_v1_zh.md`](../specs/SPEC_meta_graph_full_coverage_v1_zh.md)  
> **代签授权**：[`NOTE_00_process_signoff_auth_20260828.md`](../../harness/invokes/by-task/meta-graph-full-coverage/NOTE_00_process_signoff_auth_20260828.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-full-coverage-w0` |
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
| **graph_delta** | `none` |
| **graph_delta_note** | 本波只核对/冻结 SPEC 附录 A，不改 yaml |
| **graph_gate** | `close_partial_or_final` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 本 Epic 改 `docs/_tech_graph` Inform 层，不写 `docs/coding_wiki/` |
| **wiki_promotion** | `none` |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | 过程轨 `cyning/meta` 图谱补全 · 无强制上游 PR |
| **experience_capture** | `not_applicable` |
| **experience_capture_note** | 图谱登记/索引，不沉淀 coding_wiki 条目 |
| **kpi_aggregator** | `CLOSE` |
| **entry_invoke_30** | `docs/harness/invokes/by-task/meta-graph-full-coverage/PROMPT_30_meta-graph-full-coverage-w0.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved 2026-08-28 | 20-R1, 30 | 00 代签 · 维护者授权过程文档 |
| HG-AUDIT-R1 | approved 2026-08-28 | 30 | 审查文 `docs/harness/reviews/task_meta_graph_full_coverage_w0_audit_R1_20260828.md` · 00 代签 |
| HG-GRAPH-MODULES | 见 `01_struct.md` | 30 业务码 | 本 task 只动 Inform；W1 扩表后 00 回写 approved |

### 依赖

- 无前序 task。SPEC 已 HG-SPEC-SIGNOFF approved。

---

## 1. 背景与目标

Epic 已 spec-signed。本 task 只交付本波增量，**不**单独承担全图谱。完整性由 W0→W1→W2→W3-mcp→W3-subagent→W-close 链保证。

## 2. 范围

- [x] 复盘 `apps/*` `packages/*` vs SPEC 附录 A.1，无静默缺口
- [x] 确认 `kimi-migration-legacy` 仍为 stub（仅 package.json）→ defer
- [x] 确认 MCP / subagent 锚文件仍存在（附录 A.4）
- [x] 落盘 `docs/harness/invokes/by-task/meta-graph-full-coverage/W0_FREEZE_20260828.md`：结论 freeze / 追加缺口（若有则先改 SPEC 附录再 freeze）
- [x] **禁止**改 `*.graph.yaml` / `01_struct.md` / flow_map

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
| 发现静默缺口却不改附录就 freeze | 下一波按过时清单补行 | 是 | 先补附录 |

## 验收标准

- [x] W0_FREEZE 文存在且结论为 freeze（或已回写 SPEC 附录后再 freeze）
- [x] 未修改图谱编辑源

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
| **residual_risks** | 附录相对 workspace 可能再漂移；W0 只冻结当下。 |

## 7. 给 30 必读

- `docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md` 附录 A
- `docs/_tech_graph/01_struct.md`
- `docs/_tech_graph/graph_module_flow_map.yaml`
- `docs/_tech_graph/00_main.graph.yaml`
- `docs/harness/prompts/30-execute-code.md` · GATE_VERIFY 首输出

### 自检结论

**帽**：30 · **日期**：2026-08-28 · **结论**：附录 A **freeze** · 无静默缺口 · 可派 W1

**GATE_VERIFY（task 表真值）**

| human_gate_id | task表status | 用户/invoke声称 | 一致？ | blocks_30 | 30可开工？ |
|---------------|--------------|-----------------|--------|-----------|------------|
| HG-TASK-DRAFT | approved 2026-08-28 | approved 2026-08-28 | Y | Y（本波仅 Inform） | ✅ |
| HG-AUDIT-R1 | approved 2026-08-28 | approved 2026-08-28 | Y | Y | ✅ |
| HG-GRAPH-MODULES | 见 `01_struct.md` = approved | — | — | 仅 30 业务码 | ✅ 本波不改业务码 |

reviews：`docs/harness/reviews/task_meta-graph-full-coverage-w0_audit_R1_20260828.md` 存在 · R1 **pass**。task 表路径用下划线文件名，实有为 hyphen slug（过程注，非附录缺口）。

`npx dsh-coding-kit verify` 把 `approved 2026-08-28` 误解析为 pending → 机械 BLOCKED。**以 task 表为准**，可开工。冲突规则未触发（声称与表一致）。

**核对**：`ls -1d apps/*/ packages/*/` 与附录 A.1 一一对应；`packages/kimi-migration-legacy/` 仍仅 `package.json`；A.4 11 个锚文件均存在（`McpConnectionManager` / `attachMcpTools` / `SessionSubagentHost`）。未改 yaml / struct / flow_map / 生产码。

**交付**：`W0_FREEZE_20260828.md` · `invoke_20260828_30_w0.md`

