---
graph_id: 10_flow_subagent
version: 2026-08-28
generated_at: 2026-08-28T08:27:10Z
source: docs/_tech_graph/10_flow_subagent.graph.yaml
---

# Flow：Subagent 装配 · spawn/batch · 生命周期（切片）

Session 装配 SessionSubagentHost → spawn/resume/retry 或 runQueued(SubagentBatch) → lifecycle events

## Mermaid

```mermaid
flowchart TD
    SA_ASM[Session.createAgent 装配 subagentHost]
    SA_HOST[SessionSubagentHost]
    SA_QUEUE[runQueued → SubagentBatch.run]
    SA_KIND[spawn / resume / retry?]
    SA_SPAWN[spawn · createAgent + resolveProfile]
    SA_RESUME[resume / retry idle child]
    SA_CFG[configureChild · inheritUserTools]
    SA_TURN[runPromptTurn · waitForChildCompletion]
    SA_OK[subagent.completed]
    SA_ERR[subagent.failed]
    SA_SUSP[rate-limit · suspended · requeue]
    SA_TUI[TUI SubAgentEventHandler（可选消费）]

    SA_ASM --> SA_HOST
    // → packages/agent-core/src/session/index.ts#L732
    SA_HOST --> SA_QUEUE
    // → packages/agent-core/src/session/subagent-host.ts#L199
    SA_HOST --> SA_SPAWN
    // → packages/agent-core/src/session/subagent-host.ts#L114
    SA_QUEUE --"?>"--> SA_KIND
    // → packages/agent-core/src/session/subagent-batch.ts#L179
    SA_KIND --"spawn"--> SA_SPAWN
    // → packages/agent-core/src/session/subagent-batch.ts#L329
    SA_KIND --"resume / retry"--> SA_RESUME
    // → packages/agent-core/src/session/subagent-batch.ts#L320
    SA_SPAWN --> SA_CFG
    // → packages/agent-core/src/session/subagent-host.ts#L360
    SA_CFG --"~>"--> SA_TURN
    // → packages/agent-core/src/session/subagent-host.ts#L300
    SA_RESUME --"~>"--> SA_TURN
    // → packages/agent-core/src/session/subagent-host.ts#L141
    SA_TURN --"[ok]"--> SA_OK
    // → packages/agent-core/src/session/subagent-host.ts#L349
    SA_TURN --"[err]"--> SA_ERR
    // → packages/agent-core/src/session/subagent-host.ts#L453
    SA_QUEUE --"[err]"--> SA_SUSP
    // → packages/agent-core/src/session/subagent-batch.ts#L426
    SA_SUSP --"::triggers"--> SA_KIND
    // → packages/agent-core/src/session/subagent-host.ts#L204
    SA_OK --"::yields"--> SA_TUI
    // → apps/kimi-code/src/tui/controllers/subagent-event-handler.ts#L133
    SA_ERR --"::yields"--> SA_TUI
    // → apps/kimi-code/src/tui/controllers/subagent-event-handler.ts#L54

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| SA_ASM | Session.createAgent 装配 subagentHost | flow |
| SA_HOST | SessionSubagentHost |  |
| SA_QUEUE | runQueued → SubagentBatch.run |  |
| SA_KIND | spawn / resume / retry? |  |
| SA_SPAWN | spawn · createAgent + resolveProfile |  |
| SA_RESUME | resume / retry idle child |  |
| SA_CFG | configureChild · inheritUserTools |  |
| SA_TURN | runPromptTurn · waitForChildCompletion |  |
| SA_OK | subagent.completed |  |
| SA_ERR | subagent.failed |  |
| SA_SUSP | rate-limit · suspended · requeue |  |
| SA_TUI | TUI SubAgentEventHandler（可选消费） |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| SA_ASM | SA_HOST | -> | depends_on |  | 1 anchor(s) |
| SA_HOST | SA_QUEUE | -> | depends_on |  | 1 anchor(s) |
| SA_HOST | SA_SPAWN | -> | depends_on |  | 1 anchor(s) |
| SA_QUEUE | SA_KIND | ?> | condition |  | 1 anchor(s) |
| SA_KIND | SA_SPAWN | [ok] | depends_on | spawn | 1 anchor(s) |
| SA_KIND | SA_RESUME | -> | depends_on | resume / retry | 1 anchor(s) |
| SA_SPAWN | SA_CFG | -> | depends_on |  | 1 anchor(s) |
| SA_CFG | SA_TURN | ~> | async_calls |  | 1 anchor(s) |
| SA_RESUME | SA_TURN | ~> | async_calls |  | 1 anchor(s) |
| SA_TURN | SA_OK | [ok] | depends_on |  | 1 anchor(s) |
| SA_TURN | SA_ERR | [err] | depends_on |  | 1 anchor(s) |
| SA_QUEUE | SA_SUSP | [err] | depends_on |  | 1 anchor(s) |
| SA_SUSP | SA_KIND | ::triggers | triggers |  | 1 anchor(s) |
| SA_OK | SA_TUI | ::yields | yields |  | 1 anchor(s) |
| SA_ERR | SA_TUI | ::yields | yields |  | 1 anchor(s) |

## Notes

**切片**：swarm 调度细节（首批 5、700ms ramp、rate-limit capacity）不画全；见 `subagent-batch.ts` 文件头契约。
**TUI** 仅为可选消费节点，不单独成图。`startBtw` / `cancelAll` 未展开。
**佐证**：`packages/agent-core/test/session/subagent-host.test.ts`。
本波不改 `00_main.graph.yaml`（FLOW_SUB 索引留给 W-close）。


