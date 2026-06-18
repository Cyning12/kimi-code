# Task：Read 双限同时触发时并列上报 MAX_LINES 与 MAX_BYTES · #94（阶段 C3）

> **状态**：`done` — 上游 PR OPEN，待 merge（与 C2 #583 同口径）  
> **审查**：[`task_fix_read_dual_limit_94_audit_R1_20260612.md`](../../harness/reviews/task_fix_read_dual_limit_94_audit_R1_20260612.md)（R1 通过 · 两闸 approved）  
> **上游 Issue**：[MoonshotAI/kimi-code#94](https://github.com/MoonshotAI/kimi-code/issues/94) · issue 回复 [`ISSUE_REPLY_94_20260613.md`](../../harness/invokes/by-task/fix-read-dual-limit-94/ISSUE_REPLY_94_20260613.md)  
> **上游 PR**：[MoonshotAI/kimi-code#708](https://github.com/MoonshotAI/kimi-code/pull/708)  
> **关联图谱**：[`10_flow_read_tool.md`](../../_tech_graph/10_flow_read_tool.md) · [`01_struct.md`](../../_tech_graph/01_struct.md) `agent_core`  
> **扫描分级**：工作区 `Projects/docs/harness/guides/ISSUE_SCAN_kimi_code_open_c2_v1_zh.md` v1.4.3  
> **试点真值**：`[docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)`

---

## Harness 元信息


| 字段                        | 值                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **task_slug**             | `fix-read-dual-limit-94`                                                                                                        |
| **test_strategy**         | `required`                                                                                                                      |
| **test_strategy_note**    | 先红后绿：`read.test.ts` 双限场景须同时含两行上限文案                                                                                              |
| **code_quality_bar**      | `strict`                                                                                                                        |
| **track**                 | `bugfix`（跳过 10-spec）                                                                                                            |
| **orchestration**         | **10-task**（R0–R5）→ **20** → **30** · V2                                                                                        |
| **entry_invoke_10_task**  | `[PROMPT_kimi_agent_rethink_R1_R5.md](../../harness/invokes/by-task/fix-read-dual-limit-94/PROMPT_kimi_agent_rethink_R1_R5.md)` |
| **entry_invoke_00_draft** | 工作区 `docs/harness/prompts/PROMPT_00_draft_spec_or_task_v1_zh.md`                                                                |
| **audit_profile**         | `human_only`                                                                                                                    |
| **git_branch**            | `feature/fix-94-read-dual-limit`                                                                                                |
| **worktree_root**         | `/Users/cyning/Desktop/Projects/kimi-code`                                                                                      |
| **meta_worktree**         | `/Users/cyning/Desktop/Projects/kimi-code-meta`                                                                                 |
| **module_id**             | `agent_core`                                                                                                                    |
| **graph_delta**           | `10_flow_read_tool`                                                                                                             |
| **graph_delta_note**      | —                                                                                                                               |
| **graph_gate**            | `skeleton_before_30` · `close_partial_or_final`                                                                                 |


### 人工闸


| human_gate_id | status   | blocks_hats | 说明                                      |
| ------------- | -------- | ----------- | --------------------------------------- |
| HG-TASK-DRAFT | approved | 20-R1, 30   | §4 + skeleton（签闸前勿 30）                  |
| HG-AUDIT-R1   | approved | 30          | 20 R1 + 人签 · harness GATE_VERIFY sync 后 |


---

## 1. 需求摘要（来自 #94）

Read 同时触发 `MAX_LINES`（1000）与 `MAX_BYTES`（100 KiB）时，`<system>` 状态只报行数上限；根因 `finishMessage` 的 `else if` 链。


| 方          | 说明                                               |
| ---------- | ------------------------------------------------ |
| **issue**  | jiang1997 分支就绪未 PR · #98/#99 撤回 · #216 关闭未 merge |
| **ktwu01** | 2026-06-10 确认 `main` 未修；**2026-06-13 issue 协调回复已发**（见 invoke `ISSUE_REPLY_94_20260613.md`） |


### 图谱交付


| 时点       | 交付                                                      |
| -------- | ------------------------------------------------------- |
| **30 前** | `10_flow_read_tool` skeleton + `00_main` + `02_version` |
| **关账**   | flow partial · invoke                                   |


---

## 2. 非范围

- Read 其它路径大改 · ReadMediaFile
- harness / task 进上游 PR

---

## 3. 失败路径


| 触发条件                           | 系统行为       | 可重试 |
| ------------------------------ | ---------- | --- |
| 无 §4 交接物 / 无 invoke PROMPT     | 10 **拒开工** | 是   |
| `graph_delta≠none` 且无 skeleton | 30 **拒开工** | 是   |
| §5 未完成即 30                     | 拒开工        | 是   |
| PR 已开但 meta 无图谱关账              | 不得 `done/` | 是   |


---

## 4. 给 10-task 交接物（00 起草 · V2）

> **分工**：**00 相位**落盘 §4 + invoke；**不**填 §5。链式时读本节组 Handoff → **派发 10-task**。  
> **单人模式**：Open `kimi-code`，复制 `entry_invoke_10_task` 内 ````text` 块。


| 字段              | 值                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **帽子**          | **10-task**（`track: bugfix` · 无 10-spec）                                                                                        |
| **Open Folder** | `kimi-code`                                                                                                                     |
| **invoke**      | `[PROMPT_kimi_agent_rethink_R1_R5.md](../../harness/invokes/by-task/fix-read-dual-limit-94/PROMPT_kimi_agent_rethink_R1_R5.md)` |
| **回填协议**        | `[FRAGMENT_rethink_backfill_task_v1_zh.md](../../harness/FRAGMENT_rethink_backfill_task_v1_zh.md)`                              |
| **10-task 真值**  | 工作区 `docs/harness/prompts/10-task-requirements.md`                                                                              |


### 必读路径（`@` 自 `kimi-code` 根）


| 路径                                                                                                     | 用途                  |
| ------------------------------------------------------------------------------------------------------ | ------------------- |
| `../kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md`                                | 读本 task · **回填 §5** |
| `../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.md`                                              | 图谱 partial / R5 核对  |
| `../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.ai.md`                                           | 双轨 flowchart        |
| `../kimi-code-meta/docs/_tech_graph/01_struct.md`                                                      | `agent_core`        |
| `packages/agent-core/src/tools/builtin/file/read.ts`                                                   | R1 · finishMessage  |
| `packages/agent-core/test/tools/read.test.ts`                                                          | R3/R4 测试面           |
| [https://github.com/MoonshotAI/kimi-code/issues/94](https://github.com/MoonshotAI/kimi-code/issues/94) | Issue 原文            |


### 禁止（10 会话）

- 改 `packages/**`、`apps/**`、`.changeset`
- `git commit` / `git push`

### 10-task 产出（交给 20）

- §5 各轮回填 + **思考轮控制**（无裸 `（待填）`）
- 可选：`invoke_*_rethink_*.md` 快照
- **不**签发 `HG-AUDIT-R1`

### 00 Handoff 最小字段（链式时由 00 从本节抽取）

```text
hat_code: 10-task
task_path: kimi-code-meta/docs/tasks/done/task_fix_read_dual_limit_94_v1.md
read_paths: 见上表「必读路径」
forbidden: 产品代码 · commit
output_shape: task §5 回填 + 思考轮控制
entry_invoke: docs/harness/invokes/by-task/fix-read-dual-limit-94/PROMPT_kimi_agent_rethink_R1_R5.md §可复制块
```

---

## 5. Kimi Code Agent · 思考轮次（10 回填 · R0+R1–R5）

### 思考轮控制


| 字段                    | 值                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **actual_last_round** | R5                                                                                                                                                                |
| **early_stop**        | false                                                                                                                                                             |
| **early_stop_reason** | —                                                                                                                                                                 |
| **residual_risks**    | ① 上游 PR [#708](https://github.com/MoonshotAI/kimi-code/pull/708) 待 merge。② jiang1997 分支已 issue 协调，避免重复 PR。 |


### R0 · 读 task

```text
【需求】#94：Read 同时触发 MAX_LINES(1000) 与 MAX_BYTES(100 KiB) 时，<system> 状态只报行数上限；根因 finishMessage 的 else if 链吞掉 bytes 文案。

【双限 repro 思路】构造 ≥1001 行、每行足够长（如 200 字符）的文本：readForward 先触发行数上限收集 1000 行（maxLinesReached=true），渲染累计字节时再触字节上限（maxBytesReached=true）；修复前 status 仅含 "Max 1000 lines reached."。

【图谱交付】graph_delta=10_flow_read_tool；PILOT §5.2：30 前 skeleton（✅ meta 已有）· 关账 partial（✅ 2026-06-12）。

【非范围】Read 其它路径大改 · ReadMediaFile · harness/task 进上游 PR。

【协调方】jiang1997 称分支就绪未开 PR；ktwu01 2026-06-10 复核 upstream/main 仍未修，建议开 PR 前 issue 回复；#98/#99 已撤回 · #216（kermanx）关闭未 merge。

【工作树】kimi-code 当前在 main、working tree clean；修复草稿在 feature/fix-94-read-dual-limit，与 task git_branch 一致。
```

### R1 · 代码事实

```text
【upstream/main ≡ 本地 main · 禁止方案】

readForward（read.ts L271–347）
- 扫描 kaos.readLines：selectedEntries 达 effectiveLimit 且 effectiveLimit≥MAX_LINES → maxLinesReached=true（L297–300、L291–293 续扫分支）。
- 渲染循环独立维护 bytes / maxBytesReached：下一行加入会超 MAX_BYTES 或累计达上限 → break（L322–334）。
- 两 flag 可同时为 true，经 finishReadResult 传入 finishMessage。

readTail（L350–421）
- maxLinesReached 恒 false（L415）；仅 bytes 路径设 maxBytesReached（L387–401）。
- 双限 bug 仅影响 readForward + finishMessage，tail 单 bytes 路径本就只报 bytes。

finishMessage（L436–461 · bug 点）
- L447–452：if (maxLinesReached) … else if (maxBytesReached) … else if (lineCount < requestedLines) EOF
- 双限时 bytes 分支永不执行；EOF 亦被 else if 挡住（双限时通常无 "End of file reached."，但语义依赖互斥链，不稳健）。

finishOutput（L430–433）
- renderedLines.join('\n') + '\n<system>' + message + '</system>'；status 与正文分离。

read.test.ts（main · 46 passed）
- 单限行数：caps default reads at MAX_LINES、reads through bounded byte preflight…
- 单限字节：checks the byte cap before adding the next rendered line、tail byte truncation…
- 无「双限同时命中」用例。

【fork feature/fix-94-read-dual-limit vs upstream/main】
- read.ts：else if → 两个独立 if；EOF 改为 !maxLinesReached && !maxBytesReached && lineCount < requestedLines（+4 行逻辑）。
- read.test.ts：+it('reports both line and byte caps when both limits are hit')（13 行）。
- .changeset/fix-read-dual-limit-status.md：agent-core + kimi-code patch，Fixes #94。
- 单提交 602cec16。
```

### R2 · 方案对比

```text
| 方案 | 内容 | 评价 |
|------|------|------|
| A | 仅改 finishMessage：maxBytesReached 与 EOF 从 else if 改为独立 if + 显式否定守卫 | ✅ 推荐 |
| B | 抽取 status 构建器 / 枚举截断原因 | 弃选：bugfix track、改动面大、无额外收益 |
| C | 拒工等 jiang1997 开 PR | 弃选：ktwu01 已证 main 未修；fork 已有可复现修复与测试，延误无必要 |

【推荐 A 理由】
- 与 readForward 双 flag 语义对齐（收集与渲染已独立设 flag，status 应独立追加文案）。
- diff 极小（read.ts 6 行语义变更），回归面可控。
- fork 分支已落地，与图谱 partial 描述一致。

【与 #98/#216 关系】
- #98/#99 撤回、#216 关闭未 merge，不构成合并阻塞；本修复以独立 if 为准，PR 前在 #94 说明 fork 方案与协调意图即可，避免多方重复 PR。
```

### R3 · 边界 / 测试

```text
| 场景 | maxLines | maxBytes | 期望 status 片段 | 现有覆盖 |
|------|----------|----------|------------------|----------|
| 仅行数 | true | false | Max 1000 lines reached. | caps default reads at MAX_LINES 等 |
| 仅字节 | false | true | Max 102400 bytes reached. | checks the byte cap…、tail byte truncation… |
| 双限（forward） | true | true | 两行上限文案并列；无 End of file reached. | fork 新用例（main 缺失） |
| EOF 守卫 | false | false | End of file reached.（lineCount < requestedLines） | reads text content…、empty file 等 |
| 双限+EOF 误报 | true | true | 不得出现 End of file reached. | 新用例 expect(output).not.toContain |
| tail 模式 | false | * | 仅 bytes（或无 Max） | tail byte truncation、tail n_lines… |
| 行内截断 | * | * | Lines [n] truncated. 独立于上限链 | truncates long lines… |
| ReadMediaFile | — | — | 不触及 | 现有 image/video/NUL 用例隔离 |

【回归要点】
- A 方案不改变 readForward/readTail 截断行为，只改 status 文案组合。
- EOF 显式否定防止未来若两 flag 与「短于请求行数」并存时的误报（当前双限路径 lineCount 通常等于 effectiveLimit）。
- truncated / mixed line endings 在 finishMessage 末尾追加，与上限 if 无关，无回归风险。
```

### R4 · 测试与 PR 策略

```text
【先红后绿】
1. 从 upstream/main 切 feature/fix-94-read-dual-limit（或复用现有 602cec16）。
2. 先仅加双限 vitest → main 上应 FAIL（仅有 lines 文案或缺 bytes 断言）。
3. 再合入 finishMessage 独立 if → 全绿。

【用例表 · 双限（新增）】
| 字段 | 值 |
|------|-----|
| 用例名 | reports both line and byte caps when both limits are hit |
| 输入 | path=/tmp/dual-limit.txt；默认 line_offset/n_lines |
| 夹具 | MAX_LINES+1 行，每行 'x'.repeat(200) |
| 断言 | output 含 `Max ${MAX_LINES} lines reached.` 且 `Max ${MAX_BYTES} bytes reached.` 且不含 `End of file reached.` |

【验证命令】
cd /Users/cyning/Desktop/Projects/kimi-code/packages/agent-core
pnpm test test/tools/read.test.ts

【PR 边界 · git diff upstream/main 纪律】
- 允许：packages/agent-core/src/tools/builtin/file/read.ts
- 允许：packages/agent-core/test/tools/read.test.ts
- 允许：.changeset/fix-read-dual-limit-status.md（patch · agent-core + kimi-code bundle）
- 禁止：apps/**、其它 packages、meta/harness 进上游 PR

【PR 元数据】
- 标题：fix(read): report both MAX_LINES and MAX_BYTES caps when both are hit
- 正文：Fixes MoonshotAI/kimi-code#94；简述 else if → 独立 if + EOF 守卫
- 分支：feature/fix-94-read-dual-limit → upstream/main
- 开 PR 前：在 #94 回复 @ktwu01 / @jiang1997，说明 fork PR 意图与 diff 范围，避免重复
```

### R5 · 图谱 + 协调 + 关账判断

```text
【10_flow_read_tool partial】✅ 完整
- 人类版 + .ai.md 双轨语义等价；#94 切片表（upstream bug vs fork fix）；常量契约；主路径 mermaid；代码锚点清单已勾选。
- 00_main.md L22/L36 已链入；02_version.md 2026-06-12 条目已记。
- 锚点 L447–455 描述 fork 态 finishMessage，与 602cec16 一致（upstream 仍为 else if）。

【issue #94 回复建议（PR 前）】
> 已在 fork `feature/fix-94-read-dual-limit` 落地修复：finishMessage 将 maxBytesReached 从 else if 改为独立 if，EOF 增加双 flag 否定守卫；新增双限 vitest。计划向 upstream 提 PR（Fixes #94）。若 @jiang1997 另有分支，可对比合并，避免重复。

【关账判断】
- §5 思考轮：R0–R5 闭合 → 可进入 20 人签（HG-AUDIT-R1）→ 30 改码/提 PR。
- 图谱：skeleton + partial 已满足 graph_gate；关账无需再扩 scope。
- 判定：【可 30】（非 early_stop；待 HG-AUDIT-R1 approved 后执行）。
```

---

## 6. 验收标准（关账）

- [x] §5 闭合 · `HG-AUDIT-R1` approved（2026-06-13）
- [x] vitest 绿（47 passed）· 图谱 partial 关账 · 上游 PR [#708](https://github.com/MoonshotAI/kimi-code/pull/708) `Fixes #94`

---

## 7. 给 30 帽必读（`HG-AUDIT-R1` 后 · 另开会话）

1. 仓根 `AGENTS.md`
2. 本 task §1 + **§5 结论**
3. `@../kimi-code-meta/docs/_tech_graph/01_struct.md`
4. `@../kimi-code-meta/docs/_tech_graph/10_flow_read_tool.md`（skeleton 已 meta commit）
5. Issue #94
6. `[PROMPT_kimi_agent_rethink_R1_R5.md](../../harness/invokes/by-task/fix-read-dual-limit-94/PROMPT_kimi_agent_rethink_R1_R5.md)` §「30 开工」· `[30-execute-code.md](../../harness/prompts/30-execute-code.md)`

---

## 8. 验证命令

```bash
cd /Users/cyning/Desktop/Projects/kimi-code/packages/agent-core
pnpm test test/tools/read.test.ts
```

---

## 9. 实现备忘（30 回填）


| 项                   | 状态      | 备注                                                                            |
| ------------------- | ------- | ----------------------------------------------------------------------------- |
| §4 给 10-task        | ✅       | invoke 已落盘                                                                    |
| 图谱 skeleton/partial | ✅       | meta 已落盘                                                                      |
| §5 思考轮              | ✅       | R0–R5                                                                         |
| 20 R1               | ✅       | R1 通过 · 2026-06-13 签闸                                                              |
| 人工闸                 | approved | gate-check **exit 0**（2026-06-13）                                              |
| issue 回复            | ✅       | 2026-06-13 · `ISSUE_REPLY_94_20260613.md`                                        |
| 30 改码               | ✅       | commit `602cec16` · vitest 47 passed                                              |
| harness 纪律          | ✅       | GATE_VERIFY 双终端验证见 invoke `VALIDATION_30_gate_verify_claude_kimi_20260613.md` |
| 上游 PR               | ✅       | [#708](https://github.com/MoonshotAI/kimi-code/pull/708) · `Fixes #94` · OPEN     |

### 关账自检（2026-06-13）

| 命令 | cwd | 退出码 | 摘要 |
|------|-----|--------|------|
| `pnpm test test/tools/read.test.ts` | `packages/agent-core` | **0** | **47 passed** |

**可关账** — 待 upstream PR merge。


