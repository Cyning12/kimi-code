# Task：修复 Bash 取消时 tool_call telemetry 误分类 · #583（阶段 C2）

> **状态**：`done` — 上游 PR OPEN，待 merge（与 C1 #622 同口径：不等 merge 视为 C2 验证完成）  
> **上游 Issue**：[MoonshotAI/kimi-code#583](https://github.com/MoonshotAI/kimi-code/issues/583)  
> **上游 PR**：[MoonshotAI/kimi-code#630](https://github.com/MoonshotAI/kimi-code/pull/630)  
> **关联图谱**：`docs/_tech_graph/01_struct.md`（`agent_core`）· 增量 `10_flow_agent_turn`（C-图）  
> **扫描分级**：工作区 `Projects/docs/harness/guides/ISSUE_SCAN_kimi_code_open_c2_v1_zh.md`（首推本 issue）  
> **试点真值**：`[docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)`

---

## Harness 元信息


| 字段                     | 值                                                            |
| ---------------------- | ------------------------------------------------------------ |
| **task_slug**          | `fix-telemetry-bash-cancel-583`                              |
| **test_strategy**      | `required`                                                   |
| **test_strategy_note** | 先写/补 **vitest** 覆盖 `telemetryToolOutcome` 与用户取消路径；再改实现       |
| **code_quality_bar**   | `strict`                                                     |
| **orchestration**      | Cursor / Kimi Code Agent · **三轮思考后 30**                      |
| **audit_profile**      | `human_only`                                                 |
| **git_branch**         | `feature/fix-583-telemetry-cancel`                           |
| **worktree_root**      | `/Users/cyning/Desktop/Projects/kimi-code`（产品改码 Open Folder） |
| **meta_worktree**      | `/Users/cyning/Desktop/Projects/kimi-code-meta`              |


### 人工闸


| human_gate_id | status   | blocks_hats | 说明                        |
| ------------- | -------- | ----------- | ------------------------- |
| HG-TASK-DRAFT | approved | 22-R1, 30   | 维护者确认 task + R1～R3 已填     |
| HG-AUDIT-R1   | approved | 30          | 22 R1 落盘 + **三轮思考完成** 后人签 |


> `**HG-GRAPH-MODULES`** 已在 `01_struct` 签 `approved`。

---

## 1. 需求摘要（来自 #583）

### 问题

`tool_call` telemetry 的 `outcome` 由 **tool output 字符串** 推断（`telemetryToolOutcome`），导致：


| 场景                                        | 当前                | 期望                                       |
| ----------------------------------------- | ----------------- | ---------------------------------------- |
| Bash 用户中断，文案 `Interrupted by user`        | 记为 `error`        | 记为 `cancelled`                           |
| Bash 超时 `Command killed by timeout (...)` | 记为 `error`        | **维持 `error`**（本 task 默认；若改分类须在 R2 写明理由） |
| 真错误消息含 `aborted` / `cancelled` 等词         | 可能被记为 `cancelled` | 记为 `error`（且保留 `error_type`）             |


### 影响面

Issue 作者判断：**主要影响 telemetry 分布与 `error_type`**，未发现 UI/重试强依赖 `outcome`。实现时仍须 **rg 确认** 无隐藏消费者。

### 涉及代码（必读）


| 路径                                                    | 角色                                                        |
| ----------------------------------------------------- | --------------------------------------------------------- |
| `packages/agent-core/src/agent/turn/index.ts`         | `telemetryToolOutcome` · `tool.result` 事件处理               |
| `packages/agent-core/src/loop/tool-call.ts`           | `abortedToolOutput` · `isUserCancellation(signal.reason)` |
| `packages/agent-core/src/tools/builtin/shell/bash.ts` | Bash 中断/超时用户可见文案                                          |
| `packages/agent-core/src/utils/abort.ts`              | `isUserCancellation` 定义                                   |


### Issue 建议方向

1. **最小**：在 `telemetryToolOutcome` 增加字符串如 `interrupted`（**不推荐单独采用**，R2 须说明残留误分类风险）。
2. **推荐**：在 `tool.result` / 内部事件链传递 **结构化取消信号**，telemetry 读结构而非猜 output。

### 完成态（验收口径）

- [ ] 用户主动取消（`isUserCancellation`）→ telemetry `outcome: cancelled`
- [ ] 真实 tool 错误 → `outcome: error` 且 `error_type` 合理（不因 output 含 cancel 类词误判）
- [ ] Bash 超时 → 默认仍为 `error`（或 R2 书面选择 + 测试）
- [ ] **vitest** 覆盖上述分支（先红后绿）
- [ ] 上游 PR 仅 `packages/agent-core/`**（+ 必要 `.changeset`）；`Fixes #583`
- [ ] `git diff upstream/main --name-only` 无 harness / task 路径

---

## 2. 非范围

- 修改 SDK 对外 event 契约（除非 R2 证明最小改动必须且 maintainer 可接受）
- 其它 tool（非 Bash）的全面 telemetry 重构
- `docs/harness`、`.cursor`、本 task 进上游 PR
- 向 Moonshot PR 图谱增量（`10_flow_*` 只 commit 在 **meta**）

---

## 3. 失败路径


| 触发条件                  | 系统行为          | 可重试 |
| --------------------- | ------------- | --- |
| 未完成 R1～R3 即 30        | Agent **拒开工** | 是   |
| `HG-AUDIT-R1` pending | 30 拒开工        | 是   |
| 仅改字符串匹配、无结构化路径且无测试    | 22/50 应判不通过   | 是   |
| PR 含 `docs/tasks` 等   | 维护者拒合并        | 是   |


---

## 4. Kimi Code Agent · 思考轮次（**改码前 mandatory**）

> **推荐（一次会话）**：复制 `[PROMPT_kimi_agent_rethink_R1_R3.md](../../harness/invokes/by-task/fix-telemetry-bash-cancel-583/PROMPT_kimi_agent_rethink_R1_R3.md)` §「连续四轮」**一条发完**；Agent 按 R0→R1→R2→R3 顺序输出。  
> **可提前停止**：某轮末尾写 `【停止 · 原因】` 即不再输出后续轮次 — 但 **签闸前** 须有 R1 + **可执行测试计划**（完整 R3，或 R2 停止原因内已含测试表与 `pnpm` 命令）。  
> **禁止改码** 直至维护者签 `HG-AUDIT-R1` 并另开 30 会话。  
> 结论粘贴回本 task §4 回填区（或整段 invoke）→ **meta** commit。

### 复制用 · 总 Prompt（Round 0 · 读 task）

> **Open Folder = `kimi-code`**（非 meta）。task 在 meta 仓，须 `../kimi-code-meta/` 前缀。

```text
你是审阅 Agent，不是实现 Agent。阅读以下路径（只读，@ 自 kimi-code 根）：
@../kimi-code-meta/docs/tasks/active/task_fix_telemetry_bash_cancel_583_v1.md
@packages/agent-core/src/agent/turn/index.ts
@packages/agent-core/src/loop/tool-call.ts
@packages/agent-core/src/utils/abort.ts

确认你已理解 #583 需求。不要写代码。回复「已读 task，开始 R1」。
```

### Round 1 · R1 代码事实（数据流）

**Prompt：**

```text
【R1 · 仅事实 · 禁止方案与改码】

从 tool 执行中止到 telemetry.track('tool_call')，画出数据流：
1. 哪些路径设置 tool.result？AbortSignal 在哪传入？
2. Bash 用户中断 vs 超时的 output 字符串各是什么？
3. telemetryToolOutcome 当前精确逻辑（引用行号）？
4. 除 turn/index.ts 外，还有哪些读取 outcome / error_type？

输出格式：
## R1 结论
- 数据流：（bullet）
- 风险点：（bullet）
- 待 R2 决策的问题：（编号列表）
```

**回填区（Agent / 维护者填写）：**

## R1 结论

- **数据流**：
  - 用户 Stop / RPC cancel：`TurnFlow.cancel()` → `abortTurn()` → `controller.abort(reason)`，默认 `userCancellationReason()`（`UserCancellationError`，`abort.ts` L18–33）；`signal` 传入 `runTurn` → `runToolCallBatch(step)`（`tool-call.ts` L69、L556–561）。
  - 中止 settle：`tool-call.ts` 在 `signal.aborted` / `isAbortError` 时调用 `abortedToolOutput(toolName, signal)`（L56–61、L301–302、L469–488）；用户取消输出含 `**manually interrupted`**。
  - Bash 实际执行：`bash.ts` 监听 abort；`timedOut` 优先 → 超时文案，否则 `aborted` → `**Interrupted by user**`（L320–328）。
  - 终端：`runToolCallBatch` dispatch `tool.result`（L150–155）→ `trackLoopTelemetry` → `trackToolLifecycle`（`turn/index.ts` L799–816）→ `telemetryToolOutcome(event.result)` → `telemetry.track('tool_call', …)`。
  - SDK 对外：`mapLoopEvent` 的 `tool.result` 仅 `output` / `isError`（L937–944），不含 outcome。
- **Bash 文案**：用户中断 `'Interrupted by user'`；超时 ``Command killed by timeout (${timeoutLabel})``（如 `2s`）。loop 层用户取消：`The user manually interrupted "…" …`；非用户 abort：`Tool "…" was aborted`。
- `**telemetryToolOutcome`（L1107–1114）**：`isError !== true` → `success`；否则 output 小写含 `aborted` / `cancelled` / `manually interrupted` → `cancelled`，否则 `error`。`error_type` 仅 `outcome === 'error'` 时由 `telemetryToolErrorType` 推断（L812–815）。
- **消费者（rg）**：**写入**仅 `turn/index.ts`；**读取**仅 `test/agent/turn.test.ts` 断言；无生产 UI/SDK 依赖 `tool_call` outcome。
- **风险点**：
  - **#583 根因**：Bash `'Interrupted by user'` 不匹配三关键词 → `error`；approval 阶段 cancel 走 `abortedToolOutput` → 已 `cancelled`（`turn.test.ts` L1507–1515，与 Bash 跑起来后 cancel **不同路径**）。
  - **假阳性**：真错误含 `aborted`/`cancelled` → 现判 `cancelled`；grace timeout ``aborted by grace timeout``（`tool-call.ts` L585）亦误判 `cancelled`。
  - **假阴性（方案 A）**：只加 `interrupted` 无法消除 cancelled 词假阳性。
  - `bash.ts` L327–328 对任意 abort 均返回「Interrupted by user」，未用 `isUserCancellation`（模型文案，telemetry 可独立修）。
- **待 R2 决策**：① A vs B；② 标记落 `ExecutableToolResult` 还是 event 元数据；③ 是否顺带修 grace timeout 误分类；④ 单测 vs 集成测；⑤ Bash 超时维持 `error`（默认是）。

---

### Round 2 · R2 方案对比（1～3 遍推敲核心）

**Prompt：**

```text
【R2 · 方案对比 · 仍禁止改码】

基于 R1，比较至少两种实现：
A) 仅扩展 telemetryToolOutcome 字符串表
B) 结构化传递取消原因（tool.result 或内部 metadata）

对每种方案说明：
- diff 范围（文件列表）
- 是否消除「output 含 cancelled 词」假阳性
- Bash 超时 outcome 建议（error vs 新枚举）及理由
- 是否触及 SDK 对外类型
- 推荐方案（一条）与「若不采纳 Issue 首选方案」的风险

若你认为需要第 2 遍推敲，在文末写「R2-追加」并自行反驳推荐方案一次。

输出格式：
## R2 结论
- 方案对比表（A/B）
- 推荐方案：
- 超时语义：
- changeset 级别建议：patch / minor
```

**回填区：**

## R2 结论

- **方案对比表（A/B）**：


| 维度                           | A) 扩展字符串表               | B) 结构化取消信号（**推荐**）                                     |
| ---------------------------- | ----------------------- | ------------------------------------------------------ |
| diff                         | 主要 `turn/index.ts` + 测试 | `turn/index.ts`、`tool-call.ts`、`types.ts`、`bash.ts`、测试 |
| 消除 cancelled 词假阳性            | **否**                   | **是**                                                  |
| 修 Bash `Interrupted by user` | 加 `interrupted` 可修      | `isUserCancellation` 打标                                |
| grace timeout 误分类            | 不修复                     | 可一并修                                                   |
| SDK                          | 不动                      | 不动                                                     |


