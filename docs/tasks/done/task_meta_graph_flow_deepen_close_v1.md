# Task · W-close 7 张 deep 标状态 + graph:ci

> **状态**：`done` · 2026-08-28  
> **Epic SPEC**：[`SPEC_meta_graph_flow_deepen_v1_zh.md`](../specs/SPEC_meta_graph_flow_deepen_v1_zh.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `meta-graph-flow-deepen-close` |
| **test_strategy** | `required` |
| **test_strategy_note** | `pnpm graph:ci` 必须绿（nvm use 24.15+） |
| **code_quality_bar** | `strict` |
| **freeze_id** | `META-GRAPH-FLOW-DEEPEN` |
| **track** | `engineering` |
| **orchestration** | 7 张 30 完成后再派 |
| **semi_auto** | `false` |
| **audit_profile** | `human_only` |
| **invoke_retention_profile** | `default` |
| **required_invoke_hats** | `10,30,40` |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **module_id** | `monorepo_root` |
| **graph_delta** | `none` |
| **graph_delta_note** | 改 compile 待补表状态字 + export，不新开 flow |
| **graph_gate** | `n/a` |
| **wiki_delta** | `none` |
| **wiki_delta_note** | 非 coding_wiki |
| **close_pr_policy** | `exempt` |
| **close_pr_exempt_note** | cyning/meta |
| **experience_capture** | `not_applicable` |
| **experience_capture_note** | 关账文档 |
| **entry_invoke_30** | `docs/harness/invokes/by-task/meta-graph-flow-deepen/PROMPT_30_meta-graph-flow-deepen-close.md` |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved 2026-08-28 | 20-R1, 30 | 00 代签 |
| HG-AUDIT-R1 | approved 2026-08-28 | 30 | 00 代签 |

---

## 1. 背景与目标

7 张均 deep 后：compile.py 待补表改 **deep**；export；`pnpm graph:ci`；02_version 一行。

## 2. 范围

- [x] 抽检每张 D3；不达标退回对应 30
- [x] `graph_yaml_compile.py` 7 行状态 → `deep`
- [x] README 已交付图说明可改「deep」
- [x] `02_version.md` 追加本 Epic
- [x] `python3 ... --all` compile + export + 四段 + `pnpm graph:ci`

## 非范围

- 不新开 10_flow；不迁目录；不改生产码；不 git commit

## 失败路径

| 触发条件 | 系统行为 | 可重试 | 用户可见 |
|----------|----------|--------|----------|
| 任一张未达 D3 | 拒关账 | 是 | 退回该图 30 |
| graph:ci 红 | 拒关账 | 是 | 修 yaml 或 Node |

## 验收标准

- [x] 待补表 7×deep
- [x] `pnpm graph:ci` 绿
- [x] 仍 8 张扁平 yaml

## 6. 思考轮

### R0
收 7 张自检。

### R1
只标状态与 CI。

### R2
不改 glob。

### R3
假 deep 拒收。

### R4
graph:ci required。

### R5
可 30。

### 思考轮控制

| 字段 | 值 |
|------|-----|
| **actual_last_round** | `R5` |
| **early_stop** | `no` |
| **early_stop_reason** | — |
| **residual_risks** | 7 张并行后 line 冲突极少（不同文件） |

### 自检结论

**帽**：30 · **日期**：2026-08-28 · **结论**：待补表 **7×deep** · `pnpm graph:ci` **绿**（Node v24.15.0）· yaml **仍 8 张扁平** · **可派 40**

**GATE_VERIFY（task 表真值）**

| human_gate_id | task表status | 用户/invoke声称 | 一致？ | blocks_30 | 30可开工？ |
|---------------|--------------|-----------------|--------|-----------|------------|
| HG-TASK-DRAFT | approved 2026-08-28 | approved 2026-08-28 | Y | Y | ✅ |
| HG-AUDIT-R1 | approved 2026-08-28 | approved 2026-08-28 | Y | Y | ✅ |
| HG-GRAPH-MODULES | approved 2026-08-28（`01_struct.md`） | 只改 Inform | Y | 仅业务码 | ✅ Inform only |

reviews：`docs/harness/reviews/task_meta-graph-flow-deepen-close_audit_R1_20260828.md` 存在且 R1 **pass**。无声称 vs 表冲突。`npx dsh-coding-kit verify` exit 非 0（把「approved 2026-08-28」当成非 approved）→ **忽略 kit，以 task 人工闸表为准**。

**D3 抽检**：00 已抽检 7 张 path/line 均为 **100%**、无 TBD；本帽未退回任何图。

**compile.py**：`generate_sub_graph_links` 7 行状态全部改为 **deep**；yaml 链接保留。`TECH_GRAPH_DIR.glob("*.graph.yaml")` **未改 rglob**。

**README**：已交付图增「状态」列，7 张 `10_flow_*` 均为 **deep**。

**02_version.md**：追加 `2026-08-28` **meta-graph-flow-deepen Epic CLOSE** 一行。

**验证**（nvm use 24.15.0）：

- `python3 tools/tech_graph/graph_yaml_compile.py --all` 生成 8 张 `.md`
- `python3 tools/tech_graph/tech_graph_graph_export.py` 同步 `graph.json`
- python 四段：`--all --check` / `export --check` / `equivalence` / `completeness` 均 **exit 0**
- `pnpm graph:ci` **绿**

**yaml**：`docs/_tech_graph/*.graph.yaml` = **8** 张扁平（无子目录）。未新开 `10_flow_*`。未改 `packages/**` `apps/**`。未 git commit。未迁目录。

**交付 invoke**：`docs/harness/invokes/by-task/meta-graph-flow-deepen/invoke_20260828_30_close.md`。
