from __future__ import annotations

"""
graph.json 完整性 lint（meta-graph-interview-complete · WS-0）。

退出码：
- 0：通过（P1 缺失仅 stderr warn）
- 4：completeness 未达阈值
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = _SCRIPT_DIR.parent.parent
DEFAULT_GRAPH = REPO_ROOT / "docs" / "_tech_graph" / "graph.json"
DEFAULT_STRUCT = REPO_ROOT / "docs" / "_tech_graph" / "01_struct.md"

P0_MODULES = frozenset({"cli", "agent_core", "node_sdk", "monorepo_root"})
P1_MODULES = frozenset({"kosong", "kaos", "oauth", "telemetry"})
P0_EDGE_EXEMPT = frozenset({"monorepo_root"})
MODULE_DEP_TOUCH_MIN = 8
TOTAL_EDGES_MIN = 100


def _stderr(msg: str) -> None:
    print(msg, file=sys.stderr)


def parse_struct_module_ids(struct_path: Path) -> set[str]:
    """从 01_struct.md 模块表解析 module_id。"""
    text = struct_path.read_text(encoding="utf-8")
    ids: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"^\|\s*`([^`]+)`\s*\|", line)
        if m and m.group(1) != "module_id":
            ids.add(m.group(1))
    if not ids:
        raise ValueError(f"未从 {struct_path} 解析到 module_id")
    return ids


def _node_index(nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {n["id"]: n for n in nodes if isinstance(n, dict) and "id" in n}


def _module_id_of(node: dict[str, Any] | None) -> str | None:
    if not node:
        return None
    mid = node.get("module_id")
    return mid if isinstance(mid, str) and mid else None


def check_completeness(
    graph: dict[str, Any],
    *,
    struct_ids: set[str],
) -> tuple[list[str], list[str]]:
    """返回 (errors, warnings)。"""
    errors: list[str] = []
    warnings: list[str] = []

    nodes = graph.get("nodes") or []
    edges = graph.get("edges") or []
    by_id = _node_index(nodes)

    module_ids_on_nodes = {
        mid for n in nodes if (mid := _module_id_of(n)) is not None
    }

    for mid in sorted(module_ids_on_nodes - struct_ids):
        errors.append(f"孤儿 module_id（不在 01_struct）: {mid}")

    for mid in sorted(P0_MODULES):
        if mid not in module_ids_on_nodes:
            errors.append(f"P0 缺 struct 节点 module_id={mid}")

    for mid in sorted(P1_MODULES):
        if mid not in module_ids_on_nodes:
            warnings.append(f"P1 warn: 缺 struct 节点 module_id={mid}")

    module_dep_touch = 0
    p0_in_module_edges: set[str] = set()

    for edge in edges:
        if not isinstance(edge, dict):
            continue
        if edge.get("type") != "depends_on":
            continue
        if "ref" in edge:
            continue
        src = _module_id_of(by_id.get(edge.get("from", "")))
        dst = _module_id_of(by_id.get(edge.get("to", "")))
        if src or dst:
            module_dep_touch += 1
            if src in P0_MODULES:
                p0_in_module_edges.add(src)
            if dst in P0_MODULES:
                p0_in_module_edges.add(dst)

    for mid in sorted(P0_MODULES - P0_EDGE_EXEMPT):
        if mid not in p0_in_module_edges:
            errors.append(f"P0 module_id={mid} 未出现在 module depends_on 边中")

    if module_dep_touch < MODULE_DEP_TOUCH_MIN:
        errors.append(
            f"module depends_on 触达边 {module_dep_touch} < {MODULE_DEP_TOUCH_MIN}"
        )

    total_edges = len(edges)
    if total_edges < TOTAL_EDGES_MIN:
        errors.append(f"graph.json edges.length {total_edges} < {TOTAL_EDGES_MIN}")

    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="graph.json 模块完整性 lint")
    parser.add_argument(
        "--graph",
        type=Path,
        default=DEFAULT_GRAPH,
        help="graph.json 路径",
    )
    parser.add_argument(
        "--struct",
        type=Path,
        default=DEFAULT_STRUCT,
        help="01_struct.md 路径",
    )
    args = parser.parse_args(argv)

    if not args.graph.is_file():
        _stderr(f"graph.json 不存在: {args.graph}")
        return 4
    if not args.struct.is_file():
        _stderr(f"01_struct 不存在: {args.struct}")
        return 4

    graph = json.loads(args.graph.read_text(encoding="utf-8"))
    struct_ids = parse_struct_module_ids(args.struct)
    errors, warnings = check_completeness(graph, struct_ids=struct_ids)

    for w in warnings:
        _stderr(f"WARN: {w}")

    if errors:
        _stderr("completeness FAIL:")
        for e in errors:
            _stderr(f"  - {e}")
        return 4

    print("OK: graph completeness check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
