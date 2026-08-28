# Task：Session 中 orphan tool_calls 导致 provider 400 · #705（阶段 C3）

> **状态**：`draft`（§2.2 模块扫描已填 · 图谱 skeleton · **待 10-task §5**）  
> **上游 Issue**：[MoonshotAI/kimi-code#705](https://github.com/MoonshotAI/kimi-code/issues/705) · 原文 [`ISSUE_upstream_705_20260613.md`](../../../docs/harness/guides/issues/ISSUE_upstream_705_20260613.md)  
> **关联图谱**：[`10_flow_context_tool_exchange.md`](../../_tech_graph/10_flow_context_tool_exchange.md) · [`01_struct.md`](../../_tech_graph/01_struct.md) `agent_core`  
> **扫描分级**：工作区 `Projects/docs/harness/guides/ISSUE_SCAN_kimi_code_open_c2_v1_zh.md` v1.4.4  
> **试点真值**：[`docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md`](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `fix-open-tool-calls-705` |
| **test_strategy** | `required` |
| **test_strategy_note** | `context.test.ts` / `resume.test.ts` / `turn.test.ts` 增量；须覆盖 projection trim + pending lifecycle；steer 竞态用 integration 或最小 repro |
| **code_quality_bar** | `strict` |
| **track** | `bugfix` |
| **orchestration** | **10-task**（R0–R5）→ **20** → **30**（**分 ST 子任务**）→ **40** · V2 |
| **entry_invoke_10_task** | [`PROMPT_kimi_agent_rethink_R1_R5.md`](../../harness/invokes/by-task/fix-open-tool-calls-705/PROMPT_kimi_agent_rethink_R1_R5.md) |
| **entry_invoke_00_draft** | 工作区 `docs/harness/prompts/PROMPT_00_draft_spec_or_task_v1_zh.md` |
| **audit_profile** | `human_only` |
| **git_branch** | `feature/fix-705-open-tool-calls` |
| **worktree_root** | `/Users/cyning/Desktop/Projects/kimi-code` |
| **meta_worktree** | `/Users/cyning/Desktop/Projects/kimi-code-meta` |
| **module_id** | `agent_core` |
| **graph_delta** | `10_flow_context_tool_exchange` |
| **graph_delta_note** | — |
| **graph_gate** | `skeleton_before_30` · `close_partial_or_final` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 既有 #705 bugfix · 本 Epic 不改其 wiki；补字段以满足 lint-wiki-delta |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | pending | 20-R1, 30 | §4 + 图谱 skeleton（本起草已落盘 flow · 待 commit） |
| HG-AUDIT-R1 | pending | 30 | 20 R1 + 人签 · **须 ST-705-B 方案闭合后** |

---

## 1. 需求摘要（来自 #705）

Provider **400**：`assistant message with 'tool_calls' must be followed by tool messages responding to each 'tool_call_id'`（例 `Read:158`）。

| 维度 | 说明 |
|------|------|
| **触发** | Resume 会话；或活跃 turn 中 **turn.steer**（后台任务通知）与 in-flight tool 交错 |
| **后果** | turn / retry / **compaction** 均 400；脏 state 持久化，session 不可用 |
| **期望** | 送 LLM 前 repair 或阻止 malformed history；resume 可恢复 |
| **同族** | #269 · #660 · #701 · PR [#664](https://github.com/MoonshotAI/kimi-code/pull/664) DRAFT（**勿抢 #660**） |

---

## 2. 非范围

- `apps/kimi-code` TUI 快捷键（#700 Cmd+V）
- Read 工具 status（#94 · 已 PR [#708](https://github.com/MoonshotAI/kimi-code/pull/708)）
- telemetry Bash cancel（#583 · #630）
- harness / task / meta 图谱进上游 PR
- 单方面 merge PR #664 改动而不在 issue 协调

---

## 2.1 子任务分解（ST · 顺序执行）

> **原则**：面大 · 分 ST 签核；每 ST 结束更新图谱锚点勾选 + task §10。

| ST | 名称 | 帽子 | 交付 | 依赖 |
|----|------|------|------|------|
| **ST-705-A** | 模块认知 + 图谱 skeleton | 00/起草 | `10_flow_context_tool_exchange` skeleton · 本 task §2.2 · `01_struct` 备注 | — |
| **ST-705-B** | 思考轮 + 方案对齐 | **10-task** → **20** | §5 R0–R5 · 对比 #664 / #701 fork / steer defer 方案 · R1 签闸 | ST-705-A |
| **ST-705-C** | Phase1 · projection + pending | **30** | `project()` trim 或等价 · pending turn/resume 清理 · `context.test.ts` 绿 | ST-705-B · HG-AUDIT-R1 |
| **ST-705-D** | Phase2 · steer 竞态 | **30** | defer steer 或 repair 非尾部 orphan · `turn.test.ts` / integration | ST-705-C 绿 |
| **ST-705-E** | Phase3 · resume + compaction 护栏 | **30** | resume cleanup（对齐 #664 或子集）· compaction 400 不 persist · `resume.test.ts` | ST-705-C |
| **ST-705-F** | 关账 + 上游 PR | **40** | 图谱 partial · issue 协调 · PR `Fixes #705` · changeset | ST-705-C–E 绿 |

**30 会话建议**：Open `kimi-code` · **一次 ST 一会话**（或 ST-C/D 同 PR 两 commit，须 task §10 记录）。

---

## 2.2 代码模块扫描（main · 2026-06-13）

> 扫描基线：本地 `kimi-code` · `packages/agent-core` · 对照 #705 / #701 / PR #664 公开 diff。

### A · ContextMemory（`agent/context/index.ts`）

| 符号 | 行号 | 行为 | #705 风险 |
|------|------|------|-----------|
| `pendingToolResultIds` | 29, 260–270, 290–298 | tool.call 入 set · result 出 set | 残留 → `appendMessage` 永久 defer |
| `deferredMessages` | 30, 282–294 | open exchange 时缓冲 user/system | steer 后 prompt 不在 history 尾部 |
| `messages` | 196–198 | `project(history)` → LLM | **不 trim** orphan assistant |
| `useProjectedHistoryFrom` | 200–203 | **唯一** `trimTrailingOpenToolExchange` | 子 agent 继承；主 session 不走 |
| `appendLoopEvent` | 205–275 | step/tool 事件写 history | 正常路径 |
| `flushDeferredMessagesIfToolExchangeClosed` | 289–295 | pending 空后 flush | 依赖 pending 正确清空 |

**main 缺失**：`cleanupOrphanedToolCalls()` · `clearPendingToolResultIds()`（#664 / #701 有）。

### B · Projector（`agent/context/projector.ts`）

| 符号 | 行号 | 行为 | #705 风险 |
|------|------|------|-----------|
| `project()` | 5–16 | 过滤 partial assistant · merge user | orphan `tool_calls` **直通** |
| `trimTrailingOpenToolExchange()` | 74–92 | 仅检查**最后一个**非 tool assistant | steer 后 orphan **非尾部** → 无效 |
| 边界 | 81–82 | 无 assistant 时返回 `[]` | 误删 history（#664 拟修） |

### C · TurnFlow（`agent/turn/index.ts`）

| 符号 | 行号 | 行为 | #705 风险 |
|------|------|------|-----------|
| `steer()` | 132–143 | active turn → `steerBuffer` | #705 时间线：mid-step steer |
| `flushSteerBuffer()` | 265–273 | `appendUserMessage` 每条 steer | 在 `beforeStep` 调用 |
| `beforeStep` | 608–614 | flush steer → 再 LLM step | 与 pending tool 交错 |
| `runOneTurn` | 415+ | turn 起止 | **不** clear pending（#701 拟补） |
| `buildMessages` | ~593 | `() => context.messages` | 脏 history 直达 provider |

### D · Resume / Replay

| 符号 | 文件:行 | 行为 | #705 风险 |
|------|---------|------|-----------|
| `Agent.resume()` | index.ts:297–305 | replay → finishResume | 无 orphan cleanup |
| `AgentRecords.replay()` | records/index.ts:175+ | wire 还原 context/turn | 持久化脏 state |
| `restoreSteer` | turn/index.ts:196–203 | replay steer 缓冲 | resume 路径 |
| `Session.resumeAgent` | session/index.ts:632+ | 用户入口 | 与 #705 repro 一致 |

### E · Background → steer（`agent/background/index.ts`）

| 符号 | 行号 | 行为 |
|------|------|------|
| `notifyBackgroundTask` | ~557–561 | live → `turn.steer()` |
| `restoreBackgroundTaskNotification` | ~564–568 | resume → 直接 `appendUserMessage` |

### F · Compaction（`agent/compaction/full.ts`）

| 符号 | 行号 | 行为 | #705 风险 |
|------|------|------|-----------|
| compaction LLM | ~256–278 | `context.project(messagesToCompact)` | 同 400 |
| 失败 | ~347+ | log `compaction failed` | 与 issue log 一致 |

### G · 现有测试（缺口）

| 文件 | 已有 | 缺口 |
|------|------|------|
| `test/agent/context.test.ts` | deferred + compaction pending | `project()` orphan trim |
| `test/agent/resume.test.ts` | replay 顺序 · deferred flush | orphan assistant 400 repro |
| `test/agent/turn.test.ts` | steer 缓冲 | steer **mid tool call** |
| `test/session/init.test.ts` | inherit trim | — |

### H · 外部修复对照（方案输入 · 非 main）

| 来源 | 核心改动 | 覆盖 #705 steer 竞态 |
|------|----------|---------------------|
| **PR #664** | `cleanupOrphanedToolCalls` on resume · `project()` trailing trim | resume 后 ✅ · live 非尾部 △ |
| **#701 fork** | `clearPendingToolResultIds` at turn/resume · **全局** projection trim | live ✅ 倾向 |
| **#705 建议** | defer steer · validate pairing · 非尾部 trim · compaction 护栏 | 目标全集 |

---

## 3. 失败路径

| 触发条件 | 系统行为 | 可重试 |
|----------|----------|--------|
| 无 §4 / invoke | 10 **拒开工** | 是 |
| 图谱 skeleton 未 meta commit | 30 **拒开工** | 是 |
| §5 未闭合 / HG-AUDIT-R1 pending | 30 **拒开工** | 是 |
| 未读 #664 协调即开 competing PR | 维护者 **拒合并** | 是 |
| ST-705-C 未绿即做 ST-705-D | 执行 Agent **应拒** | 是 |
| PR 已开无图谱关账 | 不得 `done/` | 是 |

---

## 4. 给 10-task 交接物（00 起草 · V2）

| 字段 | 值 |
|------|-----|
| **帽子** | **10-task**（`track: bugfix`） |
| **Open Folder** | `kimi-code` |
| **invoke** | [`PROMPT_kimi_agent_rethink_R1_R5.md`](../../harness/invokes/by-task/fix-open-tool-calls-705/PROMPT_kimi_agent_rethink_R1_R5.md) |
| **回填协议** | [`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../harness/FRAGMENT_rethink_backfill_task_v1_zh.md) |
| **10-task 真值** | 工作区 `docs/harness/prompts/10-task-requirements.md` |

### 必读路径（`@` 自 `kimi-code` 根）

| 路径 | 用途 |
|------|------|
| `../kimi-code-meta/docs/tasks/active/task_fix_open_tool_calls_705_v1.md` | 读本 task · **§2.2 模块扫描** · 回填 §5 |
| `../kimi-code-meta/docs/_tech_graph/10_flow_context_tool_exchange.md` | 图谱 · R5 核对 |
| `../kimi-code-meta/docs/_tech_graph/10_flow_context_tool_exchange.ai.md` | 双轨 flowchart |
| `../kimi-code-meta/docs/_tech_graph/01_struct.md` | `agent_core` |
| `../../../docs/harness/guides/issues/ISSUE_upstream_705_20260613.md` | Issue 原文 |
| `packages/agent-core/src/agent/context/index.ts` | ContextMemory |
| `packages/agent-core/src/agent/context/projector.ts` | project / trim |
| `packages/agent-core/src/agent/turn/index.ts` | steer / step |
| `packages/agent-core/src/agent/index.ts` | resume |
| `packages/agent-core/src/agent/records/index.ts` | replay |
| `packages/agent-core/src/agent/background/index.ts` | background steer |
| `packages/agent-core/src/agent/compaction/full.ts` | compaction LLM |
| `packages/agent-core/test/agent/context.test.ts` | 测试面 |
| `packages/agent-core/test/agent/resume.test.ts` | resume |
| `packages/agent-core/test/agent/turn.test.ts` | steer |
| https://github.com/MoonshotAI/kimi-code/issues/705 | Issue |
| https://github.com/MoonshotAI/kimi-code/pull/664 | PR 协调 |
| https://github.com/thecannabisapp/kimi-code/commit/0291e891f0d304add982598e6bcba992dd27042e | #701 fork |

### 禁止（10 会话）

- 改 `packages/**`、`apps/**`、`.changeset`
- `git commit` / `git push`

### 10-task 产出（交给 20）

- §5 各轮 + **思考轮控制**（R2 **必须**对比 #664 / #701 / 自建方案）
- ST-705-B 方案选定 · 是否 rebase #664 子集
- **不**签发 `HG-AUDIT-R1`

### 00 Handoff 最小字段

```text
hat_code: 10-task
task_path: kimi-code-meta/docs/tasks/active/task_fix_open_tool_calls_705_v1.md
read_paths: 见上表 + §2.2
forbidden: 产品代码 · commit
output_shape: task §5 + ST-705-B 方案表
entry_invoke: docs/harness/invokes/by-task/fix-open-tool-calls-705/PROMPT_kimi_agent_rethink_R1_R5.md
```

---

## 5. Kimi Code Agent · 思考轮次（10 回填 · R0+R1–R5）

### 思考轮控制

| 字段 | 值 |
|------|-----|
| **actual_last_round** | （待填） |
| **early_stop** | （待填） |
| **early_stop_reason** | — |
| **residual_risks** | （待填 · 须含 #664 协调 · steer repro 难度） |

### R0 · 读 task

```text
（待填）
```

### R1 · 代码事实

```text
（待填 · 须引用 §2.2 并增量核对 main 行号）
```

### R2 · 方案对比

```text
（待填 · 至少：A 对齐 #664 子集+705 steer · B #701 全局 trim+pending · C defer steer · D 等 #664 merge）
```

### R3 · 边界 / 测试

```text
（待填 · 按 ST-705-C/D/E 分测试矩阵）
```

### R4 · 测试与 PR 策略

```text
（待填 · PR 正文 Fixes #705 · 说明与 #664/#660 关系）
```

### R5 · 图谱 + 协调 + 关账判断

```text
（待填 · 更新 flow 锚点勾选 · issue 回复草案）
```

---

## 6. 验收标准（关账）

- [ ] §5 闭合 · `HG-AUDIT-R1` approved
- [ ] ST-705-C–F 完成 · vitest 绿
- [ ] 图谱 `10_flow_context_tool_exchange` partial + `02_version`
- [ ] 上游 PR `Fixes #705` · 已 issue 协调 #664 / #701
- [ ] 无 harness 路径进上游 diff

---

## 7. 给 30 帽必读（签闸后 · 按 ST 执行）

1. 仓根 `AGENTS.md`
2. 本 task §1 · **§2.1 ST** · **§5 结论**
3. `@../kimi-code-meta/docs/_tech_graph/01_struct.md`
4. `@../kimi-code-meta/docs/_tech_graph/10_flow_context_tool_exchange.md`
5. Issue #705 + §2.2 模块扫描
6. invoke §「30 开工」· `30-execute-code.md` · **首输出 GATE_VERIFY**

---

## 8. 验证命令

```bash
cd /Users/cyning/Desktop/Projects/kimi-code/packages/agent-core
pnpm test test/agent/context.test.ts
pnpm test test/agent/resume.test.ts
pnpm test test/agent/turn.test.ts

cd /Users/cyning/Desktop/Projects/kimi-code
pnpm lint
git diff upstream/main --name-only
```

---

## 9. 维护者签闸清单

- [ ] §2.2 模块扫描已读
- [ ] 图谱 skeleton meta commit
- [ ] §4 + invoke PROMPT 已落盘
- [ ] 10-task §5 + 20 R1 + HG 两闸
- [ ] ST 顺序执行记录于 §10

---

## 10. 实现备忘（30+ 回填）

| 项 | ST | 状态 | 备注 |
|----|-----|------|------|
| 模块扫描 + flow skeleton | A | ✅ | 2026-06-13 起草 |
| 10-task §5 + 20 R1 | B | ⏳ | |
| projection + pending | C | ⏳ | |
| steer 竞态 | D | ⏳ | |
| resume + compaction | E | ⏳ | |
| PR Fixes #705 | F | ⏳ | |
| 人工闸 | — | pending | |
| 上游 PR | F | ⏳ | |

### ST 执行日志

```text
（30 各 ST 完成后追加：commit · 测试 · 风险）
```
