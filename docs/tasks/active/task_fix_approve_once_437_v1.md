# Task：修复 Approve once vs session 无差异 · #437（阶段 C）

> **状态**：`active` · HG-TASK-DRAFT **approved**（2026-06-18）  
> **前序**：`[task_meta_graph_issue_sync_gate_v1.md](../done/task_meta_graph_issue_sync_gate_v1.md)` **CLOSE**  
> **上游 Issue**：[MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437)  
> **关联图谱**：`[10_flow_cli_session.graph.yaml](../../_tech_graph/10_flow_cli_session.graph.yaml)` · `[01_struct.md](../../_tech_graph/01_struct.md)` `cli`  
> **试点真值**：`[POINTER_PILOT_adoption_workspace_v1_zh.md](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)`

---

## Harness 元信息


| 字段                       | 值                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| **task_slug**            | `fix-approve-once-437`                                                                              |
| **test_strategy**        | `required`                                                                                          |
| **test_strategy_note**   | TUI approval reverse-rpc · agent-core permission session 缓存 · Write 同目录复用                           |
| **code_quality_bar**     | `strict`                                                                                            |
| **track**                | `bugfix`                                                                                            |
| **orchestration**        | **10-task**（R0–R5）→ **20** → **30** → **40**                                                        |
| **audit_profile**        | `human_only`                                                                                        |
| **git_branch**           | `feature/fix-437-approve-once-clean`（产品 · 30 G0）· meta `cyning/meta` |
| **worktree_root**        | `/Users/cyning/Desktop/Projects/kimi-code`                                                          |
| **meta_worktree**        | `/Users/cyning/Desktop/Projects/kimi-code-meta`                                                     |
| **product_worktree**     | `/Users/cyning/Desktop/Projects/kimi-code`                                                          |
| **product_base_ref**     | `upstream/main...HEAD`                                                                              |
| **module_id**            | `cli`                                                                                               |
| **graph_delta**          | `10_flow_cli_session.graph.yaml` · `10_flow_agent_turn.graph.yaml`                                  |
| **graph_delta_note**     | —                                                                                                   |
| **graph_gate**           | `yaml_edit_before_30` · `close_partial_or_final`                                                    |
| **entry_invoke_10_task** | `[PROMPT_START_10_v1.md](../../harness/invokes/by-task/fix-approve-once-437/PROMPT_START_10_v1.md)` |


### 人工闸


| human_gate_id | status   | blocks_hats | 说明                               |
| ------------- | -------- | ----------- | -------------------------------- |
| HG-TASK-DRAFT | approved | 20-R1, 30   | meta skeleton 已 commit · 可 30 产品 |
| HG-AUDIT-R1   | approved | 30          | 22 R1 复审通过 · 2026-06-18 维护者签 |


---

## 1. 需求摘要（#437）

TUI 工具审批时，「Approve once」与「Approve for this session」行为相同：同会话后续同类工具仍重复弹窗。  
Issue comment：目录下多次 **Write** 选 session 仍多次提示。

**预期**：

- **Approve once**：仅当次 · 不写入 session 规则
- **Approve for session**：写入 `sessionApprovalRule` · 后续匹配调用免弹窗（Bash 同命令 · Write/Edit 等同会话粒度见 R1）

---

## 2. 非范围

- 重开 batch YAML 迁移 · 改未触达 flow
- harness/task 进上游 PR
- ACP 适配大改（除非复现路径在 acp-adapter）

---

## 3. 失败路径


| 触发条件                   | 行为         | 可重试 |
| ---------------------- | ---------- | --- |
| 无 meta skeleton commit | 30 **拒开工** | 是   |
| `HG-AUDIT-R1` pending  | 30 **拒开工** | 是   |
| PR 已开但 meta 无图谱 commit | 不得 `done/` | 是   |
| `graph:issue-sync` 失败  | 关账 **拒**   | 是   |


---

## 4. 给 10-task 交接物


