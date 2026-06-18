# Task：修复 agent 写出无效 SKILL.md 被静默丢弃 · #580（阶段 C3）

> **状态**：`local_done` — 30/40/50 完成 · **上游 PR 暂缓**（等 #580 回复 · 窗口至 **2026-06-13**）  
> **上游 Issue**：[MoonshotAI/kimi-code#580](https://github.com/MoonshotAI/kimi-code/issues/580)  
> **Issue 回复**：[comment #4678337270](https://github.com/MoonshotAI/kimi-code/issues/580#issuecomment-4678337270)（已发 · 暂不开 PR）  
> **关联图谱**：`docs/_tech_graph/01_struct.md`（`agent_core`）· 增量 `10_flow_skill_load.md`  
> **扫描分级**：`Projects/docs/harness/guides/ISSUE_SCAN_kimi_code_open_c2_v1_zh.md`  
> **试点真值**：[`docs/harness/POINTER_PILOT_adoption_workspace_v1_zh.md`](../harness/POINTER_PILOT_adoption_workspace_v1_zh.md)

---

## Harness 元信息

| 字段 | 值 |
|------|-----|
| **task_slug** | `fix-skill-frontmatter-580` |
| **test_strategy** | `required` |
| **test_strategy_note** | parser / scanner 行为变更须 vitest；system.md 变更配合人工或现有 prompt 测试 |
| **code_quality_bar** | `strict` |
| **orchestration** | Kimi Code Agent · **五轮思考后 30** |
| **audit_profile** | `human_only` |
| **git_branch** | `feature/fix-580-skill-frontmatter` |
| **worktree_root** | `/Users/cyning/Desktop/Projects/kimi-code` |
| **meta_worktree** | `/Users/cyning/Desktop/Projects/kimi-code-meta` |
| **module_id** | `agent_core` |
| **graph_delta** | `10_flow_skill_load.md` |
| **graph_delta_note** | — |
| **graph_gate** | `skeleton_before_30` · `close_partial_or_final` |
| **upstream_social** | 已 comment @puppylpg · 知悉 ktwu01 不竞争 · **PR 暂缓至 2026-06-13**（见 §9） |

### 人工闸

| human_gate_id | status | blocks_hats | 说明 |
|---------------|--------|-------------|------|
| HG-TASK-DRAFT | approved | 22-R1, 30 | 图谱 skeleton + R1～R5 已落盘 · 2026-06-11 |
| HG-AUDIT-R1 | approved | 30 | 维护者同意方案 B（prompt + parser）· 2026-06-11 |

---

## 1. 需求摘要（来自 #580 · ktwu01 复核）

### 恶性循环

1. 用户让 agent「写 skill」→ agent 读 `system.md`，Skills 段只说明目录/`SKILL.md` 或独立 `.md`，**未教 YAML frontmatter** 与 `name` / `description`。
2. agent 写出缺 frontmatter 或缺字段的 `SKILL.md`。
3. `parser.ts` 对 **directory** `SKILL.md` 强制 frontmatter + `name` + `description`（L107–145），否则 `SkillParseError`。
4. `scanner.ts` 捕获后 **警告并静默跳过**，skill 未进入 `SkillRegistry`。
5. 用户与 agent 均不知道 skill 未加载。

### ktwu01 结论（2026-06-10）

- `main` 上问题 **仍成立**。
- fallback `name ?? skillDirName`、`description ?? descriptionFromBody` **存在但被前置 throw 挡住**。
- **倾向**：prompt 更新 + parser 放宽 **一起做**（防 agent 写坏 + 防用户 skill 误丢）。

### 涉及代码（必读）

| 路径 | 角色 |
|------|------|
| `packages/agent-core/src/profile/default/system.md` | Skills 段 · 教 agent SKILL 格式 |
| `packages/agent-core/src/skill/parser.ts` | frontmatter / name / description 校验 |
| `packages/agent-core/src/skill/scanner.ts` | 扫描与 `SkillParseError` 处理 |
| `packages/agent-core/src/skill/types.ts` | `SkillDefinition` / metadata |

### 完成态（验收口径）

- [x] `system.md` 说明 SKILL.md frontmatter 形状（`name` / `description` / 可选字段）
- [x] directory skill：缺 `name`/`description` 时 fallback（方案 B · R2）
- [x] 无 frontmatter 的 directory `SKILL.md` 加载 + fallback · 有测试
- [x] vitest 覆盖典型坏/好 SKILL.md（2522 passed · test/skill）
- [ ] 上游 PR · `Fixes #580`（**暂缓** · §9）
- [x] meta：`10_flow_skill_load` partial · fork + `02_version` 一行

---

## 2. 非范围

- sub-skill 实验特性全面文档化
- 修改 SDK 对外 skill 契约（除非 R2 证明最小必要）
- harness / task 进上游 PR
- **因 puppylpg branch 而放弃本地修复**（维护者 2026-06-11 决策：暂不占坑拒工）

---

## 3. 失败路径

| 触发条件 | 系统行为 | 可重试 |
|----------|----------|--------|
| 无 `10_flow_skill_load` skeleton commit | 30 **拒开工** | 是 |
| 未完成 R1～R5（或合法提前停/需更多轮未处理）即 30 | 30 **拒开工** | 是 |
| `HG-AUDIT-R1` pending | 30 **拒开工** | 是 |
| R5 为「需更多轮」且未开追加思考 | 不得签 `HG-AUDIT-R1` | 是 |
| PR 已开但 meta 无图谱关账 | 不得 `done/` | 是 |

---

## 4. Kimi Code Agent · 五轮思考（**改码前 mandatory**）

> **推荐**：[`PROMPT_kimi_agent_rethink_R1_R5.md`](../../harness/invokes/by-task/fix-skill-frontmatter-580/PROMPT_kimi_agent_rethink_R1_R5.md) **一条发完**（R0～R5）。  
> **回填 mandatory**：Agent 须将结论 **写入本节回填区**（替换 `（待填）`），见 [`FRAGMENT_rethink_backfill_task_v1_zh.md`](../../harness/FRAGMENT_rethink_backfill_task_v1_zh.md) — **禁止**仅在聊天输出就结束。  
> **可提前停止**：`【停止 · 原因】` — 已完成的轮次仍须写入 task。  
> **可要求更多轮**：`【需更多轮 · 提纲】` — 写入 R5 回填区后再决定 R6+。

### R0 · 读 task

（Agent 执行 PROMPT §R0）

**回填区：**

```text
【R0 结论 · 2026-06-11】

恶性循环（#580 · ktwu01 复核仍成立）：
  用户/agent 写 skill → system.md 未教 YAML frontmatter
  → directory SKILL.md 缺 frontmatter 或缺 name/description
  → parser L109–145 throw SkillParseError
  → scanner L386–387 warn 后静默 skip → SkillRegistry 无该 skill → 用户/agent 无感知

涉及文件（实现帽必读）：
  · packages/agent-core/src/profile/default/system.md — Skills 段 L130–153
  · packages/agent-core/src/skill/parser.ts — L107–145（directory 硬校验）
  · packages/agent-core/src/skill/scanner.ts — parseAndRegister L379–391
  · packages/agent-core/src/skill/types.ts — SkillDefinition / SkillMetadata

ktwu01 验证要点（2026-06-10）：
  · main 上问题仍成立
  · fallback（name ?? skillDirName、description ?? descriptionFromBody）在 L150–151 存在，但被 L109–111 / L140–145 前置 throw 挡住
  · 倾向：prompt 更新 + parser 放宽一起做

本 fork 纪律：
  · 暂不以 puppylpg branch 占坑为拒工理由（§2 非范围已写明）
  · R5 写上游协调建议；PR 前可选 issue comment

task 元信息：test_strategy=required · git_branch=feature/fix-580-skill-frontmatter · graph_delta=10_flow_skill_load.md
```

### R1 · 代码事实

**Prompt 要点**：system.md Skills 段 · parser L107–145 · scanner 静默 · flat vs directory · 现有测试。

**回填区：**

```text
【R1 结论 · 代码事实 · 禁止方案】

1) system.md Skills 段（L130–153）
  · 仅说明：skill = 目录+SKILL.md 或独立 .md 文件
  · 未说明 YAML frontmatter、`name`/`description` 必填形状、可选字段（type/whenToUse 等）
  · agent 创作 skill 时无格式真值 → 易写出无 frontmatter 的 directory SKILL.md

2) parser.ts 关键分支（L107–159）
  · isDirectorySkill = basename(skillMdPath) === 'SKILL.md'（L108）
  · directory 专属硬门槛：
    - 首行非 `---` → throw Missing frontmatter（L109–111）
    - frontmatter 缺 name 或 description → throw Missing required field（L140–145）
  · flat .md（basename !== SKILL.md）：无上述门槛；可无 frontmatter
  · L150–151 fallback 已实现但 directory 路径到不了：
    name ?? skillDirName
    description ?? descriptionFromBody(content)（首非空行，超 240 字截断+…；空 body → "No description provided."）
  · 仍拒绝：FrontmatterError（YAML 无效/缺闭合 `---`）、非 mapping、UnsupportedSkillTypeError

3) scanner.ts（L353–392 parseAndRegister）
  · SkillParseError → onWarning("Skipping invalid skill…") 后 return undefined（静默丢弃）
  · UnsupportedSkillTypeError → onSkippedByPolicy（非 warn 路径）
  · 无向 agent/用户反馈「skill 未加载」的上层通道

4) flat vs directory 不对称（根因）
  · flat .md：parser.test.ts 已测 filename stem + body 首行 fallback 可加载
  · directory SKILL.md：scanner.test.ts L148–190 显式断言 no-frontmatter / missing-name / missing-description 均被 skip（仅 valid 注册）
  · #580 核心：agent 默认写 directory bundle，却享受比 flat 更严的校验

5) types.ts
  · SkillDefinition.name/description 为 string（非 optional）；metadata.name/description 为 optional
  · 放宽 parser 后仍可通过 fallback 满足 SkillDefinition 契约

6) 现有测试文件（30 须改/扩）
  · packages/agent-core/test/skill/parser.test.ts — flat fallback、unclosed fence（flat+subdir 均 skip）
  · packages/agent-core/test/skill/parser-frontmatter.test.ts — parseFrontmatter 单元
  · packages/agent-core/test/skill/scanner.test.ts — L148–190「skips directory skills with missing frontmatter metadata」（当前行为真值）
  · packages/agent-core/test/skill/builtin-*.test.ts — built-in 加载回归

7) built-in skill 样例
  · src/skill/builtin/**/SKILL.md 均有完整 frontmatter（name+description）
  · 放宽 directory 规则不应影响 built-in 加载
```

### R2 · 方案对比

**Prompt 要点**：A prompt-only · B prompt+parser · C parser-only；推荐 + R2-追加。

**回填区：**

```text
【R2 结论 · 方案对比】

方案 A · prompt-only（仅改 system.md）
  · 在 Skills 段增加 SKILL.md frontmatter 模板（--- / name / description / 可选 type 等）
  · 优点：从源头减少 agent 写坏；改动面小
  · 缺点：不修复用户手写/第三方/历史 skill；parser 仍静默丢弃 → #580 半解决

方案 B · prompt + parser（推荐 · 对齐 ktwu01）
  · system.md：教正确格式（预防）
  · parser.ts：directory SKILL.md 与 flat .md 对齐 fallback 语义
    - 删除或放宽 L109–111（无 frontmatter 时不 throw，整文作 body）
    - 删除 L140–145 directory 专属 name/description 硬要求，走 L150–151 fallback
  · 优点：双保险；用户/agent skill 不再被静默丢弃；fallback 代码已存在，实现量小
  · 缺点：缺 frontmatter 的 skill 可能 name=目录名、description=正文首行，质量参差（可接受，优于不可见）

方案 C · parser-only
  · 仅放宽 parser，不改 system.md
  · 优点：立刻止损静默丢弃
  · 缺点：agent 无格式指导，恶性循环上半段仍在；与 ktwu01「一起做」不一致

【推荐】方案 B（prompt + parser），最小 diff：
  1. system.md：新增「Creating skills」小节 + frontmatter 示例（directory 与 flat 均适用）
  2. parser.ts：移除 directory 对 frontmatter/name/description 的 throw；保留 YAML 语法错误与 unsupported type 拒绝
  3. scanner.test.ts：反转 L148–190 期望（缺字段应注册+fallback，而非 skip）

【R2-追加 · 可选，非 30 阻塞】
  · scanner 在 fallback 生效时 emit 低优先级 warn（便于调试），或 CLI 启动摘要列出「以 fallback 加载的 skill」
  · 不在本 PR 改 SDK 对外契约（types 不变）
```

### R3 · 边界与回归

**Prompt 要点**：各缺字段场景 · fallback 生效条件 · built-in skill 回归。

**回填区：**

```text
【R3 结论 · 边界与回归】

缺字段场景矩阵（#580 后预期 · directory SKILL.md）：

| 场景 | 当前 | #580 后 |
|------|------|---------|
| 无 frontmatter（正文直接起笔） | skip · Missing frontmatter | 加载 · name=skillDirName · desc=descriptionFromBody(body) |
| 有 `---` 但缺 name | skip · Missing "name" | 加载 · name=skillDirName · desc=frontmatter 或 body |
| 有 `---` 但缺 description | skip · Missing "description" | 加载 · name=frontmatter 或 skillDirName · desc=descriptionFromBody |
| name+description 齐全 | 加载 | 加载（不变） |
| frontmatter 空 mapping `---\n---\n` | skip（缺 name/desc） | 加载 · 双 fallback |
| body 全空 | skip 或 desc fallback | 加载 · desc="No description provided." |
| YAML 无效 / 缺闭合 `---` | skip · Invalid frontmatter | 仍 skip（不变） |
| frontmatter 非 mapping（数组） | skip | 仍 skip（不变） |
| type 非 prompt/inline/flow | skip · onSkippedByPolicy | 仍 skip（不变） |

flat .md 行为：不变（已有 fallback 测试 parser.test.ts）

fallback 生效条件（实现后）：
  · name：frontmatter.name 为非空字符串，否则 skillDirName（目录名或 .md stem）
  · description：frontmatter.description 非空，否则 body 首非空行（≤240 字）

built-in / 回归：
  · builtin/**/SKILL.md 均有完整 frontmatter → 解析路径不变
  · 跑 test/skill/builtin-*.test.ts + registry + scanner 全量
  · sub-skill / flow / plugin metadata 不受 name/description 放宽影响

非目标（仍 skip）：
  · 蓄意 malformed YAML、unclosed fence（parser.test.ts L113–137 行为保持）
  · 不支持 type

风险：
  · 同名碰撞：skillDirName fallback 可能与 flat .md 或其他目录同名 — 沿用现有 normalizeSkillName 首 wins 规则
  · description 质量：正文首行可能是 `# Title` 而非摘要 — 比静默丢弃更可接受；prompt 侧教 agent 写 description
```

### R4 · 测试与 PR

**Prompt 要点**：用例表 · vitest 路径 · diff 边界 · changeset · Fixes #580。

**回填区：**

```text
【R4 结论 · 测试与 PR 边界】

用例表（vitest · test_strategy=required）：

| ID | 输入 | 期望 |
|----|------|------|
| T1 | directory/SKILL.md 无 frontmatter，body 首行 "Do X" | discoverSkills 长度 1；name=目录名；description 含 "Do X" |
| T2 | directory/SKILL.md `---` 仅 description | name=skillDirName |
| T3 | directory/SKILL.md `---` 仅 name | description=body 首行或 "No description provided." |
| T4 | directory/SKILL.md 完整 frontmatter | 与现有一致 |
| T5 | directory/SKILL.md unclosed `---` | skip + warn（Invalid frontmatter） |
| T6 | flat plain.md 无 frontmatter | 不变（parser.test.ts 已有） |
| T7 | builtin skills 加载 | builtin-*.test.ts 全绿 |

测试文件（优先改现有，少建新文件）：
  · test/skill/scanner.test.ts — 重写/拆分 L148–190「skips…」为「loads with fallback…」
  · test/skill/parser.test.ts — 可选补 directory 直调 parseSkillText 用例
  · system.md — 无专用单测；靠 profile/default-agent-profiles.test.ts 或人工确认 Skills 段渲染

pnpm 命令：
  cd /Users/cyning/Desktop/Projects/kimi-code
  pnpm --filter @moonshot-ai/agent-core test -- test/skill
  pnpm lint
  git diff upstream/main --name-only   # 期望仅 agent-core + .changeset

PR diff 边界：
  · 允许：packages/agent-core/**（system.md, parser.ts, test/skill/*）
  · 允许：.changeset/*.md（patch @moonshot-ai/agent-core）
  · 禁止：apps/**、harness、meta task/图谱（图谱关账在 meta 另 commit）
  · PR 标题 Conventional Commit；正文 Fixes MoonshotAI/kimi-code#580
  · changeset：patch（行为放宽 + prompt，非 breaking）
```

### R5 · 图谱 + 协调 + 关账判断

**Prompt 要点**：`10_flow_skill_load` 增量 · issue comment 是否建议 · 可30 / 停止 / 需更多轮。

**回填区：**

```text
【R5 结论 · 图谱 + 协调 + 关账判断】

图谱增量（10_flow_skill_load.md）：
  · 30 前：skeleton 已有（00_main/01_struct/02_version 一行若未完成则 30 拒开工）
  · 30 后关账：flow partial/终稿须补锚点：
    - parser.parseSkillText directory 分支：移除 Missing frontmatter / Missing required field throw
    - fallback 边：name ?? skillDirName、description ?? descriptionFromBody
    - scanner：SkillParseError 仍 warn+skip，但 #580 场景不再触发 parse error
    - system.md Skills 段新增 frontmatter 教学
  · 同步 10_flow_skill_load.ai.md + 02_version 关账行

上游协调建议（PR 前可选，不阻塞 30）：
  · 在 MoonshotAI/kimi-code#580 comment：
    「本地 fork 按 ktwu01 建议实施 B（system.md + parser fallback 对齐 flat）。
     知悉 puppylpg branch / ktwu01 不竞争；若上游已有 PR 将 rebase 或协作合入。」
  · 不要求等待 puppylpg 回复再 30（维护者 2026-06-11 决策）

关账判断：【可 30】
  · R0–R5 已回填
  · 待维护者：HG-TASK-DRAFT + HG-AUDIT-R1 → approved
  · 30 执行帽按 §4 R2 方案 B 改码 + §4 R4 用例 + changeset
  · PR 合并后 meta：10_flow_skill_load partial 关账 + task → done/

不需更多轮（R6+ 无阻塞未决项）。
```

---

## 5. 验收标准（关账）

- [x] §4 R1～R5 已回填
- [x] `HG-AUDIT-R1` → `approved`
- [x] vitest / lint 通过
- [ ] 上游 PR · `Fixes #580`（**暂缓** · §9）
- [x] invoke 30/40/50 落盘
- [x] **图谱**（fork partial 已 commit；upstream merge 后再改状态）：
  - [x] 30 前 skeleton
  - [x] 关账 partial · fork（`516958cb` · 待 upstream merge）

---

## 9. 上游 PR 策略（维护者 · 2026-06-11）

| 项 | 决定 |
|----|------|
| **本地修复** | ✅ `feature/fix-580-skill-frontmatter` · `516958cb` · fork 已 push |
| **Issue comment** | ✅ [4678337270](https://github.com/MoonshotAI/kimi-code/issues/580#issuecomment-4678337270) · 说明复现/方案/协作意愿 · **暂不开 PR** |
| **等待窗口** | **至 2026-06-13**（约 2 天）· 观察 @puppylpg / @ktwu01 / maintainer 回复 |
| **窗口内** | 不 `gh pr create`；若作者 PR 出现则评估 rebase/协作/撤 fork PR |
| **窗口后仍无动静** | 维护者可开 upstream PR · `Fixes #580` · 正文链 issue comment |
| **提前开 PR** | maintainer 在 issue 明确要 PR · 或 puppylpg 表示 branch 不提交 |

**复查日期**：2026-06-13（或收到回复当日）

---

## 6. 给执行帽必读（30 前）

1. `AGENTS.md` · `packages/agent-core` 邻近说明（若有）
2. 本 task §1 + §4 R1～R5
3. `@../kimi-code-meta/docs/_tech_graph/10_flow_skill_load.md`
4. `@../kimi-code-meta/docs/_tech_graph/01_struct.md`
5. Issue #580 + ktwu01 评论

---

## 7. 验证命令

```bash
cd /Users/cyning/Desktop/Projects/kimi-code
git checkout main && git fetch upstream && git reset --hard upstream/main
git checkout -b feature/fix-580-skill-frontmatter

pnpm --filter @moonshot-ai/agent-core test -- test/skill   # 路径按 R4 调整
pnpm lint
git diff upstream/main --name-only
```

---

## 8. 维护者签闸清单

- [x] 图谱 skeleton 已 meta commit（可与 task 草稿同批）
- [x] 五轮思考完成或「需更多轮」已处理
- [x] 同意 R2 推荐方案（方案 B · 2026-06-11）
- [x] `HG-TASK-DRAFT` / `HG-AUDIT-R1` → `approved`
- [x] 30：`@../kimi-code-meta/docs/tasks/active/...` + `30-execute-code.md`（2026-06-11 完成）

---

## 10. 执行复查摘要（2026-06-11）

| 维度 | 结果 | 备注 |
|------|------|------|
| **方案** | ✅ B（prompt + parser） | 与 ktwu01 / R2 一致 |
| **代码** | ✅ 4 files vs upstream | system.md · parser.ts · scanner.test.ts · changeset |
| **测试** | ✅ 2522 passed · lint 0 | test/skill 全量 |
| **diff 边界** | ✅ | 无 harness / apps |
| **思考链** | ✅ R0–R5 §4 回填 | HG 已签 |
| **invoke** | ✅ 30/40/50 + REPRO + issue comment | README 已索引 |
| **图谱** | ✅ partial · fork | 待 upstream merge 改 `partial` |
| **人工复现** | ✅ CLI 0.14.0 | main 静默丢弃 → fix 后 /skill 可见 |
| **上游 PR** | ⏸ 暂缓至 2026-06-13 | comment 已发 · 无 competing PR |
| **缺口** | scanner fallback warn · SDK | 非范围 · R2-追加 |

**结论**：本地 C3 执行 **合格**；关账仅剩 upstream PR（按 §9 窗口后或 maintainer 催）。

---

## 实现备忘（30 后回填）

| 项 | 状态 | 备注 |
|----|------|------|
| 图谱 skeleton | ✅ | `10_flow_skill_load.md` |
| 图谱 partial · fork | ✅ | `10_flow_skill_load` 双轨 · 待 upstream merge 改 `partial` |
| R1～R5 | ✅ | 2026-06-11 审阅 Agent 回填 §4 |
| 测试 | ✅ | test/skill 全绿 · lint 通过 |
| 人工 CLI 复现 | ✅ | `REPRO_manual_cli_580_v1.md` · main vs fix-580（CLI 0.14.0） |
| 50 独立复检 | ✅ | `invoke_20260611_50_fix-skill-frontmatter-580.md` |
| 上游 PR | ⏸ | commit `516958cb` · **暂缓至 2026-06-13** · [comment 已发](https://github.com/MoonshotAI/kimi-code/issues/580#issuecomment-4678337270) |

### 自检结论（执行者）

```text
【30 自检 · 2026-06-11】

人工闸：HG-TASK-DRAFT=approved · HG-AUDIT-R1=approved → 通过开工

实现（方案 B）：
  · parser.ts：移除 directory 专属 Missing frontmatter / Missing required field throw
  · system.md：新增 Creating skills 小节 + frontmatter 模板
  · scanner.test.ts：L148–190 改为 loads with fallback（T1–T3）

验证：
  · pnpm --filter @moonshot-ai/agent-core test -- test/skill → 2522 passed
  · pnpm lint → 通过
  · git diff upstream/main --name-only → 仅 agent-core + .changeset

Commit：516958cb on feature/fix-580-skill-frontmatter
Changeset：.changeset/fix-skill-frontmatter-fallback.md（patch agent-core + kimi-code）

未做（非范围）：scanner fallback warn · SDK 契约 · meta 图谱关账
下一棒：40 自检 或维护者开 PR（Fixes #580）

---

【40 自检 · 2026-06-11】

命令（cwd=/Users/cyning/Desktop/Projects/kimi-code）：
  · git log -1 → 516958cb（exit 0）
  · pnpm --filter @moonshot-ai/agent-core test -- test/skill → exit 0 · 2522 passed
  · pnpm lint → exit 0 · 0 errors
  · git diff upstream/main --name-only → 4 files（仅 agent-core + .changeset）✓
  · test/skill/builtin → exit 0 · 2522 passed

验收：A1–A8 pass · A9 pending（gh pr list 空）· A10 pending（图谱关账另帽）
R4：T1–T3 pass（scanner.test L148–197）· T5 pass（parser.test L126–137）· T7 pass

建议：可开 PR（Fixes MoonshotAI/kimi-code#580）
已知未测：上游 PR 未 push · meta 10_flow_skill_load partial 关账 · scanner fallback warn（非范围）
下一棒：维护者 push + gh pr create · 或 50 独立复检

---

【50 独立复检 · 2026-06-11】

diff upstream/main...HEAD（516958cb）：4 files · vitest 2522 passed · lint 0 errors
Judgment：代码 PASS · 建议合并 · 无返工
阻塞（流程）：PR 未开 · 图谱关账待合并后
invoke：`docs/harness/invokes/by-task/fix-skill-frontmatter-580/invoke_20260611_50_fix-skill-frontmatter-580.md`

---

【人工 CLI 复现 · 方案 A · 2026-06-11 · CLI 0.14.0】

方法：坏 User skill 写入 ~/.kimi-code/skills/（保留 config.toml）· dev:cli-only
全文：`docs/harness/invokes/by-task/fix-skill-frontmatter-580/REPRO_manual_cli_580_v1.md`

修复前 main @ 0.14.0：
  · /help 面板无 /skill:ai-chat-summary、/skill:sync-xiaomi-photos
  · /skill 补全无上述 User skill
  · agent User:（无）· Built-in: update-config
  · 磁盘 SKILL.md 存在 → 静默丢弃 ✅ 复现 #580

修复后 feature/fix-580-skill-frontmatter @ 0.14.0：
  · /help 有 /skill:ai-chat-summary、/skill:sync-xiaomi-photos
  · agent User: 两条均有 · /skill:ai-chat-summary → ▶ Activated skill ✅

清理：rm -rf ~/.kimi-code/skills/ai-chat-summary sync-xiaomi-photos（测后）
```
