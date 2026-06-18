#!/usr/bin/env python3
"""L3 · 产品 diff ↔ 模块 ↔ flow ↔ task graph_delta 跨 worktree 校验."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from graph_sync_common import (
    REPO_ROOT,
    load_flow_map,
    meta_graph_files_with_diff,
    parse_task_harness_fields,
    resolve_graph_delta_targets,
    get_product_diff_files,
)


def run_l3(
    task_path: Path,
    repo_root: Path,
    product_root: Path,
    product_ref: str,
    allow_graph_none: bool = False,
    allow_reason: str | None = None,
    map_path: Path | None = None,
) -> tuple[int, list[str]]:
    messages: list[str] = []

    if not task_path.is_file():
        messages.append(f"ERROR: task 不存在: {task_path}")
        return 2, messages

    if allow_graph_none and not (allow_reason and allow_reason.strip()):
        messages.append("ERROR: --allow-graph-none 须配合 --reason")
        return 2, messages

    code, product_paths, err = get_product_diff_files(product_root, product_ref)
    if code != 0:
        messages.append(err)
        return code, messages

    if not product_paths:
        messages.append(f"L3 OK: 产品 diff 无 apps/packages 变更 ({product_ref})")
        return 0, messages

    messages.append(f"产品 diff ({len(product_paths)}): {product_paths[:5]}{'…' if len(product_paths) > 5 else ''}")

    rules = load_flow_map(map_path)
    from graph_sync_common import collect_flows_for_paths

    required_flows, warn_flows, skip_only = collect_flows_for_paths(product_paths, rules)

    if warn_flows:
        messages.append(f"WARN: node_sdk 等触达 flow: {sorted(warn_flows)}")

    if skip_only and not required_flows:
        messages.append("L3 OK: 仅触达 skip 路径（harness/docs）")
        return 0, messages

    fields = parse_task_harness_fields(task_path)
    graph_delta = fields.get("graph_delta", "").strip()
    delta_targets = resolve_graph_delta_targets(graph_delta)

    if graph_delta.lower() == "none":
        if allow_graph_none:
            messages.append(
                f"L3 OVERRIDE: graph_delta=none · reason={allow_reason.strip()}"
            )
            return 0, messages
        messages.append(
            "ERROR: 产品触达模块但 task graph_delta=none · 改 task 或 --allow-graph-none --reason"
        )
        return 2, messages

    if not delta_targets:
        messages.append("ERROR: graph_delta 无法解析为 flow 文件")
        return 2, messages

    missing_in_delta = sorted(required_flows - set(delta_targets))
    if missing_in_delta:
        messages.append(
            f"ERROR: 期望 flow {missing_in_delta} 未包含在 task graph_delta ({delta_targets})"
        )
        return 1, messages

    diff_map = meta_graph_files_with_diff(repo_root, list(required_flows))
    missing_meta = [name for name, has_diff in diff_map.items() if not has_diff]
    if missing_meta:
        messages.append(
            f"ERROR: 产品触达模块 · 期望 flow 无 meta diff: {missing_meta}"
        )
        return 1, messages

    messages.append(f"L3 OK: required flows {sorted(required_flows)} ⊆ graph_delta · meta 有 diff")
    return 0, messages


def main() -> None:
    parser = argparse.ArgumentParser(description="L3 product diff ↔ module ↔ flow sync check")
    parser.add_argument("--task", required=True, type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--product-root", required=True, type=Path)
    parser.add_argument(
        "--product-ref",
        default="upstream/main...HEAD",
        help="git diff ref（默认 upstream/main...HEAD）",
    )
    parser.add_argument("--allow-graph-none", action="store_true")
    parser.add_argument("--reason", default="", help="--allow-graph-none 时必填")
    parser.add_argument("--map", type=Path, default=None, help="自定义 flow map 路径")
    args = parser.parse_args()

    task_path = args.task if args.task.is_absolute() else args.repo_root / args.task
    product_root = (
        args.product_root
        if args.product_root.is_absolute()
        else args.repo_root / args.product_root
    ).resolve()

    code, messages = run_l3(
        task_path,
        args.repo_root,
        product_root,
        args.product_ref,
        allow_graph_none=args.allow_graph_none,
        allow_reason=args.reason,
        map_path=args.map,
    )
    for line in messages:
        print(line)
    sys.exit(code)


if __name__ == "__main__":
    main()
