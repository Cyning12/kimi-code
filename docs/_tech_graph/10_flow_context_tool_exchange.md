---
graph_id: 10_flow_context_tool_exchange
version: 2026-06-18
generated_at: 2026-06-18T14:26:55Z
source: docs/_tech_graph/10_flow_context_tool_exchange.graph.yaml
---

# Flow：Context · tool_call / tool_result 配对与 LLM 投影（C3 #705）

ContextMemory · projector · steer · resume · orphan tool_calls

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
    CTX_FIN[turn.finishResume]
    CTX_ORPHAN[orphan tool_calls → provider 400]
    CTX_TRIM[trimTrailingOpenToolExchange]
    CTX_INHERIT[仅 useProjectedHistoryFrom]

    CTX_LOOP --> CTX_TC
    // → packages/agent-core/src/agent/context/index.ts#L247
    CTX_TC --> CTX_TR
    // → packages/agent-core/src/agent/context/index.ts#L263
    CTX_TR --> CTX_GET
    // → packages/agent-core/src/agent/context/index.ts#L196
    CTX_GET --> CTX_PROJ
    // → packages/agent-core/src/agent/context/projector.ts#L5
    CTX_PROJ --> CTX_LLM
    // → packages/agent-core/src/agent/turn/index.ts
    CTX_BG --"::triggers"--> CTX_STEER
    // → packages/agent-core/src/agent/background/index.ts#L557
    CTX_STEER --> CTX_FLUSH
    // → packages/agent-core/src/agent/turn/index.ts#L608
    CTX_FLUSH --> CTX_AUM
    CTX_AUM --"?>"--> CTX_PEND
    CTX_PEND --"[ok]"--> CTX_DEFER
    // → packages/agent-core/src/agent/context/index.ts#L282
    CTX_PEND --"[err]"--> CTX_HIST
    CTX_RES --> CTX_AR
    // → packages/agent-core/src/agent/index.ts#L297
    CTX_AR --> CTX_REP
    // → packages/agent-core/src/agent/records/index.ts#L175
    CTX_REP --> CTX_FIN
    // → packages/agent-core/src/agent/turn/index.ts#L275
    CTX_FIN --> CTX_GET
    CTX_PROJ --"[err]"--> CTX_ORPHAN
    CTX_TRIM --"::gates"--> CTX_INHERIT
    // → packages/agent-core/src/agent/context/projector.ts#L74

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| CTX_LOOP | appendLoopEvent |  |
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
| CTX_FIN | turn.finishResume |  |
| CTX_ORPHAN | orphan tool_calls → provider 400 |  |
| CTX_TRIM | trimTrailingOpenToolExchange |  |
| CTX_INHERIT | 仅 useProjectedHistoryFrom |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| CTX_LOOP | CTX_TC | -> | depends_on |  | 1 anchor(s) |
| CTX_TC | CTX_TR | -> | depends_on |  | 1 anchor(s) |
| CTX_TR | CTX_GET | -> | depends_on |  | 1 anchor(s) |
| CTX_GET | CTX_PROJ | -> | depends_on |  | 1 anchor(s) |
| CTX_PROJ | CTX_LLM | -> | depends_on |  | 1 anchor(s) |
| CTX_BG | CTX_STEER | ::triggers | triggers |  | 1 anchor(s) |
| CTX_STEER | CTX_FLUSH | -> | depends_on |  | 1 anchor(s) |
| CTX_FLUSH | CTX_AUM | -> | depends_on |  |  |
| CTX_AUM | CTX_PEND | ?> | condition |  |  |
| CTX_PEND | CTX_DEFER | [ok] | depends_on |  | 1 anchor(s) |
| CTX_PEND | CTX_HIST | [err] | depends_on |  |  |
| CTX_RES | CTX_AR | -> | depends_on |  | 1 anchor(s) |
| CTX_AR | CTX_REP | -> | depends_on |  | 1 anchor(s) |
| CTX_REP | CTX_FIN | -> | depends_on |  | 1 anchor(s) |
| CTX_FIN | CTX_GET | -> | depends_on |  |  |
| CTX_PROJ | CTX_ORPHAN | [err] | depends_on |  |  |
| CTX_TRIM | CTX_INHERIT | ::gates | gates |  | 1 anchor(s) |

## Notes

**Path A**：loop → LLM · **Path B**：steer #705 race · **Path C**：resume · **main gap**：orphan tool_calls / trim 仅 inherit 路径。


