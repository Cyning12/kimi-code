# SPEC · 全量补全本仓技术图谱（覆盖补全 · v1）

> **状态**：`closed`（**HG-SPEC-SIGNOFF approved 2026-08-28** · Epic CLOSE 00 复检 2026-08-28）  
> **track**：`epic`  
> **域**：Track C · `Cyning12/kimi-code` @ **`cyning/meta`** · 本地目录 **`kimi-code-meta/`**  
> **关联图谱**：`docs/_tech_graph/` · [`01_struct.md`](../../_tech_graph/01_struct.md) · [`graph_module_flow_map.yaml`](../../_tech_graph/graph_module_flow_map.yaml) · [`00_main.md`](../../_tech_graph/00_main.md)  
> **前序 Epic**：[`SPEC_meta_graph_interview_complete_v1_zh.md`](./SPEC_meta_graph_interview_complete_v1_zh.md) · **closed**（面试最小集 + `pnpm graph:ci`）· **本 SPEC 是后续覆盖补全，不是重开那份，也不是把现有 6 张图推倒重来**  
> **下游**：00 拆波次 task → 30 subagent 落地 · 本窗 00 **不**改 yaml  
> **非主线**：不改 dsh-coding-kit · 不改 Ops-desk / ops-desk-api · 不迁 l0/l1/l2

---

## Harness 元信息

| 字段 | 值 |
| --- | --- |
| **spec_slug** | `meta-graph-full-coverage` |
| **freeze_id** | `META-GRAPH-FULL-COVERAGE` |
| **test_strategy** | `required` |
| **test_strategy_note** | 关账仍须 `pnpm graph:ci` 可失败为红（回归闸）。覆盖完成另订 §4.2 口径，**不以**面试 Epic 的 completeness 阈值（P0 四模块 / `MODULE_DEP_TOUCH_MIN=8` / `TOTAL_EDGES_MIN=100`）作为本 Epic **唯一**验收。 |
| **orchestration** | 本仓根 `kimi-code-meta/` · **00 编排** · **30 全交 subagent** · 阶段完成自动下一波 · 00 **不**改 `*.graph.yaml` |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **graph_layout** | **维持扁平** `docs/_tech_graph/*.graph.yaml`（非递归 `glob`）· **禁止**迁入 ops-desk `l0/l1/l2` |
| **human_gate（维护者）** | 见下表 · **2026-08-28 授权 00 代签过程文档** |

### 人闸表

| human_gate_id | 本 SPEC 状态 | 谁签 | 触发与策略 |
| --- | --- | --- | --- |
| **HG-SPEC-SIGNOFF** | **approved 2026-08-28** | 维护者签收 · 00 落盘 | 维护者明示「签收 spec」。审查文 `docs/harness/reviews/spec_meta-graph-full-coverage_audit_R1_20260828.md`。 |
| **HG-GRAPH-MODULES** | 扩表内容以附录 A 为已签计划；W1 落地后 00 在 `01_struct` 人签记录写 **approved 2026-08-28** | 维护者授权 00 代签 | **扩表仍须留痕**。W2/W3 30 开工前表须为 approved。00 **不**改业务包代码。 |
| **HG-AUDIT-R1** | 各波 task 表由 00 代签 `approved`（审查文先落盘） | 维护者授权 00 | 真值仍在 **task 人工闸表**。pending → 30 拒开工。 |

---

## 1. 背景与目标

**背景**

- 前序 Epic `meta-graph-interview-complete` 已 **closed**：面试最小集（P0 `cli` / `agent_core` / `node_sdk` / `monorepo_root` + P1 四子系统物化）+ 本地 `graph:ci` 门禁已落地。
- 工作区实有包已超过 `01_struct` / `AGENTS.md` Project Map：`apps/kimi-web`、`packages/protocol`、`packages/server`、`packages/server-e2e` 未登记；`packages/kimi-migration-legacy` 与 `migration_legacy` 易混。
- `00_main` 待补清单仍点名 `10_flow_mcp_tool`、`10_flow_subagent`（无 yaml）。现有 5 张 `10_flow_*` 为骨架/partial/skeleton **切片**，不是领域全量。
- 本仓工具链假定 **扁平** `docs/_tech_graph/*.graph.yaml`：`graph_yaml_compile.py` `--all` 使用 `TECH_GRAPH_DIR.glob("*.graph.yaml")`（**非递归**）。迁目录未改 glob 会漏扫。

**目标（完成态）**

1. **登记全量**：每个实有 workspace 应用/包在 `01_struct` + `graph_module_flow_map.yaml` 有 `module_id`（无包不编造；stub 包 defer 并写理由）。
2. **索引可导航**：`00_main` 为已登记模块补 struct 节点与 **有证据的** 依赖边；点名待补 flow 在代码锚存在时建 yaml 并挂索引。
3. **回归不回退**：关账时 `pnpm graph:ci` 绿；覆盖完成用 §4.2 口径，不把面试阈值当「全量」定义。
4. **布局不变**：本 Epic **维持扁平**；不学 ops-desk 把 flow 塞进 `l1/`；indexes + `rglob` 仅后继可选。