- **推荐方案**：**B** — abort settle 时写内部标记（如 `cancelledByUser: true`），`telemetryToolOutcome` 优先读标记；删除或极窄保留字符串 fallback。
- **超时语义**：Bash `Command killed by timeout (...)` **维持 `outcome: error`**；不设 user-cancel 标记。
- **changeset**：**patch**（`@moonshot-ai/agent-core` + bundle `@moonshot-ai/kimi-code`）。
- **R2-追加**：A 一行可修 #583 主场景，但无法满足假阳性验收与 task §3「仅字符串匹配应不通过」；故仍选 B。

---

### Round 3 · R3 测试与 PR 边界

**Prompt：**

```text
【R3 · 测试与交付 · 仍禁止改码】

按 R2 推荐方案，列出：
1. 测试文件路径（优先并入已有 test，遵守 AGENTS.md「少建新文件」）
2. 每个用例：输入 → 期望 outcome / error_type（表格）
3. 验证命令（pnpm test 具体路径）
4. PR 文件清单预测 + git diff upstream/main 自检
5. gen-changesets 是否必要（agent-core patch？）

最后自检：是否 Fixes #583 且未扩 scope？

输出格式：
## R3 结论
- 测试计划：
- 验证命令：
- PR 边界：
- 开工前剩余风险：（≤3 条）
```