| 字段              | 值                                                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Open Folder** | `kimi-code`                                                                                                                                              |
| **必读**          | 本 task · `10_flow_cli_session` · Issue #437 · `[PROMPT_START_10_v1.md](../../harness/invokes/by-task/fix-approve-once-437/PROMPT_START_10_v1.md)`（§5 回填） |
| **禁止**          | 10 会话改产品码（可选补 §5）                                                                                                                                        |


### 必读路径


| 路径                                                                    | 用途           |
| --------------------------------------------------------------------- | ------------ |
| `../kimi-code-meta/docs/tasks/active/task_fix_approve_once_437_v1.md` | 本 task       |
| `../kimi-code-meta/docs/_tech_graph/10_flow_cli_session.graph.yaml`   | 图谱 skeleton  |
| `apps/kimi-code/src/tui/reverse-rpc/approval/`                        | TUI 审批链      |
| `packages/agent-core/src/agent/permission/`                           | session 规则缓存 |


---

## 5. Kimi Code Agent · 思考轮次（改码前 · R0–R5）

> **回填协议**：`[FRAGMENT_rethink_backfill_task_v1_zh.md](../../harness/FRAGMENT_rethink_backfill_task_v1_zh.md)`  
> **invoke 快照**：`[invoke_20260618_10_fix-approve-once-backfill.md](../../harness/invokes/by-task/fix-approve-once-437/invoke_20260618_10_fix-approve-once-backfill.md)`

### 思考轮控制（Agent 填 · 22 审）


| 字段                    | 值                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **actual_last_round** | `R5`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **early_stop**        | `no`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **early_stop_reason** | —                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **residual_risks**    | ① Write/Edit **工具名** session 缓存 vs Bash **命令级** 缓存 · manual 验收：Write A + Write B（不同 path）session 仅 1 次弹窗；Bash 不同 command 仍分别弹窗。② session 缓存 **不**覆盖 explicit deny rule（已有 `does not let session approval override an explicit deny rule`）。③ Approve once：第二次同类 Write **仍**弹窗（无 `scope: session` · 无 pattern 写入）。④ 脏分支 `feature/fix-437-approve-once` 可能含 #94 read · **30 须用 clean** `feature/fix-437-approve-once-clean` / `98f1fa5f`。 |


### R0 · 读 task

**回填区：**

```text
Issue #437（OPEN）：v0.9.0+ TUI 选「Approve once」与「Approve for this session」行为相同——同会话后续工具调用仍重复弹窗；Huaweidev comment 复现：目录下多次 Write 选 session 仍多次提示。

预期语义（task §1）：
- Approve once：仅当次批准 · 不写入 sessionApprovalRule / localSessionApprovalRulePatterns
- Approve for session：写入 session 规则 · 后续匹配调用由 session-approval-history 免弹窗

Task 元信息：task_slug=fix-approve-once-437 · test_strategy=required · graph_delta=10_flow_cli_session + 10_flow_agent_turn（后者仅备注）· graph_gate=yaml_edit_before_30 · close_partial_or_final。HG-TASK-DRAFT approved · HG-AUDIT-R1 pending（10 不代签）。双 worktree：meta=kimi-code-meta/cyning/meta · product=kimi-code。

分支纪律：干净修复在 feature/fix-437-approve-once-clean · 单 commit 98f1fa5f（仅 agent-core 2 文件）；脏分支 feature/fix-437-approve-once（eedd430c）可能混入 #94 read · 30 禁止用脏分支开 PR。

§8 原 aspirational ✅ 已在本轮改为可审计备注（见 §8 表）；§6 验收项仍为 [ ] · 待 30/40 关账。
```

### R1 · 代码事实（禁止方案）

**回填区：**

