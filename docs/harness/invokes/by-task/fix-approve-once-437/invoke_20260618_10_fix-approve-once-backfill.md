# Invoke 快照 · 10 任务分析 / 思考轮回填 · fix-approve-once-437

| 元信息 | 值 |
|--------|-----|
| **日期** | 2026-06-18 |
| **analyst_hat** | `10-requirements` / 10-task |
| **轮次** | R0–R5 回填（承接 22 R1 退回 · B1） |
| **task** | [`docs/tasks/active/task_fix_approve_once_437_v1.md`](../../../../tasks/active/task_fix_approve_once_437_v1.md) |
| **启动 Prompt** | [`PROMPT_START_10_v1.md`](./PROMPT_START_10_v1.md) |
| **Open Folder（读码）** | `kimi-code/` · `feature/fix-437-approve-once-clean` · `98f1fa5f` |
| **Open Folder（写 task）** | `kimi-code-meta/` · 分支 `cyning/meta` |
| **22 退回依据** | [`task_fix_approve_once_437_v1_audit_R1_20260618.md`](../../reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md) |

---

## User 消息（触发 · 全文）

```text
你是 **10 任务分析 Agent**（#437 Approve once vs session · 思考轮回填 · 承接 22 R1 退回）。

【开帽 · GATE_SCAN · 缺一 STOP】
- HG-TASK-DRAFT: **approved** ✓（2026-06-18）
- HG-AUDIT-R1: **pending**（10 不代签 · 不附 30 Prompt）
- Open Folder（读码）: **kimi-code/** · `feature/fix-437-approve-once-clean` 或 upstream/main + 只读 diff `98f1fa5f`
- Open Folder（写 task）: **kimi-code-meta/** · `cyning/meta`
- cwd 写 task: kimi-code-meta/ 仓根
- **禁止** 改 packages/** · apps/** 产品代码
- **禁止** git commit / push（除非 user 明确要求）
- **禁止** 开上游 PR · changeset · graph:issue-sync 关账（30/40 帽）
- **禁止** 仅聊天输出结论就结束 — **必须** 编辑 task §5

真值帽规：
- docs/harness/prompts/10-requirements.md
- docs/harness/FRAGMENT_rethink_backfill_task_v1_zh.md
- docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md（22 退回清单 · residual_risks 验收口径）
- docs/tasks/TASK_TEMPLATE_upstream_pr_v1.md §5（R0–R5 结构）

读序（@ 相对 kimi-code 或 kimi-code-meta）：
1. ../kimi-code-meta/docs/tasks/active/task_fix_approve_once_437_v1.md（§1–§8 · 当前 §5 待填）
2. ../kimi-code-meta/docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md（B1 阻塞 · 需 10 回填清单）
3. ../kimi-code-meta/docs/_tech_graph/10_flow_cli_session.graph.yaml
4. https://github.com/MoonshotAI/kimi-code/issues/437（Issue + comment 复现）
5. packages/agent-core/src/agent/permission/index.ts（resolveSessionApprovalRule · recordApprovalResult）
6. packages/agent-core/src/agent/permission/policies/session-approval-history.ts
7. packages/agent-core/test/agent/permission.test.ts（#437 Write 用例 · Bash session 用例）
8. apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts · controller.ts · handler.ts
9. apps/kimi-code/test/tui/reverse-rpc/approval-adapter.test.ts

10 交付（mandatory · 写 task 文件）：
- 扩展 task §5 为 TASK_TEMPLATE §5 完整形态（R0–R5 + 思考轮控制）
- 回填 actual_last_round / early_stop / residual_risks
- 可选 §8 备注列 aspirational → 可审计表述
```

---

## 开帽 GATE_SCAN（执行时）

| gate | status | 说明 |
|------|--------|------|
| HG-TASK-DRAFT | approved | 2026-06-18 |
| HG-AUDIT-R1 | pending | 10 不代签 |
| 产品代码 | 未改 | 只读 `98f1fa5f` |
| git commit | 未执行 | 按帽规 |

---

## 只读交叉验证摘要

| 项 | 结果 |
|----|------|
| 产品干净分支 | `feature/fix-437-approve-once-clean` · 单 commit `98f1fa5f` · 2 文件 |
| 脏分支警示 | `feature/fix-437-approve-once` · `eedd430c` + 可能含 #94 read |
| task §5 | 已回填 R0–R5 · `actual_last_round=R5` |

---

## 产出

- task §5 思考轮闭合：[`task_fix_approve_once_437_v1.md`](../../../../tasks/active/task_fix_approve_once_437_v1.md)
- 下一棒：22 R1 复审 · [`PROMPT_START_22_v1.md`](./PROMPT_START_22_v1.md)
