# invoke · fix-read-dual-limit-94

| 项 | 值 |
|----|-----|
| **task** | `docs/tasks/done/task_fix_read_dual_limit_94_v1.md` |
| **branch** | `feature/fix-94-read-dual-limit` |
| **issue** | [#94](https://github.com/MoonshotAI/kimi-code/issues/94) |
| **PR** | [#708](https://github.com/MoonshotAI/kimi-code/pull/708) OPEN |
| **图谱** | `docs/_tech_graph/10_flow_read_tool.md`（partial · 关账 2026-06-13） |

## 10-task · 思考 Prompt（V2 · bugfix 轨跳过 10-spec）

[`PROMPT_kimi_agent_rethink_R1_R5.md`](./PROMPT_kimi_agent_rethink_R1_R5.md) — Open `kimi-code`，复制 §「可复制块」到新会话。

## 顺序

1. **10**：R0–R5 思考 → 回填 task §4（本 Prompt）
2. **22**：`TEMPLATE-task-audit-invoke` 或 `22-task-audit.md`
3. meta：图谱 skeleton（**30 前**）→ **30** 改码 → partial 关账
4. issue 回复 · commit · 上游 PR

## 当前进度

- [x] GATE_VERIFY 双终端验证（Claude + Kimi · 未签闸 STOP）→ [`VALIDATION_30_gate_verify_claude_kimi_20260613.md`](./VALIDATION_30_gate_verify_claude_kimi_20260613.md)
- [x] 人签 `HG-TASK-DRAFT` + `HG-AUDIT-R1` · gate-check **exit 0**（2026-06-13）
- [x] issue 协调回复 → [`ISSUE_REPLY_94_20260613.md`](./ISSUE_REPLY_94_20260613.md)
- [x] 30 改码 · vitest 47 passed · PR [#708](https://github.com/MoonshotAI/kimi-code/pull/708) `Fixes #94`
- [x] meta 图谱 partial 关账 · task → `done/`（2026-06-13）

## invoke 索引

| 阶段 | 文件 |
|------|------|
| 10-task | [`PROMPT_kimi_agent_rethink_R1_R5.md`](./PROMPT_kimi_agent_rethink_R1_R5.md) |
| 20 R1 | [`task_fix_read_dual_limit_94_audit_R1_20260612.md`](../../reviews/task_fix_read_dual_limit_94_audit_R1_20260612.md) |
| 30 | [`invoke_20260613_30_fix-read-dual-limit-94.md`](./invoke_20260613_30_fix-read-dual-limit-94.md) |
| 复盘 | [`PROMPT_30_execution_audit.md`](./PROMPT_30_execution_audit.md) · [`SOLUTION_30_human_gate_bypass_v1_zh.md`](./SOLUTION_30_human_gate_bypass_v1_zh.md) |
