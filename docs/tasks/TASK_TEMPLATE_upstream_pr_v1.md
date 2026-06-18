# Task：<动词 + 范围> · #<issue>（阶段 C）

> **状态**：`draft`  
> **上游 Issue**：[MoonshotAI/kimi-code#xxx](https://github.com/MoonshotAI/kimi-code/issues/xxx)  
> **关联图谱**：`docs/_tech_graph/01_struct.md`（`module_id`）· **增量** `graph_delta` 见下表  
> **试点真值**：[`docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md`](../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)  
> **工作区 PILOT**：`Projects/docs/harness/guides/PILOT_kimi_code_fork_adoption_v1_zh.md` §5.2

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `<slug>` |
| **test_strategy** | `required` / `recommended` / `not_applicable` |
| **test_strategy_note** | （`not_applicable` 时必填） |
| **code_quality_bar** | `strict` |
| **track** | `bugfix`（上游 Issue）/ `feature`（须 SPEC 或显式跳过理由） |
| **orchestration** | **10-task**（R0–R5）→ **20** → 30 · V2 见工作区 `GUIDANCE_harness_hat_v2_chain_v1_zh.md` |
| **audit_profile** | `human_only` |
| **git_branch** | `feature/fix-<issue>-<short>` |
| **worktree_root** | `/path/to/kimi-code`（产品改码 Open Folder） |
| **meta_worktree** | `/path/to/kimi-code-meta` |
| **product_worktree** | `/path/to/kimi-code`（L3 · 默认 `../kimi-code`） |
| **product_base_ref** | `upstream/main...HEAD`（L3 产品 diff 基线） |
| **module_id** | `agent_core` / `monorepo_root` / …（来自 `01_struct`） |
| **graph_delta** | `10_flow_*.graph.yaml` **或** `none` |
| **graph_delta_note** | `graph_delta=none` 时 **必填** 一行 |
| **graph_gate** | `skeleton_before_30` · `close_partial_or_final` |
| **entry_invoke_10_task** | `docs/harness/invokes/by-task/<slug>/PROMPT_kimi_agent_rethink_R1_R5.md` |
| **entry_invoke_10_spec** | （`feature` 填；bugfix 留空） |
| **entry_invoke_00_draft** | 工作区 `docs/harness/prompts/PROMPT_00_draft_spec_or_task_v1_zh.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | pending | 20-R1, 30 | **§4 给 10-task 交接物** + skeleton |
| HG-AUDIT-R1 | pending | 30 | **20 思考审查通过** + skeleton commit 后人签 |

> `HG-GRAPH-MODULES` 已在阶段 B 签 `approved`；本 task 不重复签模块表，但 **仍须** flow 增量。

---

## 1. 需求摘要

（来自 Issue）

---

## 2. 非范围

- `docs/harness`、task、invoke 进上游 PR
- 未在 `graph_delta` 列出的 flow 大改（须另开图谱子 task）

---

## 3. 失败路径

| 触发条件 | 系统行为 | 可重试 |
|----------|----------|--------|
| `graph_delta≠none` 且无 skeleton meta commit | 30 **拒开工** | 是 |
| 无 §4 给 10 交接物 / 无 invoke PROMPT | 10 **拒开工** | 是 |
| 未完成 §5 思考轮闭合（R1–R5 仍有 `（待填）`） | **20 退回 10-task** · 30 **拒开工** | 是 |
| `early_stop=yes` 但缺 reason / residual_risks | **20 退回 10-task** | 是 |
| 未完成思考轮即 30 | 30 **拒开工** | 是 |
| `HG-AUDIT-R1` pending | 30 **拒开工** | 是 |
| PR 已开但 meta 无图谱关账 commit | 维护者 **不得** `done/` | 是 |
| PR 含 harness/task 路径 | 维护者拒合并上游 | 是 |

---

## 4. 给 10-task 交接物（00 起草 **必写**）

> **谁写**：**00 相位**（人或 Agent）在 `draft` 落盘；见工作区 [`PROMPT_00_draft_spec_or_task_v1_zh.md`](../../../docs/harness/prompts/PROMPT_00_draft_spec_or_task_v1_zh.md)。  
> **00 不填 §5**；**10-task** 专责 R0–R5 回填。

| 字段 | 值 |
|------|-----|
| **帽子** | **10-task**（非 10-spec；bugfix 跳过 spec） |
| **Open Folder** | `kimi-code` |
| **invoke** | `entry_invoke_10_task` |
| **回填协议** | [`FRAGMENT_rethink_backfill_task_v1_zh.md`](../harness/FRAGMENT_rethink_backfill_task_v1_zh.md) |
| **10-task 真值** | 工作区 `docs/harness/prompts/10-task-requirements.md` |

### 必读路径（`@` 自 `kimi-code` 根）

| 路径 | 用途 |
|------|------|
| `../kimi-code-meta/docs/tasks/active/<本 task>` | 读需求 · **回填 §5** |
| `../kimi-code-meta/docs/_tech_graph/<graph_delta>` | 图谱增量 YAML（`.graph.yaml` · compile 生成 `.md`） |
| `../kimi-code-meta/docs/_tech_graph/01_struct.md` | `module_id` |
| （按 Issue 列）`packages/...` 源码 | R1 代码事实 |

### 禁止（10 会话）

- 改 `packages/**`、`apps/**` 产品代码
- `git commit` / `git push`

### 10-task 产出（交接给 20）

- task **§5** + **思考轮控制** 已填
- 可选：invoke 思考快照
- **不**签发 `HG-AUDIT-R1`（**20** + 人签）

---

## 5. Kimi Code Agent · 思考轮次（改码前 · 默认 R0 + R1–R5）

> **10 帽义务**：预置 **五槽思考轮**（C1–C3 实证）；工作区 [`10-requirements.md`](../../../docs/harness/prompts/10-requirements.md) OSS 阶段 C 节。  
> **invoke**：`docs/harness/invokes/by-task/<slug>/PROMPT_kimi_agent_rethink_*.md`  
> **回填协议**：[`docs/harness/FRAGMENT_rethink_backfill_task_v1_zh.md`](../harness/FRAGMENT_rethink_backfill_task_v1_zh.md) — Agent **必须**将结论写入本节 + **思考轮控制**，**禁止**仅在聊天输出。

### 思考轮控制（Agent 填 · 22 审）

| 字段 | 值 |
|------|-----|
| **actual_last_round** | `R5` / `R3` / … |
| **early_stop** | `no` / `yes` |
| **early_stop_reason** | （`early_stop=yes` **必填**） |
| **residual_risks** | `none` 或逐条（**必填**） |

### R0 · 读 task

**回填区：**

```text
（待填）
```

### R1 · 代码事实

**回填区：**

```text
（待填）
```

### R2 · 方案对比

**回填区：**

```text
（待填）
```

### R3 · 边界 / 测试

**回填区：**

```text
（待填）
```

### R4 · 测试与 PR 策略

**回填区：**

```text
（待填）
```

### R5 · 图谱增量 + 关账判断

**回填区：**

```text
（待填）
```

### R6+ · 扩展轮（仅当 Agent 增轮时追加）

**扩展理由：**

```text
（无则删除本节）
```

**回填区：**

```text
（待填）
```

---

## 6. 验收标准（关账）

- [ ] §5 思考轮闭合 · **思考轮控制** 已填 · **20** 思考审查通过
- [ ] `HG-AUDIT-R1` → `approved`
- [ ] vitest / lint 通过（与 `test_strategy` 一致）
- [ ] 上游 PR 已开 · `Fixes #<issue>`
- [ ] invoke 落盘 `docs/harness/invokes/by-task/<slug>/`
- [ ] **图谱**（`graph_delta≠none` 时 **必勾**，禁止标可选）：
  - [ ] 30 **前**：`docs/_tech_graph/<graph_delta>` 存在 + `pnpm graph:compile` + `00_main` 清单状态
  - [ ] **关账**：`graph_delta` YAML 已合 · `pnpm graph:compile` + `02_version` 一行
  - [ ] 必要时 `01_struct` 模块备注

---

## 7. 给 30 帽必读（签 `HG-AUDIT-R1` 后）

1. 仓根 `AGENTS.md`
2. 本 task §1 + **§5 结论**
3. `@../kimi-code-meta/docs/_tech_graph/01_struct.md`
4. `@../kimi-code-meta/docs/_tech_graph/<graph_delta>`（YAML 须已 meta commit · compile 出 `.md`）
5. Issue 原文
6. invoke §「30 开工」块 · [`30-execute-code.md`](../../harness/prompts/30-execute-code.md)

---

## 8. 验证命令

```bash
cd /path/to/kimi-code
git checkout main && git fetch upstream && git reset --hard upstream/main
git checkout -b feature/fix-<issue>-<short>
pnpm --filter @moonshot-ai/agent-core test   # 按范围调整
pnpm lint
git diff upstream/main --name-only

# meta · cyning/meta（关账前必跑 · #437 起）
cd ../kimi-code-meta
pnpm graph:issue-sync \
  --task docs/tasks/active/task_fix_<issue>_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD
```

---

## 9. 维护者签闸清单

- [ ] **§4 给 10 交接物** 已填 · invoke `PROMPT_kimi_agent_rethink_*` 已落盘
- [ ] `graph_delta` 已填；`none` 则有 `graph_delta_note`
- [ ] 若触图谱：skeleton 已 meta commit **先于** 30
- [ ] §5 R0–R5 / **思考轮控制** / `HG-AUDIT-R1`（22 通过后人签）
- [ ] 关账同波：图谱 + invoke + task → `done/`

---

## 10. 实现备忘（30 后回填）

| 项 | 状态 | 备注 |
|----|------|------|
| 图谱 skeleton | ⏳ | |
| 图谱关账 | ⏳ | |
| **meta_graph_commit** | ⏳ | meta `_tech_graph` 关账 commit SHA |
| **upstream_pr_commit** | ⏳ | 产品 `feature/fix-*` 顶 commit SHA |
| **graph_issue_sync** | ⏳ | `pnpm graph:issue-sync` 输出摘要 · exit 0 |
| 测试 | ⏳ | |
| 上游 PR | ⏳ | |

### 自检结论（执行者）

（30 完成后回填）
