# invoke · 30 · fix-docs-node-565

## 元信息表

| 字段 | 值 |
|------|-----|
| hat_id | 30 |
| task_slug | `fix-docs-node-565` |
| freeze_id | — |
| task_paths | `docs/tasks/active/task_fix_docs_node_565_v1.md` |
| related_review_or_none | `无` |
| git_branch | `feature/fix-565-docs-node` |
| worktree_root | `/Users/cyning/Desktop/Projects/kimi-code` |
| created_utc_or_local | 2026-06-10 |
| notes | 阶段 C 首张业务 task · 上游 #565 |

---

## 可复制 Prompt 快照

```text
@../kimi-code-meta/docs/tasks/active/task_fix_docs_node_565_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md

先输出人工闸扫描；通过后改 en/zh getting-started 的 Node 版本说明。
```

---

## 交付摘要（本帽结束时填）

- **验证命令** + 退出码
  - `rg "Node.js|node" docs/en/guides/getting-started.md docs/zh/guides/getting-started.md` → exit 0；npm 段均为 22.19.0
  - `git diff upstream/main --name-only` → 仅 `docs/en/guides/getting-started.md`、`docs/zh/guides/getting-started.md`
- **变更路径**
  - `docs/en/guides/getting-started.md` — `24.15.0` → `22.19.0`
  - `docs/zh/guides/getting-started.md` — `24.15.0` → `22.19.0`
- **上游 PR**：https://github.com/MoonshotAI/kimi-code/pull/622（`Fixes #565`）
- **下一棒**：交还维护者（PR 合并后 task 关账）
