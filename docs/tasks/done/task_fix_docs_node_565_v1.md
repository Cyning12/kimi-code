# Task：对齐 npm 安装文档 Node 版本 · #565（阶段 C）

> **状态**：`done`  
> **上游 Issue**：[MoonshotAI/kimi-code#565](https://github.com/MoonshotAI/kimi-code/issues/565)  
> **上游 PR**：[MoonshotAI/kimi-code#622](https://github.com/MoonshotAI/kimi-code/pull/622)  
> **关联图谱**：`docs/_tech_graph/01_struct.md`（`monorepo_root` · 文档站）  
> **试点真值**：`[docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)`

---

## Harness 元信息


| 字段                     | 值                                                                      |
| ---------------------- | ---------------------------------------------------------------------- |
| **task_slug**          | `fix-docs-node-565`                                                    |
| **test_strategy**      | `recommended`                                                          |
| **test_strategy_note** | 文档 task；改后人工核对 en/zh 一致；可选 `pnpm lint`                                 |
| **orchestration**      | Cursor Task 链                                                          |
| **audit_profile**      | `human_only`                                                           |
| **git_branch**         | `feature/fix-565-docs-node`                                            |
| **worktree_root**      | `/Users/cyning/Desktop/Projects/kimi-code`（**产品改码** Open Folder）       |
| **meta_worktree**      | `/Users/cyning/Desktop/Projects/kimi-code-meta`（**过程轨** task / invoke） |


### 人工闸


| human_gate_id | status   | blocks_hats | 说明          |
| ------------- | -------- | ----------- | ----------- |
| HG-TASK-DRAFT | approved | 22-R1, 30   | task 初稿人扫   |
| HG-AUDIT-R1   | approved | 30          | 22 R1 落盘后人签 |


> `**HG-GRAPH-MODULES`** 已在阶段 B `01_struct` 签 `approved`；本 task 不重复签。

---

## 背景与目标

Getting Started 文档写 npm 安装需 Node.js **24.15.0+**，但 `apps/kimi-code/package.json` 声明 `engines.node >= 22.19.0`，与已发布 npm 包元数据不一致，易误导 Node 22 LTS 用户。

**完成态**：en/zh getting-started 中 npm 安装路径的 Node 版本说明与 package `engines` 一致（或明确区分 monorepo 开发 vs npm 用户；本 task 采用 **对齐 engines**）。

---

## 范围

- [x] `docs/en/guides/getting-started.md` — npm 安装 Node 要求
- [x] `docs/zh/guides/getting-started.md` — 同上（中文）

## 非范围

- 修改 `package.json` engines（除非维护者另开 task）
- 安装脚本 / CDN / 其它文档页
- 向 Moonshot PR `docs/harness`、`docs/tasks`、`.cursor` 等过程轨文件

---

## 失败路径


| 触发条件                          | 系统行为          | 可重试 | 用户可见                  |
| ----------------------------- | ------------- | --- | --------------------- |
| `HG-AUDIT-R1` pending 即 30 改码 | Agent **拒开工** | 是   | 先 22 + 人签             |
| PR diff 含 harness 路径          | 维护者拒合并 / 自检失败 | 是   | 仅 `feature/*` 产品 diff |
| en/zh 版本号不一致                  | 验收不通过         | 是   | 两文件须同步改               |


---

## 验收标准

- [x] en/zh getting-started npm 段 Node 版本与 `>=22.19.0` 一致（或等价表述）
- [x] `git diff upstream/main --name-only` 仅含 `docs/**` 预期路径
- [x] 上游 PR 正文含 `Fixes #565`
- [x] invoke 落盘 `docs/harness/invokes/by-task/fix-docs-node-565/`

---

## 给执行帽的必读列表

1. 仓根 `AGENTS.md`（产品纪律）
2. `docs/_tech_graph/01_struct.md` — `HG-GRAPH-MODULES` 已 approved
3. `apps/kimi-code/package.json` — `engines.node`
4. 本 task · Issue #565 正文

---

## 验证命令

```bash
# 在 feature 分支 worktree（kimi-code）执行
rg "Node.js|node" docs/en/guides/getting-started.md docs/zh/guides/getting-started.md
# 可选
pnpm lint
```

---

## 环境配置（本机 · 2026-06-10）


| 路径                        | 分支                          | 用途                                    |
| ------------------------- | --------------------------- | ------------------------------------- |
| `Projects/kimi-code`      | `feature/fix-565-docs-node` | Open Folder · 改文档 · PR                |
| `Projects/kimi-code-meta` | `cyning/meta`               | task · invoke · `@` harness prompts   |
| `Projects/cyning-harness` | —                           | 可选 `gate-check.sh`；日常用 meta 内嵌 prompt |


**30 会话 @ 列表**（Open Folder = `kimi-code` feature）：

```text
@../kimi-code-meta/docs/tasks/active/task_fix_docs_node_565_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md
```

---

## 给维护者

1. 在 **meta** 上 `@` `22-task-audit.md` 审计本 task
2. 将 `HG-TASK-DRAFT`、`HG-AUDIT-R1` 改为 `approved` 并 commit `cyning/meta`
3. 切 **feature** 开 30 改码 → push → `gh pr create` → Moonshot
4. invoke 与 task 关账 commit 回 **meta**

---

## 实现备忘（子 Agent 回填）


| 项         | 状态  | 备注                                                                 |
| --------- | --- | ------------------------------------------------------------------ |
| 文档 diff   | ✅   | commit `d6fa7c96` · en/zh getting-started npm 段 22.19.0            |
| 上游 PR URL | ✅   | https://github.com/MoonshotAI/kimi-code/pull/622                   |


### 自检结论（执行者）

- 人工闸：HG-TASK-DRAFT / HG-AUDIT-R1 均为 `approved`，30 开工合法。
- 改码：npm 安装段 `24.15.0` → `22.19.0`，与 `engines.node >=22.19.0` 一致；en/zh 同步。
- 验证：`rg` 通过；`git diff upstream/main --name-only` 仅两文件。
- 上游：PR #622 已开，正文含 `Fixes #565`；待 Moonshot 维护者 review / merge。
- invoke：`docs/harness/invokes/by-task/fix-docs-node-565/invoke_20260610_30_fix-docs-node-565.md`