**「全量」定义（本 Epic 唯一口径）**

- **是**：工作区包/应用在 `01_struct` + `flow_map` 有登记；P0 路径有可导航 flow（既有 5 张切片 + W3 两张有锚 flow）；`00_main` 能从主干走到已登记模块与已有 flow。
- **不是**：为每个 `.ts` 画一张图；把 5 张现 flow 从 skeleton 补到生产完备；画全部 builtin tool 独立 flow；把现图迁入 l0/l1/l2。

---

## 2. 范围

### 2.1 Inform 覆盖补全（kimi-code-meta · 增量）

- [x] **W0** 以本 SPEC **附录 A 缺口清单**为真值定稿（路径级证据；禁止凭记忆改口径）。
- [x] **W1** 扩 `01_struct` 模块表 + 同步 `graph_module_flow_map.yaml`（缺的 package/app **补行**；无包不编造；stub defer）。
- [x] **W1** 扩表后 00 在 `01_struct` 回写 **HG-GRAPH-MODULES approved**（维护者 2026-08-28 授权代签）才允许后续 30。
- [x] **W2** 更新 `00_main.graph.yaml`：为 **已存在且已登记** 的模块补 struct 节点与依赖边（证据：`package.json` dependencies / 源码 import / 运行时调用注释）。**不发明依赖。**
- [x] **W3** 待补 flow：`10_flow_mcp_tool`、`10_flow_subagent` —— **仅在附录 A.4 代码锚存在时** 建 `.graph.yaml`，并在 `00_main` 加索引边。锚缺失则该条 **defer** 并写理由（本盘点：**锚均存在，默认建 yaml**）。
- [x] 关账：`02_version.md` 追加本 Epic 一行；`docs/_tech_graph/README.md`「已交付图」表增 W3 两张（若落地）。
- [x] 可选附属（非业务逻辑）：`AGENTS.md` Project Map 补上与 workspace 一致的缺行（`kimi-web` / `protocol` / `server` / `server-e2e`），避免 `01_struct`「真值来源 Project Map」再次漂移。

### 2.2 波次（每波一个可验收增量 · 可派 10-task）

| 波 | 可派 task 主题 | 验收增量 | 触及 HG-GRAPH-MODULES？ |
| --- | --- | --- | --- |
| **W0** | 缺口清单定稿 | 附录 A 与仓库核对无新增静默缺口；作为后续波输入冻结 | 否 |
| **W1** | `01_struct` + `flow_map` 包覆盖 | 附录 A.1 应补行均有 `module_id`；flow_map 1:1；无包不编造 | **是**（扩表 → pending → 人再签） |
| **W2** | `00_main` 索引边与模块依赖边 | 已登记模块均有 struct 节点；边均有附录 A.3 证据 | 否（不改模块表行） |
| **W3** | `10_flow_mcp_tool` / `10_flow_subagent` | 两 yaml 可 compile；`00_main` 索引；锚路径写入 yaml `anchors` | 否（agent_core 已登记；只加 flow） |
| **W4** | indexes + `rglob`（**可选 P2**） | 见 §3：本 Epic **默认不实施** | 若改扫描语义需单独 SPEC |

派工序：**W0 → W1（人签模块表）→ W2 / W3 可并行**（W3 不依赖新包节点，但索引边建议与 W2 同 PR 或 W2 之后合入以免 `00_main` 冲突）。**禁止** W1 未人签就派 30 改 `01_struct`。

### 2.3 现有 5 张 `10_flow_*` 的地位

| graph_id | `00_main` 清单状态 | yaml 规模（本盘点） | 本 Epic 态度 |
| --- | --- | --- | --- |
| `10_flow_cli_session` | **骨架** | 16 节点 / 18 边 | **已有切片** · 不强制充实 |
| `10_flow_agent_turn` | **partial** | 16 / 20 | 同上 |
| `10_flow_read_tool` | **partial** | 20 / 21 | 同上 |
| `10_flow_context_tool_exchange` | **skeleton** | 20 / 17 | 同上 |
| `10_flow_skill_load` | **partial · fork** | 12 / 13 | 同上 |

「全量」**不包含**把上表补到生产完备。后续业务 Issue 仍按增量触达维护。

### 2.4 工具与 CI（回归 · 非本棒实现）

- [x] 关账命令与 `.github/workflows/` 本仓图谱脚本一致：`pnpm graph:ci`（`compile:check` → `export:check` → `equivalence` → `completeness`）。
- [x] **保留**面试 Epic 阈值作回归下限，**不**把其当作本 Epic 覆盖完成定义。
- [x] **建议（W1 可做、非 P0 阻塞）**（本 Epic 仍用附录 A + 人工核验，未改 completeness 扫 workspace）：completeness 增加「workspace 实有包 vs `01_struct` 登记」检查（当前 `graph_completeness_check.py` **不**扫 `pnpm-workspace.yaml`，未登记包不会红）。未做则 W0/W1 用附录 A 人工核验。
- [x] **不改** `graph_id` 声明值口径；**不把路径当 `graph_id`**；**不改** export `FREEZE_ID`（现 `KIMI-META-GRAPH-V2-BATCH@0fa2d54f`）除非另开 schema SPEC。

