# 30 · W0 缺口清单定稿

Open Folder = kimi-code-meta 仓根。帽子 30。

task: docs/tasks/active/task_meta_graph_full_coverage_w0_v1.md
SPEC 附录 A: docs/tasks/specs/SPEC_meta_graph_full_coverage_v1_zh.md
帽: docs/harness/prompts/30-execute-code.md

## GATE_VERIFY（首输出）

读 task 人工闸表。HG-TASK-DRAFT / HG-AUDIT-R1 应为 approved 2026-08-28。
禁止改 packages/apps 生产代码。本波禁止改 *.graph.yaml / 01_struct.md / flow_map。

## 做

1. 复盘 ls apps/*/ packages/*/ 与附录 A.1，找静默缺口
2. 确认 kimi-migration-legacy 仍仅 package.json
3. 确认 A.4 锚文件仍存在
4. 落盘 docs/harness/invokes/by-task/meta-graph-full-coverage/W0_FREEZE_20260828.md
5. 回填 task ### 自检结论
6. 落盘 invoke_20260828_30_w0.md 短记

若发现静默缺口：先改 SPEC 附录 A 再 freeze，并在回报列出。

禁止 git commit / push。禁止迁 l0/l1/l2。

回报 ≤10 行：freeze 与否、新增缺口、改了哪些文件。
