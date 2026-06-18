---
graph_id: 10_flow_skill_load
version: 2026-06-18
generated_at: 2026-06-18T14:26:55Z
source: docs/_tech_graph/10_flow_skill_load.graph.yaml
---

# Flow：Skill 发现 · 解析 · 注册（C3 #580）

scanner → parser → registry · directory SKILL.md frontmatter fallback

## Mermaid

```mermaid
flowchart TD
    SK_SCAN[scanner.discoverSkills]
    SK_READ[读取 SKILL.md]
    SK_PARSE[parseSkillText]
    SK_OK[解析成功?]
    SK_REG[SkillRegistry.byName]
    SK_SKIP[warn · skip skill]
    SK_SYS[system.md Creating skills]
    SK_AUTHOR[agent 创作 SKILL.md]
    SK_META[directory SKILL.md frontmatter / 字段]
    SK_INVALID[无效 YAML / 非 mapping]
    SK_FB[name ?? skillDirName · description ?? descriptionFromBody]
    SK_LIST[getModelSkillListing → KIMI_SKILLS]

    SK_SCAN --> SK_READ
    // → packages/agent-core/src/skill/scanner.ts#L143
    SK_READ --> SK_PARSE
    // → packages/agent-core/src/skill/parser.ts#L107
    SK_PARSE --"?>"--> SK_OK
    SK_OK --"[ok]"--> SK_REG
    // → packages/agent-core/src/skill/registry.ts
    SK_OK --"[err]"--> SK_SKIP
    // → packages/agent-core/src/skill/scanner.ts#L386
    SK_SYS --"::triggers"--> SK_AUTHOR
    // → packages/agent-core/src/profile/default/system.md#L149
    SK_AUTHOR --"~>"--> SK_READ
    SK_PARSE --"?>"--> SK_META
    SK_META --"[err]"--> SK_INVALID
    SK_INVALID --> SK_SKIP
    SK_META --"[ok]"--> SK_FB
    // → packages/agent-core/src/skill/parser.ts#L139
    SK_FB --> SK_REG
    SK_REG --"::yields"--> SK_LIST
    // → packages/agent-core/src/skill/registry.ts#L132

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| SK_SCAN | scanner.discoverSkills |  |
| SK_READ | 读取 SKILL.md |  |
| SK_PARSE | parseSkillText |  |
| SK_OK | 解析成功? |  |
| SK_REG | SkillRegistry.byName |  |
| SK_SKIP | warn · skip skill |  |
| SK_SYS | system.md Creating skills |  |
| SK_AUTHOR | agent 创作 SKILL.md |  |
| SK_META | directory SKILL.md frontmatter / 字段 |  |
| SK_INVALID | 无效 YAML / 非 mapping |  |
| SK_FB | name ?? skillDirName · description ?? descriptionFromBody |  |
| SK_LIST | getModelSkillListing → KIMI_SKILLS |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| SK_SCAN | SK_READ | -> | depends_on |  | 1 anchor(s) |
| SK_READ | SK_PARSE | -> | depends_on |  | 1 anchor(s) |
| SK_PARSE | SK_OK | ?> | condition |  |  |
| SK_OK | SK_REG | [ok] | depends_on |  | 1 anchor(s) |
| SK_OK | SK_SKIP | [err] | depends_on |  | 1 anchor(s) |
| SK_SYS | SK_AUTHOR | ::triggers | triggers |  | 1 anchor(s) |
| SK_AUTHOR | SK_READ | ~> | async_calls |  |  |
| SK_PARSE | SK_META | ?> | condition |  |  |
| SK_META | SK_INVALID | [err] | depends_on |  |  |
| SK_INVALID | SK_SKIP | -> | depends_on |  |  |
| SK_META | SK_FB | [ok] | depends_on |  | 1 anchor(s) |
| SK_FB | SK_REG | -> | depends_on |  |  |
| SK_REG | SK_LIST | ::yields | yields |  | 1 anchor(s) |

## Notes

**fork 真值**（516958cb）：directory `SKILL.md` 缺 frontmatter 时 parse fallback 注册；upstream main 未合并。


