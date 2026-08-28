# SPEC · 现有 10_flow_* 画完画深（v1）

> **状态**：`closed`（**HG-SPEC-SIGNOFF approved 2026-08-28** · 维护者本会话授权 00 统筹至关账 · 00 代签过程文档）  
> **track**：`epic`  
> **前序**：[`SPEC_meta_graph_full_coverage_v1_zh.md`](./SPEC_meta_graph_full_coverage_v1_zh.md) **closed**（登记全量 + 8 张扁平 yaml + `graph:ci`）。**本 SPEC 不重开覆盖 Epic，不新增包模块，不迁 l0/l1/l2。**  
> **目标**：把已有 **7 张** `10_flow_*.graph.yaml` 从骨架/partial/skeleton 提升到可导航的 **`deep`**。  
> **编排**：00 拆 task · 30 subagent 按图落地 · 00 不改 yaml。

---

## Harness 元信息

| 字段 | 值 |
| --- | --- |
| **spec_slug** | `meta-graph-flow-deepen` |
| **freeze_id** | `META-GRAPH-FLOW-DEEPEN` |
| **test_strategy** | `required` |
| **test_strategy_note** | 每波 compile 本图；关账 `pnpm graph:ci`（Node ≥24.15.0 / `nvm use`）。 |
| **orchestration** | 00 编排 · **每张 flow 一张 30** · 完成自动下一波 · 00 **不**落地 |
| **git_branch** | `cyning/meta` |
| **worktree_root** | `kimi-code-meta/` |
| **graph_layout** | 维持扁平 `docs/_tech_graph/*.graph.yaml` |
| **human_gate** | 见下表 · 维护者 2026-08-28 授权 00 代签过程文档 |

### 人闸表

| human_gate_id | 状态 | 谁签 | 说明 |
| --- | --- | --- | --- |
| **HG-SPEC-SIGNOFF** | **approved 2026-08-28** | 维护者授权 00 落盘 | 本会话「spec 到最终完成的统筹」 |
| **HG-GRAPH-MODULES** | 维持 `01_struct` **approved 2026-08-28** | 不重开 | **本 Epic 不扩模块表** |
| **HG-AUDIT-R1** | 各波 task 表 00 代签 | 审查文先落盘 | pending → 30 拒开工 |

---

## 1. 背景与目标

**背景**：覆盖 Epic 已让 7 张 `10_flow_*` **存在且可 compile**，但 `00_main` 待补表仍全部是 骨架 / partial / skeleton。协议要求硬边可追溯（`anchors.path` + 尽量 `line`）；现状极不均（`read_tool` 21 边仅 3 锚；`agent_turn` 几乎只有 #583 telemetry 切片，未画 `TurnFlow.runStepLoop`）。

**「画完」**：7 张现图均不再标 skeleton/骨架；happy path 从入口走到本域终点。  
**「画深」**：达到 §4.2 **D 条**；不是每 `.ts` 一张图，不是全部 builtin tool 新开 `10_flow_*`。

**完成态**

1. 7 张 yaml **原地加深**（保留 `graph_id`；禁止推倒换 id）。
2. compile.py 待补表 7 行状态改为 **`deep`**。
3. `pnpm graph:ci` 绿。
4. 无新模块行、无 l0/l1/l2、无生产逻辑改码。

---

## 2. 范围

### 2.1 只加深这 7 张（冻结名单）

