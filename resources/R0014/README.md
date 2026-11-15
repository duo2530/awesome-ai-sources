# KiroCrew

[← 全部内容](../README.md) · [GitHub 来源](../../sources/S0010.md) · [背景文章](../R0013/README.md)

- 内容编号：R0014
- 原链接：https://github.com/kirodotdev/KiroCrew
- 发布来源：[GitHub / kirodotdev（S0010）](../../sources/S0010.md)
- 平台：GitHub
- 形式：代码仓库
- 仓库所有者：kirodotdev（GitHub API 标为组织）
- 作者与维护者：见下方固定版本的维护者名单，不以所有者账号代替个人作者
- 原文发布日期：不适用（代码仓库）
- 日期依据：GitHub 仓库元数据；创建日期、commit 日期与资料阅读日期分开
- 仓库创建时间：2026-07-16 21:21:54 UTC（GitHub created_at；不是本地时区日期）
- 首次版本发布日期：未核验，不以创建时间或 README 中版本示例替代
- 收录日期：2026-11-15
- 内容处理：已读 README、文档索引、维护者与许可证；未读业务源码、未运行
- 我的阅读：未记录
- 留存理由：作为已收录 Kiro Crew 文章对应的代码仓库，继续关注具体实现入口；未记录个人采用决定

## 一眼了解

按项目 README 的描述，Kiro Crew 是运行在用户本地或远程硬件上的持久开发工作空间，提供桌面、Web、CLI 和消息入口。它把会话、记忆、计划任务、应用扩展与执行可见性组织到 Gateway，目标是让工作跨会话持续推进。

适合本库继续研究的问题是：多会话如何保存与恢复状态、记忆如何限制作用范围、定时或事件工作如何组织，以及权限和审计的边界如何落实。这里是文档阅读后的用途归纳，不是源码验证或运行效果结论。

## 阅读依据

- 最近阅读日期：2026-11-15
- 分支：main（本次查询时的默认分支）
- 固定 commit：[`ced9489e96a142877514ae0fd4820038bc9c52c7`](https://github.com/kirodotdev/KiroCrew/commit/ced9489e96a142877514ae0fd4820038bc9c52c7)
- 此 commit 的提交时间：2026-11-15 03:50:32 UTC（GitHub commit metadata）
- 已读取：GitHub 仓库元数据、根目录列表、README 功能与使用说明、docs/README.md、MAINTAINERS.md、LICENSE。
- 未深入读取：README 末尾贡献者头像墙、架构详述、业务源码、测试实现、安装指南正文、发布历史、最新 release 与各安全控制的实现。
- 方法：通过 GitHub 连接工具只读获取上述内容；没有克隆或保存一份上游代码副本。

## 维护者与文章作者

固定版本 [MAINTAINERS.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/MAINTAINERS.md) 列出：

| 维护者 | GitHub | 本库关联 |
|---|---|---|
| Bolin Chen | [@bolichen97](https://github.com/bolichen97) | [已有作者档案](../../authors/A0009.md) |
| Joe Guo | [@iamwhatever](https://github.com/iamwhatever) | [文章署名 Zhejiang (Joe) Guo](../../authors/A0008.md) |
| Ray Xu | [@buluoray](https://github.com/buluoray) | 目前仅记录仓库列名，未额外核验个人背景 |
| Zezhen Xu | [@CrysisDeu](https://github.com/CrysisDeu) | [已有作者档案](../../authors/A0010.md) |

这是该版本列出的维护者，不是完整作者名单或全部贡献者。名单会随仓库变化，不能将它永久视为当前状态。

## 值得看哪些地方

以下入口全部固定到本次 commit。“推荐后续阅读”表示路径由已读 README / 文档索引引出，尚未阅读目标正文。

| 路径 | 为什么值得看 | 本轮阅读情况 |
|---|---|---|
| [README.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/README.md) | 功能定位、Gateway 与运行入口、各平台起步要求 | 已读功能与使用说明，未审贡献者头像墙 |
| [docs/README.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/docs/README.md) | 区分贡献者文档、用户文档、架构、规范和决策入口 | 已读 |
| [MAINTAINERS.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/MAINTAINERS.md) | 谁对合入与设计决定负责 | 已读 |
| [LICENSE](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/LICENSE) | 项目许可证 | 已读，Apache-2.0 |
| [docs/architecture/overview.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/docs/architecture/overview.md) | 继续看组件边界 | 推荐后续阅读，README 链接 |
| [docs/system-specs/modules/session.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/docs/system-specs/modules/session.md) | 继续研究会话生命周期与隔离 | 推荐后续阅读，README 链接 |
| [docs/system-specs/modules/memory-skills-hooks.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/docs/system-specs/modules/memory-skills-hooks.md) | 继续研究记忆、技能与 hooks | 推荐后续阅读，README 链接 |
| [docs/system-specs/modules/security.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/docs/system-specs/modules/security.md) | 继续研究权限边界的正式说明 | 推荐后续阅读，README 链接 |
| [docs/guides/install.md](https://github.com/kirodotdev/KiroCrew/blob/ced9489e96a142877514ae0fd4820038bc9c52c7/docs/guides/install.md) | 按实际环境选择安装方式 | 推荐后续阅读，未执行 |

## 标签与相关问题

**标签**：[多 Agent 协作](../../tags/多Agent协作.md) · [自动化闭环](../../tags/自动化闭环.md) · [知识沉淀](../../tags/知识沉淀.md) · [运行时治理](../../tags/运行时治理.md)

- [并行会话太多，怎样协调？](../../problems/并行会话太多如何协调.md)
- [怎样建立有停止条件和证据的自动化闭环？](../../problems/可信自动化闭环怎么建.md)

## 适用条件与限制

- README 提供桌面、安装包、容器和源码等使用路径。其源码构建说明列出 Python 3.12+、Node.js 22.12+ 等要求；Windows 单独走对应指南。本库未验证机器兼容性或依赖完整性。
- README 说明默认 agent 走需另行安装并登录的 kiro-cli，其他 harness 有各自前提；不能把工作空间安装成功等同于模型或所有后端可用。
- 固定版本 LICENSE 为 Apache License 2.0；其他组件或服务的使用条件应按各自依据查看，本轮未逐项审第三方依赖。
- 持久化、自学习、隔离、权限、沙箱和遥测等均有文档说明，但本轮没有核对实现或实际运行，不以文档用词保证效果。
- GitHub 查询时未标记 archived，只能说明当时的仓库元数据，不代表稳定、成熟或维护承诺。
- 本次阅读基于 main commit，不将它当成已发布稳定版本；首次 release 与当前稳定版未核验。

## 更新关注

未配置抓取或定时任务。以后重点看会话、记忆、调度、权限边界和版本升级的实际变化；重读时记录新 commit，与此记录比较，而不把旧结论自动套给新版本。

## 关联阅读

- [R0013：Kiro Crew 一周合并 1,000 PR 的文章](../R0013/README.md)：理解作者提出的阶段与协调瓶颈，再按仓库文档入口查实现；文章中的产出数字不由这次仓库阅读独立证明。
- [R0005：Loops You Can Trust](../R0005/README.md)：对照证据和停止条件，帮助之后检视自动化行为是否可信。

补充：[R0018：LoopForge](../R0018/README.md) 以聊天与 SOP 组织团队交付，可对照会话、调度和人工确认的边界；均未在本库运行。

## 我的笔记与实践

未记录。没有克隆、安装、执行、部署或验证实际任务，也未创建空正文文件。
