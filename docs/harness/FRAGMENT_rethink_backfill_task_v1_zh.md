# FRAGMENT · 思考轮结论回填 task（mandatory）

> 嵌入 `PROMPT_kimi_agent_rethink_*.md` 与 `TASK_TEMPLATE_upstream_pr_v1.md` §4。

## 问题

仅在本会话输出 `## R1 结论` **不算完成**；维护者需要 task §4 真值 + **思考轮控制** 表，22 才能审、才能签 `HG-AUDIT-R1`。

## 回填协议（Agent 必执行）

### 允许修改（仅此）

| 路径 | 操作 |
|------|------|
| `../kimi-code-meta/docs/tasks/active/<task>.md`（或 `done/`） | 写入 §4 各轮 **回填区** + **思考轮控制** |
| `docs/harness/invokes/by-task/<slug>/invoke_*_rethink_*.md` | 可选：整段思考快照 |

### 禁止

- `packages/**`、`apps/**` 等产品代码
- `git commit` / `git push`

### 步骤

1. 完成 R0～Rn 思考（默认槽位 **R0 + R1–R5**）。
2. 填写 **思考轮控制**：`actual_last_round` · `early_stop` · `early_stop_reason` · `residual_risks`。
3. **打开 task 文件**，在 §4 替换各轮 `（待填）`；**跳过轮**写 `（跳过 · 见思考轮控制）`。
4. 在本回复 **末尾** 输出回填自检表 + `回填完成 · 未 commit · 未改产品代码`。

### 无法写 meta 文件时

在回复末尾输出 `## BACKFILL_PACK`；并写：`⚠️ 未能写入 task 文件，请维护者粘贴或换 Open Folder 为 kimi-code-meta`。

## 提前停止 / 增轮

| 情况 | 必填 |
|------|------|
| **提前停止** | `early_stop=yes` · reason · `residual_risks`（无则 `none`） |
| **增 R6+** | 追加 `### R6 · …` + **扩展理由** |

**22 审查**：reason 不充分或 residual 未落入 §3/§5 → **退回 10 帽** 补思考后再 22 R+1。

## task §4 回填区标记

每轮：`### Rk` → `**回填区：**` → ` ```text ` 围栏内为结论或 `（跳过 · 见思考轮控制）`。
