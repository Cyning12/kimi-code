# Task · W3a 10_flow_mcp_tool（有锚才建）

> **状态**：`done` · 2026-08-28  
> **Epic SPEC**：[`SPEC_meta_graph_full_coverage_v1_zh.md`](../specs/SPEC_meta_graph_full_coverage_v1_zh.md)  
> **代签授权**：[`NOTE_00_process_signoff_auth_20260828.md`](../../harness/invokes/by-task/meta-graph-full-coverage/NOTE_00_process_signoff_auth_20260828.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-full-coverage-w3-mcp` |
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
| **graph_delta** | `docs/_tech_graph/10_flow_mcp_tool.graph.yaml` |
| **graph_delta_note** | 新建 mcp flow；不改 00_main（索引归 W-close） |
| **graph_gate** | `close_partial_or_final` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 本 Epic 改 `docs/_tech_graph` Inform 层，不写 `docs/coding_wiki/` |
| **wiki_promotion** | `none` |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | 过程轨 `cyning/meta` 图谱补全 · 无强制上游 PR |
| **experience_capture** | `not_applicable` |
| **experience_capture_note** | 图谱登记/索引，不沉淀 coding_wiki 条目 |
| **kpi_aggregator** | `CLOSE` |
| **entry_invoke_30** | `docs/harness/invokes/by-task/meta-graph-full-coverage/PROMPT_30_meta-graph-full-coverage-w3-mcp.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved 2026-08-28 | 20-R1, 30 | 00 代签 · 维护者授权过程文档 |
| HG-AUDIT-R1 | approved 2026-08-28 | 30 | 审查文 `docs/harness/reviews/task_meta_graph_full_coverage_w3_mcp_audit_R1_20260828.md` · 00 代签 |
| HG-GRAPH-MODULES | 见 `01_struct.md` | 30 业务码 | 本 task 只动 Inform；W1 扩表后 00 回写 approved |

### 依赖

- 前序：W1 done（agent_core 已登记）。可与 W2/W3-subagent 并行，但 **禁止**改 `00_main.graph.yaml`。

---

## 1. 背景与目标

Epic 已 spec-signed。本 task 只交付本波增量，**不**单独承担全图谱。完整性由 W0→W1→W2→W3-mcp→W3-subagent→W-close 链保证。

## 2. 范围

- [x] 新建 `docs/_tech_graph/10_flow_mcp_tool.graph.yaml`（扁平目录 · 非 l1/）
- [x] 锚必须落在 SPEC A.4：`packages/agent-core/src/mcp/connection-manager.ts` · `mcp/index.ts` · `agent/tool/index.ts`（`attachMcpTools`）· `skill/builtin/mcp-config.ts`；次要可注 `services/mcp/mcp.ts`
- [x] 切片级 skeleton/partial 即可，**不要**为每个 MCP transport 各画一张图
- [x] `graph_id` 声明值 `10_flow_mcp_tool`（路径不当 id）
- [x] compile 生成对应 `.md`
- [x] 若锚文件消失：defer 并写理由到 invoke，**不**建空 yaml

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
| 锚缺失仍建空图 | 退回 | 是 | defer |

## 验收标准

- [x] `10_flow_mcp_tool.graph.yaml` 存在且可 compile
- [x] 至少 1 条边含 A.4 路径 anchors
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
| **residual_risks** | daemon IMcpService 不另开图。 |

## 7. 给 30 必读

- `docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md` 附录 A
- `docs/_tech_graph/01_struct.md`
- `docs/_tech_graph/graph_module_flow_map.yaml`
- `docs/_tech_graph/00_main.graph.yaml`
- `docs/harness/prompts/30-execute-code.md` · GATE_VERIFY 首输出

### 自检结论

**帽**：30 · **日期**：2026-08-28 · **结论**：W3a Inform 落地 · `10_flow_mcp_tool` yaml+md · **未改** `00_main`

**GATE_VERIFY（task 表真值）**

| human_gate_id | task表status | 用户/invoke声称 | 一致？ | blocks_30 | 30可开工？ |
|---------------|--------------|-----------------|--------|-----------|------------|
| HG-TASK-DRAFT | approved 2026-08-28 | approved 2026-08-28 | Y | Y（本波仅 Inform） | ✅ |
| HG-AUDIT-R1 | approved 2026-08-28 | approved 2026-08-28 | Y | Y | ✅ |
| HG-GRAPH-MODULES | 见 `01_struct.md` approved 2026-08-28 | W1 扩表后 00 代签 | Y | 仅 30 业务码 | ✅ Inform only |

reviews：`docs/harness/reviews/task_meta-graph-full-coverage-w3-mcp_audit_R1_20260828.md` 存在。无声称 vs 表冲突。未跑会改 `graph.json` 的 export。

**交付**：`docs/_tech_graph/10_flow_mcp_tool.graph.yaml` + compile `10_flow_mcp_tool.md`。`graph_id: 10_flow_mcp_tool`。节点 14 · 边 15。stdio/sse/http 折叠进 `createClient`。daemon `IMcpService` 仅 notes。

**A.4 锚 path**：`packages/agent-core/src/mcp/connection-manager.ts` · `mcp/index.ts` · `agent/tool/index.ts`（`attachMcpTools` L68）· `skill/builtin/mcp-config.ts`。次要 `services/mcp/mcp.ts` 只在 notes。

**未改**：`00_main.graph.yaml` · `01_struct` · `flow_map` · `packages/**` · `apps/**` · 未迁 l0/l1/l2 · 未 git commit。

**交付 invoke**：`docs/harness/invokes/by-task/meta-graph-full-coverage/invoke_20260828_30_w3_mcp.md`。
