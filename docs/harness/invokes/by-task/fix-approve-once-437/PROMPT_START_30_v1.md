# 启动 Prompt · 30 执行 · fix-approve-once-437

> **用法**：Open Folder **`kimi-code/`**（产品仓）→ **新对话** → 复制 **§3 代码块** 全文。  
> **前置**：10 §5 闭合 · 22 R1 复审 **通过** · **HG-AUDIT-R1 approved**（2026-06-18 · 须读 task 表核验）  
> **task（meta）**：[`docs/tasks/active/task_fix_approve_once_437_v1.md`](../../../../tasks/active/task_fix_approve_once_437_v1.md)  
> **审查**：[`task_fix_approve_once_437_v1_audit_R1_20260618_reaudit.md`](../../reviews/task_fix_approve_once_437_v1_audit_R1_20260618_reaudit.md)  
> **Issue**：[MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437)

| 项 | 值 |
| --- | --- |
| **task_slug** | `fix-approve-once-437` |
| **产品分支** | **`feature/fix-437-approve-once-clean`**（`98f1fa5f` · 仅 agent-core 2 文件） |
| **脏分支（禁止 PR）** | `feature/fix-437-approve-once`（可能含 #94 read） |
| **meta 分支** | `cyning/meta`（G3 关账 · 勿混上游 PR） |
| **已有修复 commit** | `98f1fa5f`（= `eedd430c` 语义 · clean cherry-pick） |
| **HG-AUDIT-R1** | **approved**（2026-06-18 · 读 task 人工闸表核验） |
| **harness** | `npx @cyning/harness verify` |

---

## 1. 背景（给接棒 Agent）

