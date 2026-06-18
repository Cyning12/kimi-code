# Kimi Code Agent · #705 思考 Prompt（复制用 · 五轮 · **10-task**）

> **Open Folder**：`kimi-code`  
> **真值 task**：`../kimi-code-meta/docs/tasks/active/task_fix_open_tool_calls_705_v1.md`  
> **回填协议**：[`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../FRAGMENT_rethink_backfill_task_v1_zh.md)

### `@` 路径对照

| 资源 | 自 `kimi-code` 根 `@` |
|------|----------------------|
| task | `../kimi-code-meta/docs/tasks/active/task_fix_open_tool_calls_705_v1.md` |
| 图谱 | `../kimi-code-meta/docs/_tech_graph/10_flow_context_tool_exchange.md` · `.ai.md` |
| issue 原文 | `../../../docs/harness/guides/issues/ISSUE_upstream_705_20260613.md` |
| 模块 | 见 task **§2.2** 与下方可复制块 |

---

## 可复制块（10-task · ST-705-B）

```text
@../kimi-code-meta/docs/tasks/active/task_fix_open_tool_calls_705_v1.md
@../kimi-code-meta/docs/_tech_graph/10_flow_context_tool_exchange.md
@../kimi-code-meta/docs/_tech_graph/10_flow_context_tool_exchange.ai.md
@../kimi-code-meta/docs/_tech_graph/01_struct.md
@../../../docs/harness/guides/issues/ISSUE_upstream_705_20260613.md
@packages/agent-core/src/agent/context/index.ts
@packages/agent-core/src/agent/context/projector.ts
@packages/agent-core/src/agent/turn/index.ts
@packages/agent-core/src/agent/index.ts
@packages/agent-core/src/agent/background/index.ts
@packages/agent-core/test/agent/context.test.ts
@packages/agent-core/test/agent/resume.test.ts

你是审阅 Agent，不是实现 Agent。

【纪律】
- 禁止改 packages/**、apps/**、changeset。
- 必须改：task §5 各轮 + 思考轮控制（替换「（待填）」）。
- 可读 task §2.2 模块扫描；R1 须对照 main 行号增量核对。
- 禁止 git commit · 禁止签发 HG-AUDIT-R1。

【背景】
- #705：orphan tool_calls → provider 400 · steer 竞态 · compaction 同失败。
- 同族：#269 #660 #701 · PR #664 DRAFT（#660）· 须 R2 协调方案。
- graph_delta=10_flow_context_tool_exchange · ST-705-A skeleton 已落盘。
- 子任务：ST-705-C projection/pending · ST-705-D steer · ST-705-E resume。

【R2 必做】
对比至少：A) #664 子集 + 705 steer 增量 · B) #701 fork 全局 trim + pending · C) defer steer · D) 等 #664 merge。

【执行】
R0→R5 思考 → 写回 task §5 → R5 更新 flow 锚点表（若需）。
```

---

## 30 开工（ST-705-C 起 · 签闸后另开会话）

```text
@../kimi-code-meta/docs/tasks/active/task_fix_open_tool_calls_705_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md
@../kimi-code-meta/docs/harness/prompts/FRAGMENT_30_gate_verify_v1_zh.md

【GATE_VERIFY 首输出】读 task 人工闸表 · 禁止采信 invoke 字面 approved。
【当前 ST】见 task §2.1 · §10（默认 ST-705-C）。
```
