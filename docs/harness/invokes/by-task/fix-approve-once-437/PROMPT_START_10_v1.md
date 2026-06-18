# 启动 Prompt · 10 任务分析 / 思考轮回填 · fix-approve-once-437

> **用法**：Open Folder **`kimi-code/`**（产品仓 · 只读代码）→ **新对话** → 复制下方 **§3 代码块** 全文。  
> **触发**：22 R1 **不通过** · task §5 未闭合 → [`task_fix_approve_once_437_v1_audit_R1_20260618.md`](../../reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md)  
> **task**：[`docs/tasks/active/task_fix_approve_once_437_v1.md`](../../../../tasks/active/task_fix_approve_once_437_v1.md)  
> **Issue**：[MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437)  
> **下一帽（回填完成后）**：[`PROMPT_START_22_v1.md`](./PROMPT_START_22_v1.md)（22 R1 复审）

| 项 | 值 |
| --- | --- |
| **task_slug** | `fix-approve-once-437` |
| **analyst_hat** | `10-requirements` / 10-task（真值 [`10-requirements.md`](../../prompts/10-requirements.md)） |
| **Open Folder（执行）** | `kimi-code/` · 只读源码 |
| **Open Folder（写 task）** | `kimi-code-meta/` · 分支 `cyning/meta` |
| **产品只读分支** | `feature/fix-437-approve-once-clean` · `98f1fa5f` |
| **回填协议** | [`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../FRAGMENT_rethink_backfill_task_v1_zh.md) **mandatory** |
| **禁止** | 改 `packages/**` · `apps/**` · `git commit`（除非维护者另嘱） |

---

## 1. 背景（给接棒 Agent）

- **22 R1 阻塞**：§5 `actual_last_round` = `（待 10）` · 缺 R0–R5 回填区 → **退回 10**。
- **现象**（#437）：TUI「Approve once」与「Approve for session」无差异；同会话多次 **Write** 选 session 仍重复弹窗。
- **meta 已就绪**：`10_flow_cli_session.graph.yaml` skeleton · `HG-TASK-DRAFT approved`。
- **产品已有本地修复**（只读对照）：`98f1fa5f` / `eedd430c` · 仅 `packages/agent-core` 2 文件 · `resolveSessionApprovalRule`。
- **10 交付**：把思考结论 **写入 task §5**（非仅聊天）→ 供 22 复审 → 维护者签 **HG-AUDIT-R1** → 30。

---

## 2. 开帽前（只读核验）

```bash
# meta · task 与 22 审查文存在
cd kimi-code-meta && git checkout cyning/meta
test -f docs/tasks/active/task_fix_approve_once_437_v1.md
test -f docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md

grep -q 'actual_last_round.*（待 10）' docs/tasks/active/task_fix_approve_once_437_v1.md \
  && echo "OK: §5 待回填" || echo "NOTE: §5 可能已回填 · 核对后执行"

# 产品 · 干净分支（只读）
cd ../kimi-code
git fetch upstream 2>/dev/null || true
git log --oneline -1 feature/fix-437-approve-once-clean 2>/dev/null || echo "NOTE: checkout clean 分支"
git diff --stat upstream/main...feature/fix-437-approve-once-clean 2>/dev/null \
  | grep -v 'packages/agent-core' && echo "WARN: diff 超出 agent-core" || true
```

---

## 3. 启动 Prompt（复制整段）

```text
你是 **10 任务分析 Agent**（#437 Approve once vs session · 思考轮回填 · 承接 22 R1 退回）。

【开帽 · GATE_SCAN · 缺一 STOP】
- HG-TASK-DRAFT: **approved** ✓（2026-06-18）
- HG-AUDIT-R1: **pending**（10 不代签 · 不附 30 Prompt）
- Open Folder（读码）: **kimi-code/** · `feature/fix-437-approve-once-clean` 或 upstream/main + 只读 diff `98f1fa5f`
- Open Folder（写 task）: **kimi-code-meta/** · `cyning/meta`
- cwd 写 task: kimi-code-meta/ 仓根
- **禁止** 改 packages/** · apps/** 产品代码
- **禁止** git commit / push（除非 user 明确要求）
- **禁止** 开上游 PR · changeset · graph:issue-sync 关账（30/40 帽）
- **禁止** 仅聊天输出结论就结束 — **必须** 编辑 task §5

真值帽规：
- docs/harness/prompts/10-requirements.md
- docs/harness/FRAGMENT_rethink_backfill_task_v1_zh.md
- docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md（22 退回清单 · residual_risks 验收口径）
- docs/tasks/TASK_TEMPLATE_upstream_pr_v1.md §5（R0–R5 结构）

读序（@ 相对 kimi-code 或 kimi-code-meta）：
1. ../kimi-code-meta/docs/tasks/active/task_fix_approve_once_437_v1.md（§1–§8 · 当前 §5 待填）
2. ../kimi-code-meta/docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_20260618.md（B1 阻塞 · 需 10 回填清单）
3. ../kimi-code-meta/docs/_tech_graph/10_flow_cli_session.graph.yaml
4. https://github.com/MoonshotAI/kimi-code/issues/437（Issue + comment 复现）
5. packages/agent-core/src/agent/permission/index.ts（resolveSessionApprovalRule · recordApprovalResult）
6. packages/agent-core/src/agent/permission/policies/session-approval-history.ts
7. packages/agent-core/test/agent/permission.test.ts（#437 Write 用例 · Bash session 用例）
8. apps/kimi-code/src/tui/reverse-rpc/approval/adapter.ts · controller.ts · handler.ts
9. apps/kimi-code/test/tui/reverse-rpc/approval-adapter.test.ts

═══════════════════════════════════════════════════════════
 Invoke 快照（开帽第 0 步 · 硬）
═══════════════════════════════════════════════════════════

落盘本 user 消息全文：
docs/harness/invokes/by-task/fix-approve-once-437/invoke_YYYYMMDD_10_fix-approve-once-backfill.md

═══════════════════════════════════════════════════════════
 10 交付（mandatory · 写 task 文件）
═══════════════════════════════════════════════════════════

【A · 扩展 task §5 结构】
将当前 §5「思考轮控制」单表，扩展为 TASK_TEMPLATE §5 完整形态：
- ### 思考轮控制（Agent 填 · 22 审）
- ### R0 · 读 task
- ### R1 · 代码事实（禁止方案）
- ### R2 · 方案对比
- ### R3 · 边界 / 安全
- ### R4 · 测试与 PR 策略
- ### R5 · 图谱 + 关账判断
每轮含 **回填区：** ```text ... ``` · 替换全部 `（待 10）` / `（待填）`

【B · 思考轮控制 · 必填字段】
| 字段 | 要求 |
|------|------|
| actual_last_round | 填 `R5` 或实际末轮（**禁止** `（待 10）`） |
| early_stop | `no` / `yes`（本 bugfix 预期 `no` · 与 clean diff 一致则填 no） |
| early_stop_reason | early_stop=no 时写 `—` |
| residual_risks | 逐条 · 须含 R1 审查建议口径（见下） |

residual_risks 须覆盖（可合并为 2–3 条）：
- Write/Edit **工具名** session 缓存 vs Bash **命令级** 缓存 · manual 验收差异
- session 缓存不覆盖 explicit deny rule
- Approve once：第二次同类 Write **仍**弹窗
- 脏分支 `feature/fix-437-approve-once` 可能含 #94 read · 30 须用 **clean** 分支

【C · 各轮要点（写入回填区 · 非提纲）】

R0 · 读 task + Issue #437
- 现象 · comment（目录多 Write · session 仍多次弹窗）
- 预期：Approve once 不写 session · Approve for session 写 sessionApprovalRule
- task 元信息 · graph_delta · 分支纪律 · §8 aspirational 备注

R1 · 代码事实（禁止方案）
- TUI：ApprovalPanel 四选项 → adaptPanelResponse（approved vs approved_for_session → scope）
- ApprovalController.autoResolveFor（同 action + session scope 队列）
- PermissionManager.requestToolApproval → resolveSessionApprovalRule（Write/Edit → 工具名；Bash → 完整规则）
- session-approval-history 如何匹配 pattern
- 现有测试：#437 Write 多 path · Bash session 复用 · deny 不被 session 覆盖
- clean 分支 `98f1fa5f` vs 脏分支警示

R2 · 方案对比
- A：resolveSessionApprovalRule 工具名粒度（已实现 · 推荐）
- B：TUI/controller 层改（弃选 · 根因在 agent-core 缓存 key）
- C：放宽 matchesRule 全局（弃选 · 安全边界）
- 推荐 A + 理由 · 与 Issue 语义对齐

R3 · 边界 / 安全
- Write/Edit 同会话不同 path · Bash 不同 command · Approve once 不复用
- deny rule 优先 · yolo/auto 模式与 #437 关系（非本 Issue 主路径）
- Edit 代码对称 · 测试仅 Write（30 可选补 Edit 镜像 · 非阻塞）

R4 · 测试与 PR 策略
- permission.test.ts 用例表 + pnpm 命令
- TUI approval-adapter / controller 覆盖面
- PR：仅 agent-core 2 文件 · Fixes #437 · changeset patch · 禁止 harness/docs 进上游
- G0：feature/fix-437-approve-once-clean from upstream/main

R5 · 图谱 + 关账判断
- 10_flow_cli_session skeleton 与修复语义一致 · 10_flow_agent_turn 仅备注
- graph:issue-sync 关账时机（30 G3 · meta SHA 回填 §8）
- 结论：`可 22 复审` / `【停止 · 原因】` / `【需更多轮 · 提纲】`

【D · 可选 · §8 备注列】
将 aspirational ✅ 改为可审计表述，例如：
- 产品 Write session 粒度 →「本地 clean `98f1fa5f` 已验证 · 待 upstream PR」
- graph_issue_sync →「L3 mock 绿 · 待 G3 关账 SHA」

【E · 禁止改】
- §1–§3 需求/failure_paths（除非发现事实错误 · 须注明）
- 人工闸表 HG-TASK-DRAFT / HG-AUDIT-R1 状态（10 不签 HG-AUDIT-R1）
- batch 其它 flow YAML

═══════════════════════════════════════════════════════════
 回报格式 · 硬
═══════════════════════════════════════════════════════════

## 回填自检
| 项 | 状态 |
|----|------|
| §5 思考轮控制 actual_last_round | |
| R0–R5 回填区无 `（待填）` | |
| residual_risks 含验收口径 | |
| §8 备注（若改） | |
| 未改产品代码 | |
| 未 commit | |

## invoke_snapshot 路径
## 下一棒
回填完成 → 维护者确认 → [`PROMPT_START_22_v1.md`](./PROMPT_START_22_v1.md) 22 R1 **复审**
```

---

## 4. task §5 目标结构（参考 · 10 Agent 落盘）

> 完整模板见 [`TASK_TEMPLATE_upstream_pr_v1.md`](../../../../tasks/TASK_TEMPLATE_upstream_pr_v1.md) §5。

```markdown
## 5. Kimi Code Agent · 思考轮次（改码前 · R0 + R1–R5）

> invoke：本文件 · 回填协议：FRAGMENT_rethink_backfill_task_v1_zh.md

### 思考轮控制（Agent 填 · 22 审）

| 字段 | 值 |
|------|-----|
| **actual_last_round** | `R5` |
| **early_stop** | `no` |
| **early_stop_reason** | `—` |
| **residual_risks** | （逐条） |

### R0 · 读 task
**回填区：** …

### R1 · 代码事实
**回填区：** …

（R2–R5 同上）
```

---

## 5. 帽序（本 task · 当前位）

```text
10-task（本 Prompt · §5 回填）← 你在这里
  → 22 R1 复审（PROMPT_START_22_v1.md）
  → 维护者签 HG-AUDIT-R1 approved
  → 30 G0–G3（PROMPT_START_30_v1.md）
  → 40 · graph:issue-sync 关账 · task → done/
```

---

## 6. 与 22 审查对齐（B1 清单）

| # | 22 要求 | 10 动作 |
|---|---------|---------|
| 1 | `actual_last_round` 删除 `（待 10）` | 思考轮控制表 |
| 2 | R0–Rn 事实链 | R0–R5 回填区 |
| 3 | residual_risks 验收口径 | 控制表 + R3/R4 回填 |
| 4 | §8 aspirational 备注 | 可选 §8 备注列 |
