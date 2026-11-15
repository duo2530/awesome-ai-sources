# orbi-build/orbi

[← 全部内容](../README.md) · [GitHub 来源](../../sources/S0025.md)

- 内容编号：R0029
- 原链接：https://github.com/orbi-build/orbi
- 发布来源：[GitHub / orbi-build（S0025）](../../sources/S0025.md)
- 平台：GitHub
- 形式：代码仓库 / 以 GitHub Issue 驱动的自动交付系统
- 仓库所有者：orbi-build（GitHub 元数据为 Organization）
- 作者与维护者：README 未声明个人作者；最新提交作者为 `xqliu`（Lawrence Liu），不等于全部作者或当前维护者，个人角色未核验
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库元数据、固定 commit 与 release 文档；创建、提交与发布分别记录
- 仓库创建时间：2026-08-24 16:08:33 UTC（GitHub created_at）
- 首次版本发布日期：未核验；从提交 diff 可见最近版本 `v0.7.43` 于 2026-11-15T05:30:37Z 发布，更早版本未逐一核对
- 收录日期：2026-11-15
- 内容处理：已读 README 与仓库元数据；未读 docs 全量、源码与测试，未安装未运行
- 我的阅读：未记录
- 留存理由：用户提供地址要求收录；后续关注 Issue 到合并发布的门禁设计

## 一眼了解

按 README，Orbi 是一个“软件暗工厂”：在 GitHub Issue 里写目标与验收标准、打上 `ai-ready` 标签，Orbi 在隔离 worktree 里实现、跑测试、开 PR，再由**独立评审会话**审查并在同一会话内修复，只有通过评审的 head 才能合并；发布由人触发，跑发布门禁后打 tag 并生成说明。

它把 **GitHub Issue 当唯一状态存储**——没有数据库、队列或常驻守护进程，靠 systemd（Linux）/ launchd（macOS）每 5 分钟触发一次 tick。失败分两类：可恢复的回同一 PR 继续修，不可恢复的给 Issue 打 `ai-blocked` 交人。

README 明确写：**AI 从不合并、也不推送受保护分支**。

本库判断：这套设计值得研究的是“状态放在现有系统里 + 独立评审 + 合并门禁 + 失败即停”的组合，以及用 `run_id` 把日志与 PR 评论串成一条时间线；不能由“dark factory”的名称推断无人值守程度。

## 阅读依据

