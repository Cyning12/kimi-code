# 启动 Prompt · 30 执行 · meta-graph-issue-sync-gate

> **用法**：Open Folder **`kimi-code-meta/`**（`cyning/meta`）→ **新对话** → 复制下方 **§3 代码块** 全文。  
> **task**：[`docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md`](../../../../tasks/active/task_meta_graph_issue_sync_gate_v1.md)  
> **审查**：[`docs/harness/reviews/task_meta_graph_issue_sync_gate_v1_audit_R1_20260618.md`](../../../reviews/task_meta_graph_issue_sync_gate_v1_audit_R1_20260618.md)  
> **工作区副本**：`Projects/docs/harness/invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_30_v1.md`

| 项 | 值 |
| --- | --- |
| **task_slug** | `meta-graph-issue-sync-gate` |
| **git_branch** | `cyning/meta` |
| **npm harness** | `@cyning/harness@2.0.1` |
| **test_strategy** | `required`（L2/L3 pytest · #437 mock） |
| **graph_delta** | `none`（门禁脚本 · 不增量单 flow） |
| **HG-AUDIT-R1** | **approved**（2026-06-18 · 须读表核验） |

---

## 1. 开帽第 0 步（Agent 自动 · 非维护者手跑）

```bash
cd kimi-code-meta && git checkout cyning/meta
npx @cyning/harness verify --target . --task docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md
```

**首输出**（改码前 · 见 `FRAGMENT_30_gate_verify_v1_zh.md`）：人工闸扫描表 + verify 摘要；**未过则零 diff STOP**。

---

## 2. 前置检查（维护者可选）

```bash
grep 'HG-AUDIT-R1' docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md | grep -q approved \
  || { echo "STOP: HG-AUDIT-R1 未 approved"; exit 1; }
grep -q 'actual_last_round.*R3' docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md \
  || { echo "STOP: §9 未闭合"; exit 1; }
pnpm graph:compile:check || { echo "STOP: L1 未绿"; exit 1; }
echo "OK: 可开 30"
```

---

## 3. 启动 Prompt（复制整段）

