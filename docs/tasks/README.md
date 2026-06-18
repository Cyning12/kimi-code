# tasks · kimi-code-meta（过程轨）

| 目录 | 用途 |
|------|------|
| `active/` | 进行中业务 task |
| `done/` | 已关账 task |

## 新建上游 PR 类 task

1. 复制 [`TASK_TEMPLATE_upstream_pr_v1.md`](./TASK_TEMPLATE_upstream_pr_v1.md)
2. 填写 **§4 给 10 帽交接物** + 落盘 `invokes/by-task/<slug>/PROMPT_kimi_agent_rethink_*.md`
3. 必读 PILOT §5.2：**触模块必更新图谱**（30 前 skeleton · 关账 partial/终稿）
4. 落盘 `active/task_<slug>_v1.md` → 关账 `git mv` 至 `done/`

**00 vs 10**：交接物由 **task 起草**写入 §4；**00** 链式编排时读本节并 Task 派发 10，不代替 10 思考。

## 关联

- 工作区 PILOT：`Projects/docs/harness/guides/PILOT_kimi_code_fork_adoption_v1_zh.md`
- 图谱：`docs/_tech_graph/`
