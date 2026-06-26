"""graph_completeness_check 单元测试."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "tools" / "tech_graph"
GRAPH = REPO_ROOT / "docs" / "_tech_graph" / "graph.json"


def test_completeness_check_passes_on_committed_graph() -> None:
    result = subprocess.run(
        [sys.executable, str(TOOLS / "graph_completeness_check.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout


def test_completeness_fails_when_p0_module_missing(tmp_path: Path) -> None:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    data["nodes"] = [n for n in data["nodes"] if n.get("module_id") != "cli"]
    bad = tmp_path / "graph.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            str(TOOLS / "graph_completeness_check.py"),
            "--graph",
            str(bad),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 4
    assert "cli" in (result.stderr or "")


def test_graph_ci_script_exists() -> None:
    pkg = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))
    assert "graph:ci" in pkg.get("scripts", {})
