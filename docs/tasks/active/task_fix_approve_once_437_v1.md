# Task：修复 Approve once vs session 无差异 · #437（阶段 C）

> **状态**：`active` · HG-TASK-DRAFT **approved**（2026-06-18）  
> **前序**：`[task_meta_graph_issue_sync_gate_v1.md](../done/task_meta_graph_issue_sync_gate_v1.md)` **CLOSE**  
> **上游 Issue**：[MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437)  
> **关联图谱**：`[10_flow_cli_session.graph.yaml](../../_tech_graph/10_flow_cli_session.graph.yaml)` · `[01_struct.md](../../_tech_graph/01_struct.md)` `cli`  
> **试点真值**：`[POINTER_PILOT_adoption_workspace_v1_zh.md](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)`

---

## Harness 元信息


| 字段                       | 值                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **task_slug**            | `fix-approve-once-437`                                                                                      |
| **test_strategy**        | `required`                                                                                                  |
| **test_strategy_note**   | TUI approval reverse-rpc · agent-core permission session 缓存 · Write 同目录复用                                   |
| **code_quality_bar**     | `strict`                                                                                                    |
| **track**                | `bugfix`                                                                                                    |
| **orchestration**        | **10-task**（R0–R5）→ **20** → **30** → **40**                                                                |
| **audit_profile**        | `human_only`                                                                                                |
| **git_branch**           | `feature/fix-437-approve-once`（产品）· meta 图谱 `cyning/meta`                                                   |
| **worktree_root**        | `/Users/cyning/Desktop/Projects/kimi-code`                                                                  |
| **meta_worktree**        | `/Users/cyning/Desktop/Projects/kimi-code-meta`                                                             |
| **product_worktree**     | `/Users/cyning/Desktop/Projects/kimi-code`                                                                  |
| **product_base_ref**     | `upstream/main...HEAD`                                                                                      |
| **module_id**            | `cli`                                                                                                       |
| **graph_delta**          | `10_flow_cli_session.graph.yaml` · `10_flow_agent_turn.graph.yaml`                                          |
| **graph_delta_note**     | —                                                                                                           |
| **graph_gate**           | `yaml_edit_before_30` · `close_partial_or_final`                                                            |
| **entry_invoke_10_task** | `[docs/harness/invokes/by-task/fix-approve-once-437/](../../harness/invokes/by-task/fix-approve-once-437/)` |


### 人工闸


| human_gate_id | status   | blocks_hats | 说明                               |
| ------------- | -------- | ----------- | -------------------------------- |
| HG-TASK-DRAFT | approved | 20-R1, 30   | meta skeleton 已 commit · 可 30 产品 |
| HG-AUDIT-R1   | pending  | 30          | 20 R1 + 人签                       |


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


| 字段              | 值                                           |
| --------------- | ------------------------------------------- |
| **Open Folder** | `kimi-code`                                 |
| **必读**          | 本 task · `10_flow_cli_session` · Issue #437 |
| **禁止**          | 10 会话改产品码（可选补 §5）                           |


### 必读路径


| 路径                                                                    | 用途           |
| --------------------------------------------------------------------- | ------------ |
| `../kimi-code-meta/docs/tasks/active/task_fix_approve_once_437_v1.md` | 本 task       |
| `../kimi-code-meta/docs/_tech_graph/10_flow_cli_session.graph.yaml`   | 图谱 skeleton  |
| `apps/kimi-code/src/tui/reverse-rpc/approval/`                        | TUI 审批链      |
| `packages/agent-core/src/agent/permission/`                           | session 规则缓存 |


---

## 5. Kimi Code Agent · 思考轮次（待 10 回填）


| 字段                    | 值                         |
| --------------------- | ------------------------- |
| **actual_last_round** | （待 10）                    |
| **early_stop**        | no                        |
| **residual_risks**    | Write 会话粒度 vs 精确路径 · 安全边界 |


---

## 6. 验收标准

- [x] meta：`10_flow_cli_session.graph.yaml` skeleton + compile
- [ ] 产品：`feature/fix-437-approve-once` · 修复 + 测试
- [ ] `pnpm graph:issue-sync` exit 0
- [ ] 上游 PR · `Fixes #437`
- [ ] `HG-AUDIT-R1` approved · task → `done/`

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
git checkout -b feature/fix-437-approve-once
pnpm --filter @moonshot-ai/agent-core test -- permission.test.ts
pnpm --filter @moonshot-ai/kimi-code test -- test/tui/reverse-rpc/approval
```

---

## 8. 实现备忘


| 项                   | 状态  | 备注                                   |
| ------------------- | --- | ------------------------------------ |
| meta skeleton YAML  | ✅   | `e08a56b2` · `d76c4da5` · `1a89ab2e` |
| 产品 Write session 粒度 | ✅   | `kimi-code` `eedd430c`               |
| graph_issue_sync    | ✅   | L1+L2+L3 PASS                        |