| graph_id | 现状（2026-08-28 盘点） | 本 Epic 加深重点 |
| --- | --- | --- |
| `10_flow_cli_session` | 骨架 · 16n/18e · 锚 8/7lined | `apps/kimi-code` 启动 → SDK `createSession` → TUI/ACP 分叉 → ApprovalPanel 四选项（已有骨架）补真实 path+line：`cli/run-prompt.ts` · `tui/reverse-rpc/approval/adapter.ts` · `approval/controller.ts` |
| `10_flow_agent_turn` | partial · 16n/20e · 锚 5/1lined | **补主干** `TurnFlow.runOneTurn` / `runStepLoop`（`packages/agent-core/src/agent/turn/index.ts`）；现有 telemetry #583 **降为侧链**，禁止只加深 outcome 三色而仍无 loop |
| `10_flow_read_tool` | partial · 20n/21e · 锚 **3** | 拓扑已有，**补锚**：`tools/builtin/file/read.ts` 全硬边；补文件不存在 / schema 校验 `[err]`（若代码有） |
| `10_flow_context_tool_exchange` | skeleton · 20n/17e · 锚 12/11lined | 核对 resume/orphan/#705 与现码；补缺口边+line；已对齐则升 `deep` 并写 notes |
| `10_flow_skill_load` | partial · fork · 12n/13e · 锚 7 | 补 `discoverSkills` / `resolveSkillRoots` 多根扫描；保留 invalid YAML `[err]` |
| `10_flow_mcp_tool` | skeleton · 14n/15e · 锚 18 lined | 补 needs-auth / reconnect 侧链（`connection-manager` 已有 status）；transport 保持折叠 |
| `10_flow_subagent` | skeleton · 12n/15e · 锚 15 lined | 补 timeout / user-cancel / rate-limit 侧链（`subagent-batch.ts` 注释合同已存在） |

### 2.2 波次（一图一 task）

| 波 | task | 可并行 |
| --- | --- | --- |
| W-cli | 只改 `10_flow_cli_session.graph.yaml` | 与其它 W-* 并行 |
| W-turn | 只改 `10_flow_agent_turn.graph.yaml` | 并行 |
| W-read | 只改 `10_flow_read_tool.graph.yaml` | 并行 |
| W-ctx | 只改 `10_flow_context_tool_exchange.graph.yaml` | 并行 |
| W-skill | 只改 `10_flow_skill_load.graph.yaml` | 并行 |
| W-mcp | 只改 `10_flow_mcp_tool.graph.yaml` | 并行 |
| W-sub | 只改 `10_flow_subagent.graph.yaml` | 并行 |
| W-close | compile.py 待补表 7 行 → `deep` · `02_version` · README 状态字 · `pnpm graph:ci` · export | **7 张 yaml 均 deep 之后** |

并行纪律：30 **只** `compile --graph-id <本图>`；**禁止** `--all`、禁止 export `graph.json`、禁止改 `00_main.graph.yaml` / `01_struct` / `flow_map` / `compile.py`（后三项归 W-close，flow_map 本 Epic 默认不动）。

---

## 3. 非范围

- 不新增 `10_flow_*`（不画 shell/web/planning/goal 等独立图）
- 不为 `kimi_web` / `server` / `protocol` 开新 flow（登记已在覆盖 Epic）
- 不迁 l0/l1/l2；不改 glob→rglob；不做 indexes
- 不改 `agent-core` / `apps/**` 生产逻辑「为了有图而改代码」
- 不扩 `01_struct` 模块集
- 不把「画深」做成 1700 文件一图
- 不改 dsh-coding-kit / Ops-desk
- 不重开 `meta-graph-full-coverage`

---

## 4. 验收

### 4.1 关账可勾选

- [x] 7 张 `graph_id` 未改；仍扁平 8 yaml（含 `00_main`）
- [x] 每张达到 §4.2 D 条；compile.py 表 7 行均为 **`deep`**
- [x] `pnpm graph:ci` 绿
- [x] 无生产码 diff；无 l0/l1/l2
- [x] HG-SPEC-SIGNOFF 已签；各波 HG-AUDIT-R1 已签

### 4.2 画深口径（D 条 · 每张 30 自检必填）

