# docs/harness（个人 fork · 过程轨）

**勿 PR 到 Moonshot 上游**。

| 项 | 内容 |
|----|------|
| **纪律层 / CLI** | [`spec-wave`](https://github.com/Cyning12/SpecWave)（现行包；曾用名 `@cyning/harness` → `dsh-coding-kit`） |
| **仓内落盘** | `.coding-kit/`（manifest / host-tools / invoke_index）；`.cyning-harness/` 为 legacy 只读，勿当新标准 |
| **常用命令** | `npx spec-wave check` · `npx spec-wave verify --task <path>` · `npx spec-wave upgrade --yes` |
| **迁移说明** | 产品仓 [`MIGRATION.md`](https://github.com/Cyning12/SpecWave/blob/main/MIGRATION.md) |

工作区真值：[`POINTER_PILOT_adoption_workspace_v1_zh.md`](./POINTER_PILOT_adoption_workspace_v1_zh.md)