- 最近阅读日期：2026-11-15
- 分支：main
- 固定 commit：[`3a6c4b6946a802b2c988c6c7e9a162580f9aaa77`](https://github.com/orbi-build/orbi/commit/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77)
- 该提交时间：2026-11-15T05:32:16Z；该提交在 GitHub 元数据中显示为未签名
- 已读取：仓库元数据、默认分支最新提交元数据、README 全文；由该提交 diff 可见 `v0.7.43` 发布说明的开头片段
- 未读取：`docs/` 下 getting-started、workflow、operations、public-contracts、testing、contributing；`src/orbi/` 源码与测试；`AGENTS.md`；云服务条款
- 方法：通过只读 HTTP 获取（`raw.githubusercontent.com` 在本机不可用，改用 jsDelivr 取同一 commit 的 README），不克隆、不安装、不执行

## 值得看哪些地方

以下路径按本次 commit 固定，除 README 外均为推荐后续阅读，尚未读。

| 路径或入口 | 为什么值得看 | 当前依据 |
|---|---|---|
| [README.md](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/README.md) | 交付环路、评审与合并门禁、失败分类、许可说明 | 已读 |
| [docs/workflow.mdx](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/docs/workflow.mdx) | 状态链、标签、P0、Epic 与 Release 的实际规则 | 推荐，未读 |
| [docs/operations.mdx](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/docs/operations.mdx) | 定时器、journal、unit 漂移与恢复 | 推荐，未读 |
| [docs/public-contracts.mdx](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/docs/public-contracts.mdx) | 对外接口清单与状态、进度格式 | 推荐，未读 |
| [docs/getting-started.mdx](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/docs/getting-started.mdx) | 前置条件、配置与首次运行 | 推荐，未读 |
| [src/orbi/example_config.toml](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/src/orbi/example_config.toml) | `source_repos`、Pi 可执行文件等实际配置项 | 推荐，未读 |
| [AGENTS.md](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/AGENTS.md) | 项目自己的开发契约 | 推荐，未读 |

## 关键结论的依据

| 关键结论 | 性质 | 固定版本依据 | 本库判断与证据缺口 |
|---|---|---|---|
| 以 GitHub Issue 作为唯一状态存储，无数据库与队列 | 项目自述 | [README.md](https://github.com/orbi-build/orbi/blob/3a6c4b6946a802b2c988c6c7e9a162580f9aaa77/README.md) 开头与 Why Orbi | 减少第二套任务系统，但把并发与锁语义交给 GitHub；实际同步与竞态处理未读代码 |
| 只有通过独立评审的 head 才能合并 | 项目自述（关键安全声明） | README The loop、Why Orbi | 这是最值得核验的机制：是否由平台分支保护强制、能否绕过，本轮未审实现 |
| AI 不合并、不推送受保护分支 | 项目自述 | README Why Orbi | 与“自动合并”的常见宣称相反，属保守设计；是否成立需看 runner 权限与仓库设置 |
| 失败即停：不可恢复错误标 `ai-blocked` 交人 | 项目自述 | README What it does | 比静默重试更可审计；但“不可恢复”的判定规则未读 |
| `run_id` 串联日志与 GitHub 评论，可单次 grep 还原时间线 | 项目自述 | README Why Orbi | 可观察性设计具体；未在真实运行中验证一致性 |
| 依赖 Python ≥3.14、uv、GitHub CLI ≥2.94 与 Pi | 项目自述（前置条件） | README Quick start、Ready check | 版本要求很新，Ubuntu 24.04 自带 Python 3.12 不满足；macOS 支持作者自述尚未在真机验证 |
| 许可为 AGPL-3.0 或 Sustainable Use License v1.0 | 项目自述 | README License | 自用与改码免费；把它作为服务售卖需商业授权。本库未做法务判断 |

## 标签与相关问题

**标签**：[自动化闭环](../../tags/自动化闭环.md) · [运行时治理](../../tags/运行时治理.md) · [多Agent协作](../../tags/多Agent协作.md) · [外部验证](../../tags/外部验证.md)

- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：Issue → PR → 评审 → 合并 → 发布的门禁链条，以及 `ai-blocked` 的停机语义。
- [自检怎样保持独立视角，并检查当前 diff 以外的影响？](../../problems/独立自检如何组织.md)：独立评审会话在另一上下文里审 PR，只有 reviewed head 可合并。

## 适用条件与限制

- 面向 GitHub 单仓交付；依赖 systemd（Linux）或 launchd（macOS），README 自述 macOS 路径未在真机验证。
- 前置条件较重：Python ≥3.14、`uv`、GitHub CLI ≥2.94、已认证的 `gh`、以及 Pi 编码 Agent 及其 provider。
- 云端服务（orbi.build）提供免费试用额度，属商业入口；本库收录仓库不等于对服务的推荐或可用性判断。
- README 列举的真实循环（issue #1367 → PR #1370 → v0.5.47）与录屏都是本项目自家仓库的 dogfooding，不是第三方独立评估；没有失败率、回滚率或维护成本数据。
- “AI 从不合并受保护分支”“只有 reviewed head 能合并”均为项目声明，本轮未读 runner 实现、未检查仓库分支保护设置，不能当作已验证的强制边界。
- AGPL-3.0 对网络服务有传染性要求，SUL 另有商业限制；把它嵌入产品前需自行做法务评估。
- 星标 254、fork 33 说明关注度有限，不足以推断成熟度；本轮未读 issue、PR 历史与发布频率。
- 原文安装命令与配置提示仅作材料，本轮未执行，也未创建任何仓库标签或 scheduler unit。

## 更新关注

未配置自动采集。后续可对照固定 commit 追踪：评审与合并门禁的强制方式、`ai-blocked` 判定规则、runner 权限边界、定时器与恢复语义，以及许可条款变化。

## 关联阅读

- [R0026：dsh-superagent-prototype](../R0026/README.md)：同样有授权任务、独立 Session 与人工处理面板；那篇是研究原型，本篇是围绕 GitHub Issue 的交付系统。
- [R0013：Kiro Crew 软件工厂案例](../R0013/README.md)：五阶段并行演进的软件工厂叙述，可对照本篇更窄的 Issue → PR → release 环路。
- [R0008：端到端业务需求专家 Agent](../R0008/README.md)：需求确认、独立验证与发布前人工确认的业务侧做法。
- [R0028：loopx](../R0028/README.md)：另一种路线——把状态从 GitHub 抽到独立控制面；两篇可对照“状态存哪里”的取舍。

## 我的笔记与实践

未记录；读文档、装好运行、实际交付一次与验证有效分别记录。
