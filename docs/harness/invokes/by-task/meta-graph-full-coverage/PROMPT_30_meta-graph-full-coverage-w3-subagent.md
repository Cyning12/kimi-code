# 30 · W3b 10_flow_subagent

扁平新建 docs/_tech_graph/10_flow_subagent.graph.yaml
graph_id: "10_flow_subagent"
风格对齐 10_flow_skill_load.graph.yaml

锚：
- packages/agent-core/src/session/subagent-host.ts (SessionSubagentHost)
- packages/agent-core/src/session/subagent-batch.ts
- packages/agent-core/src/session/index.ts (subagentHost 装配)
可选：test/session/subagent-host.test.ts；TUI subagent-event-handler.ts 只作消费注释，不单独成图。

切片即可。不要改 00_main.graph.yaml。不要 git commit。
compile。回填自检 + invoke_20260828_30_w3_subagent.md