---

## 3. 非范围

- **不迁** `docs/_tech_graph/` 入 ops-desk-api 的 `l0/` / `l1/` / `l2/`。那套 G-L0 / G-L1 / G-L2 语义不同（ops-desk 的 `10_flow` 在 l1；G-L2 是 indexes）。本仓 `compile` / `export` / `completeness` / `issue-sync` 假定扁平 `*.graph.yaml`。
- **不**把 G-L1 当作「所有 flow 的目录」；未来 L2 超过约 15 张才考虑 `flows/<域>/`，且 **必须先** 把 `glob` 改为 `rglob`（后继 Epic，非本 P0）。
- **W4 indexes + rglob 工具改造**：本 Epic **明确非范围**（后继可选 P2）。不得当 P0、不得与 W1–W3 绑死。
- **不**画全部 builtin tool 的独立 flow（`packages/agent-core/src/tools/builtin/` 下 file / shell / web / planning 等）。
- **不**改 `agent-core`（或任何包）生产逻辑「为了有图而改代码」。yaml 只引用已有锚。
- **不**把面试 Epic 的 completeness 阈值当本 Epic **唯一**验收。
- **不**改 dsh-coding-kit 模板语义；**不**改 Ops-desk / ops-desk-api。
- **不**重开 / 改写已 closed 的 `meta-graph-interview-complete` 目标（一次性面试加速）。
- **不**推倒重来现有 6 张图（`00_main` + 5 张 `10_flow_*`）。
- **不**为 stub 包 `packages/kimi-migration-legacy` 编造模块或空 yaml。
- MoonshotAI **上游产品行为**、给上游开功能 PR：非范围。
- 本 10-spec 棒：**不**修改任何 `*.graph.yaml` / `01_struct.md` / `graph_module_flow_map.yaml` / `tools/tech_graph/*`。

---

## 4. 验收标准

### 4.1 可勾选（关账）

- [x] 附录 A 与仓库核对：无「目录存在但 SPEC 未记录」的静默缺口。
- [x] `01_struct` 模块表覆盖附录 A.1「应登记」行；`kimi_migration_legacy` 按 A.1 defer 策略执行。
- [x] `graph_module_flow_map.yaml` 的 `module_id` 与 `01_struct` **无孤儿、无漏登记**。
- [x] `00_main`：已登记模块均有 `module_id` struct 节点；新增/补边均能指向附录 A.3 证据（`package.json` 或源码路径）。
- [x] W3：`10_flow_mcp_tool.graph.yaml`、`10_flow_subagent.graph.yaml` 存在且 `pnpm graph:compile` 可生成对应 `.md`；`00_main` 有索引边；yaml `anchors.path` 落在附录 A.4 所列文件。
- [x] **`pnpm graph:ci` 本地全绿**（可失败为红 · 回归闸）。
- [x] 现有 5 张 `10_flow_*` yaml **未被删除或改 `graph_id`**。
- [x] 10-spec **R0–R5** 已回填 · 思考轮控制表已填。
- [x] 维护者 **HG-SPEC-SIGNOFF** `approved`；W1 扩表后 **HG-GRAPH-MODULES** 人再签 `approved`。
- [x] 目录仍为扁平 `docs/_tech_graph/*.graph.yaml`（无 `l0/l1/l2` 迁移）。

### 4.2 覆盖率口径（本 Epic · 区别于面试阈值）

| ID | 口径 | 测法 |
| --- | --- | --- |
| **C1 登记** | 实有 `apps/*` + `packages/*`（扣 stub、扣已折叠的 `vis/server` `vis/web` `docs`）均有 `module_id` | 对照附录 A.1 与 `01_struct` 表 |
| **C2 映射** | 每个 `module_id` 在 flow_map ≥1 条 rule（`default_flow` 或 `none` + severity） | diff 两文件 module_id 集合 |
| **C3 索引** | 每个已登记模块在 `00_main` 有 struct 节点；`depends_on`/`calls` 边有证据 | 对照附录 A.3 |
| **C4 可导航 P0** | 既有 5 张 flow 可 compile；W3 两张有锚则落地并被 `00_main` 索引 | `glob("*.graph.yaml")` 列出 |
| **C5 回归** | `graph:ci` 绿（沿用 P0 四模块 / dep≥8 / edges≥100） | `pnpm graph:ci` exit 0 |
| **C6 禁超范围** | 不因「全量」新增 per-file 图；不把 `TOTAL_EDGES_MIN` 抬到文件数级 | SPEC 作废条件见 §5 |

面试白名单 P0/P1/P2 **可对照、不可复制为唯一目标**。本 Epic 把原 P2（`vis` / `acp_adapter` / `migration_legacy`）升为 **须登记且须 `00_main` 节点**；其 `default_flow: none` + `severity: skip` 可保留（不强制新 yaml）。