**回填区：**

## R3 结论

- **测试计划**：
  - 文件：`packages/agent-core/test/agent/turn.test.ts`（集成 + telemetry 断言，不新建 test 文件）。
  - 抽出 `src/agent/turn/tool-telemetry.ts`，在 `turn.test.ts` import 做单测（**R4-③ 必做**）。

  | #   | 场景                                                | 期望 outcome  | 期望 error_type |
  | --- | ------------------------------------------------- | ----------- | ------------- |
  | 1   | Bash 长跑 + 用户 cancel（output `Interrupted by user`） | `cancelled` | 无             |
  | 2   | Bash timeout（`Command killed by timeout (1s)`）    | `error`     | `ToolError`   |
  | 3   | 真错误 output 含 `cancelled`/`aborted`、无 user 标记      | `error`     | 对应 taxonomy   |
  | 4   | approval 阶段 cancel（`turn.test.ts` L1463–1515 回归）  | `cancelled` | 无             |
  | 5   | 非用户 abort（`Tool "X" was aborted`）                 | `error`     | `ToolError`   |
  | 6   | grace timeout（`aborted by grace timeout`）         | `error`     | `ToolError`   |

- **验证命令**：
  ```bash
  cd /Users/cyning/Desktop/Projects/kimi-code
  pnpm --filter @moonshot-ai/agent-core test -- test/agent/turn.test.ts
  pnpm --filter @moonshot-ai/agent-core test -- test/tools/bash.test.ts test/tools/shell-cancel.test.ts
  pnpm lint
  git diff upstream/main --name-only
  ```
