---
graph_id: 10_flow_context_tool_exchange
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_context_tool_exchange.graph.yaml
---

# Flow：Context · tool_call / tool_result 配对与 LLM 投影（C3 #705）

ContextMemory · projector · steer · resume · orphan tool_calls；trim 仅 inherit

## Mermaid

```mermaid
flowchart TD
    CTX_LOOP[appendLoopEvent]
    CTX_TC[tool.call · pending add]
    CTX_TR[tool.result · pending delete]
    CTX_GET[ContextMemory.messages]
    CTX_PROJ[project · microCompaction]
    CTX_LLM[generate / compaction]
    CTX_BG[Background notify]
    CTX_STEER[TurnFlow.steer · buffer]
    CTX_FLUSH[beforeStep flushSteerBuffer]
    CTX_AUM[appendUserMessage]
    CTX_PEND[pendingToolResultIds?]
    CTX_DEFER[deferredMessages]
    CTX_HIST[pushHistory]
    CTX_RES[Session.resumeAgent]
    CTX_AR[Agent.resume]
    CTX_REP[AgentRecords.replay]
    CTX_FIN[finishResume · closePendingToolResults]
    CTX_ORPHAN[orphan tool_calls → provider 400]
    CTX_TRIM[trimTrailingOpenToolExchange]
    CTX_INHERIT[仅 useProjectedHistoryFrom]

    CTX_LOOP --> CTX_TC
    // → packages/agent-core/src/agent/context/index.ts#L300
    // → packages/agent-core/src/agent/context/index.ts#L360
    CTX_TC --> CTX_TR
    // → packages/agent-core/src/agent/context/index.ts#L376
    // → packages/agent-core/src/agent/context/index.ts#L387
    CTX_TR --> CTX_GET
    // → packages/agent-core/src/agent/context/index.ts#L263
    CTX_GET --> CTX_PROJ
    // → packages/agent-core/src/agent/context/index.ts#L259
    // → packages/agent-core/src/agent/context/index.ts#L263
    // → packages/agent-core/src/agent/context/projector.ts#L6
    CTX_PROJ --> CTX_LLM
    // → packages/agent-core/src/agent/turn/index.ts#L641
    CTX_BG --"::triggers"--> CTX_STEER
    // → packages/agent-core/src/agent/background/index.ts#L652
    // → packages/agent-core/src/agent/background/index.ts#L655
    CTX_STEER --> CTX_FLUSH
    // → packages/agent-core/src/agent/turn/index.ts#L134
    // → packages/agent-core/src/agent/turn/index.ts#L657
    CTX_FLUSH --> CTX_AUM
    // → packages/agent-core/src/agent/turn/index.ts#L282
    // → packages/agent-core/src/agent/turn/index.ts#L286
    CTX_AUM --"?>"--> CTX_PEND
    // → packages/agent-core/src/agent/context/index.ts#L51
    // → packages/agent-core/src/agent/context/index.ts#L399
    CTX_PEND --"[ok]"--> CTX_DEFER
    // → packages/agent-core/src/agent/context/index.ts#L399
    // → packages/agent-core/src/agent/context/index.ts#L400
    CTX_PEND --> CTX_HIST
    // → packages/agent-core/src/agent/context/index.ts#L403
    // → packages/agent-core/src/agent/context/index.ts#L415
    CTX_DEFER --> CTX_HIST
    // → packages/agent-core/src/agent/context/index.ts#L388
    // → packages/agent-core/src/agent/context/index.ts#L406
    // → packages/agent-core/src/agent/context/index.ts#L410
    CTX_HIST --> CTX_GET
    // → packages/agent-core/src/agent/context/index.ts#L418
    // → packages/agent-core/src/agent/context/index.ts#L263
    CTX_RES --> CTX_AR
    // → packages/agent-core/src/session/index.ts#L775
    // → packages/agent-core/src/session/index.ts#L812
    CTX_AR --> CTX_REP
    // → packages/agent-core/src/agent/index.ts#L263
    // → packages/agent-core/src/agent/index.ts#L264
    CTX_REP --> CTX_FIN
    // → packages/agent-core/src/agent/index.ts#L271
    // → packages/agent-core/src/agent/turn/index.ts#L292
    CTX_FIN --> CTX_GET
    // → packages/agent-core/src/agent/context/index.ts#L272
    // → packages/agent-core/src/agent/context/index.ts#L284
    CTX_PROJ --"[err]"--> CTX_ORPHAN
    // → packages/agent-core/src/agent/context/index.ts#L263
    // → packages/agent-core/src/agent/context/projector.ts#L6
    CTX_PROJ --> CTX_TRIM
    // → packages/agent-core/src/agent/context/index.ts#L267
    // → packages/agent-core/src/agent/context/index.ts#L269
    CTX_TRIM --"::gates"--> CTX_INHERIT
    // → packages/agent-core/src/agent/context/projector.ts#L96
    // → packages/agent-core/src/session/subagent-host.ts#L230

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| CTX_LOOP | appendLoopEvent | flow |
| CTX_TC | tool.call · pending add |  |
| CTX_TR | tool.result · pending delete |  |
| CTX_GET | ContextMemory.messages |  |
| CTX_PROJ | project · microCompaction |  |
| CTX_LLM | generate / compaction |  |
| CTX_BG | Background notify |  |
| CTX_STEER | TurnFlow.steer · buffer |  |
| CTX_FLUSH | beforeStep flushSteerBuffer |  |
| CTX_AUM | appendUserMessage |  |
| CTX_PEND | pendingToolResultIds? |  |
| CTX_DEFER | deferredMessages |  |
| CTX_HIST | pushHistory |  |
| CTX_RES | Session.resumeAgent |  |
| CTX_AR | Agent.resume |  |
| CTX_REP | AgentRecords.replay |  |
| CTX_FIN | finishResume · closePendingToolResults |  |
| CTX_ORPHAN | orphan tool_calls → provider 400 |  |
| CTX_TRIM | trimTrailingOpenToolExchange |  |
| CTX_INHERIT | 仅 useProjectedHistoryFrom |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| CTX_LOOP | CTX_TC | -> | depends_on |  | 2 anchor(s) |
| CTX_TC | CTX_TR | -> | depends_on |  | 2 anchor(s) |
| CTX_TR | CTX_GET | -> | depends_on |  | 1 anchor(s) |
| CTX_GET | CTX_PROJ | -> | depends_on |  | 3 anchor(s) |
| CTX_PROJ | CTX_LLM | -> | depends_on |  | 1 anchor(s) |
| CTX_BG | CTX_STEER | ::triggers | triggers |  | 2 anchor(s) |
| CTX_STEER | CTX_FLUSH | -> | depends_on |  | 2 anchor(s) |
| CTX_FLUSH | CTX_AUM | -> | depends_on |  | 2 anchor(s) |
| CTX_AUM | CTX_PEND | ?> | condition |  | 2 anchor(s) |
| CTX_PEND | CTX_DEFER | [ok] | depends_on |  | 2 anchor(s) |
| CTX_PEND | CTX_HIST | -> | depends_on |  | 2 anchor(s) |
| CTX_DEFER | CTX_HIST | -> | depends_on |  | 3 anchor(s) |
| CTX_HIST | CTX_GET | -> | depends_on |  | 2 anchor(s) |
| CTX_RES | CTX_AR | -> | depends_on |  | 2 anchor(s) |
| CTX_AR | CTX_REP | -> | depends_on |  | 2 anchor(s) |
| CTX_REP | CTX_FIN | -> | depends_on |  | 2 anchor(s) |
| CTX_FIN | CTX_GET | -> | depends_on |  | 2 anchor(s) |
| CTX_PROJ | CTX_ORPHAN | [err] | depends_on |  | 2 anchor(s) |
| CTX_PROJ | CTX_TRIM | -> | depends_on |  | 2 anchor(s) |
| CTX_TRIM | CTX_INHERIT | ::gates | gates |  | 2 anchor(s) |

## Notes

**deep**（2026-08-28 对照 context/turn/resume 现码 · 节点 20 未增 · 只补缺口边+行号）。
核对 #705 三路径均已在现码闭合，禁止为深而深加节点：
- **Path A** loop→LLM：`appendLoopEvent` `tool.call`/`tool.result` → `messages` → `project` → `runStepLoop.buildMessages`。
- **Path B** steer 竞态：`notifyBackgroundTask` → `turn.steer` → `beforeStep.flushSteerBuffer` → `appendUserMessage`；open exchange 入 `deferredMessages`，闭合后 `flushDeferredMessagesIfToolExchangeClosed` 回 `pushHistory` 再汇入 `messages`。
- **Path C** resume：`Session.resumeAgent` → `Agent.resume` → `records.replay` → `context.finishResume`（`closePendingToolResults` 合成 interrupted tool.result）+ `turn.finishResume`。task_705 表「resume 无 orphan cleanup」已过时。
- **trim**：`trimTrailingOpenToolExchange` **仅** `useProjectedHistoryFrom`（subagent inherit · `subagent-host.ts`）；live `messages` **不 trim**。未配对 `assistant.tool_calls` 直通 provider（CTX_ORPHAN [err]）。
- 行号相对 task_705 / 旧 yaml 已漂移，已按现码重锚。D3 硬边 18 · path 100% · line 100%。`00_main` 索引字 **skeleton→deep** 留给 W-close。


