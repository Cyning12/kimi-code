# invoke · 50 · fix-skill-frontmatter-580

## 元信息表

| 字段 | 值 |
|------|-----|
| hat_id | 50 |
| task_slug | `fix-skill-frontmatter-580` |
| reinspect_mode | 独立复检 |
| task_paths | `docs/tasks/active/task_fix_skill_frontmatter_580_v1.md` |
| related_review_or_none | 无 |
| git_branch | `feature/fix-580-skill-frontmatter` |
| fix_commit | `516958cb` |
| worktree_root | `/Users/cyning/Desktop/Projects/kimi-code` |
| diff_range | `upstream/main...HEAD`（4 files） |
| manual_cli_repro | [`REPRO_manual_cli_580_v1.md`](REPRO_manual_cli_580_v1.md) |
| created_utc_or_local | 2026-06-11 |

---

## 交付摘要

**状态**：✅ 50 独立复检 pass（代码）· 人工 CLI 复现 pass（main vs fix）· 2026-06-11

### 代码验收（diff + 命令）

| 验收项 | 结论 | 证据 |
|--------|------|------|
| system.md frontmatter 教学 | pass | `system.md:149-168` |
| parser directory fallback | pass | `parser.ts:107-148` |
| scanner 测试 T1–T3 | pass | `scanner.test.ts:148-197` |
| vitest test/skill | pass | 2522 passed |
| lint | pass | 0 errors |
| diff 边界 | pass | 4 files（agent-core + changeset） |
| 上游 PR Fixes #580 | pending | PR 未开 |
| meta 图谱关账 | pending | PR 合并后另帽 |

### 人工 CLI 验收（见 REPRO 全文）

| 环境 | User skill 可见 | 判定 |
|------|-----------------|------|
| main @ 0.14.0 | ❌ | #580 复现 |
| fix-580 @ 0.14.0 | ✅ slash/help/激活 | 修复有效 |

### Judgment

**代码维度 PASS，建议维护者开上游 PR 并合并；无实现返工。**

阻塞合并（流程）：PR 未开 · meta 图谱关账待合并后。

### 下一棒

1. `git push` + `gh pr create`（`Fixes MoonshotAI/kimi-code#580`）
2. PR 合并后：meta `10_flow_skill_load` partial + `02_version` + task → `done/`
