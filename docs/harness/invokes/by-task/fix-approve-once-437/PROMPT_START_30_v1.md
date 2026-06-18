# 启动 Prompt · 30 执行 · fix-approve-once-437

> **用法**：Open Folder **`kimi-code/`**（产品仓）→ **新对话** → 复制 **§3 代码块** 全文。  
> **task（meta）**：[`docs/tasks/active/task_fix_approve_once_437_v1.md`](../../../../tasks/active/task_fix_approve_once_437_v1.md)  
> **Issue**：[MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437)

| 项 | 值 |
| --- | --- |
| **task_slug** | `fix-approve-once-437` |
| **产品分支** | `feature/fix-437-approve-once`（须从 `upstream/main` 干净拉出 · 见 §3） |
| **meta 分支** | `cyning/meta`（图谱已 skeleton · 勿混上游 PR） |
| **已有修复 commit** | `eedd430c` — Write/Edit session 按工具名缓存 |
| **HG-AUDIT-R1** | **pending**（20 R1 或维护者签后 30 改码） |
| **harness** | `npx @cyning/harness@2.0.3 verify` |

---

## 1. 背景（给接棒 Agent）

- **现象**：TUI「Approve once」与「Approve for session」表现相同；同会话后续 Write 仍重复弹窗（[#437](https://github.com/MoonshotAI/kimi-code/issues/437)）。
- **meta 已就绪**：`10_flow_cli_session.graph.yaml` skeleton · `graph:issue-sync` 绿 · commit `e08a56b2` 等。
- **产品已有本地修复**：`packages/agent-core/src/agent/permission/index.ts` — session 审批对 Write/Edit 缓存 **工具名** 规则（`eedd430c`）。
- **阻塞**：当前 `feature/fix-437-approve-once` 若从 `#94 read` 分支切出，diff 含 **read.ts** · 不可进上游 PR。

---

## 2. 开帽前（meta · 只读核验）

```bash
cd kimi-code-meta && git checkout cyning/meta
npx @cyning/harness verify --target . \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md \
  --json --agent-hint
pnpm graph:issue-sync \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD
```

---

## 3. 启动 Prompt（复制整段）

```text
你是 **30 执行 Agent**（#437 Approve once vs session · 产品修复 · 上游 PR）。

【Open Folder · 分支】
- 产品：**kimi-code/** · 分支 `feature/fix-437-approve-once-clean`（从 upstream/main 新建）
- meta 只读：**kimi-code-meta/** · `cyning/meta`（图谱已 skeleton · 本 PR 禁止改 harness/task）

【GATE_VERIFY · 缺一 STOP】
1. 读 meta task 人工闸表：docs/tasks/active/task_fix_approve_once_437_v1.md
2. npx @cyning/harness verify --target ../kimi-code-meta --task docs/tasks/active/task_fix_approve_once_437_v1.md
3. HG-AUDIT-R1 pending → 仅当维护者已签 approved 后改码；否则 STOP 或只做 §4 分支整理

【真值 · 必读】
- task §1–§3 · Issue #437 原文
- meta：docs/_tech_graph/10_flow_cli_session.graph.yaml · 10_flow_cli_session.md
- 产品：
  - packages/agent-core/src/agent/permission/index.ts（sessionApprovalRule）
  - apps/kimi-code/src/tui/reverse-rpc/approval/（adapter · controller · handler）
  - packages/agent-core/test/agent/permission.test.ts（#437 Write 同会话用例）

【交付顺序】
G0 干净分支
  git fetch upstream
  git checkout -b feature/fix-437-approve-once-clean upstream/main
  git cherry-pick eedd430c   # 若冲突则手迁 resolveSessionApprovalRule + 测试

G1 验证
  pnpm --filter @moonshot-ai/agent-core test -- permission.test.ts
  pnpm --filter @moonshot-ai/kimi-code exec vitest run test/tui/reverse-rpc/approval

G2 changeset + PR（仅 packages/agent-core · 禁止 apps/kimi-code 无关改动）
  - Conventional PR · Fixes #437
  - 说明：Write/Edit approve-for-session 缓存工具名规则 · Bash 同命令仍走精确 approvalRule

G3 meta 关账（cyning/meta · 另 commit · 非上游 PR）
  cd ../kimi-code-meta
  pnpm graph:issue-sync --task docs/tasks/active/task_fix_approve_once_437_v1.md \
    --product-root ../kimi-code --product-ref upstream/main...HEAD
  回填 task §8：meta_graph_commit · upstream_pr_commit · graph_issue_sync

【非范围 · STOP】
- 混入 #94 read.ts · harness · docs/tasks 进上游 PR
- 改 batch 六图 YAML 真值（除本 task graph_delta 已列两张）
- 未跑 graph:issue-sync 即 claim done

【回报格式】
## GATE_VERIFY 表
## 分支 / cherry-pick 结果
## 测试输出摘要
## PR URL · commit SHA
## graph:issue-sync 摘要
## Blockers
```

---

## 4. 维护者签闸（可选）

- [ ] `HG-AUDIT-R1` → approved（20 R1 后）
- [ ] 上游 PR 仅 `packages/agent-core`
- [ ] meta `graph:issue-sync` exit 0 后 task → `done/`
