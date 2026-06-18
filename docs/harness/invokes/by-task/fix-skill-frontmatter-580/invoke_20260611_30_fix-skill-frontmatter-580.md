# invoke · 30 · fix-skill-frontmatter-580

## 元信息表

| 字段 | 值 |
|------|-----|
| hat_id | 30 |
| task_slug | `fix-skill-frontmatter-580` |
| freeze_id | — |
| task_paths | `docs/tasks/active/task_fix_skill_frontmatter_580_v1.md` |
| related_review_or_none | 审阅 Agent R0～R5 · 维护者同意方案 B |
| git_branch | `feature/fix-580-skill-frontmatter` |
| worktree_root | `/Users/cyning/Desktop/Projects/kimi-code` |
| created_utc_or_local | 2026-06-11 |
| notes | 阶段 C3 · Issue #580 · ktwu01 双保险 |

---

## 可复制 Prompt 快照

见 task §8 与下方维护者交付的 **30 Prompt**（Open Folder = `kimi-code` worktree）。

---

## 交付摘要（本帽结束时填）

**状态**：✅ 30 完成 · 2026-06-11

**人工闸扫描**

| human_gate_id | status | blocks_hats | 30 可开工？ |
|---------------|--------|-------------|-------------|
| HG-TASK-DRAFT | approved | 22-R1, 30 | ✅ 是 |
| HG-AUDIT-R1 | approved | 30 | ✅ 是 |
| HG-GRAPH-MODULES | — | — | ✅ 是 |

**变更文件**（`git diff upstream/main --name-only`）

- `packages/agent-core/src/skill/parser.ts`
- `packages/agent-core/src/profile/default/system.md`
- `packages/agent-core/test/skill/scanner.test.ts`
- `.changeset/fix-skill-frontmatter-fallback.md`

**Commit**：`516958cb` · `feature/fix-580-skill-frontmatter`

**验证**

- `pnpm --filter @moonshot-ai/agent-core test -- test/skill` → 2522 passed
- `pnpm lint` → 通过

**PR 草稿**：见 task 聊天输出 · Fixes MoonshotAI/kimi-code#580

**下一棒**：Harness 40 自检 或维护者 `git push` + `gh pr create`
