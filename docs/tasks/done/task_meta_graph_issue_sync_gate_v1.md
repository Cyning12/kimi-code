# Task · meta graph · Issue 修复链同步门禁（L2/L3）

> **状态**：`done` · HG-SYNC-GATE-CLOSE **approved**（2026-06-18）  
> **分支**：`cyning/meta` **only** · **无** Moonshot upstream PR  
> **前序**：`[task_meta_graph_v2_batch_migrate_v1.md](../done/task_meta_graph_v2_batch_migrate_v1.md)` **done** · YAML 六图 + 工具链  
> **安排真值**：工作区 `[PLAN_kimi_code_meta_harness_2x_v1_zh.md](../../../../docs/harness/guides/PLAN_kimi_code_meta_harness_2x_v1_zh.md)` §4.1′  
> **试点纪律**：`[PILOT_kimi_code_fork_adoption_v1_zh.md](../../../../docs/harness/guides/PILOT_kimi_code_fork_adoption_v1_zh.md)` §5.2  
> **R1 审查**：[`task_meta_graph_issue_sync_gate_v1_audit_R1_20260618.md`](../harness/reviews/task_meta_graph_issue_sync_gate_v1_audit_R1_20260618.md) · **通过**（复审）· **HG-AUDIT-R1 approved**（2026-06-18）  

---

## Harness 元信息


| 字段                       | 值                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| **task_slug**            | `meta-graph-issue-sync-gate`                                                             |
| **test_strategy**        | `required`                                                                               |
| **test_strategy_note**   | L2/L3 脚本 pytest · 关账夹具（#437 mock diff）· 接入后 `pnpm graph:issue-sync` exit 0/1             |
| **code_quality_bar**     | `strict`                                                                                 |
| **track**                | `engineering`（meta 过程轨 · 门禁基础设施）                                                         |
| **orchestration**        | **10-task**（R0–R3 轻量）→ **20** → **30** → **40** → CLOSE                                  |
| **audit_profile**        | `human_only`                                                                             |
| **git_branch**           | `cyning/meta`                                                                            |
| **worktree_root**        | `kimi-code-meta/`                                                                        |
| **meta_worktree**        | 同 `worktree_root`                                                                        |
| **freeze_id**            | `KIMI-META-GRAPH-SYNC-GATE@ecc7b9dc` |
| **module_id**            | `monorepo_root`                                                                          |
| **graph_delta**          | `none`                                                                                   |
| **graph_delta_note**     | 本 task 落盘门禁脚本与映射表 · 不增量单张 flow                                                           |
| **graph_gate**           | `n/a`                                                                                    |
| **entry_invoke_10_task** | `Projects/docs/harness/invokes/by-task/meta-graph-issue-sync-gate/`（轻量 R0–R3 · 10 帽）     |
| **entry_invoke_20**      | `Projects/docs/harness/invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_20_v1.md` |
| **entry_invoke_30**      | `Projects/docs/harness/invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_30_v1.md` |


### 人工闸


| human_gate_id          | status   | blocks_hats | 说明                    |
| ---------------------- | -------- | ----------- | --------------------- |
| **HG-TASK-DRAFT**      | approved | 20-R1, 30   | 维护者扫 §1–§3 · L2/L3 范围 |
| **HG-AUDIT-R1**        | approved | 30          | 20 R1 复审通过 · 2026-06-18 维护者签 |
| **HG-SYNC-GATE-CLOSE** | approved | done        | G3 验收 + #437 pytest mock 绿 · 2026-06-18 |


> **禁止**：与 #437 产品 `feature/fix-`* **同 PR** · 改 Ink 子仓 · 上游 CI 强绑（本阶段仅 **本地/meta 门禁**）。

---

## 1. 背景与目标

graph_v2 batch 已交付 **L1 图谱卫生**（`graph:compile:check` · export · equivalence · axioms）。  
C 轨 Issue 修复仍跨 **双 worktree**（`kimi-code` 产品 · `kimi-code-meta` 图谱），PILOT §5.2 流程闸 **无法机械验证**「产品 diff 触达模块 → meta 对应 `.graph.yaml` 已更新」。

