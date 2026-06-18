# 启动 Prompt · 22 任务审核 · fix-approve-once-437

> **用法**：Open Folder **`kimi-code-meta/`**（`cyning/meta`）→ **新对话** → 复制下方 **§3 代码块** 全文。  
> **前置**：meta skeleton 已 commit · **HG-TASK-DRAFT approved**（2026-06-18）  
> **task**：[`docs/tasks/active/task_fix_approve_once_437_v1.md`](../../../../tasks/active/task_fix_approve_once_437_v1.md)  
> **Issue**：[MoonshotAI/kimi-code#437](https://github.com/MoonshotAI/kimi-code/issues/437)  
> **下一帽（审查通过后）**：维护者签 **HG-AUDIT-R1** → [`PROMPT_START_30_v1.md`](./PROMPT_START_30_v1.md)

| 项 | 值 |
| --- | --- |
| **task_slug** | `fix-approve-once-437` |
| **auditor_hat** | `22-task-audit`（真值 [`22-task-audit.md`](../../prompts/22-task-audit.md)） |
| **git_branch（meta）** | `cyning/meta` |
| **产品只读** | `../kimi-code` · `feature/fix-437-approve-once-clean` |
| **审查轮次** | R1（首轮） |
| **test_strategy** | `required`（permission.test.ts · TUI approval reverse-rpc） |
| **blocks_hats** | `HG-AUDIT-R1` pending → **30 拒开工** |

---

## 1. 背景（给接棒 Agent）

- **现象**：TUI「Approve once」与「Approve for session」无差异；同会话多次 **Write** 选 session 仍重复弹窗（#437）。
- **meta 已就绪**：`10_flow_cli_session.graph.yaml` skeleton · `graph:compile:check` 绿 · commit `e08a56b2` 等。
- **产品已有本地修复**：`eedd430c` / 干净分支 `98f1fa5f`（cherry-pick 到 `upstream/main`）· 仅 `packages/agent-core` 2 文件。
- **已知风险**：`feature/fix-437-approve-once` 若从 `#94 read` 分支切出含 **read.ts** · 不可进上游 PR；task §5 思考轮 **可能未回填**。

---

## 2. 开帽前（只读核验）

```bash
cd kimi-code-meta && git checkout cyning/meta

test -f docs/tasks/active/task_fix_approve_once_437_v1.md \
  || { echo "STOP: task 不存在"; exit 1; }

grep -q 'HG-TASK-DRAFT.*approved' docs/tasks/active/task_fix_approve_once_437_v1.md \
  || { echo "STOP: HG-TASK-DRAFT 未 approved"; exit 1; }

npx @cyning/harness verify --target . \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md

# 产品干净分支（只读交叉验证 · 不 commit）
cd ../kimi-code
git fetch upstream
git log --oneline upstream/main..feature/fix-437-approve-once-clean 2>/dev/null \
  || echo "NOTE: clean 分支未建 · 30 G0 待做"

git diff --stat upstream/main...feature/fix-437-approve-once-clean 2>/dev/null \
  | grep -v 'packages/agent-core' && echo "WARN: diff 超出 agent-core" || true
```

---

## 3. 启动 Prompt（复制整段）

```text
你是 **22 任务审核 Agent**（#437 Approve once vs session · 产品 bugfix · 思考轮审查 · R1）。

【开帽 · GATE_SCAN · 缺一 STOP】
- HG-TASK-DRAFT: **approved** ✓（2026-06-18）
- HG-AUDIT-R1: **pending**（本帽不代签 · 通过后人签）
- Open Folder（执行）: **kimi-code-meta/** · 分支 **cyning/meta**
- Open Folder（只读）: **kimi-code/** · 分支 **feature/fix-437-approve-once-clean**（或核对 eedd430c diff）
- cwd: kimi-code-meta/ 仓根
- **禁止** 改 packages/agent-core · apps/kimi-code（30 帽）
- **禁止** 开上游 PR · changeset · graph:issue-sync 关账（30 帽）
- **禁止** 擅自改写 task 正文（阻塞仅写「需 10-task 回填清单」· 退回 10）
- **禁止** HG-AUDIT-R1 仍为 pending 时附「已 approved」的 30 Prompt

真值帽规：
- docs/harness/prompts/22-task-audit.md
- docs/harness/prompts/FRAGMENT_30_gate_verify_v1_zh.md
- docs/harness/reviews/README.md（落盘命名）
- docs/harness/HARNESS_V2_PLAN.md §5（test_strategy · failure_paths）

读序（@ 相对 kimi-code-meta 或 ../kimi-code）：
1. docs/tasks/active/task_fix_approve_once_437_v1.md（§1–§8 · 人工闸表 · 验收 §6）
2. docs/tasks/done/task_meta_graph_issue_sync_gate_v1.md（前序 CLOSE · graph:issue-sync 纪律）
3. docs/_tech_graph/10_flow_cli_session.graph.yaml · 10_flow_cli_session.md
4. docs/_tech_graph/10_flow_agent_turn.graph.yaml（graph_delta 备注 · 只读）
5. ../kimi-code/packages/agent-core/src/agent/permission/index.ts（resolveSessionApprovalRule）
6. ../kimi-code/packages/agent-core/test/agent/permission.test.ts（Write/Edit 同会话用例）
7. ../kimi-code/apps/kimi-code/src/tui/reverse-rpc/approval/（adapter · controller · handler · 只读）
8. https://github.com/MoonshotAI/kimi-code/issues/437（Issue 原文 · comment 复现路径）

═══════════════════════════════════════════════════════════
 Invoke 快照（开帽第 0 步 · 硬）
═══════════════════════════════════════════════════════════

落盘本 user 消息全文：
docs/harness/invokes/by-task/fix-approve-once-437/invoke_YYYYMMDD_22_fix-approve-once-r1.md

审查 md 元信息须填 **invoke_snapshot** 链回该文件。

═══════════════════════════════════════════════════════════
 审查职责（R1 · 本帽交付）
═══════════════════════════════════════════════════════════

【1 · Harness 字段】
- test_strategy: required · TUI approval · session 缓存 · Write 同目录复用
- code_quality_bar: strict · track: bugfix
- graph_delta: 10_flow_cli_session · 10_flow_agent_turn（备注）
- graph_gate: yaml_edit_before_30 · close_partial_or_final
- product_base_ref: upstream/main...HEAD · 双 worktree 是否写清
- failure_paths §3（无 skeleton · HG-AUDIT-R1 pending · PR 无 meta commit · graph:issue-sync 失败）
- 人工闸：HG-TASK-DRAFT · HG-AUDIT-R1

【2 · 思考轮审查（§5 · 必做）】
核对项：
- actual_last_round · early_stop · residual_risks 是否已填 · 无裸「（待 10）」「（待填）」
- 若 §5 未闭合 → **退回 10-task** · 禁止建议签 HG-AUDIT-R1
- residual_risks「Write 会话粒度 vs 精确路径 · 安全边界」是否在 R1 有明确验收口径
- early_stop = no 是否与产品 diff 范围一致

不通过 → 审查文 **「退回 10-task」** 清单 · **禁止** 附 30 Prompt。

【3 · 需求 / 修复方案 / #437 语义】
- Approve once：仅当次 · 不写入 session 规则
- Approve for session：写入 sessionApprovalRule · 后续匹配免弹窗
- resolveSessionApprovalRule：Write/Edit + hasArgumentMatcher → 缓存 **工具名**（非完整 path 规则）
- Bash 等同命令仍走精确 approvalRule（与 Write/Edit 粒度差异是否合理 · 安全边界）
- TUI 链：ApprovalPanel 四选项 → ApprovalController → agent-core PermissionManager
- 与图谱 skeleton 节点 CS_SESSION_CACHE / CS_APPROVE_SESSION 是否语义一致

【4 · 分支纪律 / 非范围 / §8 真值漂移】
- 干净分支：upstream/main + 单 commit · **仅** packages/agent-core（2 文件）
- 禁止混入 #94 read.ts · harness · docs/tasks 进上游 PR
- task §8 预填（graph_issue_sync ✅ · 产品 ✅）vs 人工闸 HG-AUDIT-R1 pending · 验收 §6 未勾 — 是否标注 ** aspirational / 待 30 关账**
- 禁止改 batch 六图 YAML 真值（除 graph_delta 已列两张）

【5 · 验收 / 可测性 / 30 预演（只读）】
- permission.test.ts：Write 同会话复用 · Edit 同理 · Bash 精确规则
- test/tui/reverse-rpc/approval：adapter/controller 行为
- 若 clean 分支已存在：核对 `git diff upstream/main...HEAD` 范围 · 测试是否可绿（报告摘要即可 · 本帽不代跑 PR）
- G2 changeset 须 gen-changesets skill · 仅 agent-core patch/minor
- G3 meta 关账：graph:issue-sync + task §8 回填 meta_graph_commit · upstream_pr_commit

【6 · 落盘审查文档（硬 · 禁止仅口头「过了」）】
路径：
docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_YYYYMMDD.md

建议结构：
- 元信息（task_path · invoke_snapshot · 轮次 R1 · auditor_hat）
- 审查结论摘要（内容 / 流程闸分列）
- 思考轮审查表（§5）
- 需求与修复方案审查（#437 · resolveSessionApprovalRule）
- 分支纪律 / graph_delta / §8 漂移
- test_strategy / failure_paths / 验收 §6
- 阻塞 / 非阻塞
- 需 10-task 回填清单（若有）
- 人工闸审查意见（HG-AUDIT-R1 建议 · **不代签**）
- 维护者签闸清单（HG-AUDIT-R1 pending 时 **禁止** 附 30 Prompt）

【7 · commit 纪律】
审查 md + invoke 快照落盘后，在 **kimi-code-meta** commit（cyning/meta）。
用户本轮写明「不要 commit」则跳过 · 对话末尾报 short-hash 或「未 commit」。

═══════════════════════════════════════════════════════════
 通过 / 不通过 · 下一棒
═══════════════════════════════════════════════════════════

**R1 通过**（零内容阻塞 · 思考轮闭合 · 分支纪律清晰）：
1. 审查文：「思考轮审查：通过 · 建议 30 开工（须 task 表 HG-AUDIT-R1 = approved 后）」
2. 请维护者 task 表 **HG-AUDIT-R1** → `approved`（附日期）
3. 文末仅输出 **维护者签闸清单**（见 22-task-audit.md · **禁止** 附「已 approved」30 Prompt）

**R1 不通过**：
1. 「退回 10-task」逐条清单（补 §5 · 缺事实 · 图谱/需求不一致）
2. **禁止** 建议签 HG-AUDIT-R1 · **禁止** 30 Prompt

═══════════════════════════════════════════════════════════
 非范围（STOP）
═══════════════════════════════════════════════════════════
- G0–G3 产品实现 · 上游 PR · changeset
- graph:issue-sync 关账 · task → done/
- 代签 HG-AUDIT-R1
- 50 代码走查 · Bugbot
- 改 batch 其它 flow YAML

【回报格式 · 硬】
## 审查结论（通过 / 不通过 / 维持 pending）
## 思考轮审查表
## #437 修复方案审查摘要
## 分支纪律 / §8 漂移
## 阻塞 / 非阻塞
## 审查 md 路径 · invoke_snapshot 路径
## 维护者签闸清单（HG-AUDIT-R1）
## 下一棒（通过 → 维护者签闸后 PROMPT_START_30_v1.md · 不通过 → 10 清单）
```

---

## 4. 审查落盘路径（真值）

| 产出 | 路径 |
| --- | --- |
| **审查全文** | `docs/harness/reviews/task_fix_approve_once_437_v1_audit_R1_YYYYMMDD.md` |
| **Invoke 快照** | `docs/harness/invokes/by-task/fix-approve-once-437/invoke_YYYYMMDD_22_fix-approve-once-r1.md` |

---

## 5. 帽序（本 task）

```text
10-task（§5 思考轮 · 可选补全）
  → 22 R1（本 Prompt）→ reviews 落盘
  → 维护者签 HG-AUDIT-R1 approved
  → 30 G0–G3（PROMPT_START_30_v1.md · kimi-code 上游 PR）
  → 40 · meta graph:issue-sync 关账 · task → done/
```
