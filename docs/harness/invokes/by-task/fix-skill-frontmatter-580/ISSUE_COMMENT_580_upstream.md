# Issue comment · MoonshotAI/kimi-code#580

> **状态**：已发布 · 2026-06-11  
> **GitHub URL**：https://github.com/MoonshotAI/kimi-code/issues/580#issuecomment-4678337270  
> **发布方式**：`gh issue comment 580 --repo MoonshotAI/kimi-code`  
> **关联分支**：`Cyning12/kimi-code@feature/fix-580-skill-frontmatter` · commit `516958cb`  
> **策略**：暂不开上游 PR · **复查日 2026-06-13** · 等待 @puppylpg / @ktwu01 / maintainer

---

## 正文（英文 · 与 GitHub 发布一致）

Thanks @puppylpg for the clear write-up — I reproduced the same vicious cycle locally on **CLI 0.14.0** and landed a fix on a local branch.

I'm **not opening a competing PR** for now: you mentioned you already have a branch ready, and @ktwu01 noted they won't open one either. I'll wait for maintainer direction (or your branch landing) before pushing anything upstream.

### Reproduction

Two intentionally broken user skills under `~/.kimi-code/skills/` (same shape as your examples):

1. `ai-chat-summary/SKILL.md` — no YAML frontmatter, body starts with `# AI 对话总结`
2. `sync-xiaomi-photos/SKILL.md` — frontmatter with `description` only, **missing `name`**

Both files exist on disk. On current `main` @ 0.14.0:

| Check | Before fix (`main`) |
|-------|---------------------|
| `/help` lists `/skill:ai-chat-summary` | ❌ |
| `/skill:` autocomplete | ❌ (project/builtin only) |
| Agent "User" skills | **(none)** — Built-in shows `update-config` only |
| `/skill:ai-chat-summary` | skill does not exist |

Parser throws → scanner skips → no UI warning → the agent never sees the skill.

### My fix

Local branch: `feature/fix-580-skill-frontmatter` (commit `516958cb`)

1. **`system.md`** — document expected `SKILL.md` layout: YAML frontmatter with at least `name` and `description`, plus optional fields.
2. **`parser.ts`** — for directory `SKILL.md`, stop hard-rejecting missing frontmatter or missing `name`/`description`; keep rejecting invalid YAML and unsupported types. Use existing fallbacks: `name ?? skillDirName`, `description ?? first non-empty body line`.
3. **`scanner.test.ts`** — update expectations: incomplete directory skills **load with fallbacks** instead of being skipped.

Scope: 4 files (`packages/agent-core/` + `.changeset`, patch). Tests: `pnpm --filter @moonshot-ai/agent-core test -- test/skill` → 2522 passed.

### After the fix (same broken files, same paths)

| Check | After fix (`feature/fix-580-skill-frontmatter`) |
|-------|--------------------------------------------------|
| `/help` | ✅ `/skill:ai-chat-summary`, `/skill:sync-xiaomi-photos` |
| Agent User skills | ✅ both listed |
| `/skill:ai-chat-summary` | ✅ `▶ Activated skill: ai-chat-summary` |

### Next steps

Happy to collaborate if maintainers prefer your branch — rebase, review notes, or fold ideas together. If there's no movement for a while or a maintainer asks for a PR, I can open one from my fork; holding off until then.

Fork reference (branch pushed, no PR): https://github.com/Cyning12/kimi-code/tree/feature/fix-580-skill-frontmatter  
Commit: https://github.com/Cyning12/kimi-code/commit/516958cb