**本 task 目标**：在 meta 落盘 **L2 task↔图谱** 与 **L3 产品 diff↔模块↔flow** 本地门禁，并写入 Issue task 关账 checklist；#437 起 **关账必跑**。

### 完成态

- [ ] `docs/_tech_graph/graph_module_flow_map.yaml`（machine-readable · 模块→flow 映射）
- [ ] `tools/tech_graph/graph_task_close_check.py`（**L2**）
- [ ] `tools/tech_graph/graph_product_sync_check.py`（**L3** · 跨 worktree）
- [ ] `pnpm graph:issue-sync` 聚合 L1+L2+L3（或 `graph:close-check`）
- [ ] `docs/tasks/TASK_TEMPLATE_upstream_pr_v1.md` 增关账字段（`product_worktree` · 双 SHA）
- [ ] `docs/harness/prompts/FRAGMENT_30_gate_verify_v1_zh.md` 或关账 FRAGMENT 链指 L2/L3
- [ ] pytest `tests/tech_graph/test_issue_sync_gate.py`（含 #437 mock）
- [ ] invoke README · 工作区 pointer · PLAN §4.1′ 更新

### 不在范围（L4 · 另靠流程）


| 项                     | 说明                     |
| --------------------- | ---------------------- |
| 图谱语义与代码行为 **完全一致**    | 22 R1 + 测试 + 人审        |
| Moonshot upstream CI  | 本 task 仅 meta 本地/维护者关账 |
| `graph_query` CLI 产品化 | backlog                |
| HGM ingest            | Track G · 正交           |


---

## 2. 门禁分层（真值）

```text
L1 图谱卫生（已有 · batch done）
  pnpm graph:compile:check · graph:export:check · graph:equivalence
  npx @cyning/harness graph axioms check

L2 task ↔ meta 图谱（本 task · G1）
  graph_task_close_check.py --task docs/tasks/active/task_*.md

L3 产品 diff ↔ 模块 ↔ flow（本 task · G2）
  graph_product_sync_check.py \
    --product-root ../kimi-code \
    --product-ref upstream/main...HEAD \
    --task docs/tasks/active/task_*.md

L4 语义一致（流程 · 非本 task）
  10-task R1 @ 源码+YAML · 22 · test_strategy · task §10 双 SHA
```

### 2.1 L2 规则（task 关账）


| 条件                              | 行为                                                                         |
| ------------------------------- | -------------------------------------------------------------------------- |
| `graph_delta` 指向 `*.graph.yaml` | meta 上该文件 **相对 task 起草后** 有 diff                                           |
| `graph_delta=none`              | 必须有 `graph_delta_note` · L3 若产品触模块则 **FAIL**（除非 `--allow-graph-none` 维护者码） |
| 任意                              | L1 全绿 · `02_version.md` 含 task slug 或 issue 行（WARN 可配置）                    |


### 2.2 L3 规则（跨 worktree）

```text
产品 git diff --name-only（apps/ packages/）
  → 匹配 01_struct module_id（path glob）
  → 查 graph_module_flow_map.yaml → 期望 flow 列表
  → 读 task graph_delta / graph_delta_note
  → 若触达模块且 graph_delta≠none：期望 flow ⊆ graph_delta 指向文件 · 且 meta 有 diff
  → 若触达模块且 graph_delta=none：exit 2 + 提示改 task 或显式 override
```

### 2.3 模块→flow 映射（初版 · G0 落盘）


| module_id                          | 默认 flow（`graph_module_flow_map.yaml`）      | 备注                                  |
| ---------------------------------- | ------------------------------------------ | ----------------------------------- |
| `cli`                              | `10_flow_cli_session.graph.yaml`           | #437                                |
| `agent_core`                       | `10_flow_agent_turn.graph.yaml`            | 可 + read/context/skill 子域           |
| `agent_core` + `builtin/file/read` | `10_flow_read_tool.graph.yaml`             | 路径启发式优先                             |
| `agent_core` + skill 路径            | `10_flow_skill_load.graph.yaml`            | `packages/agent-core/src/skills/**` |
| `agent_core` + context/turn        | `10_flow_context_tool_exchange.graph.yaml` | #705 域                              |
| `node_sdk`                         | `10_flow_cli_session.graph.yaml`           | 次要 · WARN                           |
| `monorepo_root`                    | `none`                                     | 仅 harness/docs                      |