---

## 5. failure_paths

| 触发条件 | 系统行为 | 可重试 |
| --- | --- | --- |
| 扩 `01_struct` 未人签（HG-GRAPH-MODULES 仍 pending 或未改 pending 就当已签）就派 30 改码 | **拒开工** · 只输出 `gate_id` + `01_struct.md` 路径 | 是 · 等人签 |
| 先迁 `l0/l1/l2`（或 `flows/` 子目录）未把 `glob` 改为 `rglob` | `graph:ci` **假绿或漏图**（`--all` 扫不到子目录 yaml） | 是 · **回滚目录**；本 Epic 禁止此路径 |
| 无代码锚预建空 yaml | 20-task-audit / 审查 **退回** | 是 · 补锚或 defer |
| 「全量」被理解成 ~1700 文件一图 / 每 tool 一张 flow | **SPEC 作废** · 重写范围后再签 | 否 · 重开 10-spec |
| 把面试 completeness 阈值当本 Epic 唯一验收（登记缺口仍在但 `graph:ci` 绿即关账） | 00 / 40 **拒关账** | 是 · 按 §4.2 C1–C4 补 |
| 为画图改 `agent-core` 生产逻辑 | 20-task-audit **reject** | 是 · 回退业务 diff |
| 混淆 `migration_legacy` 与 `kimi-migration-legacy`，给 stub 编造模块或合并两包 | 审查退回 | 是 · 按附录 A.1 拆分 |
| `pnpm graph:ci` 因 Node engines 失败、未区分环境 vs 图谱 | 关账记录须写明；**不**把环境红当成图谱红来「修图」 | 是 · 换 Node≥24.15.0 再跑 pnpm，或记录直跑 python 四段 |

---

## 6. 依赖与引用

- 前序 closed SPEC：[`SPEC_meta_graph_interview_complete_v1_zh.md`](./SPEC_meta_graph_interview_complete_v1_zh.md)
- 模块表：[`docs/_tech_graph/01_struct.md`](../../_tech_graph/01_struct.md)
- 顶层图：[`00_main.graph.yaml`](../../_tech_graph/00_main.graph.yaml) · [`00_main.md`](../../_tech_graph/00_main.md)
- 映射：[`graph_module_flow_map.yaml`](../../_tech_graph/graph_module_flow_map.yaml)
- 工具：`tools/tech_graph/graph_yaml_compile.py`（`--all` → `TECH_GRAPH_DIR.glob("*.graph.yaml")`）· `tech_graph_graph_v2_yaml.py` 同 glob · `graph_completeness_check.py`（P0/P1 常量、不扫 workspace）
- 工作区成员真值：`pnpm-workspace.yaml`（`packages/*` · `apps/*` · `apps/vis/server` · `apps/vis/web` · `docs`）+ `flake.nix` `workspacePaths`
- 代码地图（**滞后于 workspace**）：根 [`AGENTS.md`](../../../AGENTS.md) Project Map
- 10-spec 帽：[`docs/harness/prompts/10-spec-requirements.md`](../../harness/prompts/10-spec-requirements.md)
- freeze：export `FREEZE_ID` 现值为 `KIMI-META-GRAPH-V2-BATCH@0fa2d54f` · 本 Epic **不改**；SPEC 级 `freeze_id` = `META-GRAPH-FULL-COVERAGE`

---

## 7. 思考轮（10-spec 回填 · R0–R5）

### R0 · 读入与约束

- **Open Folder**：`kimi-code-meta/`。禁止改 dsh-coding-kit、Ops-desk。
- **前序**：`meta-graph-interview-complete` closed · `graph.json` **100 nodes · 103 edges · 6 graphs** · freeze `KIMI-META-GRAPH-V2-BATCH@0fa2d54f`。
- **工具**：`--all` = 非递归 `glob("*.graph.yaml")`（`graph_yaml_compile.py:333` · `tech_graph_graph_v2_yaml.py:52`）。迁子目录必漏。
- **闸**：`HG-SPEC-SIGNOFF` pending（本棒不代签）；`HG-GRAPH-MODULES` 现行 approved，扩表须再签。
- **graph:ci（本盘点）**：`pnpm graph:ci` 因 Node `v24.14.1` < engines `>=24.15.0` **未能执行**。直跑 python：`compile:check=0` · `export:check=0` · `equivalence=0` · `completeness=0` → **图谱语义绿**。本棒不修环境红。
- **约束已钉**：不推倒 6 张现图；不复制面试「一次性加速」目标。

### R1 · 范围 / 非范围 / 角色与场景

- **角色**：图谱维护者 / 00 派工 / 30 只改 Inform 层 yaml 与模块表。
- **场景 S1**：新同事问「仓库有哪些包、依赖怎么走」→ `01_struct` + `00_main` 能答到 web/server/protocol，而不仅是 CLI 面试四件套。
- **场景 S2**：改 MCP 或 subagent 代码 → issue-sync 能命中对应 `10_flow_*`，而不是只有待补清单空行。
- **场景 S3（失败）**：有人把「全量」做成每文件一图 → §5 作废 SPEC。
- **非范围**已在 §3 闭合：禁迁目录、禁空 yaml、禁改生产逻辑、禁 kit/ops-desk。