```text
TUI 四选项链（apps/kimi-code/src/tui/reverse-rpc/approval/）：
- DEFAULT_APPROVAL_CHOICES：Approve once → response='approved'；Approve for session → 'approved_for_session'
- adaptPanelResponse：approved_for_session → { decision:'approved', scope:'session' }；approved → { decision:'approved' } 无 scope
- ApprovalController.autoResolveFor：decision=approved 且 scope=session 且 queued.action===resolved.action 时队列内 auto-resolve（TUI 层同 action 免二次弹窗）
- handler.createApprovalRequestHandler → controller.show(adaptApprovalRequest(event))

agent-core PermissionManager（packages/agent-core/src/agent/permission/index.ts）：
- requestToolApproval：response.decision==='approved' && scope==='session' 时调用 resolveSessionApprovalRule(name, approvalRule, matchesRule!==undefined) 得 sessionApprovalRule
- recordApprovalResult：decision!=='approved' 或 scope!=='session' 时 early return · 不写 pattern；否则 localSessionApprovalRulePatterns.add(pattern)
- resolveSessionApprovalRule（#437 修复点）：有 argPattern 且 toolName 为 Write/Edit 时返回 parsed.toolName（如 'Write'），否则保留完整 approvalRule（如 Bash(command)）

session-approval-history（policies/session-approval-history.ts）：
- evaluate 遍历 agent.permission.sessionApprovalRulePatterns
- matchPermissionRule({ pattern, toolName, execution }) 命中则 kind:'approve' · 跳过 ask 弹窗

现有测试（permission.test.ts · clean 分支）：
- #437：reuses approve-for-session for Write to different paths — Write /a.ts + Write /b.ts · requestApproval 1 次 · patterns 含 'Write'
- Bash session：reuses approve-for-session even when ask rule matches · 同 command 第二次免弹窗
- Approve once：keeps approved once responses one-shot · 两次 Bash · requestApproval 2 次
- 安全：does not let session approval override an explicit deny rule · deny 优先 · 不弹窗

TUI 单测 approval-adapter.test.ts：maps approved-for-session → scope:'session' · 未断言 agent-core 多 path 粒度（非阻塞 · agent-core 已覆盖）

分支对照：98f1fa5f（clean）= eedd430c 同修复语义 · 单 commit 无 #94；脏分支 eedd430c 之上另有 read dual-limit 提交。
```

### R2 · 方案对比

**回填区：**

```text
方案 A（已实现 · 推荐）：agent-core resolveSessionApprovalRule — Write/Edit 有 matchesRule 时 session 缓存工具名而非完整 path 规则。
  理由：根因在 sessionApprovalRulePatterns 写入粒度；TUI 已正确区分 scope · 旧行为把 Write(/path/a.ts) 写入导致 /path/b.ts 不匹配 session-approval-history。
  与 Issue 语义对齐：Approve for session 后同会话任意 Write 免弹窗；Approve once 不写 pattern。

方案 B（弃选）：仅改 TUI ApprovalController.autoResolveFor 或 adapter。
  弃因：只能消同 action 队列内重复 · 无法解决 agent-core 第二次 beforeToolCall 仍走 ask；且跨 turn 复用依赖 session-approval-history。

方案 C（弃选）：放宽 matchesRule 全局匹配或合并所有 Write path。
  弃因：破坏 Bash 命令级安全边界 · 可能让未批准的具体 command/path 被误放行。

结论：推荐 A · clean diff 98f1fa5f 仅 index.ts + permission.test.ts · 与 22 R1 审查一致。
```

### R3 · 边界 / 安全

**回填区：**

```text
粒度边界：
- Write/Edit + Approve for session：同会话不同 path 共享工具名 pattern 'Write'/'Edit' · 符合 #437 comment（目录多文件）
- Bash + Approve for session：仍缓存完整 Bash(command) · 不同 command 分别弹窗（stores runtime rules with literal glob escaping 等用例）
- Approve once：scope 非 session · recordApprovalResult 不写 pattern · 第二次同类 Write 仍弹窗

安全边界：
- explicit deny rule 优先于 session-approval-history（does not let session approval override an explicit deny rule）
- yolo/auto 模式与 #437 主路径无关（Issue 为 manual TUI 审批）；plan mode Bash session 有独立用例 · 非本 bug 回归面

对称性：
- resolveSessionApprovalRule 覆盖 Write 与 Edit 分支 · 测试仅 Write #437 镜像 · 30 可选补 Edit 用例 · 非阻塞

TUI controller autoResolveFor 要求同 action 字符串 · 与 agent-core 工具名粒度互补 · 非冲突。
```

