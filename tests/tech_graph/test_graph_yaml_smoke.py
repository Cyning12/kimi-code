"""tech_graph 工具链 smoke tests（meta graph_v2 batch）."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TECH_GRAPH = REPO_ROOT / "docs" / "_tech_graph"
TOOLS = REPO_ROOT / "tools" / "tech_graph"

EXPECTED_GRAPHS = [
    "00_main",
    "10_flow_cli_session",
    "10_flow_agent_turn",
    "10_flow_read_tool",
    "10_flow_context_tool_exchange",
    "10_flow_skill_load",
]


def test_all_graph_yaml_sources_exist() -> None:
    for graph_id in EXPECTED_GRAPHS:
        path = TECH_GRAPH / f"{graph_id}.graph.yaml"
        assert path.is_file(), f"missing {path}"


def test_graph_yaml_compile_all() -> None:
    result = subprocess.run(
        [sys.executable, str(TOOLS / "graph_yaml_compile.py"), "--all"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    for graph_id in EXPECTED_GRAPHS:
        md = TECH_GRAPH / f"{graph_id}.md"
        assert md.is_file(), f"missing compiled {md}"


def test_graph_export_and_schema() -> None:
    export = subprocess.run(
        [sys.executable, str(TOOLS / "tech_graph_graph_export.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert export.returncode == 0, export.stderr or export.stdout
    graph_json = TECH_GRAPH / "graph.json"
    assert graph_json.is_file()
    data = graph_json.read_text(encoding="utf-8")
    assert '"schema_version": "graph_v2"' in data


def test_equivalence_check_passes() -> None:
    subprocess.run(
        [sys.executable, str(TOOLS / "tech_graph_graph_export.py")],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
    )
    result = subprocess.run(
        [sys.executable, str(TOOLS / "tech_graph_graph_equivalence_check.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout
