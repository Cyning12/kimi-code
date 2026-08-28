# 30 · W-close 索引 + 关账

W3 yaml 已存在：
- docs/_tech_graph/10_flow_mcp_tool.graph.yaml
- docs/_tech_graph/10_flow_subagent.graph.yaml

## 做
1. 00_main.graph.yaml 增加 FLOW_MCP / FLOW_SUB 节点（label >10_flow_mcp_tool.md 与 >10_flow_subagent.md）及从 TOOLS 或 AC 的索引边，风格对齐 FLOW_SKILL。
2. 更新 tools/tech_graph/graph_yaml_compile.py 里 generate_sub_graph_links 硬编码待补清单：两张改为已有 yaml（skeleton/partial），不要改 glob 为 rglob，不要迁目录。
3. graph_module_flow_map.yaml 为 agent_core 增 MCP / subagent 专链（path_globs 指向 mcp/** 与 session/subagent-*.ts，priority 10）。
4. docs/_tech_graph/README.md 已交付图表增两行。
5. 02_version.md 追加 Epic 关账行 2026-08-28 meta-graph-full-coverage。
6. python3 四段：compile --all --check, export --check, equivalence, completeness。能跑则 pnpm graph:ci；Node engines 失败则记录直跑 python 绿。
7. 对照 SPEC §4.2 C1-C5 在自检勾选。

禁止改生产业务逻辑。禁止 git commit。禁止 l0/l1/l2。
回填自检 + invoke_20260828_30_w_close.md。
