# 30 · W2 00_main 模块节点与有证据边

Open Folder = kimi-code-meta 仓根。
task: docs/tasks/active/task_meta_graph_full_coverage_w2_v1.md

只改 docs/_tech_graph/00_main.graph.yaml（编辑源），然后 python3 tools/tech_graph/graph_yaml_compile.py --all 与 tech_graph_graph_export.py 同步 md/json。

## 补 struct 节点（module_id 必填）
vis, acp_adapter, migration_legacy, kimi_web, protocol, server, server_e2e
不要为 kimi-migration-legacy stub 加节点。

## 边（禁止发明）
- agent_core to protocol (depends_on)
- server to agent_core and protocol
- server_e2e to protocol
- kimi_web to server 用 mark ::triggers 或 type calls（禁止 kimi_web depends_on agent_core/protocol）
- acp_adapter to agent_core, kaos, node_sdk
- vis to agent_core, kosong；禁止 vis to node_sdk
- migration_legacy to agent_core
- 可选：cli 到 server/kimi_web 若画，须注释 devDependencies/bundle

不要加 FLOW_MCP / FLOW_SUB（W-close）。
不要新建 10_flow yaml。
不要 git commit。不要迁目录。

回填自检 + invoke_20260828_30_w2.md。
跑 python compile --all --check, export --check, equivalence, completeness。
