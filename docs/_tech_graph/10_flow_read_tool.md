---
graph_id: 10_flow_read_tool
version: 2026-06-18
generated_at: 2026-06-18T14:26:55Z
source: docs/_tech_graph/10_flow_read_tool.graph.yaml
---

# Flow：Read 工具 · 行/字节截断与 status 组装（C3 #94）

ReadTool readForward/readTail · MAX_LINES/MAX_BYTES · finishMessage

## Mermaid

```mermaid
flowchart TD
    RT_EXEC[ReadTool.execution]
    RT_ROUTE[line_offset < 0?]
    RT_TAIL[readTail]
    RT_FWD[readForward]
    RT_SCAN[kaos.readLines]
    RT_COLLECT[收集 selectedEntries]
    RT_LCAP[达到 MAX_LINES?]
    RT_ML[maxLinesReached = true]
    RT_RENDER[renderLine · 累计 bytes]
    RT_BCAP[超过 MAX_BYTES?]
    RT_MB[maxBytesReached = true]
    RT_FIN[finishReadResult]
    RT_MSG[finishMessage]
    RT_STATUS[maxLinesReached?]
    RT_PL[parts += Max MAX_LINES lines]
    RT_PB[maxBytesReached?]
    RT_PBYTES[parts += Max MAX_BYTES bytes]
    RT_EOF[!ML && !MB && 未到请求行数?]
    RT_PEOF[End of file reached.]
    RT_OUT[finishOutput · system 标签]

    RT_EXEC --> RT_ROUTE
    RT_ROUTE --"[ok]"--> RT_TAIL
    RT_ROUTE --"[err]"--> RT_FWD
    // → packages/agent-core/src/tools/builtin/file/read.ts#L253
    RT_FWD --"::yields"--> RT_SCAN
    RT_SCAN --> RT_COLLECT
    RT_COLLECT --"?>"--> RT_LCAP
    RT_LCAP --"[ok]"--> RT_ML
    RT_COLLECT --> RT_RENDER
    RT_RENDER --"?>"--> RT_BCAP
    RT_BCAP --"[ok]"--> RT_MB
    RT_ML --"::merges"--> RT_FIN
    RT_MB --"::merges"--> RT_FIN
    RT_TAIL --> RT_FIN
    RT_FIN --> RT_MSG
    // → packages/agent-core/src/tools/builtin/file/read.ts#L436
    RT_MSG --"?>"--> RT_STATUS
    RT_STATUS --"[ok]"--> RT_PL
    RT_STATUS --> RT_PB
    RT_PB --"[ok]"--> RT_PBYTES
    RT_PB --"?>"--> RT_EOF
    RT_EOF --"[ok]"--> RT_PEOF
    RT_MSG --> RT_OUT
    // → packages/agent-core/src/tools/builtin/file/read.ts#L430

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| RT_EXEC | ReadTool.execution |  |
| RT_ROUTE | line_offset < 0? |  |
| RT_TAIL | readTail |  |
| RT_FWD | readForward |  |
| RT_SCAN | kaos.readLines |  |
| RT_COLLECT | 收集 selectedEntries |  |
| RT_LCAP | 达到 MAX_LINES? |  |
| RT_ML | maxLinesReached = true |  |
| RT_RENDER | renderLine · 累计 bytes |  |
| RT_BCAP | 超过 MAX_BYTES? |  |
| RT_MB | maxBytesReached = true |  |
| RT_FIN | finishReadResult |  |
| RT_MSG | finishMessage |  |
| RT_STATUS | maxLinesReached? |  |
| RT_PL | parts += Max MAX_LINES lines |  |
| RT_PB | maxBytesReached? |  |
| RT_PBYTES | parts += Max MAX_BYTES bytes |  |
| RT_EOF | !ML && !MB && 未到请求行数? |  |
| RT_PEOF | End of file reached. |  |
| RT_OUT | finishOutput · system 标签 |  |

### Edges

| From | To | Mark | Type | Label | Anchors |
|------|----|------|------|-------|---------|
| RT_EXEC | RT_ROUTE | -> | depends_on |  |  |
| RT_ROUTE | RT_TAIL | [ok] | depends_on |  |  |
| RT_ROUTE | RT_FWD | [err] | depends_on |  | 1 anchor(s) |
| RT_FWD | RT_SCAN | ::yields | yields |  |  |
| RT_SCAN | RT_COLLECT | -> | depends_on |  |  |
| RT_COLLECT | RT_LCAP | ?> | condition |  |  |
| RT_LCAP | RT_ML | [ok] | depends_on |  |  |
| RT_COLLECT | RT_RENDER | -> | depends_on |  |  |
| RT_RENDER | RT_BCAP | ?> | condition |  |  |
| RT_BCAP | RT_MB | [ok] | depends_on |  |  |
| RT_ML | RT_FIN | ::merges | merges |  |  |
| RT_MB | RT_FIN | ::merges | merges |  |  |
| RT_TAIL | RT_FIN | -> | depends_on |  |  |
| RT_FIN | RT_MSG | -> | depends_on |  | 1 anchor(s) |
| RT_MSG | RT_STATUS | ?> | condition |  |  |
| RT_STATUS | RT_PL | [ok] | depends_on |  |  |
| RT_STATUS | RT_PB | -> | depends_on |  |  |
| RT_PB | RT_PBYTES | [ok] | depends_on |  |  |
| RT_PB | RT_EOF | ?> | condition |  |  |
| RT_EOF | RT_PEOF | [ok] | depends_on |  |  |
| RT_MSG | RT_OUT | -> | depends_on |  | 1 anchor(s) |

## Notes

| 常量 | 值 |
|------|-----|
| MAX_LINES | 1000 |
| MAX_BYTES | 102400 (100 KiB) |
| MAX_LINE_LENGTH | 2000 |