### R2 · 方案对比

| 方案 | 做法 | 结论 |
| --- | --- | --- |
| **A · 维持扁平（推荐）** | 继续 `docs/_tech_graph/*.graph.yaml`；W1 补登记；W2 补 `00_main` 边；W3 有锚才建 2 张 flow | **采纳**。现图 6 张，远低于 ~15 张分组阈值；零工具改动即可覆盖。 |
| **B · 迁 ops-desk l0/l1/l2** | 现图改目录对齐 G-L0/G-L1/G-L2 | **禁止**。语义不同；本仓 glob 非递归 → 假绿/漏图。 |
| **C · 本 Epic 做 indexes + rglob** | 新增 `indexes/` + 扫描改 `rglob` | **弃选为 P0**。列为后继可选（§3 W4 非范围）。未改 glob 先分子目录会直接违反失败路径。 |

**推荐项不违反**：不迁目录；子流程增量；有锚才建 yaml；扩模块表人再签。

### R3 · 边界 / 失败语义 / 安全与依赖

- **模块表边界**：扩行 = HG-GRAPH-MODULES 重开 pending。W2 只加 `00_main` 节点/边不算扩表。
- **依赖边边界**：只允许附录 A.3 证据（package.json 或 import）。`kimi-web` **禁止**画到 `agent-core`/`protocol` 的 package `depends_on`（`apps/kimi-web/AGENTS.md`：不依赖 agent-core；wire 本地重实现）；只允许运行时 `kimi_web` → `server`（`::calls` / HTTP+WS）。
- **`acp_adapter` 出边漂移**：`01_struct` 写 → `node_sdk`；`packages/acp-adapter/package.json` 实有 `agent-core` + `kaos` + `kimi-code-sdk`。W1 纠正出边 = 改模块表 = **触及闸**。
- **`agent_core` 出边漂移**：表写 → kosong/kaos/oauth/telemetry；`package.json` 另有 **`@moonshot-ai/protocol`**。W1 应补出边，不发明。
- **`vis` 出边漂移**：表写 → `node_sdk`, `agent_core`；`apps/vis/server/package.json` 实有 `agent-core` + `kosong`，根包与 `vis/web` 无 moonshot 依赖。W1 纠正；W2 **禁止**无证据画 vis → node_sdk。
- **安全**：图谱 yaml 无 secret；不改业务鉴权。
- **失败语义**：见 §5。空 yaml、未签扩表、迁目录未 rglob 均为硬拒。

### R4 · 验收 / 可测性 / test_strategy

- **`test_strategy: required`**：关账必须能跑红 `pnpm graph:ci`（环境满足 Node≥24.15.0）。
- **可测**：C1–C5 均有对照文件或命令；建议 W1 增 workspace↔struct 检查，否则附录 A 人工勾选。
- **T 用例（关账）**：T1 新 module_id 出现在 struct+flow_map+`00_main`；T2 stub 包无编造行；T3 两张 W3 yaml `glob` 可见且 compile；T4 旧 5 张 `graph_id` 不变；T5 `graph:ci` exit 0。
- **不测**：builtin 全 tool 覆盖率；ops-desk snapshot ingest。

### R5 · SPEC 签收就绪 · 是否可交 00 出 task

- **就绪条件**：本文件 R0–R5 + 附录 A 路径证据 + 人闸策略写清。
- **下一棒**：**20-spec-audit** 书面审（先）→ 人签 `HG-SPEC-SIGNOFF` → 00 拆 **W0** task（不要跳过审计直接 30）。
- **不可**：本棒代签；本棒改 yaml/工具；未签就拆 W1 的 30。

---

### 思考轮控制

| 字段 | 值 |
| --- | --- |
| `actual_last_round` | `R5` |
| `early_stop` | `no` |
| `early_stop_reason` | R2 已钉「维持扁平 + 禁迁目录」，仍跑完 R3–R5 以闭合闸策略、覆盖口径与 W3 锚。 |
| `residual_risks` | **indexes 延后**（无 path/symbol 倒排；图变多时检索仍靠手翻 yaml）。L2 若未来超过约 15 张须另开 SPEC：先 `rglob` 再域目录（如 `flows/agent/`），禁止先迁后改工具。`pnpm graph:ci` 受 Node engines 约束，关账环境须 ≥24.15.0。`HG-GRAPH-MODULES` 现行签核人/日期栏空，扩表再签时建议补全。 |
| `round_extension_note` | 未扩 R6；并行切片交 00 拆 task，不在 10-spec 写 workstream 实现细节。 |

---

## 8. 维护者签收点

