# 图谱版本时间线

| 日期 | 事件 |
|------|------|
| 2026-06-10 | 阶段 B bootstrap：`01_struct` + `00_main` + `10_flow_cli_session` 骨架 |
| 2026-06-10 | 移除无用 `10_flow_MAIN*`（harness HTTP 模板） |
| 2026-06-10 | C2 #583：`10_flow_agent_turn` 切片（tool.result → telemetry · PR [#630](https://github.com/MoonshotAI/kimi-code/pull/630)） |
| 2026-06-11 | C3 #580：`10_flow_skill_load` 骨架（task 草稿 · 待思考/30） |
| 2026-06-11 | C3 #580：`10_flow_skill_load` **partial · fork**（`516958cb` · issue comment · **待 upstream merge**） |
| 2026-06-12 | C3 #94：`10_flow_read_tool` skeleton → **partial**（`finishMessage` 双限 · fork · 待 PR） |
| 2026-06-13 | C3 #94：`10_flow_read_tool` partial 关账 · PR [#708](https://github.com/MoonshotAI/kimi-code/pull/708) OPEN · task `done/` |
| 2026-06-13 | C3 #705：`10_flow_context_tool_exchange` **skeleton** · task `task_fix_open_tool_calls_705_v1` · 模块扫描 §2.2 |
| 2026-06-18 | **graph_v2 batch CLOSE**：6 图 `*.graph.yaml` 唯一编辑源 · compile → `.md` · export `graph.json` v2 · task `meta-graph-v2-batch-migrate` |
| 2026-06-18 | **issue sync gate CLOSE**：L2/L3 门禁 · `graph_module_flow_map.yaml` · `pnpm graph:issue-sync` · `KIMI-META-GRAPH-SYNC-GATE@ecc7b9dc` |
| 2026-06-18 | C3 #437：`10_flow_cli_session` **skeleton** · approve-once vs session · task `fix-approve-once-437` |
| 2026-06-26 | **meta-graph-interview-complete Epic CLOSE**：WS-0–5 · `graph:ci` · flow_map 全模块 · 00 复检 |
| 2026-08-28 | **meta-graph-full-coverage Epic CLOSE**：W0–W3 + W-close · 8 图扁平 `*.graph.yaml` · `FLOW_MCP`/`FLOW_SUB` 索引 · C1–C4；C5 见自检 |
| 2026-08-28 | **meta-graph-flow-deepen Epic CLOSE**：7 张 `10_flow_*` 待补表 → **deep** · D3 path/line 抽检 100% · 仍 8 张扁平 `*.graph.yaml` · `graph:ci` |
