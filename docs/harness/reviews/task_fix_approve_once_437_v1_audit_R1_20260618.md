# 任务审核 · fix-approve-once-437 · R1

| 元信息 | 值 |
|--------|-----|
| **task_path** | `docs/tasks/active/task_fix_approve_once_437_v1.md` |
| **task_slug** | `fix-approve-once-437` |
| **轮次** | R1（首轮） |
| **日期** | 2026-06-18 |
| **auditor_hat** | `22-task-audit` |
| **invoke_snapshot** | [`invoke_20260618_22_fix-approve-once-r1.md`](../invokes/by-task/fix-approve-once-437/invoke_20260618_22_fix-approve-once-r1.md) |
| **git_branch（meta）** | `cyning/meta` |
| **产品只读分支** | `feature/fix-437-approve-once-clean` · `98f1fa5f` |
| **HG-AUDIT-R1** | **pending**（本帽不代签） |

---

## 审查结论摘要

| 维度 | 结论 |
|------|------|
| **内容** | **不通过** · 思考轮 §5 未闭合（硬阻塞） |
| **流程闸** | `HG-AUDIT-R1` **pending** · 本帽 **禁止** 建议签闸 · **禁止** 附 30 Prompt |

**一句话**：需求、修复方案、分支纪律、图谱 skeleton 与产品干净 diff 交叉验证 **可执行**；但 task §5 `actual_last_round` 仍为裸占位 `（待 10）`，违反 22 帽思考轮闭合要求 → **退回 10-task** 补 §5 后再开 R1 复审（或同轮次维护者补填后重审）。

---

## 思考轮审查表（§5）

| 核对项 | 结论 |
|--------|------|
| `actual_last_round` | **`（待 10）`** ❌ 裸占位 · 未填 |
| `early_stop` | `no` ✓（与 agent-core 单点修复范围一致） |
| `residual_risks` | 已写「Write 会话粒度 vs 精确路径 · 安全边界」✓ · 但缺 R0–Rn 事实链支撑 |
| 裸「（待 10）」「（待填）」 | **`actual_last_round` 一行未闭合** ❌ |
| early_stop 与 diff 范围 | ✓ 仅 `packages/agent-core` 2 文件 · 无 early_stop 必要 |
| residual_risks 验收口径（R1 可读性） | 见下文「#437 修复方案审查」· 非阻塞 · 待 §5 闭合后写入 task |

**思考轮结论**：**不通过** → **退回 10-task** · **禁止** 建议签 **`HG-AUDIT-R1`**。

---

## #437 修复方案审查摘要

### Issue 语义

- **现象**（#437 + comment）：TUI 选「Approve for this session」后，同会话后续 **Write**（同目录多文件）仍重复弹窗；「Approve once」与 session 选项行为相同。
- **根因（产品 diff）**：`Approve for session` 曾把 **完整 path 级** `approvalRule`（如 `Write(/workspace/pkg/a.ts)`）写入 `sessionApprovalRulePatterns`；下一文件 path 不匹配 → `session-approval-history` 不命中。

### 修复方案（`98f1fa5f` · 只读核对）

| 项 | 结论 |
|----|------|
| **Approve once** | `adaptPanelResponse` → `decision: approved` **无** `scope: session` → **不**写 `sessionApprovalRule` ✓ |
| **Approve for session** | `approved_for_session` → `scope: 'session'` → `resolveSessionApprovalRule` ✓ |
| **Write/Edit 粒度** | 有 `matchesRule` 时缓存 **工具名**（`Write` / `Edit`），非完整 path 规则 ✓ |
| **Bash 粒度** | 仍缓存完整 `Bash(command)` 规则 · 与 Write/Edit 差异 **合理**（命令级安全边界） ✓ |
| **TUI 链** | `ApprovalPanel` 四选项 → `adapter.adaptPanelResponse` → `ApprovalController.autoResolveFor`（同 action + session scope 队列复用）→ agent-core `PermissionManager` ✓ |
| **图谱 skeleton** | `CS_APPROVE_ONCE` / `CS_APPROVE_SESSION` / `CS_SESSION_CACHE` / `CS_SESSION_HIST` 与上述语义 **一致** ✓ |
| **测试** | 新增 `reuses approve-for-session for Write to different paths (#437)` · `requestApproval` 仅 1 次 · pattern 含 `Write` ✓ |
| **Edit 对称** | 代码分支覆盖 `Edit` · 测试 **仅 Write** · **非阻塞** · 建议 30 可选补 Edit 镜像用例 |
| **TUI 单测** | `apps/kimi-code/test/tui/reverse-rpc/approval-adapter.test.ts` 覆盖 `approved_for_session` → scope · **未**断言 agent-core 缓存粒度 · **非阻塞**（agent-core 已覆盖 #437） |

### residual_risks 建议验收口径（供 10 回填 §5）

| 风险 | R1 验收口径 |
|------|-------------|
| Write/Edit **会话级** vs Bash **命令级** | manual 模式下：Write A + Write B（不同 path）session 仅 1 次弹窗；Bash 不同 command 仍分别弹窗 |
| 安全边界 | session 缓存 **不**覆盖 explicit deny rule（已有 `does not let session approval override an explicit deny rule`） |
| Approve once | 第二次同类 Write **仍**弹窗（scope 非 session · 无 pattern 写入） |