| 序 | 节点 | 维护者动作 |
| --- | --- | --- |
| 1 | **初版 SPEC（本文件）** | 读 §1–§6 + 附录 A · 改 **HG-SPEC-SIGNOFF** `approved`（当前 **pending**） |
| 2 | **20-spec-audit** | 读审查文 · 可 `conditional_pass` 带非阻塞项 |
| 3 | **W1 扩模块表** | `01_struct` 人签记录：HG-GRAPH-MODULES **pending → approved**（00 不代签） |
| 4 | **成品** | `pnpm graph:ci` 绿 · C1–C4 勾选 · 不迁目录 |

---

## 修订记录

| 日期 | 摘要 |
| --- | --- |
| 2026-08-28 | 00/10-spec 起草 · 覆盖补全（非重开面试 Epic）· 维持扁平 · 附录 A 路径级缺口清单 · HG-SPEC-SIGNOFF pending |
| 2026-08-28 | 维护者签收 SPEC · 授权 00 代签过程文档 · 00 不落地 · 波次自动推进 |
| 2026-08-28 | Epic CLOSE：8 张扁平 yaml · python graph 四段绿 · C1–C4 覆盖 · 00 复检 |

---

## 附录 A · 缺口清单（W0 真值 · 2026-08-28 盘点）

> 禁止凭记忆修改本附录口径。下一波若目录变化，先改本附录再改模块表。

### A.1 工作区目录 vs `01_struct` module_id

**盘点命令**：`ls -1d apps/*/ packages/*/` · `pnpm-workspace.yaml` · `flake.nix` `workspacePaths`。

| 实有路径 | npm name | `01_struct` module_id | flow_map | `00_main` struct 节点 | 处置 |
| --- | --- | --- | --- | --- | --- |
| `apps/kimi-code/` | `@moonshot-ai/kimi-code` | `cli` | 有 · `10_flow_cli_session` required | 有 `CLI` | 已覆盖 |
| `apps/vis/` | `@moonshot-ai/vis` | `vis` | 有 · `none` skip | **无** | W2 补节点；不强制新 flow |
| `apps/vis/server/` | `@moonshot-ai/vis-server` | （折叠进 `vis`） | `apps/vis/**` | — | 保持折叠 · 不另开 module |
| `apps/vis/web/` | `@moonshot-ai/vis-web` | （折叠进 `vis`） | 同上 | — | 保持折叠 |
| **`apps/kimi-web/`** | `@moonshot-ai/kimi-web` | **缺** | **缺** | **无** | **W1 补行** · 建议 `module_id: kimi_web` · README：Vue 浏览器客户端，经 REST+WS 对 `server` · **禁止**依赖 agent-core（`apps/kimi-web/AGENTS.md`） |
| `packages/agent-core/` | `@moonshot-ai/agent-core` | `agent_core` | 有（turn/read/skill/context 专链） | 有 `AC` | 已覆盖；出边缺 `protocol`（见 A.3） |
| `packages/node-sdk/` | `@moonshot-ai/kimi-code-sdk` | `node_sdk` | 有 · warn → cli_session | 有 `SDK` | 已覆盖 |
| `packages/kosong/` | `@moonshot-ai/kosong` | `kosong` | 有 · none warn | 有 `KS` | 已覆盖 |
| `packages/kaos/` | `@moonshot-ai/kaos` | `kaos` | 有 · none warn | 有 `KA` | 已覆盖 |
| `packages/oauth/` | `@moonshot-ai/kimi-code-oauth` | `oauth` | 有 · none warn | 有 `AUTH` | 已覆盖 |
| `packages/telemetry/` | `@moonshot-ai/kimi-telemetry` | `telemetry` | 有 · none warn | 有 `TELEM` | 已覆盖 |
| `packages/acp-adapter/` | `@moonshot-ai/acp-adapter` | `acp_adapter` | 有 · none skip | **无** | W2 补节点；出边漂移见 A.3 |
| `packages/migration-legacy/` | `@moonshot-ai/migration-legacy` | `migration_legacy` | 有 · none skip · glob `packages/migration-legacy/**` | **无** | **保留此 id** · W2 补节点 · 实有 `src/`（kimi-cli → kimi-code 数据迁移） |
| **`packages/kimi-migration-legacy/`** | `kimi-migration-legacy` | **缺** | **缺** | **无** | **defer / 不编造**：目录仅 `package.json`（name/version/private，无 `src/`）。**不是** `migration_legacy` 的别名。flake `workspaceNames` 有 `kimi-migration-legacy`。有源码后再登记。 |
| **`packages/protocol/`** | `@moonshot-ai/protocol` | **缺** | **缺** | **无** | **W1 补行** · 建议 `protocol` · 共享 REST+WS schema |
| **`packages/server/`** | `@moonshot-ai/server` | **缺** | **缺** | **无** | **W1 补行** · 建议 `server` · 本地 REST+WS，host agent-core，可 serve kimi-web 静态资源 |
| **`packages/server-e2e/`** | `@moonshot-ai/server-e2e` | **缺** | **缺** | **无** | **W1 补行** · 建议 `server_e2e` · wire E2E · `default_flow: none` + skip/warn |
| `docs/` | `kimi-code-docs` | （折叠进 `monorepo_root`） | `docs/**` skip | 有 `MONO` | 保持折叠 · 不另开 module |
| `build/**` `scripts/**` `flake.nix` | — | `monorepo_root` | 有 | 有 `MONO` | 已覆盖 |

