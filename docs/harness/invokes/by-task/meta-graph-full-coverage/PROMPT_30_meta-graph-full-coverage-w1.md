# 30 · W1 01_struct + flow_map

Open Folder = kimi-code-meta 仓根。帽子 30。
task: docs/tasks/active/task_meta_graph_full_coverage_w1_v1.md
SPEC 附录 A.1/A.2: docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md
W0 freeze: docs/harness/invokes/by-task/meta-graph-full-coverage/W0_FREEZE_20260828.md

GATE_VERIFY 首输出。闸已 approved。本波只改 Inform 文档，禁止 packages/apps 生产逻辑（AGENTS.md Project Map 文档行允许）。

## 必须落地

01_struct.md 新增行（module_id 用下表，禁止编造 kimi_migration_legacy）：

| module_id | 路径 | 出边（有证据） | flow_map |
| kimi_web | apps/kimi-web/** | 运行时 calls server，无 moonshot package 依赖 | none warn |
| protocol | packages/protocol/** | — | none warn |
| server | packages/server/** | agent_core, protocol | none warn |
| server_e2e | packages/server-e2e/** | protocol | none skip |

纠正出边：
- agent_core 加 protocol（package.json dependencies）
- acp_adapter → agent_core, kaos, node_sdk
- vis → agent_core, kosong（经 vis-server）；删除 vis→node_sdk

graph_module_flow_map.yaml 与 01_struct module_id 1:1。新包 default_flow none。不要预写 MCP/subagent 空 glob。

可选：根 AGENTS.md Project Map 补 kimi-web / protocol / server / server-e2e。

人签记录：扩表后把 HG-GRAPH-MODULES 写成 approved 2026-08-28，签核人填「00 代签（维护者 2026-08-28 授权过程文档）」。

禁止：新建 10_flow yaml；迁目录；git commit。

回填 ### 自检结论 + invoke_20260828_30_w1.md。
回报 ≤10 行：新增 module_id 列表、出边纠正、flow_map 是否 1:1。