---

## 分支纪律 / graph_delta / §8 漂移

| 项 | 结论 |
|----|------|
| **干净分支** | `upstream/main...feature/fix-437-approve-once-clean` = 单 commit `98f1fa5f` · **仅** 2 文件 ✓ |
| **禁止混入** | 无 `read.ts` · 无 harness/docs/tasks · ✓ |
| **脏分支警示** | `feature/fix-437-approve-once` 仍存在 · task 已注明可能含 #94 read · 30 须用 **clean** 分支 |
| **graph_delta** | `10_flow_cli_session` skeleton 已 commit · `10_flow_agent_turn` 仅备注（#583 切片 · 本 bugfix 不强制改边） ✓ |
| **graph_gate** | `yaml_edit_before_30` · skeleton 已满足 · 30 关账跑 `graph:issue-sync` |
| **§8 vs §6 漂移** | §8 表「产品 Write session 粒度 ✅」「graph_issue_sync ✅」为 **aspirational / 待 30 关账**；§6 验收项仍为 `[ ]` · **非阻塞** · 建议 10 或 30 在 §8 备注列标注「本地验证 / 待 PR」 |
| **双 worktree** | task 元信息已填 `meta_worktree` · `product_worktree` · `product_base_ref` ✓ |

---

## test_strategy / failure_paths / 验收 §6

| 项 | 结论 |
|----|------|
| **test_strategy** | `required` · agent-core `permission.test.ts` + TUI adapter 链 · 字段完整 ✓ |
| **failure_paths §3** | 无 skeleton · HG-AUDIT-R1 pending · PR 无 meta commit · graph:issue-sync 失败 — 四条清晰 ✓ |
| **验收 §6** | meta skeleton `[x]` · 产品 / issue-sync / PR / HG-AUDIT-R1 均为 `[ ]` · 与 §8 aspirational 一致 · 待 30/40 |
| **30 预演（只读）** | G0：确认 clean 分支 · G1：PR 仅 agent-core · G2：changeset patch · G3：`graph:issue-sync` + §8 SHA 回填 |

---

## 阻塞 / 非阻塞

### 阻塞（内容）

| # | 项 | 动作 |
|---|-----|------|
| **B1** | §5 `actual_last_round` = `（待 10）` | **10-task** 回填 Kimi Code Agent 思考轮（至少 R0–R1：Issue 读码 · 修复方案确认 · 与 `early_stop`/`residual_risks` 对齐） |

### 非阻塞

| # | 项 | 建议 |
|---|-----|------|
| N1 | §8 预填 ✅ vs §6 未勾 | 30 关账时统一回填 · 或 10 补备注「aspirational」 |
| N2 | 缺 Edit #437 镜像测试 | 30 可选补 · 代码已对称 |
| N3 | TUI 单测未断言 Write 多 path | agent-core 已覆盖 · 可接受 |
| N4 | `10_flow_agent_turn` graph_delta 仅备注 | 与 task `graph_delta_note` 一致 · 可接受 |

---

## 需 10-task 回填清单

1. **§5 · `actual_last_round`**：填实际末轮（建议 `R1` 或产品探索轮次编号），删除 `（待 10）`。
2. **§5 · 思考轮事实链**（可选表行或 §5 下子表）：Issue #437 读码路径 · `resolveSessionApprovalRule` 方案 · clean 分支 `98f1fa5f` 与 eedd430c 关系。
3. **§5 · `residual_risks`**：并入上节「建议验收口径」一行摘要（Write/Edit 工具名 vs Bash 命令级 · deny 不被 session 覆盖）。
4. **§8 备注列**（可选）：「产品 ✅」→「本地 clean 分支已验证 · 待 upstream PR」；「graph_issue_sync ✅」→「L3 mock 绿 · 待 G3 关账 SHA」。

---

## 人工闸审查意见（HG-AUDIT-R1）

| gate | R1 建议 |
|------|---------|
| **HG-AUDIT-R1** | **维持 pending** · **禁止** 代签 |

**理由**：思考轮 §5 未闭合（B1）。内容侧其余核对项无硬阻塞，但 Harness 22 帽纪律要求 **§5 闭合后** 方可建议维护者签 **`HG-AUDIT-R1`**。

---

## 维护者签闸清单（22 后 · 30 前）

> **R1 不通过**：下列清单 **暂不执行**。§5 回填并 **R1 复审通过** 后再签。

```text
## 维护者签闸（22 后 · 30 前）

- [ ] 已读 R1 审查结论（须为「通过 · 思考轮闭合」）
- [ ] 在 task 人工闸表将 HG-AUDIT-R1 改为 approved（维护者 · 日期）
- [ ] commit task 文档或确认已签
- [ ] 再下发 Harness 30 Prompt（PROMPT_START_30_v1.md）
```

**禁止** 在 `HG-AUDIT-R1` = pending 时附「已 approved」的 30 Prompt。

---

## 下一棒

| 路径 | 说明 |
|------|------|
| **退回 10-task** | 按「需 10-task 回填清单」补 §5 → 可选同对话或新对话重开 22 R1 |
| **30** | **本轮不可** · 待 §5 闭合 + R1 通过 + 维护者签 **`HG-AUDIT-R1`** |
