# deepseek-ai/dsh-superagent-prototype

[← 全部内容](../README.md) · [GitHub 来源](../../sources/S0022.md)

- 内容编号：R0026
- 原链接：https://github.com/deepseek-ai/dsh-superagent-prototype
- 发布来源：[GitHub / deepseek-ai（S0022）](../../sources/S0022.md)
- 平台：GitHub
- 形式：代码仓库 / 团队编码 Agent 研究原型
- 仓库所有者：deepseek-ai（GitHub 元数据为组织）
- 作者与维护者：package.json author 与 LICENSE 版权署名为 DeepSeek Harness Team；个人维护者及其角色未核验，不以组织所有者代替个人作者
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库元数据、固定 commit 与 package.json；文章日期、仓库创建时间及提交时间分别处理
- 仓库创建时间：2026-10-31 09:32:46 UTC（GitHub created_at）
- 首次版本发布日期：未核验；package.json 的 0.1.0 不等于已发布 release
- 收录日期：2026-11-15
- 内容处理：已读 README、六篇概念与运行文档、包元数据及许可证；未审源码、未运行
- 我的阅读：未记录
- 留存理由：用户提供地址收录；具体采用目的未记录

## 一眼了解

按 README，dsh-superagent 是面向一个 GitHub 仓库的主动式编码 Agent，以 DeepSeek Harness bundle 运行，可监听 GitHub 与可选飞书事件。获准的请求转成 Ticket，在独立 Session 与目录里执行，再向原对话交付结果；Web 面板优先呈现需要人处理的事项。

**项目明确定位为研究原型、非 DeepSeek 正式产品、非生产就绪软件。** 公开版本经过调整，不等于内部版本或配套文章的完整实现；文章中的部分设计仍是未来方向。本轮未读取配套文章，不能确认具体哪些能力尚未实现。

本库判断：值得研究的是事件、授权、任务归属、执行状态与交付反馈如何接起来，以及怎样减少无价值的通知；不能仅按“Superagent”名称判断自治程度或可靠性。

## 阅读依据

