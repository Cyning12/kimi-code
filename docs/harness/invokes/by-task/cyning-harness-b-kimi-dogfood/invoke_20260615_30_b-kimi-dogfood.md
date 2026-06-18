# Harness invoke · 30 执行快照 · Track B kimi-code-meta dogfood

| 字段 | 值 |
| --- | --- |
| hat_id | 30 |
| task_slug | `cyning-harness-b-kimi-dogfood` |
| task_paths | `Projects/docs/harness/tasks/active/task_cyning_harness_b_kimi_dogfood_v1.md` |
| git_branch | `cyning/meta` |
| worktree_root | `kimi-code-meta/` |
| npm_package | `@cyning/harness@0.3.2` |
| created | 2026-06-15 CST |
| meta_commits | `a671b5d3`（#705 前置）· `dc04a994`（dogfood upgrade） |

---

## 阶段 0 · 前快照

| # | 命令 | 退出码 | 摘要 |
| --- | --- | --- | --- |
| 0a | `git status -sb` | 0 | `cyning/meta` · 先含 #705 未提交改动 → 已 commit `a671b5d3` |
| 0b | `git branch --show-current` | 0 | `cyning/meta` |
| 0e | manifest（upgrade 前） | — | 无 manifest（仅 profile.json） |
| 0f | `git diff --name-only`（首次 upgrade 前） | — | `.cyning-harness/local.json` 脏 → 触发 S5 |

---

## 阶段 1 · npx check + upgrade

| # | 命令 | 退出码 | 摘要 |
| --- | --- | --- | --- |
| 1 | `npx @cyning/harness@0.3.2 check --target .` | 0 | 未接入 / 可升级（upgrade 前无 manifest） |
| 2a | `npx … upgrade --target . --yes --gate-check` | 1 | S5：`local.json` 脏 · apply 中止 |
| 2b | `npx … upgrade … --force` | 1 | apply ✅ · gate-check exit 2（#705 pending） |
| — | `.gitignore` + `git rm --cached local.json` | — | 本机路径不再进 Git |
| 2c | `npx … upgrade --target . --yes --gate-check` | 1 | apply ✅ · 无 S5 · gate-check exit 2 |
| 3 | `cat .cyning-harness/manifest.json` | 0 | `version: 0.3.2` · preset harness-only |

**findings**

- S5：`upgrade.sh` 在 plan→apply 间写 `local.json`，若该文件被 track 会自触发 S5；npx 路径应用 `--force` 或 gitignore `local.json`。
- gate-check exit 2 传播为 upgrade exit 1 — **非 sync 失败**（#705 `HG-TASK-DRAFT` / `HG-AUDIT-R1` pending）。

---

## 阶段 2 · diff 审查

**dogfood commit `dc04a994` 文件列表（纪律层 only · pass）**

| 路径 | 变更 |
| --- | --- |
| `.cyning-harness/manifest.json` | 新增 · 0.3.2 |
| `docs/harness/prompts/40-self-check.md` | 新增（A2 Starter） |
| `docs/harness/prompts/README.md` | 增量 |
| `.gitignore` | +`.cyning-harness/local.json` |
| `.cyning-harness/local.json` | 从 Git 移除（本机保留 ignore） |

**禁止前缀**：无 `apps/` · `packages/` · `pnpm-lock.yaml` · 产品 `package.json`。

---

## 阶段 3 · gate-check

| task | HG-TASK-DRAFT | HG-AUDIT-R1 | 30 |
| --- | --- | --- | --- |
| `task_fix_open_tool_calls_705_v1.md` | pending | pending | ❌ 拒 30 |
| `task_fix_skill_frontmatter_580_v1.md` | approved | approved | ✅ 可 30 |

gate-check 退出码：**2**（有 active task 拒 30 · 预期）。

---

## 阶段 4 · 验收结论

| 验收项 | 结果 |
| --- | --- |
| diff 仅纪律层 | ✅ pass |
| manifest @0.3.2 | ✅ pass |
| gate-check 可用 | ✅ pass（exit 2 = 业务闸 pending · 非工具故障） |
| npx upgrade dogfood | ✅ pass（S5 已用 gitignore 解） |

**Harness 状态栏**：Track B #4 dogfood **pass** · 待 push `cyning/meta` · Projects task 自检回填。

**产品 follow-up（非本棒）**：npx 路径不写 track 的 `local.json`；gate-check 非零时不令 upgrade 整体 fail。
