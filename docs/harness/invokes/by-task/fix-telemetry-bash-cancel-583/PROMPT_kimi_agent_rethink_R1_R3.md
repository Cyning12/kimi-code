# Kimi Code Agent · #583 思考 Prompt（复制用）

> **Open Folder**：`kimi-code`（产品仓）  
> **真值 task**（meta）：`../kimi-code-meta/docs/tasks/done/task_fix_telemetry_bash_cancel_583_v1.md`  
> **回填协议**：[`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../FRAGMENT_rethink_backfill_task_v1_zh.md)

### `@` 路径对照（勿混仓）

| 资源 | 自 `kimi-code` 根 `@` | 自 `kimi-code-meta` 根 `@`（备选） |
|------|----------------------|-------------------------------------|
| task | `../kimi-code-meta/docs/tasks/done/task_fix_telemetry_bash_cancel_583_v1.md` | `docs/tasks/done/task_fix_telemetry_bash_cancel_583_v1.md` |
| 源码 | `packages/agent-core/src/...` | `../kimi-code/packages/agent-core/src/...` |

---

## 推荐：一次会话 · 思考 + **写回 task**（可提前结束）

**禁止**仅在聊天里输出结论就结束；须 **编辑 task §4 回填区**（历史 task 若已填满则写入 invoke 快照即可）。

```text
@../kimi-code-meta/docs/tasks/done/task_fix_telemetry_bash_cancel_583_v1.md
@packages/agent-core/src/agent/turn/index.ts
@packages/agent-core/src/loop/tool-call.ts
@packages/agent-core/src/utils/abort.ts

你是审阅 Agent。禁止改产品代码；必须按 FRAGMENT 回填 task §4 或 invoke 快照。
禁止 git commit。

【执行顺序】
1) R0→R1→R2→R3（可提前停，见下表）。
2) 将结论写入 task §4 回填区（替换（待填））；若 §4 已填满则写 invoke_`*_rethink_*.md`。
3) 回复末尾：## 回填自检 + 回填完成 · 未 commit。

| 可提前停止 | 条件 |
| R1 后 | issue 与代码不符 / 需澄清 — 不可因 obvious 跳过 R2 |
| R2 后 | 须在 task 或回复中含完整测试表 + pnpm 命令 |
| 最低 | R0+R1 + 可执行测试计划 |

## R0 · 读 task
## R1 · 代码事实
## R2 · 方案对比
## R3 · 测试与 PR 边界

若无法写文件：输出 ## BACKFILL_PACK。
```

---

## 30 开工（签闸后 · 另开会话）

```text
@../kimi-code-meta/docs/tasks/done/task_fix_telemetry_bash_cancel_583_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md

task §4 已无（待填）；HG-AUDIT-R1 approved。Fixes #583。
```
