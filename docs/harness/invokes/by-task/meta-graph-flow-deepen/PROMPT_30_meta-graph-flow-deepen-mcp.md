# 30 · 加深 10_flow_mcp_tool

Open Folder = kimi-code-meta 仓根。帽子 30。
task: docs/tasks/active/task_meta_graph_flow_deepen_mcp_v1.md
SPEC: docs/tasks/specs/SPEC_meta_graph_flow_deepen_v1_zh.md §4.2 D1–D8 与 §2.1 `10_flow_mcp_tool` 行

GATE_VERIFY 首输出。只改 docs/_tech_graph/10_flow_mcp_tool.graph.yaml 并 compile --graph-id 10_flow_mcp_tool。

加深重点：补 needs-auth / reconnect 侧链；transport 继续折叠。

禁止：--all、export graph.json、改 00_main/01_struct/flow_map/compile.py、改生产码、git commit、新建 10_flow。

被 ignore 的路径用 Shell required_permissions=["all"]。

回填 ### 自检结论（D1–D8 + path% + line%）。
落盘 invoke_20260828_30_mcp.md。
回报 ≤10 行：是否 deep、锚覆盖率、compile 是否绿。
