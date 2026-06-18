#!/usr/bin/env python3
"""聚合 L1→L2→L3 · Issue 关账 graph:issue-sync."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="L1+L2+L3 issue sync gate")
    parser.add_argument("--task", required=True, type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--product-root", type=Path, default=None)
    parser.add_argument(
        "--product-ref",
        default="upstream/main...HEAD",
    )
    parser.add_argument("--allow-graph-none", action="store_true")
    parser.add_argument("--reason", default="")
    parser.add_argument("--skip-l3", action="store_true", help="仅跑 L1+L2")
    args = parser.parse_args()

    repo_root = args.repo_root
    task = args.task if args.task.is_absolute() else repo_root / args.task

    l2_script = TOOLS / "graph_task_close_check.py"
    l3_script = TOOLS / "graph_product_sync_check.py"

    print("=== graph:issue-sync · L1+L2 ===")
    l2 = subprocess.run(
        [sys.executable, str(l2_script), "--task", str(task), "--repo-root", str(repo_root)],
        cwd=repo_root,
    )
    if l2.returncode != 0:
        print(f"graph:issue-sync FAIL at L2 (exit {l2.returncode})")
        sys.exit(l2.returncode)

    if args.skip_l3 or args.product_root is None:
        print("=== graph:issue-sync · L3 skipped ===")
        print("graph:issue-sync PASS (L1+L2)")
        sys.exit(0)

    product_root = (
        args.product_root
        if args.product_root.is_absolute()
        else repo_root / args.product_root
    ).resolve()

    l3_cmd = [
        sys.executable,
        str(l3_script),
        "--task",
        str(task),
        "--repo-root",
        str(repo_root),
        "--product-root",
        str(product_root),
        "--product-ref",
        args.product_ref,
    ]
    if args.allow_graph_none:
        l3_cmd.append("--allow-graph-none")
        l3_cmd.extend(["--reason", args.reason])

    print("=== graph:issue-sync · L3 ===")
    l3 = subprocess.run(l3_cmd, cwd=repo_root)
    if l3.returncode != 0:
        print(f"graph:issue-sync FAIL at L3 (exit {l3.returncode})")
        sys.exit(l3.returncode)

    print("graph:issue-sync PASS (L1+L2+L3)")
    sys.exit(0)


if __name__ == "__main__":
    main()
