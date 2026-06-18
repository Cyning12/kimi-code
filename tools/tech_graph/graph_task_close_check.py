#!/usr/bin/env python3
"""L2 · task 关账 ↔ meta 图谱增量校验."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from graph_sync_common import (
    REPO_ROOT,
    check_version_warn,
    meta_graph_files_with_diff,
    parse_task_harness_fields,
    resolve_graph_delta_targets,
    run_l1_compile_check,
)


def run_l2(
    task_path: Path,
    repo_root: Path,
    skip_l1: bool = False,
    strict_version: bool = False,
) -> tuple[int, list[str]]:
    messages: list[str] = []
    if not task_path.is_file():
        messages.append(f"ERROR: task 不存在: {task_path}")
        return 2, messages

    code, l1_out = run_l1_compile_check(repo_root, skip=skip_l1)
    if code != 0:
        messages.append("L1 graph:compile:check 失败")
        if l1_out:
            messages.append(l1_out)
        return 1, messages
    messages.append("L1 graph:compile:check OK")

    fields = parse_task_harness_fields(task_path)
    graph_delta = fields.get("graph_delta", "").strip()
    graph_delta_note = fields.get("graph_delta_note", "").strip()

    if not graph_delta:
        messages.append("ERROR: task 缺少 graph_delta 字段")
        return 2, messages

    if graph_delta.lower() == "none":
        if not graph_delta_note:
            messages.append("ERROR: graph_delta=none 但缺少 graph_delta_note")
            return 1, messages
        messages.append("L2 OK: graph_delta=none · note 已填")
    else:
        targets = resolve_graph_delta_targets(graph_delta)
        diff_map = meta_graph_files_with_diff(repo_root, targets)
        missing = [name for name, has_diff in diff_map.items() if not has_diff]
        if missing:
            messages.append(
                f"ERROR: graph_delta 指向 {targets} 但 meta 无 diff: {missing}"
            )
            return 1, messages
        messages.append(f"L2 OK: graph_delta 目标已有 meta diff: {targets}")

    version_ok, version_msg = check_version_warn(task_path, strict=strict_version)
    messages.append(version_msg)
    if not version_ok:
        return 1, messages

    return 0, messages


def main() -> None:
    parser = argparse.ArgumentParser(description="L2 task ↔ meta graph close check")
    parser.add_argument(
        "--task",
        required=True,
        type=Path,
        help="task markdown 路径",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="meta 仓根（默认本仓）",
    )
    parser.add_argument("--skip-l1", action="store_true", help="测试用 · 跳过 L1")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="02_version 缺 slug/issue 时 exit 1",
    )
    args = parser.parse_args()

    task_path = args.task if args.task.is_absolute() else args.repo_root / args.task
    code, messages = run_l2(
        task_path,
        args.repo_root,
        skip_l1=args.skip_l1,
        strict_version=args.strict,
    )
    for line in messages:
        print(line)
    sys.exit(code)


if __name__ == "__main__":
    main()