> **路径启发式**：L3 先 glob `01_struct` · 再按 diff 路径子串匹配 agent_core 专链（与 PILOT §分步规则一致）。

---

## 3. 任务链 · G0–G3

```text
G0 映射表 graph_module_flow_map.yaml + 01_struct 对齐
  → G1 L2 graph_task_close_check.py + pytest
  → G2 L3 graph_product_sync_check.py + 跨仓夹具
  → G3 pnpm 聚合 · template/FRAGMENT · invoke · #437 验收夹具
```

### G0 · 映射表


| 交付                                            | 验收                                     |
| --------------------------------------------- | -------------------------------------- |
| `docs/_tech_graph/graph_module_flow_map.yaml` | 覆盖 §2.3 表 · 与 `01_struct` module_id 一致 |
| 文档头：维护规则（增 module 须同步 map）                    | README 或 map 内 comment                 |


### G1 · L2


| 交付                                                                 | 验收                    |
| ------------------------------------------------------------------ | --------------------- |
| `graph_task_close_check.py`                                        | `--task` · exit 0/1/2 |
| 读 task front matter / Harness 表：`graph_delta` · `graph_delta_note` | 解析 meta task md       |
| 集成 L1（子进程调 compile:check）                                          | 失败则 L2 不通过            |
| pytest ≥3：delta 有 diff PASS · 无 diff FAIL · none+note PASS         |                       |


### G2 · L3


| 交付                                                 | 验收                                             |
| -------------------------------------------------- | ---------------------------------------------- |
| `graph_product_sync_check.py`                      | `--product-root` · `--product-ref` · `--task`  |
| 解析产品 diff · module 映射 · 期望 flow                    | #437 mock：`apps/kimi-code` → cli → cli_session |
| `--allow-graph-none`（维护者 override · 须 log 理由）      | 文档化                                            |
| pytest：mock diff 无 meta 变更 → exit 1 · 补 YAML 后 → 0 |                                                |


### G3 · 接入与纪律


| 交付                                                                                                                        | 验收           |
| ------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `package.json`：`graph:issue-sync` 或 `graph:close-check`                                                                   | 串 L1→L2→L3   |
| 更新 `TASK_TEMPLATE_upstream_pr_v1.md`：`product_worktree` · `product_base_ref` · `meta_graph_commit` · `upstream_pr_commit` | 关账 §10 双 SHA |
| FRAGMENT / 30 关账段：Issue task **done 前** 必跑 `pnpm graph:issue-sync --task …`                                               | 文字链指         |
| invoke README（工作区）                                                                                                        | 见 §8         |


---

## 4. Issue task 关账纪律（#437 起 · 写入 template）

```bash
# meta · cyning/meta
cd kimi-code-meta
pnpm graph:issue-sync --task docs/tasks/active/task_fix_approve_once_437_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD

npx @cyning/harness@2.0.1 gate-check --target . --task docs/tasks/active/task_fix_approve_once_437_v1.md
```

**task §10 关账必填：**


| 字段                   | 说明                                    |
| -------------------- | ------------------------------------- |
| `meta_graph_commit`  | meta 上 `_tech_graph` 关账 commit SHA    |
| `upstream_pr_commit` | `feature/fix-437-*` 顶 commit SHA      |
| `graph_issue_sync`   | `pnpm graph:issue-sync` 输出摘要 · exit 0 |


**缺任一项 · 维护者不得 `done/`**（与 PILOT「上游 PR 已开但 meta 无图谱关账」并列）。

---

## 5. 非范围

- #437 产品实现（后继 task）
- batch migrate 回改
- cyning-harness npm 包内建 L3（可 backlog 包装 `harness graph sync-check`）
- pre-commit 强制安装（仅 **optional** 文档 · 对齐 G1.1 optional ingest）

---

## 6. 失败路径