| ID | 口径 | 测法 |
| --- | --- | --- |
| **D1 主干** | 本域入口→终点 happy path 连续 | 人读 mermaid 主干无断 |
| **D2 失败** | 代码有失败则图上至少 1 条 `[err]`/`[timeout]`/cancel 侧链 | yaml `mark` |
| **D3 锚覆盖** | 硬边（非纯注释元边）`anchors.path` ≥ **70%**；其中 `line` ≥ **50%** | 脚本或手计 |
| **D4 无 TBD** | 无 `TBD` 路径；禁止虚构 path | rg TBD |
| **D5 协议** | 分支用 `?>` / `[ok]` / `[err]`；不发明依赖 | 对照 99_mermaid_protocol |
| **D6 折叠** | 节点不宜无上限膨胀；子域 >7 步折叠为阶段块，**不**另开新 `10_flow_*` | 审查 |
| **D7 真码** | 新增节点能指到现存函数/文件 | 读源码 |
| **D8 回归** | 本图 `compile --graph-id` 成功 | 命令 |

`agent_turn` **额外硬条件**：必须出现 `TurnFlow` / `runStepLoop`（或 `runOneTurn`）节点，telemetry 不得充当唯一主干。

---

## 5. failure_paths

| 触发 | 行为 | 可重试 |
| --- | --- | --- |
| 为画深改生产 TS | 退回 | 是 · 回退业务 diff |
| 并行 30 改 `00_main` / `graph.json` / `compile.py` | 退回 | 是 |
| 锚覆盖 <70% 仍报 deep | W-close 拒收该图 | 是 · 补锚 |
| `agent_turn` 仍只有 telemetry 切片 | 拒收 | 是 |
| 新建第 8 张 `10_flow_*` | 退回删除 | 是 |
| 迁目录 | 回滚扁平 | 是 |
| `graph:ci` 红 | 关账失败 | 是 · 修 yaml 或 Node |

---

## 6. 依赖

- 前序 closed：`SPEC_meta_graph_full_coverage_v1_zh.md`
- 协议：`docs/_tech_graph/99_mermaid_protocol.md`
- 编辑源：`docs/_tech_graph/10_flow_*.graph.yaml`
- 代码锚见 §2.1 表

---

## 7. 思考轮 R0–R5

### R0
7 张均已存在。浅：read 锚 3；turn 缺 loop。深：mcp/sub 行号全但标 skeleton。覆盖 Epic 明确「不强制充实」；本 Epic 才是充实。

### R1
范围=原地加深 7 张。非范围=新图/新包/迁目录/改生产码。角色=图谱 30，一图一 agent。

### R2
- **A 原地加深（推荐）**：保留 graph_id 与可用拓扑，补主干+锚+失败侧链。
- **B 七张推倒重画**：弃选，丢失 issue 切片与审查成本。
- **C 每 tool 一张新 flow**：禁止，违反「全量≠每文件一图」。

### R3
并行只碰本 yaml。D3 百分比防「改两个 label 就称 deep」。turn 硬条件防切片冒充画完。

### R4
test_strategy=required。每波 D1–D8；关账 graph:ci。

### R5
可拆 7+1 task。00 不落地。

### 思考轮控制

| 字段 | 值 |
| --- | --- |
| actual_last_round | R5 |
| early_stop | no |
| early_stop_reason | — |
| residual_risks | 代码演进后 line 漂移；D3 手计可能误差；context/skill 若已接近 deep 则 30 以核对为主避免为深而深。indexes 仍非本 Epic。 |

---

## 8. 维护者签收点

| 序 | 节点 | 动作 |
| --- | --- | --- |
| 1 | SPEC | 已授权 00 代签过程文档 |
| 2 | 各波 30 | subagent |
| 3 | 成品 | `pnpm graph:ci` + 7×`deep` |

## 修订记录

| 日期 | 摘要 |
| --- | --- |
| 2026-08-28 | 00/10-spec 起草 · 7 张画完画深 · 一图一 task |
| 2026-08-28 | Epic CLOSE · 7×deep · python graph 四段绿 · 00 复检 |
