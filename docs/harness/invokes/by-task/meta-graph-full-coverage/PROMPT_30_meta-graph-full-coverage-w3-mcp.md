# 30 · W3a 10_flow_mcp_tool

扁平新建 docs/_tech_graph/10_flow_mcp_tool.graph.yaml
graph_id: "10_flow_mcp_tool"
风格对齐 10_flow_skill_load.graph.yaml（节点少、边有 anchors.path）

锚（必须至少用这些 path）：
- packages/agent-core/src/mcp/connection-manager.ts
- packages/agent-core/src/mcp/index.ts
- packages/agent-core/src/agent/tool/index.ts  (attachMcpTools)
- packages/agent-core/src/skill/builtin/mcp-config.ts
次要可注 services/mcp/mcp.ts，不要另开 server 全路由图。

切片即可。不要每个 transport 一张图。不要改 00_main.graph.yaml。
compile 该 graph 或 --all。不要 git commit。不要迁目录。
回填自检 + invoke_20260828_30_w3_mcp.md