| 触发条件                              | 行为          | exit |
| --------------------------------- | ----------- | ---- |
| batch 未 done / 无 `*.graph.yaml`   | G1 **拒开工**  | —    |
| L1 compile/export 失败              | L2/L3 不跑    | 1    |
| `graph_delta` 有目标 · meta 无 diff   | L2 FAIL     | 1    |
| 产品触模块 · task `graph_delta=none`   | L3 FAIL     | 2    |
| 产品触模块 · 期望 flow 无 meta diff       | L3 FAIL     | 1    |
| `--allow-graph-none` 无 `--reason` | argparse 错误 | 2    |
| 与 #437 feature 同 PR               | 维护者拒        | —    |


---

## 7. 给 10-task 交接物


| 字段              | 值                                                                 |
| --------------- | ----------------------------------------------------------------- |
| **Open Folder** | `kimi-code-meta/`                                                 |
| **必读**          | 本 task §1–§4 · `01_struct.md` · `graph_v2` done task · PILOT §5.2 |
| **禁止**          | G1/G2 实现 · commit                                                 |
| **产出**          | §9 R0–R3 回填 · G0 映射表草案（可写在 §12 备忘）                                |


---

## 8. invoke


| 路径  | 说明                                                                                                                      |
| --- | ----------------------------------------------------------------------------------------------------------------------- |
| 工作区 | `[meta-graph-issue-sync-gate/README.md](../../../../docs/harness/invokes/by-task/meta-graph-issue-sync-gate/README.md)` |
| 工作区 | `[PROMPT_START_20_v1.md](../../../../docs/harness/invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_20_v1.md)`    |
| 工作区 | [`PROMPT_START_30_v1.md`](../../../../docs/harness/invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_30_v1.md) |
| 仓内镜像 | [`docs/harness/invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_30_v1.md`](../../invokes/by-task/meta-graph-issue-sync-gate/PROMPT_START_30_v1.md) |


---

## 9. Kimi Code Agent · 思考轮次（10 回填）


| 字段                    | 值                                                                                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **actual_last_round** | R3                                                                                                                                                                                |
| **early_stop**        | false                                                                                                                                                                             |
| **early_stop_reason** | —                                                                                                                                                                                 |
| **residual_risks**    | L3 路径启发式误匹配（agent_core 默认 turn vs read/skill/context 专链）· `../kimi-code` 不存在时 L3 须明确 exit 2 · L2 子进程调 L1 超时/非零需 stderr 摘要 · G3 `graph:issue-sync` CLI 参数与 harness gate-check 尚未串联 |


### R0 · 读 task

- 已读 task §1–§6 · §7 交接 · batch done task · PLAN §4.1′ · PILOT §5.2 · R1 审查打回清单。
- Open Folder **`kimi-code-meta/`** · 分支 **`cyning/meta`** · **HG-TASK-DRAFT approved**（2026-06-18）。
- 本帽交付：**§9 思考轮 + §12.1 G0 映射草案**；**禁止** G1/G2 脚本实现 · **禁止** commit/push（10 纪律）。
- 关账目标：L2/L3 本地门禁 + `pnpm graph:issue-sync` · #437 起 Issue 关账必跑。
- **HG-AUDIT-R1 pending** → 20 复审通过前人签 · 30 拒开工。

### R1 · batch L1 现状 + 工具链

- **六图 YAML**：`docs/_tech_graph/` 共 **6×** `*.graph.yaml`（`00_main` + 5× `10_flow_*`）· 与 batch done task §4 一致。
- **L1 脚本**：`tools/tech_graph/` 五件（`graph_yaml_compile` · export · equivalence · v2_schema · v2_yaml）。
- **pnpm**：`graph:compile:check` / `export:check` / `equivalence` 已包装；**2026-06-18 本地** `pnpm graph:compile:check` **exit 0**（六图 slice OK）。
- **batch freeze_id**：`KIMI-META-GRAPH-V2-BATCH@0fa2d54f` · L2 设计为 **子进程复用** 上述命令 · 不重复造 compile 逻辑。
- **尚无**：`graph_task_close_check.py` · `graph_product_sync_check.py` · `graph_module_flow_map.yaml`（G0 草案见 §12.1）· `graph:issue-sync`。

### R2 · G0–G3 链与 L1–L4 分层

