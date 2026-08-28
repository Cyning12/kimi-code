---
graph_id: 10_flow_read_tool
version: 2026-08-28
generated_at: 2026-08-28T08:55:17Z
source: docs/_tech_graph/10_flow_read_tool.graph.yaml
---

# Flow：Read 工具 · 行/字节截断与 status 组装（C3 #94）

ReadTool execution 守卫 · readForward/readTail · MAX_LINES/MAX_BYTES · finishMessage

## Mermaid

```mermaid
flowchart TD
    RT_SCHEMA[ReadInputSchema · parameters]
    RT_SCHEMA_ERR[schema 校验失败]
    RT_EXEC[ReadTool.execution]
    RT_ENOENT[file does not exist]
    RT_NOTFILE[is not a file]
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

    RT_SCHEMA --"[ok]"--> RT_EXEC
    // → packages/agent-core/src/tools/builtin/file/read.ts#L237
    RT_SCHEMA --"[err]"--> RT_SCHEMA_ERR
    // → packages/agent-core/src/tools/builtin/file/read.ts#L25
    RT_EXEC --"[err]"--> RT_ENOENT
    // → packages/agent-core/src/tools/builtin/file/read.ts#L271
    RT_EXEC --"[err]"--> RT_NOTFILE
    // → packages/agent-core/src/tools/builtin/file/read.ts#L276
    RT_EXEC --> RT_ROUTE
    // → packages/agent-core/src/tools/builtin/file/read.ts#L298
    RT_ROUTE --"[ok]"--> RT_TAIL
    // → packages/agent-core/src/tools/builtin/file/read.ts#L299
    RT_ROUTE --> RT_FWD
    // → packages/agent-core/src/tools/builtin/file/read.ts#L306
    RT_FWD --"::yields"--> RT_SCAN
    // → packages/agent-core/src/tools/builtin/file/read.ts#L368
    RT_SCAN --> RT_COLLECT
    // → packages/agent-core/src/tools/builtin/file/read.ts#L388
    RT_COLLECT --"?>"--> RT_LCAP
    // → packages/agent-core/src/tools/builtin/file/read.ts#L381
    RT_LCAP --"[ok]"--> RT_ML
    // → packages/agent-core/src/tools/builtin/file/read.ts#L383
    RT_COLLECT --> RT_RENDER
    // → packages/agent-core/src/tools/builtin/file/read.ts#L398
    RT_RENDER --"?>"--> RT_BCAP
    // → packages/agent-core/src/tools/builtin/file/read.ts#L179
    RT_BCAP --"[ok]"--> RT_MB
    // → packages/agent-core/src/tools/builtin/file/read.ts#L180
    RT_ML --"::merges"--> RT_FIN
    // → packages/agent-core/src/tools/builtin/file/read.ts#L400
    RT_MB --"::merges"--> RT_FIN
    // → packages/agent-core/src/tools/builtin/file/read.ts#L400
    RT_TAIL --> RT_FIN
    // → packages/agent-core/src/tools/builtin/file/read.ts#L517
    RT_FIN --> RT_MSG
    // → packages/agent-core/src/tools/builtin/file/read.ts#L531
    RT_MSG --"?>"--> RT_STATUS
    // → packages/agent-core/src/tools/builtin/file/read.ts#L552
    RT_STATUS --"[ok]"--> RT_PL
    // → packages/agent-core/src/tools/builtin/file/read.ts#L553
    RT_STATUS --> RT_PB
    // → packages/agent-core/src/tools/builtin/file/read.ts#L554
    RT_PB --"[ok]"--> RT_PBYTES
    // → packages/agent-core/src/tools/builtin/file/read.ts#L555
    RT_PB --"?>"--> RT_EOF
    // → packages/agent-core/src/tools/builtin/file/read.ts#L556
    RT_EOF --"[ok]"--> RT_PEOF
    // → packages/agent-core/src/tools/builtin/file/read.ts#L557
    RT_MSG --> RT_OUT
    // → packages/agent-core/src/tools/builtin/file/read.ts#L535

    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef doc fill:#fff8e1,stroke:#ff6f00,stroke-width:1px
    classDef infra fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px
```

## Structured Data

### Nodes

| ID | Label | Kind |
|----|-------|------|
| RT_SCHEMA | ReadInputSchema · parameters | flow |
| RT_SCHEMA_ERR | schema 校验失败 |  |
| RT_EXEC | ReadTool.execution | flow |
| RT_ENOENT | file does not exist |  |
| RT_NOTFILE | is not a file |  |
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
| RT_SCHEMA | RT_EXEC | [ok] | depends_on |  | 1 anchor(s) |
| RT_SCHEMA | RT_SCHEMA_ERR | [err] | depends_on |  | 1 anchor(s) |
| RT_EXEC | RT_ENOENT | [err] | depends_on |  | 1 anchor(s) |
| RT_EXEC | RT_NOTFILE | [err] | depends_on |  | 1 anchor(s) |
| RT_EXEC | RT_ROUTE | -> | depends_on |  | 1 anchor(s) |
| RT_ROUTE | RT_TAIL | [ok] | condition |  | 1 anchor(s) |
| RT_ROUTE | RT_FWD | -> | condition |  | 1 anchor(s) |
| RT_FWD | RT_SCAN | ::yields | yields |  | 1 anchor(s) |
| RT_SCAN | RT_COLLECT | -> | depends_on |  | 1 anchor(s) |
| RT_COLLECT | RT_LCAP | ?> | condition |  | 1 anchor(s) |
| RT_LCAP | RT_ML | [ok] | depends_on |  | 1 anchor(s) |
| RT_COLLECT | RT_RENDER | -> | depends_on |  | 1 anchor(s) |
| RT_RENDER | RT_BCAP | ?> | condition |  | 1 anchor(s) |
| RT_BCAP | RT_MB | [ok] | depends_on |  | 1 anchor(s) |
| RT_ML | RT_FIN | ::merges | merges |  | 1 anchor(s) |
| RT_MB | RT_FIN | ::merges | merges |  | 1 anchor(s) |
| RT_TAIL | RT_FIN | -> | depends_on |  | 1 anchor(s) |
| RT_FIN | RT_MSG | -> | depends_on |  | 1 anchor(s) |
| RT_MSG | RT_STATUS | ?> | condition |  | 1 anchor(s) |
| RT_STATUS | RT_PL | [ok] | depends_on |  | 1 anchor(s) |
| RT_STATUS | RT_PB | -> | depends_on |  | 1 anchor(s) |
| RT_PB | RT_PBYTES | [ok] | depends_on |  | 1 anchor(s) |
| RT_PB | RT_EOF | ?> | condition |  | 1 anchor(s) |
| RT_EOF | RT_PEOF | [ok] | depends_on |  | 1 anchor(s) |
| RT_MSG | RT_OUT | -> | depends_on |  | 1 anchor(s) |

## Notes

| 常量 | 值 | 锚 |
|------|-----|-----|
| MAX_LINES | 1000 | read.ts#L16 |
| MAX_BYTES | 102400 (100 KiB) | read.ts#L18 |
| MAX_LINE_LENGTH | 2000 | read.ts#L17 |
schema 运行时校验在 loop/tool-call.ts validateExecutableToolArgs（本图不展开）。media/unknown/decode/nul 同 isError，折叠进侧链说明、不另开节点。RT_ROUTE→RT_FWD 为 else readForward，非失败。


