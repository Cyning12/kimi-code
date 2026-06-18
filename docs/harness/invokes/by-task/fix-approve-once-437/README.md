# Invoke · fix-approve-once-437

| 项 | 值 |
| --- | --- |
| **task** | [`docs/tasks/done/task_fix_approve_once_437_v1.md`](../../../../tasks/done/task_fix_approve_once_437_v1.md) |
| **issue** | [MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437) |
| **产品分支** | `feature/fix-437-approve-once-clean`（建议从 `upstream/main`） |
| **图谱** | `10_flow_cli_session.graph.yaml` · `10_flow_agent_turn.graph.yaml`（备注） |

## 启动

| 帽 | 文件 |
| --- | --- |
| **10 思考轮回填** | [`PROMPT_START_10_v1.md`](./PROMPT_START_10_v1.md)（22 R1 退回 · 补 §5） |
| **22 任务审核** | [`PROMPT_START_22_v1.md`](./PROMPT_START_22_v1.md) |
| **30 产品** | [`PROMPT_START_30_v1.md`](./PROMPT_START_30_v1.md)（须 **HG-AUDIT-R1 approved**） |

## 进度

- [x] meta skeleton YAML（`cyning/meta` · `e08a56b2`）
- [x] 产品修复草稿 `eedd430c`（须 cherry-pick 到干净分支）
- [x] `graph:issue-sync` L1+L2+L3 PASS
- [x] 维护者签 **HG-AUDIT-R1**（2026-06-18）
- [x] 30 G0–G2 上游 PR [#901](https://github.com/MoonshotAI/kimi-code/pull/901) · G3 关账 · task → `done/`
