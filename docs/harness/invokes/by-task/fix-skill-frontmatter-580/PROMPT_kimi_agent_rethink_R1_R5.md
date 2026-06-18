# Kimi Code Agent · #580 思考 Prompt（复制用 · 五轮）

> **Open Folder**：`kimi-code`（产品仓）  
> **真值 task**（meta）：`../kimi-code-meta/docs/tasks/active/task_fix_skill_frontmatter_580_v1.md`  
> **回填协议**：[`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../FRAGMENT_rethink_backfill_task_v1_zh.md)（**mandatory**）

### `@` 路径对照

| 资源 | 自 `kimi-code` 根 `@` |
|------|----------------------|
| task（**须回填**） | `../kimi-code-meta/docs/tasks/active/task_fix_skill_frontmatter_580_v1.md` |
| 图谱 skeleton | `../kimi-code-meta/docs/_tech_graph/10_flow_skill_load.md` |
| 源码 | 见 task §1 涉及文件列表 |

---

## 推荐：一次会话 · 思考 + **写回 task**

**禁止**仅在聊天里输出结论就结束。完成思考后 **必须编辑 task §4 回填区**。

| 结束方式 | 写法 |
|----------|------|
| 提前停止 | 该轮末 `【停止 · 原因】`；仍须回填已完成的轮次到 task |
| 需更多轮 | `【需更多轮 · 提纲】`；回填已完成轮 + R5 提纲写入 task |

```text
@../kimi-code-meta/docs/tasks/active/task_fix_skill_frontmatter_580_v1.md
@../kimi-code-meta/docs/_tech_graph/10_flow_skill_load.md
@packages/agent-core/src/profile/default/system.md
@packages/agent-core/src/skill/parser.ts
@packages/agent-core/src/skill/scanner.ts
@packages/agent-core/src/skill/types.ts

你是审阅 Agent，不是实现 Agent。

【纪律】
- 禁止改 packages/**、apps/** 等产品代码。
- 允许且必须改：../kimi-code-meta/docs/tasks/active/task_fix_skill_frontmatter_580_v1.md §4 各轮回填区（把「（待填）」换成结论）。
- 禁止 git commit。

参考 ktwu01：prompt 防 agent 写坏 skill；parser 放宽防用户 skill 被静默丢弃。
本 fork 暂不以 issue 作者 branch 为拒工理由；R5 写上游协调建议。

【执行顺序】
1) 按 R0→R5 思考（可提前停或需更多轮）。
2) 将每轮结论写入 task §4 对应「回填区」（替换（待填））。
3) 本回复末尾输出「## 回填自检」表 +「回填完成 · 未 commit」。

---

## R0 · 读 task + issue 要点
（思考要点：恶性循环 · 涉及文件 · ktwu01 验证）

## R1 · 代码事实（禁止方案）
（system.md · parser L107–145 · scanner · flat vs directory · 测试文件）

## R2 · 方案对比
（A prompt-only · B prompt+parser · C parser-only · 推荐 + 可选 R2-追加）

## R3 · 边界与回归

## R4 · 测试与 PR 边界（须含用例表 + pnpm 命令）

## R5 · 图谱 + 协调 + 关账判断
（可30 / 【停止】/ 【需更多轮】）

---

若无法编辑 meta task，输出 ## BACKFILL_PACK 供维护者粘贴。
```

---

## 30 开工（签闸后 · 另开会话）

```text
@../kimi-code-meta/docs/tasks/active/task_fix_skill_frontmatter_580_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md

确认 task §4 已无「（待填）」；HG-AUDIT-R1 approved。
先 vitest 红灯再实现。仅 packages/agent-core。Fixes #580。
```