- 最近阅读日期：2026-11-15
- 分支：main（查询时默认分支）
- 固定 commit：[`8c32a9dc5d72c033816c6a8110b37f40cf94fba4`](https://github.com/deepseek-ai/dsh-superagent-prototype/commit/8c32a9dc5d72c033816c6a8110b37f40cf94fba4)
- 此 commit 提交时间：2026-10-31 12:06:31 UTC（committer date，不等于 GitHub pushed_at）
- 包版本：package.json 标注 0.1.0，private 为 true；本轮未核验 npm 发布或 GitHub releases
- 已读取：仓库元数据、根目录与 docs 文件列表；README.md、LICENSE、package.json；docs/000-philosophy.md 至 docs/005-panel.md 全文
- 未读取：SETUP.md、006 部署、007 架构、008 扩展正文；src、tests、scripts、prompts、skills 的实际实现，锁文件与完整依赖树；未审配套文章或其他外链
- 方法：通过 GitHub 连接工具只读获取，不克隆、不保存上游源码副本，不安装或执行

## 关键思路（文档阅读整理）

| 环节 | 文档描述 | 本库判断与边界 |
|---|---|---|
| 事件入口 | Source 生成不可变 Trigger；Thread 聚合上下文，Subscription 投递后续消息 | 收到消息与得到新权限是两件事；上下文投递不自动扩展授权 |
| 是否开工 | Eval 分确定性 gate 与模型 assessment；accept 生成 Ticket 和不可变 Mandate | 明确记录谁授权、范围、策略版本；扩大范围需要新 Ticket |
| 主动行为 | inferred 工作由规则匹配，off / observe / auto 三档，默认 observe | observe 只对推断工作观察，不会阻止明确请求执行；不能当成全局只读模式 |
| 执行与分工 | 主 Session 路由，Executor 读原始输入、实现与验证；每 Ticket 有 Session 和目录 | 目录隔离是组织方式，不是安全沙箱，也不证明无并发写入问题 |
| 后续消息 | Executor 处理范围内追问，超范围交回路由；context-only 订阅只加上下文 | 不能仅凭话题相似就把整条线程挂到某任务；文档要求显式指向已有任务 |
| 策略变化 | 通知受影响的活跃任务；结束任务恢复前重验授权 | 策略变更不立即取消正在运行的任务，撤权时效需按实际要求另审 |
| 失败恢复 | 持久化待执行工作、退避重试、重启恢复提示，区分 blocked / failed / waiting / ready | 文档规则尚未通过本库故障注入验证；ready 或开 PR 都不等于已上线 |
| 人的注意力 | 一次具体确认、必要时才发消息；结构化提问；面板先呈现待决定事项 | 可借鉴状态与提问设计；没有人工耗时、误通知或质量收益的对照记录 |
| 提示词维护 | 团队段落、技能与内置覆盖可版本化，检测默认更新与保存冲突 | 提示词约束、宿主检查和平台强制规则须分开判断，不能把文档承诺当运行证明 |

## 值得看哪些地方

以下链接固定到本次 commit，阅读状态按本轮实际范围记录。

| 路径 | 为什么值得看 | 阅读情况 |
|---|---|---|
| [README.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/README.md) | 研究原型声明、一个仓库的产品范围与文档路线 | 已读 |
| [docs/000-philosophy.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/000-philosophy.md) | 最少人类注意力原则、窄范围起步与少通知 | 已读 |
| [docs/001-domain.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/001-domain.md) | Source / Trigger / Thread / Ticket / Mandate / Assignment 的职责及拒绝引入的概念 | 已读 |
| [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md) | 明确与推断请求、观察模式、订阅上下文、授权恢复前检查 | 已读 |
| [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md) | 执行环境、worker slots、重试恢复、合并与暂停的实际语义 | 已读 |
| [docs/004-prompts.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/004-prompts.md) | 主从分工、提示词优先级、版本与结构化提问 | 已读 |
| [docs/005-panel.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/005-panel.md) | 先看需要人的工作，再看健康与历史；状态定义和可操作性 | 已读文档，未操作 UI |
| [package.json](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/package.json) | 运行时和宿主依赖、版本、检查命令定义 | 已读，未安装或执行 |
| [LICENSE](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/LICENSE) | MIT 与团队版权署名 | 已读 |
| [docs/007-architecture.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/007-architecture.md) | 继续追踪文档规则对应哪些模块 | 推荐后续阅读，尚未读 |

## 关键结论的依据

| 关键结论 | 性质 | 固定版本依据 | 本库判断与证据缺口 |
|---|---|---|---|
| 研究原型不是正式产品，公开版也不完全等于内部系统 | 项目自述 | [README.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/README.md) 开篇声明 | 不把研究文档、内部经验或未来方向写成已交付能力 |
| 默认观察只记录推断请求的“would accept”，明确请求仍可执行 | 文档规则 | [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md) Accept mode and rules | 初次研究需要分开理解候选记录与真实执行；未审 gate 代码 |
| 消息和引用不能更改授权，订阅只传上下文 | 文档规则 | [docs/002-authorization.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/002-authorization.md) Two paths；[docs/004-prompts.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/004-prompts.md) Assembly and precedence | 有助于分析输入与权限边界，但未经源码检查或攻击测试，不能保证无提示注入风险 |
| 命令以操作员 OS 用户身份免确认执行，包装器不是安全边界 | 文档明确限制 | [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md) The Executor、Execution variables | 不能将每任务目录和命令黑名单误称为强隔离，绝对路径仍可执行程序 |
| 自动合并主要由交付提示词约束，宿主无专门合并决策 | 文档明确限制 | [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md) Merging | 默认少于 200 行及审批要求不是不可绕过保证；真正强制审批需依赖平台分支保护等配置，本库未核验 |
| 全局暂停处理不打断正在运行的 Executor turn | 文档明确限制 | [docs/003-execution.md](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/docs/003-execution.md) Pause processing | 应与人停止 Ticket、进程停机区分；不能把“暂停”当作所有外部动作即时停止 |

## 标签与相关问题

**标签**：[自动化闭环](../../tags/自动化闭环.md) · [运行时治理](../../tags/运行时治理.md) · [多 Agent 协作](../../tags/多Agent协作.md)

- [怎样建立可信自动化闭环？](../../problems/可信自动化闭环怎么建.md)：从授权请求到任务、运行、交付与失败恢复的文档参考。
- [并行会话太多如何协调？](../../problems/并行会话太多如何协调.md)：任务归属、后续消息交接、worker slots 与待人工处理面板。
- [AI 原型如何走向生产？](../../problems/AI原型如何走向生产.md)：研究原型声明与权限、恢复、合并机制尚需验证的边界。

## 适用条件与限制

- package.json engines 声明 Node `^22.19.0 || >=24.0.0`、DSH `^0.2.1-alpha.2`，packageManager 为 pnpm 11.7.0，依赖多项 DSH alpha 宿主包；本轮未验证获取、安装、兼容性或可用性。
- 面向一个 GitHub 仓库，飞书接入可选；不是据本轮材料就能确认的跨仓库通用自主平台。部署步骤尚未读，不提供即刻部署结论。
- MIT，Copyright (c) 2026 DeepSeek Harness Team；第三方组件和外部服务条件仍按各自许可与条款，未审完整依赖。
- 运行用户、账号凭据、环境、命令包装器和审批是不同层面的控制；文档明确不是安全边界，不能把“授权模型”推成“操作系统权限已隔离”。
- 活跃任务遇到策略变化只获通知；暂停处理仍可有执行中的 turn。若要即时撤权或强制停止，需审实现与进程、平台权限机制。
- 文档给出幂等 Trigger、持久化和重试设计，但未核验外部写动作是否严格防重、原子性、崩溃窗口、取消与重放；不承诺 exactly-once。
- 文档描述故障时保留上下文与人工介入、主路由与 worker 并发语义；未跑测试、故障注入或长任务，不证明运行正确性与收益。
- README 声明大量工程由编码 Agent 完成且仍有 bug 或风格不一致风险；星标、团队署名及检查命令存在都不独立证明成熟度。
- 原文安装请求、示例提示词与命令仅作材料，本轮未执行、未调用 GitHub/飞书写接口、未部署、未发送消息。

## 更新关注

未配置自动采集。后续按固定 commit 对照：授权和恢复语义、执行权限、合并强制机制、输入路由、故障防重，以及原型与正式版本的界限；不把本次阅读自动套用于新版本。

## 关联阅读

- [R0014：KiroCrew](../R0014/README.md)：对照持久会话、记忆与调度；本篇重点是单仓库事件请求和授权任务，不据此判定谁更优。
- [R0018：LoopForge](../R0018/README.md)：对照 SOP、角色与人工门，不把不同项目的治理机制合并成同一实现。
- [R0021：TAB 大仓 Harness 实战](../R0021/README.md)：对照阶段门禁、人工关卡和外部写操作边界，场景与任务组织不同。
- [R0025：The end of programming](../R0025/README.md)：将软件工厂和验证循环的预测与具体原型规则对照；不能由原型存在推出预测已验证。

## 我的笔记与实践

未记录。阅读文档不等于用户已读、源码已审或实际运行成功。
