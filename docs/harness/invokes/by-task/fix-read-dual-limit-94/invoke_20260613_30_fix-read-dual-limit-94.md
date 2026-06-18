# invoke · 30 · fix-read-dual-limit-94

## 元信息表

| 字段 | 值 |
|------|-----|
| hat_id | 30 |
| task_slug | `fix-read-dual-limit-94` |
| freeze_id | — |
| task_paths | `docs/tasks/done/task_fix_read_dual_limit_94_v1.md` |
| related_review_or_none | `task_fix_read_dual_limit_94_audit_R1_20260612.md` |
| git_branch | `feature/fix-94-read-dual-limit` |
| worktree_root | `/Users/cyning/Desktop/Projects/kimi-code` |
| created_utc_or_local | 2026-06-13 |
| notes | 阶段 C3 · Issue #94 · commit `602cec16` · PR [#708](https://github.com/MoonshotAI/kimi-code/pull/708) |

---

## 交付摘要（本帽结束时填）

- **验证命令** + 退出码
  - `pnpm test test/tools/read.test.ts`（agent-core）→ **47 passed**
- **变更路径**
  - `packages/agent-core/src/tools/builtin/file/read.ts` — `finishMessage` 独立 if + EOF 守卫
  - `packages/agent-core/test/tools/read.test.ts` — `reports both line and byte caps when both limits are hit`
  - `.changeset/fix-read-dual-limit-status.md` — patch · agent-core + kimi-code bundle
- **上游 PR**：https://github.com/MoonshotAI/kimi-code/pull/708（`Fixes #94` · `602cec16`）
- **下一棒**：meta 图谱关账 · task → `done/`