### R4 · 测试与 PR 策略

**回填区：**

```text
agent-core 测试（feature/fix-437-approve-once-clean）：
| 用例 | 断言要点 |
|------|----------|
| reuses approve-for-session for Write to different paths (#437) | 2×Write 不同 path · requestApproval×1 · pattern 含 Write |
| keeps approved once responses one-shot | 2×Bash approve once · requestApproval×2 |
| reuses approve-for-session even when ask rule matches | Bash session · session-approval-history 命中 |
| does not let session approval override explicit deny | block:true · 无 requestApproval |

命令：
  cd kimi-code && git checkout feature/fix-437-approve-once-clean
  pnpm --filter @moonshot-ai/agent-core test -- permission.test.ts

TUI：
  pnpm --filter @moonshot-ai/kimi-code test -- test/tui/reverse-rpc/approval-adapter.test.ts
  （scope 映射 · 不断言 Write 多 path · 可接受）

PR 策略（30）：
- G0：自 upstream/main 建/确认 feature/fix-437-approve-once-clean · 禁止脏分支
- G1：PR 仅 packages/agent-core 2 文件 · Fixes #437 · 无 harness/docs/tasks
- G2：gen-changesets · @moonshot-ai/agent-core patch
- 禁止：meta harness 进上游 · 本 task invoke/review 不进 PR
```

### R5 · 图谱 + 关账判断

**回填区：**

```text
图谱：
- 10_flow_cli_session.graph.yaml skeleton 与修复语义一致：CS_APPROVE_ONCE（无 scope）→ CS_CONTROLLER；CS_APPROVE_SESSION → CS_SESSION_CACHE → CS_SESSION_HIST → CS_TOOLS
- 10_flow_agent_turn：graph_delta 仅备注（#583 切片）· 本 bugfix 不强制改边 · 与 task graph_delta_note 一致
- meta skeleton 已 commit · 30 前 graph:compile:check 已满足 yaml_edit_before_30

关账（30 G3 · 40）：
- 上游 PR merge 后 meta 跑 pnpm graph:issue-sync --task ... --product-root ../kimi-code --product-ref upstream/main...HEAD
- §8 回填产品 SHA · §6 勾选 · task → done/ · HG-AUDIT-R1 由维护者签 approved

结论：思考轮闭合 · 方案与 clean diff 98f1fa5f 交叉验证一致 · 可 22 R1 复审。
```

---

## 6. 验收标准

- [x] meta：`10_flow_cli_session.graph.yaml` skeleton + compile
- [ ] 产品：`feature/fix-437-approve-once-clean` · 修复 + 测试 · upstream PR
- [ ] `pnpm graph:issue-sync` exit 0
- [ ] 上游 PR · `Fixes #437`
- [x] `HG-AUDIT-R1` approved（2026-06-18）
- [ ] task → `done/`（G3 关账后）

---

## 7. 验证命令

```bash
# meta
cd kimi-code-meta
pnpm graph:compile:check
pnpm graph:issue-sync \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD

# 产品
cd ../kimi-code
git checkout feature/fix-437-approve-once-clean
pnpm --filter @moonshot-ai/agent-core test -- permission.test.ts
pnpm --filter @moonshot-ai/kimi-code test -- test/tui/reverse-rpc/approval-adapter.test.ts
```

---

## 8. 实现备忘


| 项                   | 状态  | 备注                                      |
| ------------------- | --- | --------------------------------------- |
| meta skeleton YAML  | ✅   | `e08a56b2` · `d76c4da5` · `1a89ab2e`    |
| 产品 Write session 粒度 | ✅   | 本地 clean `98f1fa5f` 已验证 · 待 upstream PR |
| graph_issue_sync    | ✅   | L3 mock 绿 · 待 G3 关账 SHA                 |


