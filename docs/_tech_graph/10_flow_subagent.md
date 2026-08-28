---
graph_id: 10_flow_subagent
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_subagent.graph.yaml
---

# Flow：Subagent 装配 · spawn/batch · timeout / user-cancel / rate-limit

Session 装配 SessionSubagentHost → spawn/resume/retry 或 runQueued(SubagentBatch) → 完成；侧链 timeout / user-cancel / rate-limit（TUI 可选消费）

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
    SA_RL[isProviderRateLimitError?]
    SA_SUSP[rate-limit · suspended · requeue]
    SA_TO[task timeout · fail slot]
    SA_CANCEL[user-cancel · aborted]
    SA_TUI[TUI SubAgentEventHandler（可选消费）]

    SA_ASM --> SA_HOST
    // → packages/agent-core/src/session/index.ts#L732
    SA_HOST --> SA_QUEUE
    // → packages/agent-core/src/session/subagent-host.ts#L199
    SA_HOST --> SA_SPAWN
    // → packages/agent-core/src/session/subagent-host.ts#L114
    SA_QUEUE --"?>"--> SA_KIND
    // → packages/agent-core/src/session/subagent-batch.ts#L179
    // → packages/agent-core/src/session/subagent-batch.ts#L304
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
    SA_TURN --"[timeout]"--> SA_TO
    // → packages/agent-core/src/session/subagent-batch.ts#L627
    // → packages/agent-core/src/session/subagent-batch.ts#L653
    SA_QUEUE --"user-cancel"--> SA_CANCEL
    // → packages/agent-core/src/session/subagent-batch.ts#L171
    // → packages/agent-core/src/session/subagent-batch.ts#L553
    SA_HOST --"cancelAll"--> SA_CANCEL
    // → packages/agent-core/src/session/subagent-host.ts#L239
    SA_TURN --"rate-limit"--> SA_RL
    // → packages/agent-core/src/session/subagent-batch.ts#L346
    // → packages/agent-core/src/session/subagent-host.ts#L475
    SA_RL --"requeue"--> SA_SUSP
    // → packages/agent-core/src/session/subagent-batch.ts#L403
    // → packages/agent-core/src/session/subagent-batch.ts#L426
    SA_RL --"only unfinished"--> SA_ERR
    // → packages/agent-core/src/session/subagent-batch.ts#L394
    SA_SUSP --"::triggers"--> SA_KIND
    // → packages/agent-core/src/session/subagent-host.ts#L204
    // → packages/agent-core/src/session/subagent-batch.ts#L463
    SA_OK --"::yields"--> SA_TUI
    // → apps/kimi-code/src/tui/controllers/subagent-event-handler.ts#L273
    SA_ERR --"::yields"--> SA_TUI
    // → apps/kimi-code/src/tui/controllers/subagent-event-handler.ts#L302
    SA_SUSP --"::yields"--> SA_TUI
    // → apps/kimi-code/src/tui/controllers/subagent-event-handler.ts#L265

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
| SA_RL | isProviderRateLimitError? |  |
| SA_SUSP | rate-limit · suspended · requeue |  |
| SA_TO | task timeout · fail slot |  |
| SA_CANCEL | user-cancel · aborted |  |
| SA_TUI | TUI SubAgentEventHandler（可选消费） |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| SA_ASM | SA_HOST | -> | depends_on |  | 1 anchor(s) |
| SA_HOST | SA_QUEUE | -> | depends_on |  | 1 anchor(s) |
| SA_HOST | SA_SPAWN | -> | depends_on |  | 1 anchor(s) |
| SA_QUEUE | SA_KIND | ?> | condition |  | 2 anchor(s) |
| SA_KIND | SA_SPAWN | [ok] | depends_on | spawn | 1 anchor(s) |
| SA_KIND | SA_RESUME | -> | depends_on | resume / retry | 1 anchor(s) |
| SA_SPAWN | SA_CFG | -> | depends_on |  | 1 anchor(s) |
| SA_CFG | SA_TURN | ~> | async_calls |  | 1 anchor(s) |
| SA_RESUME | SA_TURN | ~> | async_calls |  | 1 anchor(s) |
| SA_TURN | SA_OK | [ok] | depends_on |  | 1 anchor(s) |
| SA_TURN | SA_ERR | [err] | depends_on |  | 1 anchor(s) |
| SA_TURN | SA_TO | [timeout] | depends_on |  | 2 anchor(s) |
| SA_QUEUE | SA_CANCEL | [err] | depends_on | user-cancel | 2 anchor(s) |
| SA_HOST | SA_CANCEL | ::triggers | triggers | cancelAll | 1 anchor(s) |
| SA_TURN | SA_RL | ?> | condition | rate-limit | 2 anchor(s) |
| SA_RL | SA_SUSP | -> | depends_on | requeue | 2 anchor(s) |
| SA_RL | SA_ERR | [err] | depends_on | only unfinished | 1 anchor(s) |
| SA_SUSP | SA_KIND | ::triggers | triggers |  | 2 anchor(s) |
| SA_OK | SA_TUI | ::yields | yields |  | 1 anchor(s) |
| SA_ERR | SA_TUI | ::yields | yields |  | 1 anchor(s) |
| SA_SUSP | SA_TUI | ::yields | yields |  | 1 anchor(s) |

## Notes

**主干**：`Session.createAgent` 装配 `SessionSubagentHost` → `runQueued`/`spawn` → `runPromptTurn` → `subagent.completed`。
**timeout**：`linkAttemptSignals` 按 `task.timeout` abort；`attemptErrorMessage` 返回 `Subagent timed out.`；只失败该 slot，不进入 rate-limit phase、不停其它任务。
**user-cancel**：batch 首个 `signal` 即 batch signal；`isUserCancellation` → `finishWithUserCancellation`（保留已完成结果，未完成 aborted/started 或 aborted/not_started）。非用户 abort 走 `fail` reject。Host `cancelAll` 为可选触发，不另开图。
**rate-limit**：`isProviderRateLimitError` 后若是唯一未完成任务则 `failed`；否则 `requeueRateLimited` + `enterRateLimitMode`（capacity/3min recovery 折叠，不展开）。
**折叠**：首批 5、700ms ramp（`scheduleNormalLaunch`）与 `startBtw` 不展开。
**TUI** 仅为可选消费（completed / failed / suspended），不单独成图。
**佐证**：`packages/agent-core/test/session/subagent-host.test.ts`。
本波不改 `00_main.graph.yaml`（FLOW_SUB 索引留给 W-close）。


