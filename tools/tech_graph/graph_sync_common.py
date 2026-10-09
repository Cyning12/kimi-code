"""L2/L3 issue sync gate · 共享解析与路径匹配."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
TECH_GRAPH_DIR = REPO_ROOT / "docs" / "_tech_graph"
FLOW_MAP_PATH = TECH_GRAPH_DIR / "graph_module_flow_map.yaml"
VERSION_PATH = TECH_GRAPH_DIR / "02_version.md"


def iter_graph_yaml(input_root: Path) -> list[Path]:
    """递归发现 *.graph.yaml（G-L 物理分层 · l0/l1/...）。"""
    return sorted(input_root.rglob("*.graph.yaml"))


def resolve_graph_yaml(input_root: Path, graph_id: str) -> Path:
    """按 graph_id 解析 yaml 路径；同名多份时优先较浅路径。"""
    name = f"{graph_id}.graph.yaml"
    matches = [p for p in iter_graph_yaml(input_root) if p.name == name]
    if not matches:
        # 兼容旧调用方：返回根下约定路径（可能尚不存在）
        return input_root / name
    matches.sort(key=lambda p: (len(p.relative_to(input_root).parts), str(p)))
    return matches[0]


def resolve_flow_rel(tech_graph_dir: Path, flow_name: str) -> str:
    """flow_map 中的 default_flow（可为 basename 或相对子路径）→ 相对 tech_graph 的 posix 路径。"""
    direct = tech_graph_dir / flow_name
    if direct.is_file():
        return direct.relative_to(tech_graph_dir).as_posix()
    base = Path(flow_name).name
    for p in iter_graph_yaml(tech_graph_dir):
        if p.name == base:
            return p.relative_to(tech_graph_dir).as_posix()
    return flow_name.replace("\\", "/")


COMPILE_SCRIPT = REPO_ROOT / "tools" / "tech_graph" / "graph_yaml_compile.py"

PRODUCT_PREFIXES = ("apps/", "packages/")


def parse_task_harness_fields(task_path: Path) -> dict[str, str]:
    """从 task Harness 元信息表解析字段."""
    text = task_path.read_text(encoding="utf-8")
    fields: dict[str, str] = {}
    for field in (
        "graph_delta",
        "graph_delta_note",
        "task_slug",
        "module_id",
        "freeze_id",
    ):
        match = re.search(rf"\|\s*\*\*{field}\*\*\s*\|\s*(.+?)\s*\|", text)
        if match:
            raw = match.group(1).strip()
            fields[field] = raw.replace("`", "").strip()
    return fields


def normalize_posix(path: str) -> str:
    return path.replace("\\", "/").lstrip("./")


def path_matches_glob(filepath: str, pattern: str) -> bool:
    """匹配 glob；支持 trailing `/**` 前缀语义."""
    fp = normalize_posix(filepath)
    pat = normalize_posix(pattern)
    if pat.endswith("/**"):
        return fp.startswith(pat[:-3]) or fp == pat[:-3].rstrip("/")
    if pat.endswith("**"):
        return fp.startswith(pat[:-2])
    from fnmatch import fnmatch

    return fnmatch(fp, pat)


def path_matches_substrings(filepath: str, substrings: list[str] | None) -> bool:
    if not substrings:
        return True
    fp = normalize_posix(filepath)
    return any(sub in fp for sub in substrings)


def load_flow_map(map_path: Path | None = None) -> list[dict[str, Any]]:
    path = map_path or FLOW_MAP_PATH
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    rules = data.get("rules", [])
    return sorted(rules, key=lambda rule: -(rule.get("priority") or 0))


def match_rules_for_path(filepath: str, rules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """返回匹配 filepath 的规则（已按 priority 排序）."""
    matched: list[dict[str, Any]] = []
    for rule in rules:
        globs = rule.get("path_globs") or []
        if not any(path_matches_glob(filepath, glob_pattern) for glob_pattern in globs):
            continue
        if not path_matches_substrings(filepath, rule.get("path_substrings")):
            continue
        matched.append(rule)
    return matched


def collect_flows_for_paths(
    paths: list[str],
    rules: list[dict[str, Any]],
) -> tuple[set[str], set[str], set[str]]:
    """返回 (required_flows, warn_flows, skip_only) — flow 为文件名或 none."""
    required: set[str] = set()
    warns: set[str] = set()
    skip_only = True
    for filepath in paths:
        matched = match_rules_for_path(filepath, rules)
        if not matched:
            continue
        rule = matched[0]
        severity = rule.get("severity", "required")
        flow = rule.get("default_flow", "none")
        if severity == "skip":
            continue
        skip_only = False
        if severity == "warn":
            if flow and flow != "none":
                warns.add(flow)
        else:
            if flow and flow != "none":
                required.add(flow)
    return required, warns, skip_only


def resolve_graph_delta_targets(graph_delta: str) -> list[str]:
    value = graph_delta.strip()
    if not value or value.lower() == "none":
        return []
    raw_parts = re.split(r"\s*[·|]\s*", value)
    targets: list[str] = []
    for part in raw_parts:
        part = part.strip()
        if not part:
            continue
        if "/" in part:
            name = Path(part).name
        else:
            name = part
        if not name.endswith(".graph.yaml"):
            if name.endswith(".yaml"):
                name = name.replace(".yaml", ".graph.yaml")
            else:
                name = f"{name}.graph.yaml"
        targets.append(name)
    return targets


def git_diff_name_only(repo_root: Path, *extra_args: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", *extra_args],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def collect_changed_files(repo_root: Path) -> set[str]:
    changed: set[str] = set()
    changed.update(git_diff_name_only(repo_root))
    changed.update(git_diff_name_only(repo_root, "--cached"))
    if _is_git_repo(repo_root):
        changed.update(git_diff_name_only(repo_root, "HEAD~1", "HEAD"))
        changed.update(git_diff_name_only(repo_root, "HEAD~10", "HEAD"))
        for base in ("cyning/meta", "origin/cyning/meta", "main", "origin/main"):
            mb = subprocess.run(
                ["git", "merge-base", "HEAD", base],
                cwd=repo_root,
                capture_output=True,
                text=True,
            )
            if mb.returncode != 0 or not mb.stdout.strip():
                continue
            changed.update(git_diff_name_only(repo_root, mb.stdout.strip(), "HEAD"))
            break
    return {normalize_posix(path) for path in changed}


def meta_graph_files_with_diff(
    repo_root: Path,
    flow_names: list[str],
    tech_graph_dir: Path | None = None,
) -> dict[str, bool]:
    graph_dir = tech_graph_dir or repo_root / "docs" / "_tech_graph"
    changed = collect_changed_files(repo_root)
    result: dict[str, bool] = {}
    for flow_name in flow_names:
        flow_rel = resolve_flow_rel(graph_dir, flow_name)
        rel = normalize_posix(str(graph_dir.relative_to(repo_root) / flow_rel))
        result[flow_name] = rel in changed
    return result


def _is_git_repo(path: Path) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=path,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0 and result.stdout.strip() == "true"


def run_l1_compile_check(repo_root: Path, skip: bool = False) -> tuple[int, str]:
    if skip:
        return 0, "L1 skipped"
    result = subprocess.run(
        [sys.executable, str(COMPILE_SCRIPT), "--all", "--check"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        timeout=120,
    )
    output = (result.stderr or "") + (result.stdout or "")
    return result.returncode, output.strip()


def check_version_warn(task_path: Path, strict: bool = False) -> tuple[bool, str]:
    """02_version.md 含 task slug 或 issue 号 → WARN；strict 时视为失败."""
    fields = parse_task_harness_fields(task_path)
    slug = fields.get("task_slug", "")
    text = VERSION_PATH.read_text(encoding="utf-8")
    task_text = task_path.read_text(encoding="utf-8")
    issue_match = re.search(r"#(\d+)", task_text)
    issue_token = f"#{issue_match.group(1)}" if issue_match else ""
    found = False
    if slug and slug in text:
        found = True
    if issue_token and issue_token in text:
        found = True
    if found:
        return True, "OK: 02_version.md 含 slug/issue 引用"
    if strict:
        return False, "ERROR: 02_version.md 缺少 task slug 或 issue 行（--strict）"
    return True, "WARN: 02_version.md 未含 task slug/issue（可关账时补一行）"


def filter_product_paths(paths: list[str]) -> list[str]:
    return [
        normalize_posix(path)
        for path in paths
        if any(normalize_posix(path).startswith(prefix) for prefix in PRODUCT_PREFIXES)
    ]


def get_product_diff_files(product_root: Path, product_ref: str) -> tuple[int, list[str], str]:
    if not product_root.is_dir():
        return 2, [], f"product worktree 不存在: {product_root}"
    if not _is_git_repo(product_root):
        return 2, [], f"product root 非 git 仓库: {product_root}"
    result = subprocess.run(
        ["git", "diff", "--name-only", product_ref],
        cwd=product_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = (result.stderr or result.stdout or "").strip()
        return 2, [], f"git diff 失败 ({product_ref}): {stderr}"
    paths = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return 0, filter_product_paths(paths), ""
