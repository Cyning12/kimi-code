# 人工 CLI 复现 · #580 · fix-skill-frontmatter-580

> **用途**：在 Kimi Code TUI 中体感验证 #580（directory skill 缺 frontmatter/字段被静默丢弃）。  
> **关联**：[MoonshotAI/kimi-code#580](https://github.com/MoonshotAI/kimi-code/issues/580) · task `task_fix_skill_frontmatter_580_v1.md` · 修复 commit `516958cb`  
> **记录人**：维护者人工复现 · 2026-06-11  
> **CLI 版本**：**0.14.0**（修复前 `main` 与修复后 `feature/fix-580-skill-frontmatter` 均在此版本下验证）  
> **子仓 worktree**：`/Users/cyning/Desktop/Projects/kimi-code`

---

## 1. Issue 提交人如何发现（puppylpg）

1. 用户让 agent「写 skill」→ `system.md` Skills 段未教 YAML frontmatter。
2. agent 写出 **directory** `SKILL.md`，缺 frontmatter 或缺 `name`/`description`。
3. `parser.ts` throw `SkillParseError` → `scanner.ts` warn 后 skip → **未进 SkillRegistry**。
4. `Session` 未把 scanner `onWarning` 接到 TUI → 用户**看不到** skip 警告。
5. 用户从 **「Current available skills」**（`registry.getModelSkillListing()` → system prompt `{{ KIMI_SKILLS }}`）发现：自写 User skill **不在列表**，仅 built-in `update-config` 等。

本复现用 **方案 A**：坏 skill 写在真实 `~/.kimi-code/skills/`，保留 `config.toml` API key，与 issue 环境一致。

---

## 2. 准备：写入两个「故意写坏」的 User skill

```bash
# 不使用 KIMI_CODE_HOME 临时目录，保留 ~/.kimi-code/config.toml

mkdir -p ~/.kimi-code/skills/ai-chat-summary
cat > ~/.kimi-code/skills/ai-chat-summary/SKILL.md <<'EOF'
# AI 对话总结

当用户要求总结对话时，提取要点并输出结构化摘要。
EOF

mkdir -p ~/.kimi-code/skills/sync-xiaomi-photos
cat > ~/.kimi-code/skills/sync-xiaomi-photos/SKILL.md <<'EOF'
---
description: 同步小米相册到本地
---

按步骤连接设备并同步照片。
EOF

# 确认磁盘存在
ls ~/.kimi-code/skills/ai-chat-summary/SKILL.md
ls ~/.kimi-code/skills/sync-xiaomi-photos/SKILL.md
```

| 目录 | 故意缺陷 | 对应 issue 样例 |
|------|----------|-----------------|
| `ai-chat-summary` | **无 frontmatter**，正文以 `#` 开头 | puppylpg 样例 1 |
| `sync-xiaomi-photos` | 有 `---` + `description`，**无 `name`** | puppylpg 样例 2 |

---

## 3. 启动 CLI

```bash
cd /Users/cyning/Desktop/Projects/kimi-code
# 修复前：
git checkout main
# 修复后对比：
# git checkout feature/fix-580-skill-frontmatter

pnpm --filter @moonshot-ai/kimi-code dev:cli-only
```

- 欢迎页应显示 **`Version: 0.14.0`**。
- 首次启动若提示 kimi-cli 迁移：选 **Ask me later**（与 skill 复现无关）。
- 欢迎页 **Directory** 可能为 `.../kimi-code/apps/kimi-code`（Project skills 来自仓库 `.agents/skills/`）；**User skill 扫描路径仍为 `~/.kimi-code/skills/`**，与 Directory 无关。

---

## 4. TUI 检查步骤（Step 3a–3d）

| 步骤 | 操作 | 判定要点 |
|------|------|----------|
| 3a | 输入 `/` 或 `/skill` 看补全 | User 坏 skill 是否以 `skill:<name>` 出现 |
| 3b | 输入 `/help` 并 **Enter** 打开面板 | 列表中是否有 `/skill:ai-chat-summary` 等 |
| 3c | 发送：「列出当前所有可用的 skills，按 User 和 Built-in 分组，只报名字，不要解释。」 | User 分组是否含两条 |
| 3d | 输入 `/skill:ai-chat-summary` | 是否出现 `▶ Activated skill: ai-chat-summary` |
| 4 | 终端 `ls ~/.kimi-code/skills/.../SKILL.md` | 磁盘有而 TUI 无 → 静默丢弃 |

**Project skills**（`gen-changesets`、`write-tui` 等）在 workDir 为 `apps/kimi-code` 时**始终可见**，勿与 User 结果混淆。

---

## 5. 实测结果

### 5.1 修复前 · `main` @ 0.14.0（2026-06-11）

| 步骤 | 结果 |
|------|------|
| Welcome | `Version: 0.14.0` |
| 3b `/help`（面板） | 有 Project `/skill:gen-*` 等；**无** `/skill:ai-chat-summary`、`/skill:sync-xiaomi-photos` |
| 3a `/skill` | 补全 **无** 上述两条 User skill |
| 3c 问 agent | **User:（无）** · Built-in: `update-config` |
| 3d `/skill:ai-chat-summary` | agent：不存在 `ai-chat-summary`；User 仍（无） |
| 4 磁盘 | 两个 `SKILL.md` **存在** |

**判定**：#580 复现成功（静默丢弃）。

### 5.2 修复后 · `feature/fix-580-skill-frontmatter` @ 0.14.0（2026-06-11）

| 步骤 | 结果 |
|------|------|
| Welcome | `Version: 0.14.0` |
| 3a `/skill` | 出现 `skill:sync-xiaomi-photos`（description：同步小米相册到本地）等 |
| 3b `/help` | 有 `/skill:ai-chat-summary`、`/skill:sync-xiaomi-photos` |
| 3c 问 agent | **User**: `ai-chat-summary`、`sync-xiaomi-photos` · Built-in: `update-config` |
| 3d `/skill:ai-chat-summary` | `▶ Activated skill: ai-chat-summary` · agent 按 skill 正文响应 |

**判定**：fallback 加载生效，修复验证通过。

---

## 6. 前后对照总表（均 @ 0.14.0）

| 检查点 | `main` | `feature/fix-580-skill-frontmatter` |
|--------|--------|-------------------------------------|
| 磁盘 `SKILL.md` | ✅ 存在 | ✅ 存在 |
| `/skill:` 含 `skill:ai-chat-summary` | ❌ | ✅ |
| `/help` 含 User skill | ❌ | ✅ |
| agent User 分组 | （无） | 两条均有 |
| `/skill:ai-chat-summary` 激活 | ❌ | ✅ `▶ Activated skill` |
| Project skills | ✅ 正常 | ✅ 正常 |
| Built-in `update-config` | ✅ | ✅ |

---

## 7. 清理（测完必做）

```bash
rm -rf ~/.kimi-code/skills/ai-chat-summary ~/.kimi-code/skills/sync-xiaomi-photos
```

---

## 8. 与自动化测试的关系

| 层次 | 命令 / 位置 |
|------|-------------|
| 单元/集成 | `pnpm --filter @moonshot-ai/agent-core test -- test/skill` · `scanner.test.ts:148-197` |
| 人工 CLI | 本文 §2–§6 |
| 代码锚点 | `parser.ts` 移除 directory 硬 throw · `system.md` Creating skills · `registry.ts:132-133` listing |

人工复现补足：**默认无 UI 警告**、slash/help/agent 三处用户可见面的行为。

---

## 9. 结论

- **`main` @ 0.14.0**：User 坏 skill 被静默丢弃，与 [issue #580](https://github.com/MoonshotAI/kimi-code/issues/580) 一致。
- **`feature/fix-580-skill-frontmatter`（`516958cb`）@ 0.14.0**：同文件、同路径下 User skill 可发现、可激活。
- **建议**：支持合并修复 PR；合并后 meta 补 `10_flow_skill_load` partial 关账。

---

## 修订记录

| 日期 | 摘要 |
|------|------|
| 2026-06-11 | v1：维护者人工 CLI 复现落盘（main vs fix-580，均 0.14.0） |