- **G0** → `graph_module_flow_map.yaml`（§12.1 草案）· 与 `01_struct` module_id 对齐。
- **G1 L2** → `graph_task_close_check.py`：`--task` · 解析 `graph_delta` / `graph_delta_note` · **子进程** `pnpm graph:compile:check`（L1 失败则 L2 不跑）。
- **G2 L3** → `graph_product_sync_check.py`：`--product-root ../kimi-code` · `--product-ref upstream/main...HEAD` · 读 map + task · exit 1/2 语义见 §2.2。
- **G3** → `pnpm graph:issue-sync` 串 L1→L2→L3 · TASK_TEMPLATE 双 SHA · FRAGMENT 关账链指。
- **L4**（非本 task）：22 R1 @ 源码+YAML · `test_strategy` · task §10 双 SHA · 人审语义。

### R3 · 边界 / #437 夹具 / 关账判断

- **非范围确认**：graph_query CLI · HGM ingest · cyning-harness npm 内建 L3 · #437 产品码 · pre-commit **optional only** · 不改 batch YAML 真值。
- **#437 mock 夹具（G2 验收口径）**：产品 diff 含 `apps/kimi-code/**` → module `cli` → 期望 `10_flow_cli_session.graph.yaml`；meta 无对应 diff → **exit 1**；补 YAML 增量后 → **exit 0**。
- **`graph_delta=none` 本 task**：合理（门禁基础设施）；Issue task 不得滥用 none 绕过 L3（exit 2）。
- **双 worktree**：产品仓默认 `../kimi-code`（与 PILOT 双分支一致）· ref 默认 `upstream/main...HEAD` · 路径不存在时 L3 应 **fail closed**（exit 2 + 可读 message）。
- **20 下一棒**：维护者重开 20 R1 · 核对 §9/§12.1 · 通过后签 **HG-AUDIT-R1** → 30。

---

## 10. 验收标准（关账）

- [x] G0–G3 交付完成
- [x] `pnpm graph:issue-sync` · #437 **pytest mock** 绿（draft task L2 待 skeleton）
- [x] pytest `tests/tech_graph/test_issue_sync_gate.py` 全绿
- [x] TASK_TEMPLATE · FRAGMENT 已更新
- [x] `HG-AUDIT-R1` · `HG-SYNC-GATE-CLOSE` approved
- [x] invoke CLOSE · task → `done/`
- [x] PLAN §4.1′ · 工作区 pointer（可选 · 见 invoke 40）
- [x] **可开** `task_fix_approve_once_437_v1.md`（关账 checklist 含 `graph:issue-sync`）

---

## 11. 验证命令（30 后回填）

```bash
cd kimi-code-meta && git checkout cyning/meta

pytest tests/tech_graph/test_issue_sync_gate.py -q
# → 8 passed

pnpm graph:issue-sync \
  --task docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD
# L1 OK · L2 OK · L3 exit 2（本 task graph_delta=none · 产品触模块 · 预期）

pnpm graph:issue-sync \
  --task docs/tasks/active/task_fix_approve_once_437_v1.md \
  --product-root ../kimi-code \
  --product-ref upstream/main...HEAD
# L2 exit 1（437 draft · meta 尚无 yaml diff · skeleton 前预期）
```

---

## 12. 实现备忘（30 后回填）


| 项                           | 状态  | 备注              |
| --------------------------- | --- | --------------- |
| graph_module_flow_map.yaml  | ✅   | G0 §12.1 落盘     |
| graph_task_close_check.py   | ✅   | L2              |
| graph_product_sync_check.py | ✅   | L3              |
| graph_sync_common.py        | ✅   | 共享解析          |
| graph_issue_sync.py         | ✅   | L1→L2→L3 聚合    |
| pnpm graph:issue-sync       | ✅   | package.json    |
| template / FRAGMENT         | ✅   | 关账字段 + L2/L3 链指 |
| pytest test_issue_sync_gate | ✅   | 8 passed        |
| meta commit SHA             | ✅   | `6a64dae7` · `ecc7b9dc` |
| freeze_id                   | ✅   | `KIMI-META-GRAPH-SYNC-GATE@ecc7b9dc` |


### 12.1 G0 映射草案（10 回填 · 30 落盘真值）

> **状态**：`draft` · 审查 R1 要求 · 30 写入 `docs/_tech_graph/graph_module_flow_map.yaml`。

