---
graph_id: 10_flow_skill_load
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_skill_load.graph.yaml
---

# Flow：Skill 多根发现 · 解析 · 注册

resolveSkillRoots 多根 → discoverSkills/walkSkillDir → parseSkillText → registry · invalid YAML [err]

## Mermaid

```mermaid
flowchart TD
    SK_SESS[Session.loadSkills]
    SK_EXPL[resolveSkillRoots · explicitDirs?]
    SK_CONV[project/user 约定根 · brand+generic]
    SK_MORE[extraDirs + pluginSkillRoots + builtinDir]
    SK_SCAN[loadRoots → discoverSkills · walkSkillDir]
    SK_READ[读 SKILL.md bundle / 顶层 flat .md]
    SK_PARSE[parseSkillFromFile / parseSkillText]
    SK_OK[parseAndRegister 成功?]
    SK_REG[byName first-wins]
    SK_SKIP[warn · skip skill / policy]
    SK_META[frontmatter 顶层 mapping?]
    SK_INVALID[无效 YAML / 非 mapping]
    SK_FB[flat .md · name ?? skillDirName · description ?? body]
    SK_BI[registerBuiltinSkills]
    SK_LIST[getModelSkillListing → KIMI_SKILLS]
    SK_SYS[system.md # Skills]
    SK_AUTHOR[agent 创作 SKILL.md]

    SK_SESS --"~>"--> SK_EXPL
    // → packages/agent-core/src/session/index.ts#L637
    // → packages/agent-core/src/skill/scanner.ts#L61
    // → packages/agent-core/src/skill/scanner.ts#L452
    SK_EXPL --"[ok]"--> SK_MORE
    // → packages/agent-core/src/skill/scanner.ts#L75
    SK_EXPL --> SK_CONV
    // → packages/agent-core/src/skill/scanner.ts#L86
    SK_CONV --> SK_MORE
    // → packages/agent-core/src/skill/scanner.ts#L86
    // → packages/agent-core/src/skill/scanner.ts#L96
    SK_MORE --"~>"--> SK_SCAN
    // → packages/agent-core/src/skill/scanner.ts#L108
    // → packages/agent-core/src/skill/registry.ts#L41
    SK_SCAN --> SK_READ
    // → packages/agent-core/src/skill/scanner.ts#L132
    // → packages/agent-core/src/skill/scanner.ts#L168
    SK_SCAN --"[err]"--> SK_SKIP
    // → packages/agent-core/src/skill/scanner.ts#L157
    SK_READ --"~>"--> SK_PARSE
    // → packages/agent-core/src/skill/parser.ts#L73
    // → packages/agent-core/src/skill/parser.ts#L107
    SK_PARSE --"?>"--> SK_OK
    // → packages/agent-core/src/skill/scanner.ts#L376
    SK_OK --"[ok]"--> SK_REG
    // → packages/agent-core/src/skill/scanner.ts#L396
    // → packages/agent-core/src/skill/registry.ts#L54
    SK_OK --"[err]"--> SK_SKIP
    // → packages/agent-core/src/skill/scanner.ts#L409
    SK_PARSE --"?>"--> SK_META
    // → packages/agent-core/src/skill/parser.ts#L127
    SK_META --"[err]"--> SK_INVALID
    // → packages/agent-core/src/skill/parser.ts#L101
    // → packages/agent-core/src/skill/parser.ts#L129
    SK_INVALID --> SK_SKIP
    // → packages/agent-core/src/skill/scanner.ts#L409
    SK_META --"[ok]"--> SK_FB
    // → packages/agent-core/src/skill/parser.ts#L150
    SK_FB --> SK_REG
    // → packages/agent-core/src/skill/parser.ts#L150
    SK_REG --> SK_BI
    // → packages/agent-core/src/session/index.ts#L651
    // → packages/agent-core/src/skill/builtin/index.ts#L13
    SK_BI --"::yields"--> SK_LIST
    // → packages/agent-core/src/skill/registry.ts#L133
    // → packages/agent-core/src/profile/default/system.md#L143
    SK_SYS --"::triggers"--> SK_AUTHOR
    // → packages/agent-core/src/profile/default/system.md#L120
    SK_AUTHOR --"::triggers"--> SK_READ
    // → packages/agent-core/src/profile/default/system.md#L122

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| SK_SESS | Session.loadSkills | flow |
| SK_EXPL | resolveSkillRoots · explicitDirs? |  |
| SK_CONV | project/user 约定根 · brand+generic |  |
| SK_MORE | extraDirs + pluginSkillRoots + builtinDir |  |
| SK_SCAN | loadRoots → discoverSkills · walkSkillDir |  |
| SK_READ | 读 SKILL.md bundle / 顶层 flat .md |  |
| SK_PARSE | parseSkillFromFile / parseSkillText |  |
| SK_OK | parseAndRegister 成功? |  |
| SK_REG | byName first-wins |  |
| SK_SKIP | warn · skip skill / policy |  |
| SK_META | frontmatter 顶层 mapping? |  |
| SK_INVALID | 无效 YAML / 非 mapping |  |
| SK_FB | flat .md · name ?? skillDirName · description ?? body |  |
| SK_BI | registerBuiltinSkills |  |
| SK_LIST | getModelSkillListing → KIMI_SKILLS |  |
| SK_SYS | system.md # Skills |  |
| SK_AUTHOR | agent 创作 SKILL.md |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| SK_SESS | SK_EXPL | ~> | async_calls |  | 3 anchor(s) |
| SK_EXPL | SK_MORE | [ok] | depends_on |  | 1 anchor(s) |
| SK_EXPL | SK_CONV | -> | depends_on |  | 1 anchor(s) |
| SK_CONV | SK_MORE | -> | depends_on |  | 2 anchor(s) |
| SK_MORE | SK_SCAN | ~> | async_calls |  | 2 anchor(s) |
| SK_SCAN | SK_READ | -> | depends_on |  | 2 anchor(s) |
| SK_SCAN | SK_SKIP | [err] | depends_on |  | 1 anchor(s) |
| SK_READ | SK_PARSE | ~> | async_calls |  | 2 anchor(s) |
| SK_PARSE | SK_OK | ?> | condition |  | 1 anchor(s) |
| SK_OK | SK_REG | [ok] | depends_on |  | 2 anchor(s) |
| SK_OK | SK_SKIP | [err] | depends_on |  | 1 anchor(s) |
| SK_PARSE | SK_META | ?> | condition |  | 1 anchor(s) |
| SK_META | SK_INVALID | [err] | depends_on |  | 2 anchor(s) |
| SK_INVALID | SK_SKIP | -> | depends_on |  | 1 anchor(s) |
| SK_META | SK_FB | [ok] | depends_on |  | 1 anchor(s) |
| SK_FB | SK_REG | -> | depends_on |  | 1 anchor(s) |
| SK_REG | SK_BI | -> | depends_on |  | 2 anchor(s) |
| SK_BI | SK_LIST | ::yields | yields |  | 2 anchor(s) |
| SK_SYS | SK_AUTHOR | ::triggers | triggers |  | 1 anchor(s) |
| SK_AUTHOR | SK_READ | ::triggers | triggers |  | 1 anchor(s) |

## Notes

**多根**（折叠，不另开图）：`explicitDirs` 非空则只 push 配置根（source=user）；否则 `PROJECT_BRAND_DIRS`（`.kimi-code/skills`）+ `PROJECT_GENERIC_DIRS`（`.agents/skills`）+ user brand `skills/` + `USER_GENERIC_DIRS`。随后叠加 `extraDirs` / `pluginSkillRoots` / `builtinDir`。`walkSkillDir` depth≤8；同名 first-wins。
**invalid YAML [err]**：`loadYaml` 抛 `FrontmatterError` 或顶层非 mapping → `SkillParseError` → `parseAndRegister` warn skip。directory `SKILL.md` 缺 fence / 缺 name|description 同走 parse [err]（现码无 directory fallback）。
**flat .md** 才 `name ?? skillDirName` · `description ?? descriptionFromBody`。UnsupportedSkillType → `onSkippedByPolicy`，并入 SK_SKIP。
**#580 fork 史**：516958cb 曾对缺 frontmatter fallback 注册；本图按现码。builtin 登记不走扫描。
`00_main` 索引边留给 W-close。