**`AGENTS.md` Project Map 滞后**：只列 `kimi-code` / `vis` / `agent-core` / `node-sdk` / `kosong` / `kaos` / `oauth` / `telemetry`。未列 `kimi-web`、`protocol`、`server`、`server-e2e`、`acp-adapter`、两迁移包。W1 建议同步 Project Map（文档，非业务逻辑）。

**已知缺（用户点名，本盘点确认）**：`apps/kimi-web`、`packages/protocol`、`packages/server`、`packages/server-e2e`。

### A.2 flow_map 覆盖 vs 上表

`graph_module_flow_map.yaml` 已有 `module_id`：`cli` · `agent_core`（4 条 rule）· `node_sdk` · `monorepo_root` · `kosong` · `kaos` · `oauth` · `telemetry` · `vis` · `acp_adapter` · `migration_legacy`。

**缺 rule（随 W1 新 module 补）**：`kimi_web` · `protocol` · `server` · `server_e2e`。  
**不补**：`kimi_migration_legacy`（无源码）。  
**W3 后**：`agent_core` 可增 MCP / subagent 专链（`path_globs` 指向 `packages/agent-core/**/mcp/**` 与 `**/session/subagent-*.ts`），priority 高于 default turn flow —— 属 W3，不在 W1 预写空 glob。

### A.3 `00_main` 模块节点与依赖边（只登记有证据的）

**现有 `module_id` 节点**：`cli` `node_sdk` `agent_core` `kosong` `kaos` `telemetry` `oauth` `monorepo_root`。  
**缺节点（已在 struct 但 00_main 无）**：`vis` · `acp_adapter` · `migration_legacy`。  
**缺节点（struct 亦无，W1 后补）**：`kimi_web` · `protocol` · `server` · `server_e2e`。

**证据（W2 允许的边 · 禁止发明）**：

| 边（建议） | 证据 |
| --- | --- |
| `cli` → `node_sdk` | 已有；`AGENTS.md`：CLI 经 SDK，禁止直接依赖 agent-core |
| `node_sdk` → `agent_core` | 已有；`packages/node-sdk/package.json` devDependency workspace + `src/index.ts` import |
| `agent_core` → `kosong` `kaos` `oauth` | 已有；`packages/agent-core/package.json` dependencies |
| `agent_core` → `telemetry` | 已有 00_main 边；以现图为准，W2 不删 |
| **`agent_core` → `protocol`** | **`packages/agent-core/package.json` dependencies 含 `@moonshot-ai/protocol`** · 01_struct 出边 **未写** · W1 改表 + W2 加边 |
| **`server` → `agent_core`** | `packages/server/package.json` dependencies |
| **`server` → `protocol`** | 同上 |
| **`server_e2e` → `protocol`** | `packages/server-e2e/package.json` dependencies |
| **`kimi_web` ⤳ `server`** | README / AGENTS：浏览器经 Vite proxy `/api/v1` 打到 local server；**package.json 无 moonshot 依赖**。边类型用 `calls` / `::triggers`，**不要**标 package `depends_on` |
| `cli` → `server` / `kimi_web` | `apps/kimi-code/package.json` **devDependencies** 含两者（server 随 CLI `kimi server run` 分发）。W2 可画，须在边注释标明 dev/bundle 而非 CLI 运行时 import agent-core |
| `acp_adapter` → `node_sdk` | 01_struct 已声明 |
| **`acp_adapter` → `agent_core`、`kaos`** | `packages/acp-adapter/package.json` dependencies · **纠正 01_struct 出边** |
| `migration_legacy` → `agent_core` | `packages/migration-legacy/package.json` dependencies · 与 01_struct 一致 |
| `vis`（折叠）依赖 | **不要照抄 01_struct「→ node_sdk, agent_core」**。证据：`apps/vis/package.json` 无 moonshot 依赖；`apps/vis/server/package.json` → `@moonshot-ai/agent-core` + `@moonshot-ai/kosong`；`apps/vis/web/package.json` 无 moonshot 依赖。W1 纠正 vis 出边（触及闸）；W2 只画 `vis` → `agent_core` / `kosong`（经 vis-server）。**禁止**无证据画 `vis` → `node_sdk` |

`00_main` 现有 TOOLS 聚合节点（skills · MCP · subagents）可保留；W3 落地后加 `FLOW_MCP` / `FLOW_SUB` 索引边，类比 `FLOW_SKILL`。

### A.4 待补 flow 与代码锚（W3）

