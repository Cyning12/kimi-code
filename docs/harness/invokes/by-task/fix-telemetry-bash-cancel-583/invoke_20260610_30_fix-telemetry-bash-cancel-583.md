# invoke · 30 · fix-telemetry-bash-cancel-583

## 元信息表

| 字段 | 值 |
|------|-----|
| hat_id | 30 |
| task_slug | `fix-telemetry-bash-cancel-583` |
| freeze_id | — |
| task_paths | `docs/tasks/active/task_fix_telemetry_bash_cancel_583_v1.md` |
| related_review_or_none | `40 自检 + 维护者手感验证` |
| git_branch | `feature/fix-583-telemetry-cancel` |
| worktree_root | `/Users/cyning/Desktop/Projects/kimi-code` |
| created_utc_or_local | 2026-06-10 |
| notes | 阶段 C2 · Issue #583 · commit `679db406` |

---

## 可复制 Prompt 快照

```text
@../kimi-code-meta/docs/tasks/active/task_fix_telemetry_bash_cancel_583_v1.md
@../kimi-code-meta/docs/harness/prompts/30-execute-code.md

方案 B：cancelledByUser 结构化信号；先红测试再实现。
```

---

## 交付摘要（本帽结束时填）

- **验证命令** + 退出码
  - `pnpm exec tsc -p tsconfig.json --noEmit`（agent-core）→ **0**
  - `pnpm exec vitest run test/agent/turn.test.ts test/loop/tool-call.e2e.test.ts test/tools/bash.test.ts test/tools/shell-cancel.test.ts` → **119 passed**
  - `pnpm lint`（根）→ **0 errors**
  - `git diff upstream/main...HEAD --name-only` → 7 paths（agent-core×6 + `.changeset/`×1）
- **变更路径**
  - `packages/agent-core/src/loop/types.ts` — `cancelledByUser?: true`
  - `packages/agent-core/src/loop/tool-call.ts` — user abort 打标 + normalize
  - `packages/agent-core/src/tools/builtin/shell/bash.ts` — user abort 打标（`ExecutableToolErrorResult`）
  - `packages/agent-core/src/agent/turn/tool-telemetry.ts` — 新建 outcome/error_type
  - `packages/agent-core/src/agent/turn/index.ts` — import helper
  - `packages/agent-core/test/agent/turn.test.ts` — R3 用例 1–6
  - `.changeset/fix-583-telemetry-bash-cancel.md` — patch
- **手感验证**：dev TUI · YOLO · Bash `sleep 30` · Stop → telemetry log `Bash cancelled undefined`
- **上游 PR**：https://github.com/MoonshotAI/kimi-code/pull/630（`Fixes #583` · `679db406`）
- **下一棒**：PR 合并后 task §5 关账