- **现象**：TUI「Approve once」与「Approve for session」表现相同；同会话后续 Write 仍重复弹窗（[#437](https://github.com/MoonshotAI/kimi-code/issues/437)）。
- **思考轮**：task §5 R0–R5 已闭合 · R4 含测试/PR 策略 · 22 R1 复审零内容阻塞。
- **meta 已就绪**：`10_flow_cli_session.graph.yaml` skeleton · `yaml_edit_before_30` 已满足。
- **产品修复已存在**：clean 分支 `feature/fix-437-approve-once-clean` · 单 commit `98f1fa5f` · `resolveSessionApprovalRule` + #437 测试。
- **30 主路径**：G0 验证 clean 分支 → G1 测试 → G2 upstream PR + changeset → G3 meta `graph:issue-sync` 关账。

---

## 2. 开帽前（核验 · 产品 + meta）

```bash
# meta · 闸 + L3（产品 ref 须在 clean 分支 HEAD）
cd kimi-code-meta && git checkout cyning/meta
grep 'HG-AUDIT-R1' docs/tasks/active/task_fix_approve_once_437_v1.md | grep -q approved \
  || { echo "STOP: HG-AUDIT-R1 未 approved"; exit 1; }
grep -q 'actual_last_round.*R5' docs/tasks/active/task_fix_approve_once_437_v1.md \
  || { echo "STOP: §5 未闭合"; exit 1; }

npx @cyning/harness verify --target . \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md

# 产品 · clean 分支纪律
cd ../kimi-code
git fetch upstream
git checkout feature/fix-437-approve-once-clean
git log --oneline upstream/main..HEAD          # 预期 98f1fa5f
git diff --stat upstream/main...HEAD | grep -v 'packages/agent-core' \
  && echo "STOP: diff 超出 agent-core" || echo "OK: clean diff"
```

---

## 3. 启动 Prompt（复制整段）

```text
你是 **30 执行 Agent**（#437 Approve once vs session · 产品修复 · 上游 PR · G0–G3）。

【Open Folder · 分支】
- 产品：**kimi-code/** · **`feature/fix-437-approve-once-clean`**
- meta（G3 关账）：**kimi-code-meta/** · `cyning/meta`
- **禁止** 用 `feature/fix-437-approve-once` 开上游 PR（可能含 #94 read.ts）

【GATE_VERIFY · 首输出 · 缺一 STOP】
1. 读 meta task 人工闸表：docs/tasks/active/task_fix_approve_once_437_v1.md
   - HG-TASK-DRAFT: approved
   - HG-AUDIT-R1: **须 approved** · task 表 pending → **零 diff STOP**
2. npx @cyning/harness verify --target ../kimi-code-meta \
     --task docs/tasks/active/task_fix_approve_once_437_v1.md
3. 输出「人工闸扫描（GATE_VERIFY）」表（docs/harness/prompts/FRAGMENT_30_gate_verify_v1_zh.md）
4. reviews：task_fix_approve_once_437_v1_audit_R1_20260618_reaudit.md · R1 复审通过？
5. §5 actual_last_round=R5 · 无 `（待填）`？
6. 结论：STOP 或 可进入 G0

落盘 invoke 快照（开帽第 0 步）：
docs/harness/invokes/by-task/fix-approve-once-437/invoke_YYYYMMDD_30_fix-approve-once.md

【真值 · 必读】
- task §1–§3 · §5 R4 测试表 · §8 备注
- docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_20260618_reaudit.md
- meta：docs/_tech_graph/10_flow_cli_session.graph.yaml
- 产品（clean 分支已含修复 · 以 verify 为准）：
  - packages/agent-core/src/agent/permission/index.ts（resolveSessionApprovalRule）
  - packages/agent-core/test/agent/permission.test.ts（#437 · approve once one-shot）
  - apps/kimi-code/src/tui/reverse-rpc/approval/（adapter · controller · 只读确认）
  - apps/kimi-code/test/tui/reverse-rpc/approval-adapter.test.ts

【交付顺序】

G0 干净分支（优先用已有 · 勿重建脏分支）
  git fetch upstream
  git checkout feature/fix-437-approve-once-clean
  git log --oneline upstream/main..HEAD
  git diff --stat upstream/main...HEAD
  # 仅当分支缺失：
  # git checkout -b feature/fix-437-approve-once-clean upstream/main
  # git cherry-pick 98f1fa5f

G1 验证（task §5 R4 · 须绿）
  pnpm --filter @moonshot-ai/agent-core test -- permission.test.ts
  pnpm --filter @moonshot-ai/kimi-code test -- test/tui/reverse-rpc/approval-adapter.test.ts

G2 changeset + 上游 PR（仅 packages/agent-core · 禁止 harness/docs/tasks）
  - gen-changesets skill · @moonshot-ai/agent-core patch
  - PR title Conventional Commit · **Fixes #437**
  - 说明：Write/Edit approve-for-session 缓存工具名 · Bash 仍命令级 · Approve once 不写 session pattern
  - 填 .github/pull_request_template.md

G3 meta 关账（cyning/meta · 另 commit · 非上游 PR）
  cd ../kimi-code-meta
  pnpm graph:issue-sync \
    --task docs/tasks/active/task_fix_approve_once_437_v1.md \
    --product-root ../kimi-code \
    --product-ref upstream/main...HEAD
  回填 task §8：upstream_pr_commit · graph_issue_sync SHA
  §6 勾选 · task → docs/tasks/done/（40 或维护者确认）

【非范围 · STOP】
- 混入 #94 read.ts · harness · docs/tasks 进上游 PR
- 改 batch 六图 YAML（本 task skeleton 已 commit）
- 未跑 graph:issue-sync 即 claim done
- 重复实现已在 98f1fa5f 的修复（除非测试红）

【回报格式】
## 人工闸扫描（GATE_VERIFY）
## G0 分支 / diff 摘要
## G1 测试输出摘要
## G2 PR URL · commit SHA · changeset
## G3 graph:issue-sync 摘要 · task 关账
## Blockers
```

---

## 4. 帽序与维护者清单

| 步骤 | 状态 |
| --- | --- |
| 10 §5 回填 | ✅ |
| 22 R1 复审 | ✅ |
| **HG-AUDIT-R1** | ✅ approved（2026-06-18） |
| 30 G0–G2 上游 PR | 待执行 |
| G3 graph:issue-sync · task → `done/` | 待 30/40 |

- [ ] 上游 PR 仅 `packages/agent-core`（+ `.changeset`）
- [ ] `pnpm graph:issue-sync` exit 0
- [ ] task §6 勾选 · 归档 `docs/tasks/done/`
