# invoke · 40 · fix-skill-frontmatter-580

## 元信息表

| 字段 | 值 |
|------|-----|
| hat_id | 40 |
| task_slug | `fix-skill-frontmatter-580` |
| freeze_id | — |
| task_paths | `docs/tasks/active/task_fix_skill_frontmatter_580_v1.md` |
| related_review_or_none | 30 invoke `invoke_20260611_30_fix-skill-frontmatter-580.md` · commit `516958cb` |
| git_branch | `feature/fix-580-skill-frontmatter` |
| worktree_root | `/Users/cyning/Desktop/Projects/kimi-code` |
| created_utc_or_local | 2026-06-11 |
| notes | 阶段 C3 · Issue #580 · 方案 B 验证复核 |

---

## 可复制 Prompt 快照

```text
（见 40 对话首条 user 消息 · 2026-06-11）
```

---

## 交付摘要（本帽结束时填）

**状态**：✅ 40 完成 · 2026-06-11

### 命令证据

| 命令 | cwd | 退出码 | 关键输出 |
|------|-----|--------|----------|
| `git log -1 --oneline` | kimi-code | 0 | `516958cb fix(agent-core): load directory skills with frontmatter fallbacks` |
| `pnpm --filter @moonshot-ai/agent-core test -- test/skill` | kimi-code | 0 | Test Files 167 passed · Tests 2522 passed |
| `pnpm lint` | kimi-code | 0 | 0 errors |
| `git diff upstream/main --name-only` | kimi-code | 0 | 4 files（agent-core×3 + changeset） |
| `pnpm --filter @moonshot-ai/agent-core test -- test/skill/builtin` | kimi-code | 0 | Test Files 167 passed · Tests 2522 passed |

### 验收摘要

- A1–A8：pass
- A9：pending（PR 未开）
- A10：pending（图谱关账 PR 合并后 meta 另帽）
- R4 T1–T3/T5/T7：pass（scanner.test + parser.test + builtin 全绿）

### 下一棒

维护者 `git push` + `gh pr create`（Fixes #580），或下发 50 独立复检。