**规则摘要**：

- L3 先匹配 `01_struct` path glob → `module_id`。
- `agent_core` 默认 flow = `10_flow_agent_turn`；diff 路径含下列启发式时 **优先** 专链 flow。
- `node_sdk` 触达仅 **WARN** · 不单独 FAIL（除非 task `graph_delta` 已指专链）。
- `monorepo_root` / harness-only 路径 → 期望 `graph_delta=none` + note。

**映射表（与 §2.3 对齐）**：


| module_id       | path_heuristic（可选）                                     | default_flow                               | severity |
| --------------- | ------------------------------------------------------ | ------------------------------------------ | -------- |
| `cli`           | `apps/kimi-code/**`                                    | `10_flow_cli_session.graph.yaml`           | required |
| `agent_core`    | （默认）                                                   | `10_flow_agent_turn.graph.yaml`            | required |
| `agent_core`    | `**/builtin/file/read/**` · `read_tool`                | `10_flow_read_tool.graph.yaml`             | required |
| `agent_core`    | `**/skills/**` · `skill_load` · `skill/parser`         | `10_flow_skill_load.graph.yaml`            | required |
| `agent_core`    | `**/context/**` · `turn/**` · `tool_exchange` · #705 域 | `10_flow_context_tool_exchange.graph.yaml` | required |
| `node_sdk`      | `packages/node-sdk/**`                                 | `10_flow_cli_session.graph.yaml`           | warn     |
| `monorepo_root` | `docs/**` · `tools/tech_graph/**` · harness            | `none`                                     | skip     |


**YAML 落盘草案（30 复制微调）**：

```yaml
# docs/_tech_graph/graph_module_flow_map.yaml · draft v0.1
schema_version: graph_module_flow_map_v1
source_of_truth:
  module_table: docs/_tech_graph/01_struct.md
  flow_registry: docs/_tech_graph/*.graph.yaml

rules:
  - module_id: cli
    path_globs: ["apps/kimi-code/**"]
    default_flow: 10_flow_cli_session.graph.yaml
    severity: required

  - module_id: agent_core
    path_globs: ["packages/agent-core/**"]
    default_flow: 10_flow_agent_turn.graph.yaml
    severity: required

  - module_id: agent_core
    path_globs:
      - "packages/agent-core/**/builtin/file/read/**"
      - "packages/agent-core/**/read/**"
    path_substrings: ["read_tool", "ReadTool"]
    default_flow: 10_flow_read_tool.graph.yaml
    severity: required
    priority: 10

  - module_id: agent_core
    path_globs: ["packages/agent-core/**/skills/**"]
    path_substrings: ["skill_load", "skill/parser"]
    default_flow: 10_flow_skill_load.graph.yaml
    severity: required
    priority: 10

  - module_id: agent_core
    path_globs:
      - "packages/agent-core/**/context/**"
      - "packages/agent-core/**/turn/**"
    path_substrings: ["tool_exchange", "open_tool_calls"]
    default_flow: 10_flow_context_tool_exchange.graph.yaml
    severity: required
    priority: 10

  - module_id: node_sdk
    path_globs: ["packages/node-sdk/**"]
    default_flow: 10_flow_cli_session.graph.yaml
    severity: warn

  - module_id: monorepo_root
    path_globs: ["docs/**", "tools/tech_graph/**", ".cyning-harness/**"]
    default_flow: none
    severity: skip
```

---

## 13. 修订记录


| 日期         | 说明                                            |
| ---------- | --------------------------------------------- |
| 2026-06-18 | **CLOSE** · HG-SYNC-GATE-CLOSE approved · freeze `KIMI-META-GRAPH-SYNC-GATE@ecc7b9dc` |
| 2026-06-18 | 30 G0–G3 落盘 · pytest 8 passed · graph:issue-sync 接线 |
| 2026-06-18 | HG-AUDIT-R1 approved · PROMPT_START_30 落盘 |
| 2026-06-18 | 10 回填 §9 R0–R3 · §12.1 G0 草案（R1 打回后） |
| 2026-06-18 | 初版 · batch migrate done 后 · L2/L3 · #437 启用目标 |


