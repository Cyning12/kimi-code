# Mermaid 拓扑协议（graph_v2 · kimi-code-meta）

> **编辑源**：`docs/_tech_graph/*.graph.yaml`（flowchart）。  
> **人类版**：`pnpm graph:compile` 生成同名 `.md` · 禁止手改 `.md` 与 YAML 漂移。

---

## 1. 边标记（YAML `edges[].mark`）

### 1.1 执行流

| 标记 | 语义 | 何时用 |
|------|------|--------|
| `->` | 同步顺序执行 | 普通调用 |
| `~>` | 异步 / await | 非阻塞 I/O |
| `=>` | 赋值 / 映射 | 数据转换 |
| `?>` | 条件分支 | if / switch / 路由 |

### 1.2 状态与可靠性

| 标记 | 语义 | 示例 label |
|------|------|------------|
| `[ok]` | 成功路径 | `validate → save` |
| `[err]` | 失败 / 异常 | `parse → fallback` |
| `[retry=N]` | 重试 | `call_api` |
| `[timeout]` | 超时降级 | `fetch → cache_get` |

### 1.3 元关系（`::` 命名空间）

| 标记 | 语义 |
|------|------|
| `::yields` | 流式 / 生成器产出 |
| `::triggers` | 触发子流程或后台任务 |
| `::gates` | 门禁 / 鉴权 / 依赖注入 |
| `::branches` | 并行分支 |
| `::merges` | 多路归并 |
| `::signoff` | 持久化确认 / 事务提交 |
| `::archives` | 日志 / 审计归档 |

---

## 2. 节点形状（flowchart · compile 到 `.md`）

| 形状 | 含义 | 示例 |
|------|------|------|
| `[[...]]` | 阶段 / 流程块 | `[[Query Phase]]` |
| `[...]` | 函数 / 操作 | `[process_request]` |
| `[(...)]` | 数据 / 模型 | `[(UserRecord)]` |
| `{...}` | 判断 / 路由 | `{authorized?}` |
| `>...]` | 里程碑 / 文档指针 | `>10_flow_*.md]` |
| `((...))` | 循环 / 归档 | `((write_log))` |

---

## 3. 锚点（YAML `edges[].anchors`）

每条硬边须可追溯到代码或文档：

```yaml
anchors:
  - path: packages/agent-core/src/agent/permission/index.ts
    line: 42
```

- 跨模块调用：用 `::triggers` 或侧链，不展开对方内部。
- 未知处用 `TBD` 并开 task 补锚点。

---

## 4. 分层与折叠

| 条件 | 操作 |
|------|------|
| 子图节点 ≤ 7 | 可在主图展开 |
| 子图节点 > 7 | 折叠为阶段块，链独立 `10_flow_*.graph.yaml` |
| 异常分支 | 挂侧链；Happy Path 走主干 |

---

## 5. 禁止项

- 禁止虚构文件路径。
- 禁止 onboarding 默认「全仓扫描生图」。
- 禁止手改 compile 产物 `.md`（改 YAML 后重跑 `graph:compile`）。

---

## 6. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-06-18 | graph_v2：退役 `.ai.md` 双轨 · YAML 单源 |
