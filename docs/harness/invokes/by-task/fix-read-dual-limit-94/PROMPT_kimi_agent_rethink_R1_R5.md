# Kimi Code Agent · #94 思考 Prompt（复制用 · 五轮 · **10-task**）

> **Open Folder**：`kimi-code`（产品仓）  
> **真值 task**（meta）：`../kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md`  
> **回填协议**：[`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../FRAGMENT_rethink_backfill_task_v1_zh.md)（**mandatory**）

### `@` 路径对照

| 资源 | 自 `kimi-code` 根 `@` |
|------|----------------------|
| task（**须回填**） | `../kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md` |
| 图谱 | `../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.md` · `10_flow_read_tool.ai.md` |
| 上游 Issue | https://github.com/MoonshotAI/kimi-code/issues/94 |
| 源码 | 见下方可复制块 |

---

## 推荐：一次会话 · 思考 + **写回 task**

**禁止**仅在聊天里输出结论就结束。完成思考后 **必须编辑 task §4 回填区** + **思考轮控制** 表。

| 结束方式 | 写法 |
|----------|------|
| 提前停止 | 该轮末 `【停止 · 原因】`；仍须回填已完成的轮次到 task |
| 需更多轮 | `【需更多轮 · 提纲】`；回填已完成轮 + R5 提纲写入 task |

```text
@../kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md
@../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.md
@../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.ai.md
@../kimi-code-meta/docs/_tech_graph/01_struct.md
@packages/agent-core/src/tools/builtin/file/read.ts
@packages/agent-core/test/tools/read.test.ts

你是审阅 Agent，不是实现 Agent。

【纪律】
- 禁止改 packages/**、apps/** 等产品代码（含 read.ts · 测试 · changeset）。
- 允许且必须改：../kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md **§5** 各轮回填区 + 思考轮控制（把「（待填）」换成结论）。§4 为交接物只读。
- 允许改图谱 meta：../kimi-code-meta/docs/_tech_graph/10_flow_read_tool*.md（若 R5 发现锚点/表需补）。
- 禁止 git commit。

【背景 · 必读】
- #94：双限同时触发时 finishMessage 只报 MAX_LINES，MAX_BYTES 被 else if 吞掉。
- ktwu01 2026-06-10 复核 main 仍存在；jiang1997 称分支就绪未开 PR；#98/#99 协调撤回 · #216 kermanx 关闭未 merge。
- graph_delta=10_flow_read_tool；PILOT §5.2：30 前 skeleton · 关账 partial。
- 若 fork 已有本地修复：R1 须对照 **upstream/main** 与 fork 差异陈述，R4/R5 仍须写测试表与 PR/协调策略，不得跳过。

【执行顺序】
1) 按 R0→R5 思考（可提前停或需更多轮）。
2) 将每轮结论写入 task **§5** 对应「回填区」；更新思考轮控制。
3) 本回复末尾输出「## 回填自检」表 +「回填完成 · 未 commit · 未改产品代码」。

---

## R0 · 读 task + Issue #94
（要点：双限 repro · finishMessage · 图谱交付时点 · 非范围 · 协调方 jiang1997/ktwu01）

## R1 · 代码事实（禁止方案）
（readForward L271–347 双 flag · readTail bytes 路径 · finishMessage L436–461 · finishOutput system 标签 · 现有 read.test.ts 单限用例）

## R2 · 方案对比
（A 仅改 finishMessage else if→if · B 重构 status 构建器 · C 拒工等原作者 · 推荐 + 弃选理由 · 与 #98/#216 diff 关系）

## R3 · 边界与回归
（仅 lines / 仅 bytes / 双限 / EOF 守卫 · tail 模式 · truncated 行 · 不影响 ReadMediaFile）

## R4 · 测试与 PR 边界（须含用例表 + pnpm 命令）
（先红后绿 · 双限 vitest 断言文案 · changeset · git diff upstream/main 路径纪律 · Fixes #94）

## R5 · 图谱 + 协调 + 关账判断
（10_flow_read_tool partial 是否完整 · 00_main/02_version · issue 回复建议 · 可30 / 【停止】/ 【需更多轮】）

---

若无法编辑 meta task，输出 ## BACKFILL_PACK 供维护者粘贴。
```

---

## 30 开工（签闸后 · 另开会话 · 见 FRAGMENT_30_invoke_block）

```text
@../kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md
@../kimi-code-meta/docs/harness/prompts/FRAGMENT_30_gate_verify_v1_zh.md
@../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.md

【GATE_VERIFY 首输出】读 task 人工闸表 · 禁止采信「已 approved」字面句。
【签闸后】gate-check.sh --target .. --task docs/tasks/done/task_fix_read_dual_limit_94_v1.md
分支 feature/fix-94-read-dual-limit · 先红后绿 · 仅 packages/agent-core + .changeset · Fixes #94
```