| 拟定 graph_id | `00_main` 清单 | yaml | 锚（本盘点 **存在** → 默认建 yaml，不 defer） |
| --- | --- | --- | --- |
| `10_flow_mcp_tool` | 待补 · 仅清单 | **无** | `packages/agent-core/src/mcp/connection-manager.ts`（`class McpConnectionManager`）· `packages/agent-core/src/mcp/index.ts` · `packages/agent-core/src/agent/tool/index.ts`（`attachMcpTools`）· `packages/agent-core/src/skill/builtin/mcp-config.ts` · 次要（daemon 面，可作第二切片或同图注释，**不另画全 server 图**）：`packages/agent-core/src/services/mcp/mcp.ts` · `mcpService.ts` |
| `10_flow_subagent` | 待补 · 仅清单 | **无** | `packages/agent-core/src/session/subagent-host.ts`（`class SessionSubagentHost`）· `packages/agent-core/src/session/subagent-batch.ts` · `packages/agent-core/src/session/index.ts`（`subagentHost` 装配）· `packages/agent-core/test/session/subagent-host.test.ts` · TUI 消费（**可选锚，不单独成图**）：`apps/kimi-code/src/tui/controllers/subagent-event-handler.ts` |

无真实改码触点的其它域（server REST 全路由、kimi-web 每个 SFC、全部 builtin tool）**不预画空 yaml**。

### A.5 现有 6 张图与工具扫描

非递归 `ls docs/_tech_graph/*.graph.yaml` 仅 6 个文件（与 `find` 递归结果相同，**尚无子目录 yaml**）：

- `00_main.graph.yaml`
- `10_flow_agent_turn.graph.yaml`
- `10_flow_cli_session.graph.yaml`
- `10_flow_context_tool_exchange.graph.yaml`
- `10_flow_read_tool.graph.yaml`
- `10_flow_skill_load.graph.yaml`

`graph.json` `graphs[].id` 与上表一致。`module_ids on nodes`：`agent_core` `cli` `kaos` `kosong` `monorepo_root` `node_sdk` `oauth` `telemetry`（无 vis/acp/migration/web/server/protocol）。

completeness 常量（面试回归，**非本 Epic 覆盖定义**）：`P0_MODULES={cli,agent_core,node_sdk,monorepo_root}` · `P1={kosong,kaos,oauth,telemetry}` · `MODULE_DEP_TOUCH_MIN=8` · `TOTAL_EDGES_MIN=100` · **不扫 workspace 包清单**。

### A.6 `pnpm graph:ci` 现状（只记录 · 本棒不修红）

| 入口 | 结果 |
| --- | --- |
| `pnpm graph:ci` | **未跑成**：`ERR_PNPM_UNSUPPORTED_ENGINE` · 本机 Node `v24.14.1` · 仓 `engines` `>=24.15.0`（`.npmrc` `engine-strict=true`） |
| `python3 tools/tech_graph/graph_yaml_compile.py --all --check` | exit 0 · 6 张 slice OK |
| `python3 tools/tech_graph/tech_graph_graph_export.py --check` | exit 0 |
| `python3 tools/tech_graph/tech_graph_graph_equivalence_check.py` | exit 0 |
| `python3 tools/tech_graph/graph_completeness_check.py` | exit 0 · `OK: graph completeness check passed` |

**结论**：图谱 Inform/CI 脚本语义当前为绿；pnpm 入口被 Node 引擎拦住。关账须在 Node≥24.15.0 下复跑 `pnpm graph:ci`。本 Epic **不**把升级 Node 当范围。

---

## 附录 B · 下一棒可复制 Prompt

### B.1 给 20-spec-audit（SPEC 仍 draft · 人签前）

复制下面整段（外层围栏不要一起粘）：

    你 = kimi-code-meta 仓 20-spec-audit。Open Folder = 本仓根 kimi-code-meta/。

    审：docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md
    帽：docs/harness/prompts/20-spec-audit.md
    对照（closed，勿当本 Epic 目标）：docs/tasks/specs/SPEC_meta_graph_interview_complete_v1_zh.md

    核对：范围/非范围/波次/验收 §4.2/failure_paths/R0–R5/思考轮控制/附录 A 路径证据。
    硬条件：维持扁平、禁迁 l0/l1/l2、扩 01_struct 须 HG-GRAPH-MODULES 人再签、有锚才建 mcp/subagent yaml、不把面试 completeness 当唯一验收。

    落盘：docs/harness/reviews/spec_meta-graph-full-coverage_audit_R1_YYYYMMDD.md
    判定 pass | conditional_pass | fail。不代签 HG-SPEC-SIGNOFF。不改 yaml/工具/业务代码。

### B.2 人签后给 00 拆 W0 task

    你 = kimi-code-meta 仓 00 统筹 · 帽子 10-task。Open Folder = 本仓根。

    SPEC 已 HG-SPEC-SIGNOFF approved：docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md
    只拆 W0（缺口清单定稿 / 冻结附录 A）。不要拆 W1 的 30，直到 W0 关且维护者确认附录无静默缺口。
    W1 起改 01_struct 前：HG-GRAPH-MODULES 改 pending，等人再签。
    禁止迁 l0/l1/l2。test_strategy=required。过程 invoke 落到 docs/harness/invokes/by-task/meta-graph-full-coverage/。