```text
你是 **30 执行 Agent**（meta graph · Issue 同步门禁 L2/L3 · G0–G3 · #437 启用前）。

【开帽 · GATE_VERIFY · 缺一 STOP】
- Open Folder: **kimi-code-meta/** · 分支 **cyning/meta**
- cwd: kimi-code-meta/ 仓根
- **真值**：读 task 人工闸表（非聊天声称）：
  - HG-TASK-DRAFT: approved
  - HG-AUDIT-R1: **须 approved** · pending → STOP（零 diff）
  - HG-SYNC-GATE-CLOSE: pending（G3 关账后人签）
- task §9 已闭合 · actual_last_round=R3
- **禁止** 改 apps/ · packages/ · Moonshot upstream PR
- **禁止** 同 PR / 同会话混 #437 feature/*
- **禁止** 改 Ink 子仓 · 回改 batch 六图 YAML（测试 mock 除外）

【首输出 · 硬 · 先于任何改码】
1. 读 docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md 人工闸表
2. 运行：npx @cyning/harness verify --target . --task docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md
3. 输出「人工闸扫描（GATE_VERIFY）」表（FRAGMENT_30_gate_verify_v1_zh.md 形状）
4. reviews：task_meta_graph_issue_sync_gate_v1_audit_R1_20260618.md 存在且 R1 通过？
5. 结论：STOP 或 可进入 G0

落盘 invoke 快照（开帽第 0 步）：
docs/harness/invokes/by-task/meta-graph-issue-sync-gate/invoke_YYYYMMDD_30_issue-sync-gate.md

读序：
1. docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md（§2 L1–L4 · §3 G0–G3 · §12.1）
2. docs/harness/reviews/task_meta_graph_issue_sync_gate_v1_audit_R1_20260618.md
3. docs/_tech_graph/01_struct.md · docs/_tech_graph/*.graph.yaml（L1 已有 · 6 图）
4. tools/tech_graph/（L1 五脚本 · 复用 compile/export）
5. docs/harness/prompts/30-execute-code.md · FRAGMENT_30_gate_verify_v1_zh.md
6. Projects/docs/harness/guides/PILOT_kimi_code_fork_adoption_v1_zh.md §5.2 · PLAN §4.1′

═══════════════════════════════════════════════════════════
 G0 · graph_module_flow_map.yaml
═══════════════════════════════════════════════════════════

【交付】
- docs/_tech_graph/graph_module_flow_map.yaml
- 以 task §12.1 YAML draft v0.1 为底 · 覆盖 §2.3
- 文件头：增 module 须同步 01_struct + map

【验收】
- cli → 10_flow_cli_session.graph.yaml（#437）
- agent_core 默认 + read/skill/context 专链（priority 启发式）
- node_sdk → warn · monorepo_root → skip/none

建议 commit：feat(tech_graph): add graph_module_flow_map for L3 sync gate

═══════════════════════════════════════════════════════════
 G1 · L2 graph_task_close_check.py
═══════════════════════════════════════════════════════════

【交付】
- tools/tech_graph/graph_task_close_check.py
- CLI: --task docs/tasks/active/task_*.md
- 解析 graph_delta · graph_delta_note
- 子进程 pnpm graph:compile:check（L1 失败 → L2 exit 1）
- 02_version.md 含 slug/issue → WARN（可 --strict）

【pytest ≥3】tests/tech_graph/test_issue_sync_gate.py
- delta 有 yaml diff → PASS
- delta 无 diff → FAIL exit 1
- graph_delta=none + note → PASS

【G1 未绿 → 禁止 G2】

═══════════════════════════════════════════════════════════
 G2 · L3 graph_product_sync_check.py
═══════════════════════════════════════════════════════════

【交付】
- tools/tech_graph/graph_product_sync_check.py
- --product-root ../kimi-code · --product-ref upstream/main...HEAD · --task …
- --allow-graph-none --reason（无 reason → exit 2）
- diff apps/ packages/ → map → 期望 flow

【#437 mock · 必测】
- apps/kimi-code/** → cli → cli_session · meta 无 diff → exit 1
- 补 YAML → exit 0
- 产品触模块 + task graph_delta=none → exit 2

【worktree】../kimi-code 不存在 → exit 2 + 可读 message

建议 commit：feat(tech_graph): L2/L3 issue sync gate checks

═══════════════════════════════════════════════════════════
 G3 · 聚合 · 纪律 · 关账准备
═══════════════════════════════════════════════════════════

【package.json】pnpm graph:issue-sync 串 L1→L2→L3
  --task · --product-root · --product-ref

【文档】
- docs/tasks/TASK_TEMPLATE_upstream_pr_v1.md：product_worktree · product_base_ref · meta_graph_commit · upstream_pr_commit · graph_issue_sync
- docs/harness/prompts/FRAGMENT_30_gate_verify_v1_zh.md 或关账段链指 L2/L3
- task §12 回填 · freeze_id KIMI-META-GRAPH-SYNC-GATE@<short-sha>

【验证】
pytest tests/tech_graph/test_issue_sync_gate.py -q
pnpm graph:issue-sync \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD

npx @cyning/harness@2.0.1 gate-check --target . --task docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md

【invoke】落盘 30 快照 · 更新 Projects pointer（可选）

【关账】维护者签 HG-SYNC-GATE-CLOSE · task → done/

git diff --name-only HEAD~3 -- docs/_tech_graph/ tools/ tests/ package.json docs/tasks/
# 期望：map · L2/L3 · pytest · 无 apps/ packages/

═══════════════════════════════════════════════════════════
 非范围（STOP）
═══════════════════════════════════════════════════════════
- #437 产品 fix · feature/fix-437-*
- batch migrate 回改 · 手改 .md 图源
- graph_query · HGM ingest · cyning-harness npm 内建 L3
- pre-commit 强制（仅 optional 文档）

【回报格式 · 硬】
## GATE_VERIFY 首输出表
## G0–G3 交付路径清单
## pytest + graph:issue-sync 输出摘要
## freeze_id / task §12 回填
## meta commit SHA 列表
## Blockers
## 下一棒：40 · HG-SYNC-GATE-CLOSE
```

---

## 4. 帽序

```text
G0 map → G1 L2 + pytest → G2 L3 + #437 mock → G3 pnpm + template/FRAGMENT
  → 40 → HG-SYNC-GATE-CLOSE → #437 task
```
