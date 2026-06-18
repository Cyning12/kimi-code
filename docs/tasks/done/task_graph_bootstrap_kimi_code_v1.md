# Task：图谱 bootstrap · kimi-code fork（阶段 B）

> **状态**：in_progress  
> **关联图谱**：`docs/_tech_graph/00_main.md` · `01_struct.md`  
> **试点真值**：`[docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md](../../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)` → 工作区 PILOT

---

## Harness 元信息


| 字段                     | 值                        |
| ---------------------- | ------------------------ |
| **test_strategy**      | `not_applicable`         |
| **test_strategy_note** | bootstrap 无业务 30；文档与人签关账 |
| **orchestration**      | Cursor Task 链            |
| **audit_profile**      | `human_only`             |


### 人工闸


| human_gate_id    | status   | blocks_hats | 说明                   |
| ---------------- | -------- | ----------- | -------------------- |
| HG-TASK-DRAFT    | approved | 22-R1       | task 初稿人扫            |
| HG-GRAPH-MODULES | approved | **30**      | `01_struct` 模块表维护者人签 |


> 本 task **无** `HG-AUDIT-R1`（无业务 30）。关账后开阶段 C 业务 task。

---

## 背景与目标

个人 fork 上建立 **S3 monorepo** 图谱最低交付：模块表 + 顶层图 + 待补 flow 清单；**不**一次画完全仓 flow。

---

## 范围

- [x] `docs/_tech_graph/` 模板落盘（`harness-sync` + graph track）
- [x] `01_struct` 一级模块表（对照 `AGENTS.md`）
- [x] `00_main` / `00_main.ai` CLI 主干
- [x] `10_flow_cli_session.md` **骨架**（非终稿）
- [x] 维护者签 `HG-GRAPH-MODULES` → `approved`
- [x] 维护者签 `HG-TASK-DRAFT`（可选，与上图谱闸一并）

## 非范围

- 向 Moonshot 上游 PR 图谱或 harness 文件
- 本 task 内 **30 改产品代码**
- 一次性补全 `10_flow_agent_turn` / MCP / subagent 等（留阶段 C 增量）

---

## 验收标准

- [ ] `01_struct` 模块表覆盖 `apps/` + `packages/` 一级包
- [ ] `00_main` 待补 flow 清单已列且标明阶段
- [ ] `gate-check.sh` 在签 `HG-GRAPH-MODULES` 前对业务 task 拒 30（本 task 无 30）
- [ ] task 移 `done/` 或标 done · invoke 关账记录（可选）

---

## 分步图谱（与阶段关系）


| 子步     | 内容                                | 阶段                                |
| ------ | --------------------------------- | --------------------------------- |
| B1     | 模块表 + `00_main` + 待补清单            | **阶段 B（本 task）**                  |
| B2     | 单条 flow 骨架（`10_flow_cli_session`） | **阶段 B 可选** · 已做骨架                |
| C+     | 每张 `10_flow_`* 终稿、锚点、`.ai.md`     | **阶段 C 业务 task** 或 **图谱增量子 task** |
| Epic 后 | 多 flow 对齐、CI 图谱校验（若启用）            | M2+ / 关账                          |


---

## 给维护者

签核前请打开 `docs/_tech_graph/01_struct.md` 核对模块表，然后在本表将 `HG-GRAPH-MODULES` 改为 `approved`。