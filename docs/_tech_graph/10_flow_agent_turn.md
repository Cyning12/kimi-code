---
graph_id: 10_flow_agent_turn
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_agent_turn.graph.yaml
---

# Flow：Agent 轮次 · TurnFlow.runOneTurn / runStepLoop

prompt/launch → turnWorker → runOneTurn → runStepLoop → runTurn（折叠 turn-step）→ authorize/finalize → turn.ended；#583 telemetry 为侧链

## Mermaid

```mermaid
flowchart TD
    AT_LAUNCH[TurnFlow.prompt / launch]
    AT_WORKER[turnWorker]
    AT_GOAL[driveGoal 续轮]
    AT_ONE[runOneTurn]
    AT_HOOK[applyUserPromptHook]
    AT_LOOP[runStepLoop]
    AT_STEP[runTurn 步循环（折叠 turn-step）]
    AT_AUTH[prepare + authorizeToolExecution]
    AT_EXEC[runToolCallBatch / execute]
    AT_ABORT_TOOL[abort settle / isUserCancellation]
    AT_FINAL[finalizeToolResult / budget]
    AT_CONT[shouldContinueAfterStop?]
    AT_ENDED[turn.ended]
    AT_ABORT[cancelled / isAbortError]
    AT_FAIL[failed / maxSteps / api_error]
    AT_TRACK[trackToolLifecycle（#583 侧链）]
    AT_OC[telemetryToolOutcome]
    AT_TELEM[telemetry.track tool_call]

    AT_LAUNCH --> AT_WORKER
    // → packages/agent-core/src/agent/turn/index.ts#L123
    // → packages/agent-core/src/agent/turn/index.ts#L151
    AT_WORKER --"无 active goal"--> AT_ONE
    // → packages/agent-core/src/agent/turn/index.ts#L320
    AT_WORKER --"goal.active"--> AT_GOAL
    // → packages/agent-core/src/agent/turn/index.ts#L318
    AT_GOAL --"~>"--> AT_ONE
    // → packages/agent-core/src/agent/turn/index.ts#L358
    // → packages/agent-core/src/agent/turn/index.ts#L380
    AT_ONE --> AT_HOOK
    // → packages/agent-core/src/agent/turn/index.ts#L445
    // → packages/agent-core/src/agent/turn/index.ts#L472
    AT_HOOK --"[ok]"--> AT_LOOP
    // → packages/agent-core/src/agent/turn/index.ts#L477
    // → packages/agent-core/src/agent/turn/index.ts#L622
    AT_HOOK --"UserPromptSubmit blocked"--> AT_ENDED
    // → packages/agent-core/src/agent/turn/index.ts#L568
    // → packages/agent-core/src/agent/turn/index.ts#L586
    AT_LOOP --"~>"--> AT_STEP
    // → packages/agent-core/src/agent/turn/index.ts#L626
    // → packages/agent-core/src/agent/turn/index.ts#L630
    // → packages/agent-core/src/agent/turn/index.ts#L637
    // → packages/agent-core/src/loop/run-turn.ts#L48
    AT_LOOP --"CONTEXT_OVERFLOW compaction retry"--> AT_LOOP
    // → packages/agent-core/src/agent/turn/index.ts#L765
    AT_LOOP --"maxStepsExceeded"--> AT_FAIL
    // → packages/agent-core/src/agent/turn/index.ts#L770
    // → packages/agent-core/src/loop/run-turn.ts#L78
    AT_LOOP --"stopReason aborted"--> AT_ABORT
    // → packages/agent-core/src/loop/run-turn.ts#L119
    // → packages/agent-core/src/agent/turn/index.ts#L481
    AT_STEP --"tool_use"--> AT_AUTH
    // → packages/agent-core/src/loop/run-turn.ts#L99
    // → packages/agent-core/src/loop/turn-step.ts#L46
    AT_STEP --"非 tool_use"--> AT_CONT
    // → packages/agent-core/src/loop/run-turn.ts#L103
    AT_AUTH --"~>"--> AT_EXEC
    // → packages/agent-core/src/agent/turn/index.ts#L717
    // → packages/agent-core/src/agent/turn/index.ts#L726
    // → packages/agent-core/src/agent/turn/tool-dedup.ts#L176
    // → packages/agent-core/src/agent/permission/index.ts#L96
    // → packages/agent-core/src/loop/tool-call.ts#L426
    AT_EXEC --"[ok]"--> AT_FINAL
    // → packages/agent-core/src/loop/tool-call.ts#L122
    // → packages/agent-core/src/loop/tool-call.ts#L507
    AT_EXEC --"abort settle"--> AT_ABORT_TOOL
    // → packages/agent-core/src/loop/tool-call.ts#L56
    // → packages/agent-core/src/loop/tool-call.ts#L306
    // → packages/agent-core/src/utils/abort.ts#L31
    AT_ABORT_TOOL --> AT_FINAL
    // → packages/agent-core/src/loop/tool-call.ts#L512
    AT_FINAL --> AT_CONT
    // → packages/agent-core/src/agent/turn/index.ts#L729
    // → packages/agent-core/src/agent/turn/tool-result-budget.ts#L19
    // → packages/agent-core/src/agent/turn/index.ts#L671
    AT_CONT --"continue"--> AT_STEP
    // → packages/agent-core/src/loop/run-turn.ts#L109
    AT_CONT --"stop"--> AT_ENDED
    // → packages/agent-core/src/loop/run-turn.ts#L116
    // → packages/agent-core/src/agent/turn/index.ts#L537
    AT_ONE --"isAbortError"--> AT_ABORT
    // → packages/agent-core/src/agent/turn/index.ts#L489
    AT_ONE --"failed"--> AT_FAIL
    // → packages/agent-core/src/agent/turn/index.ts#L491
    AT_ABORT --> AT_ENDED
    // → packages/agent-core/src/agent/turn/index.ts#L537
    AT_FAIL --> AT_ENDED
    // → packages/agent-core/src/agent/turn/index.ts#L498
    AT_FINAL --"#583 侧链"--> AT_TRACK
    // → packages/agent-core/src/agent/turn/index.ts#L816
    // → packages/agent-core/src/agent/turn/index.ts#L839
    AT_TRACK --> AT_OC
    // → packages/agent-core/src/agent/turn/index.ts#L852
    // → packages/agent-core/src/agent/turn/index.ts#L1160
    AT_OC --"success"--> AT_TELEM
    // → packages/agent-core/src/agent/turn/index.ts#L869
    AT_OC --"cancelled"--> AT_TELEM
    // → packages/agent-core/src/agent/turn/index.ts#L1160
    AT_OC --"error"--> AT_TELEM
    // → packages/agent-core/src/agent/turn/index.ts#L1170

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| AT_LAUNCH | TurnFlow.prompt / launch | flow |
| AT_WORKER | turnWorker |  |
| AT_GOAL | driveGoal 续轮 |  |
| AT_ONE | runOneTurn |  |
| AT_HOOK | applyUserPromptHook |  |
| AT_LOOP | runStepLoop |  |
| AT_STEP | runTurn 步循环（折叠 turn-step） |  |
| AT_AUTH | prepare + authorizeToolExecution |  |
| AT_EXEC | runToolCallBatch / execute |  |
| AT_ABORT_TOOL | abort settle / isUserCancellation |  |
| AT_FINAL | finalizeToolResult / budget |  |
| AT_CONT | shouldContinueAfterStop? |  |
| AT_ENDED | turn.ended |  |
| AT_ABORT | cancelled / isAbortError |  |
| AT_FAIL | failed / maxSteps / api_error |  |
| AT_TRACK | trackToolLifecycle（#583 侧链） |  |
| AT_OC | telemetryToolOutcome |  |
| AT_TELEM | telemetry.track tool_call |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| AT_LAUNCH | AT_WORKER | -> | depends_on |  | 2 anchor(s) |
| AT_WORKER | AT_ONE | ?> | condition | 无 active goal | 1 anchor(s) |
| AT_WORKER | AT_GOAL | ?> | condition | goal.active | 1 anchor(s) |
| AT_GOAL | AT_ONE | ~> | async_calls |  | 2 anchor(s) |
| AT_ONE | AT_HOOK | -> | depends_on |  | 2 anchor(s) |
| AT_HOOK | AT_LOOP | [ok] | depends_on |  | 2 anchor(s) |
| AT_HOOK | AT_ENDED | [err] | depends_on | UserPromptSubmit blocked | 2 anchor(s) |
| AT_LOOP | AT_STEP | ~> | async_calls |  | 4 anchor(s) |
| AT_LOOP | AT_LOOP | [err] | depends_on | CONTEXT_OVERFLOW compaction retry | 1 anchor(s) |
| AT_LOOP | AT_FAIL | [err] | depends_on | maxStepsExceeded | 2 anchor(s) |
| AT_LOOP | AT_ABORT | [err] | depends_on | stopReason aborted | 2 anchor(s) |
| AT_STEP | AT_AUTH | ?> | condition | tool_use | 2 anchor(s) |
| AT_STEP | AT_CONT | [ok] | depends_on | 非 tool_use | 1 anchor(s) |
| AT_AUTH | AT_EXEC | ~> | async_calls |  | 5 anchor(s) |
| AT_EXEC | AT_FINAL | [ok] | depends_on |  | 2 anchor(s) |
| AT_EXEC | AT_ABORT_TOOL | [err] | depends_on | abort settle | 3 anchor(s) |
| AT_ABORT_TOOL | AT_FINAL | -> | depends_on |  | 1 anchor(s) |
| AT_FINAL | AT_CONT | -> | depends_on |  | 3 anchor(s) |
| AT_CONT | AT_STEP | [ok] | depends_on | continue | 1 anchor(s) |
| AT_CONT | AT_ENDED | [ok] | depends_on | stop | 2 anchor(s) |
| AT_ONE | AT_ABORT | [err] | depends_on | isAbortError | 1 anchor(s) |
| AT_ONE | AT_FAIL | [err] | depends_on | failed | 1 anchor(s) |
| AT_ABORT | AT_ENDED | -> | depends_on |  | 1 anchor(s) |
| AT_FAIL | AT_ENDED | -> | depends_on |  | 1 anchor(s) |
| AT_FINAL | AT_TRACK | ::archives | archives | #583 侧链 | 2 anchor(s) |
| AT_TRACK | AT_OC | -> | depends_on |  | 2 anchor(s) |
| AT_OC | AT_TELEM | ?> | condition | success | 1 anchor(s) |
| AT_OC | AT_TELEM | ?> | condition | cancelled | 1 anchor(s) |
| AT_OC | AT_TELEM | ?> | condition | error | 1 anchor(s) |

## Notes

**主干**：`TurnFlow.prompt/launch` → `turnWorker` → `runOneTurn` → `runStepLoop` → `runTurn`（`turn-step` 折叠）→ `authorizeToolExecution`/`finalizeToolResult` → `turn.ended`。
**#583 telemetry**（`trackToolLifecycle` / `telemetryToolOutcome` 三色）挂 `::archives` **侧链**，不得充当唯一主干。
删除虚构 `tool-telemetry.ts`（函数在 `turn/index.ts`）；`cancelledByUser` 字段不存在，改为 `isUserCancellation` / `UserCancellationError`。
`00_main` 待补表状态字留给 W-close，本波不改 `00_main.graph.yaml`。


