"""L2/L3 issue sync gate pytest."""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "tools" / "tech_graph"
TECH_GRAPH = REPO_ROOT / "docs" / "_tech_graph"


def _run_script(script: str, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOLS / script), *args],
        cwd=cwd or REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _init_git_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "test"], cwd=path, check=True)


def _write_task(
    root: Path,
    graph_delta: str,
    graph_delta_note: str = "",
    slug: str = "test-sync-gate",
) -> Path:
    task_dir = root / "docs" / "tasks" / "active"
    task_dir.mkdir(parents=True, exist_ok=True)
    note_line = graph_delta_note or "占位说明"
    content = textwrap.dedent(
        f"""
        # Task test

        | 字段 | 值 |
        |------|-----|
        | **task_slug** | `{slug}` |
        | **graph_delta** | `{graph_delta}` |
        | **graph_delta_note** | {note_line} |
        """
    ).strip() + "\n"
    task_path = task_dir / "task_test_sync.md"
    task_path.write_text(content, encoding="utf-8")
    return task_path


def _setup_mini_meta(tmp_path: Path) -> Path:
    graph_dir = tmp_path / "docs" / "_tech_graph"
    graph_dir.mkdir(parents=True)
    (graph_dir / "02_version.md").write_text("# version\n", encoding="utf-8")
    (graph_dir / "10_flow_cli_session.graph.yaml").write_text(
        "graph_id: 10_flow_cli_session\nnodes: []\nedges: []\n",
        encoding="utf-8",
    )
    map_src = TECH_GRAPH / "graph_module_flow_map.yaml"
    if map_src.is_file():
        (graph_dir / "graph_module_flow_map.yaml").write_text(
            map_src.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
    tools_dir = tmp_path / "tools" / "tech_graph"
    tools_dir.mkdir(parents=True)
    for name in (
        "graph_sync_common.py",
        "graph_task_close_check.py",
        "graph_product_sync_check.py",
    ):
        src = TOOLS / name
        (tools_dir / name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    _init_git_repo(tmp_path)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=tmp_path, check=True, capture_output=True)
    return tmp_path


def test_l2_graph_delta_none_with_note_passes(tmp_path: Path) -> None:
    root = _setup_mini_meta(tmp_path)
    task = _write_task(root, "none", "门禁基础设施 · 无单图增量")
    result = _run_script(
        "graph_task_close_check.py",
        "--task",
        str(task),
        "--repo-root",
        str(root),
        "--skip-l1",
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_l2_graph_delta_without_diff_fails(tmp_path: Path) -> None:
    root = _setup_mini_meta(tmp_path)
    task = _write_task(root, "10_flow_cli_session.graph.yaml", "需要 yaml diff")
    result = _run_script(
        "graph_task_close_check.py",
        "--task",
        str(task),
        "--repo-root",
        str(root),
        "--skip-l1",
    )
    assert result.returncode == 1, result.stdout + result.stderr
    assert "无 diff" in result.stdout or "ERROR" in result.stdout


def test_l2_graph_delta_with_diff_passes(tmp_path: Path) -> None:
    root = _setup_mini_meta(tmp_path)
    yaml_path = root / "docs" / "_tech_graph" / "10_flow_cli_session.graph.yaml"
    yaml_path.write_text(
        yaml_path.read_text(encoding="utf-8") + "# touched\n",
        encoding="utf-8",
    )
    task = _write_task(root, "10_flow_cli_session.graph.yaml", "yaml 已改")
    result = _run_script(
        "graph_task_close_check.py",
        "--task",
        str(task),
        "--repo-root",
        str(root),
        "--skip-l1",
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_l3_product_missing_worktree_exit_2() -> None:
    task = REPO_ROOT / "docs/tasks/active/task_meta_graph_issue_sync_gate_v1.md"
    missing = REPO_ROOT / "tmp_nonexistent_product_root"
    result = _run_script(
        "graph_product_sync_check.py",
        "--task",
        str(task),
        "--product-root",
        str(missing),
        "--product-ref",
        "HEAD",
    )
    assert result.returncode == 2
    assert "不存在" in result.stdout or "不存在" in result.stderr


def test_l3_mock_cli_diff_no_meta_diff_exit_1(tmp_path: Path) -> None:
    root = _setup_mini_meta(tmp_path)
    product = tmp_path / "product"
    product.mkdir()
    _init_git_repo(product)
    (product / "apps" / "kimi-code" / "src").mkdir(parents=True)
    (product / "apps" / "kimi-code" / "src" / "foo.ts").write_text("x", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=product, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "product"], cwd=product, check=True, capture_output=True)
    (product / "apps" / "kimi-code" / "src" / "foo.ts").write_text("xy", encoding="utf-8")

    task = _write_task(root, "10_flow_cli_session.graph.yaml", "437 mock")
    result = _run_script(
        "graph_product_sync_check.py",
        "--task",
        str(task),
        "--repo-root",
        str(root),
        "--product-root",
        str(product),
        "--product-ref",
        "HEAD",
    )
    assert result.returncode == 1
    assert "无 meta diff" in result.stdout or "ERROR" in result.stdout


def test_l3_mock_cli_diff_with_meta_yaml_exit_0(tmp_path: Path) -> None:
    root = _setup_mini_meta(tmp_path)
    yaml_path = root / "docs" / "_tech_graph" / "10_flow_cli_session.graph.yaml"
    yaml_path.write_text(yaml_path.read_text(encoding="utf-8") + "# mock\n", encoding="utf-8")

    product = tmp_path / "product"
    product.mkdir()
    _init_git_repo(product)
    (product / "apps" / "kimi-code" / "src").mkdir(parents=True)
    (product / "apps" / "kimi-code" / "src" / "foo.ts").write_text("x", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=product, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "product"], cwd=product, check=True, capture_output=True)
    (product / "apps" / "kimi-code" / "src" / "foo.ts").write_text("xy", encoding="utf-8")

    task = _write_task(root, "10_flow_cli_session.graph.yaml", "437 mock")
    result = _run_script(
        "graph_product_sync_check.py",
        "--task",
        str(task),
        "--repo-root",
        str(root),
        "--product-root",
        str(product),
        "--product-ref",
        "HEAD",
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_l3_product_module_graph_delta_none_exit_2(tmp_path: Path) -> None:
    root = _setup_mini_meta(tmp_path)
    product = tmp_path / "product"
    product.mkdir()
    _init_git_repo(product)
    (product / "apps" / "kimi-code" / "src").mkdir(parents=True)
    (product / "apps" / "kimi-code" / "src" / "bar.ts").write_text("x", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=product, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "p"], cwd=product, check=True, capture_output=True)
    (product / "apps" / "kimi-code" / "src" / "bar.ts").write_text("xy", encoding="utf-8")

    task = _write_task(root, "none", "本 task 无图增量")
    result = _run_script(
        "graph_product_sync_check.py",
        "--task",
        str(task),
        "--repo-root",
        str(root),
        "--product-root",
        str(product),
        "--product-ref",
        "HEAD",
    )
    assert result.returncode == 2
    assert "graph_delta=none" in result.stdout


def test_flow_map_exists_and_covers_cli() -> None:
    map_path = TECH_GRAPH / "graph_module_flow_map.yaml"
    assert map_path.is_file()
    text = map_path.read_text(encoding="utf-8")
    assert "apps/kimi-code" in text
    assert "10_flow_cli_session.graph.yaml" in text
    assert "severity: warn" in text
    assert "monorepo_root" in text