- **PR 边界**：`turn/index.ts`、`turn/tool-telemetry.ts`、`loop/types.ts`、`loop/tool-call.ts`、`tools/builtin/shell/bash.ts`、`test/agent/turn.test.ts`、`.changeset/`。**不含** harness/task/SDK 契约变更。PR 正文 `Fixes #583`。
- **gen-changesets**：必要；agent-core + kimi-code **patch**。
- **Fixes #583 自检**：用户取消 → cancelled ✓；真错误不误判 ✓；Bash 超时仍 error ✓；vitest 先红后绿 ✓；scope 未扩 ✓。
- **开工前剩余风险**：见 §4 **R4**（已消解除，30 按 R4 执行即可）。

---

### Round 4 · R4 剩余风险消解除（维护者 / 30 必读）

> R3 三条剩余风险经追加核查后的**书面决策**；无需再开一轮思考。


| #   | R3 风险                                        | R4 决策                                                                                                                                                                                                                                                                                        |
| --- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ①   | 内部标记是否进入 transcript / model                  | 在 `ExecutableToolResult` 增加 `cancelledByUser?: true`，JSDoc 对齐 `stopTurn`（`types.ts` L67–71）：**telemetry-only，不进 model**。`toolResultOutputForModel`（`context/index.ts` L318–341）只读 `output`/`isError`，额外字段不投影。**wire JSONL 可能含该字段**（与 `stopTurn` 同类内部 hint），可接受；**不修改 SDK `tool.result` 映射**。 |
| ②   | `bash.ts` 非用户 abort 仍显示「Interrupted by user」 | **本 PR 非范围**（§2）。telemetry 仅按 `isUserCancellation(signal.reason)` 打标；**不改** Bash 用户可见文案。若 maintainer 要一并修模型文案，单开 task。                                                                                                                                                                       |
| ③   | `telemetryToolOutcome` 为 private，如何测         | **30 执行**：抽出 `packages/agent-core/src/agent/turn/tool-telemetry.ts`（导出 `telemetryToolOutcome` / `telemetryToolErrorType`），`turn/index.ts` re-export 或 import；**单元测写在 `turn.test.ts` 顶部 describe**（遵守少建新文件）。集成用例 1–6 仍保留。                                                                     |


**R4 完成** — 三条均已闭合，可直接签 `HG-AUDIT-R1` 后 30。

---

## 5. 验收标准（关账）

- [x] §4 R1 / R2 / R3 / R4 均已回填
- [x] 22 审计通过 · `HG-AUDIT-R1` → `approved`
- [x] vitest 通过 · 实现与 R2 推荐方案一致
- [x] 上游 PR 已开 · 正文 `Fixes #583` · [#630](https://github.com/MoonshotAI/kimi-code/pull/630)
- [x] invoke 落盘 `docs/harness/invokes/by-task/fix-telemetry-bash-cancel-583/`
- [x] （meta）`02_version` + `10_flow_agent_turn` 切片（C2 #583 · partial）

---

## 6. 给执行帽的必读列表（30 开工前）

1. 仓根 `AGENTS.md` · `packages/agent-core` 邻近 `AGENTS.md`（若有）
2. 本 task **§1 + §4 R1～R4 结论**（30 必按 R4 决策表执行）
3. `@../kimi-code-meta/docs/_tech_graph/01_struct.md` — module `agent_core`
4. Issue #583 原文
5. `.agents/skills/gen-changesets/SKILL.md`（PR 前）

---

## 7. 验证命令

```bash
cd /Users/cyning/Desktop/Projects/kimi-code
git checkout main && git fetch upstream && git reset --hard upstream/main
git checkout -b feature/fix-583-telemetry-cancel

# 测试（路径按 R3 调整）
pnpm --filter @moonshot-ai/agent-core test
# 或 vitest 具体文件

pnpm lint
git diff upstream/main --name-only
```

---

## 8. 给维护者签闸清单

- [x] Kimi Agent 已完成 R1～R4 并回填 §4
- [x] 同意 R2 推荐方案、R4 决策表与超时语义
- [x] `HG-TASK-DRAFT`、`HG-AUDIT-R1` → `approved`
- [x] 30 已执行 · PR [#630](https://github.com/MoonshotAI/kimi-code/pull/630) 已提交

---

## 实现备忘（30 后回填）


| 项     | 状态  | 备注                                              |
| ----- | --- | ----------------------------------------------- |
| R1～R3 | ✅   | 已回填 §4；R4 风险已闭合                                 |
| R4    | ✅   | §4 Round 4 决策表                                  |
| 测试    | ✅   | tsc + vitest 119 + lint 0 errors + dev 手感 `cancelled` |
| 上游 PR | ✅   | https://github.com/MoonshotAI/kimi-code/pull/630 |


### 自检结论（执行者）

> **关账自检** · branch `feature/fix-583-telemetry-cancel` · commit **`679db406`** · 2026-06-10

#### 命令与退出码（复验）

| 命令 | cwd | 退出码 | 摘要 |
|------|-----|--------|------|
| `pnpm exec tsc -p tsconfig.json --noEmit` | `packages/agent-core` | **0** | TS 类型（含 `bash.ts` / `tool-call.ts` `ExecutableToolErrorResult`） |
| `pnpm exec vitest run …`（R3 四文件） | `packages/agent-core` | **0** | **119 passed** |
| `pnpm lint` | `kimi-code` 根 | **0** | 0 errors |
| `git diff upstream/main...HEAD --name-only` | `kimi-code` | — | 7 paths，无 harness/task |

#### Checklist 1–7（维护者确认）

- [x] diff 边界 · vitest · lint · changeset patch
- [x] dev 手感：Bash sleep 30 + Stop → `[telemetry] Bash cancelled undefined`
- [x] 无临时 debug log 残留 · 无 Co-authored-by

#### R3 用例 1–6

全部 **pass**（见 40 自检表；commit `679db406` 含 TS 收紧，行为不变）。

#### task §5 关账

- [x] §4 R1–R4 · vitest · diff 边界
- [x] `HG-AUDIT-R1` approved
- [x] 上游 PR 已开 · [MoonshotAI/kimi-code#630](https://github.com/MoonshotAI/kimi-code/pull/630) · `Fixes #583`
- [x] invoke 30 落盘 `docs/harness/invokes/by-task/fix-telemetry-bash-cancel-583/`

#### 结论

**可关账** — 待 upstream PR merge。