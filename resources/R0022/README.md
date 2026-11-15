# Harness engineering: leveraging Codex in an agent-first world

[← 全部内容](../README.md) · [发布来源](../../sources/S0018.md) · [作者](../../authors/A0014.md)

- 内容编号：R0022
- 原链接：https://openai.com/index/harness-engineering/
- 发布来源：[OpenAI / Index（S0018）](../../sources/S0018.md)
- 作者：[Ryan Lopopolo（A0014）](../../authors/A0014.md)
- 作者背景：用户提供姓名和 X；正文 Author 段署名一致，文章以团队成员视角叙述 OpenAI 内部实践；正式头衔与账号关联未独立核验
- 平台：独立网站 / OpenAI 官网
- 形式：文章 / 工程实践复盘
- 原文发布日期：2026-02-11
- 日期依据：用户明确提供 February 11, 2026；粘贴正文没有日期页头，本轮未远程核验
- 收录日期：2026-11-15
- 整理日期：2026-11-15
- 内容处理：已有正文与 AI 摘要
- 正文语言：英语
- 我的阅读：未记录
- 留存理由：未记录

## 阅读前：作者是谁

正文 Author 段署名 Ryan Lopopolo，Acknowledgements 另列参与文章的 Victor Zhu 与 Zach Brock；致谢不自动视作共同署名。作者叙述团队构建 OpenAI 内部产品的经历，正式职位和职责范围未独立核验，详见[作者档案](../../authors/A0014.md)。

## 正文

[阅读用户提供的正文](正文.md)。保留原有起止标记、正文及页尾推荐链接；推荐链接不自动计入收藏。本轮未联网补图或核验原页。

## 一句话说明

让 Agent 可靠交付的关键投入，是把项目知识、运行环境、架构约束与持续反馈做成它能读取、执行和检验的工程系统。

## AI 摘要与要点

作者复盘从空仓库构建内部 beta 产品的实验：约束团队不手写代码，转而由人确定目标、提供环境与反馈，让 Codex 完成实现。经验核心不在代码生成量，而在消除 Agent 看不见事实、无法运行应用、缺少约束和持续复制坏模式的障碍。

| 关注点 | 文中做法 | 阅读价值 |
|---|---|---|
| 工程师职责 | 失败时追问缺了什么能力，再补工具、抽象、文档和约束 | 从单次提示词转向可复用的工程改进 |
| 应用可观察性 | 每个 worktree 可启动独立应用，通过 CDP 操作 UI，并查询隔离的日志、指标和 traces | Agent 能验证行为及性能目标，减少人工逐项检查 |
| 仓库知识 | 约百行 AGENTS.md 充当目录，docs 保存规格、设计、执行计划、债务与参考 | 用渐进披露连接权威信息，不把所有规则塞进常驻上下文 |
| 知识维护 | lint 与 CI 检查链接、结构和更新，周期性 doc-gardening 生成修订 PR | 文档导航需要随代码维护，不能只创建一次 |
| 架构约束 | 固定业务分层和依赖方向，以自定义 lint、结构测试强制执行；错误消息带修复提示 | 集中约束边界，在边界内保留实现自由 |
| 审查与合并 | 本地自检加其他 Agent 审查，较少阻塞门禁，短生命周期 PR，部分问题后续修正 | 取舍依赖反馈和修正成本，不能直接套给所有项目 |
| 持续清理 | 将人对质量的判断编码成 golden principles，后台任务小步修正漂移与技术债 | 避免低质量模式被 Agent 反复复制放大 |

### 渐进阅读建议

先读 Increasing application legibility，再读 We made repository knowledge the system of record 和 Enforcing architecture and taste：分别回答“怎样看见运行结果”“怎样找到可信知识”“怎样把边界变成检查”。最后读 Entropy and garbage collection，思考已有模式如何持续维护。

## 标签与相关问题

**标签**：[按需上下文](../../tags/按需上下文.md) · [知识沉淀](../../tags/知识沉淀.md) · [架构约束](../../tags/架构约束.md) · [外部验证](../../tags/外部验证.md) · [自动化闭环](../../tags/自动化闭环.md)

- [项目资料如何按需读取？](../../problems/项目资料如何按需读取.md)：AGENTS.md 作目录、docs 作权威知识、机械检查漂移。
- [哪些约束该下沉到工具？](../../problems/提示词约束何时下沉.md)：架构依赖、边界解析与带修复提示的 lint。
- [怎样建立可信自动化闭环？](../../problems/可信自动化闭环怎么建.md)：先准备可运行环境、可观察结果和恢复能力，再扩展自治。
- [AI 生成的代码和文档怎样持续清理，避免坏模式扩散？](../../problems/AI生成代码如何持续清理.md)：golden principles、质量评分和小步修订。

## 接下来读哪篇

- [R0021：TAB 大仓 Harness 实战](../R0021/README.md)：对照半自动关卡、基线和角色边界。两篇对人审和阻断的选择不同，不能归纳成唯一模式。
- [R0016：pstack](../R0016/README.md)：补项目验证技能、Feature Map 和维护流程的文件入口；本库未执行该插件。
- [R0015：mattpocock/skills](../R0015/README.md)：对照面向 Agent 的文档指针与单一事实来源。
- [R0012：AI-native SDLC playbook](../R0012/README.md)：从六阶段产物、治理和结果指标补充本文的系统投入视角。

## 回正文定位

| 想找什么 | 章节或短语 |
|---|---|
| 从手写代码转向环境与反馈设计 | Redefining the role of the engineer |
| UI、日志、指标与 traces 供 Agent 验证 | Increasing application legibility |
| 精简 AGENTS.md、知识目录与文档维护 | We made repository knowledge the system of record |
| 可发现知识与依赖选择 | Agent legibility is the goal |
| 分层边界、结构测试和 lint 修复指引 | Enforcing architecture and taste |
| 少阻塞门禁与快速修正的前提 | Throughput changes the merge philosophy |
| 端到端自治的条件与升级 | Increasing levels of autonomy |
| 坏模式复制与周期性清理 | Entropy and garbage collection |
| 多年架构演化仍未知 | What we’re still learning |

## 适用边界与查漏补缺

- 百万行包含应用、基础设施、工具与文档；约 1,500 PR、每人每天 3.5 PR、零手写代码均为作者实验陈述，本库没有仓库、样本或独立测量。代码量和 PR 数不等于质量。
- 约十分之一人工开发耗时是团队估计，不是有完整对照数据的普遍效率结论。团队由三人扩大到七人的描述也不足以单独证明因果增益。
- 产品从空仓库起步，已到内部 beta 与外部 alpha 试用阶段；不能直接推广到长期遗留、监管或高风险生产系统。文章明确多年架构一致性尚未知。
- 文中性能时间值是环境支持的目标示例，不是本库测得的产品性能指标。每 worktree 隔离的具体权限、数据、凭据与资源限制实现未提供充分细节。
- “Agent 看不到的知识等于不存在”是在说明可访问性；不代表所有平台都只能读仓库。实际可达来源与权限应按环境确认。
- 文中自行实现部分并发工具是特定依赖与可观察性取舍，同时也主张共享工具优先；不能据此鼓励普遍重写依赖。100% 覆盖率不是无缺陷证明。
- 少阻塞合并门禁和 Agent 间审查依赖高吞吐、便宜修正与充分反馈；文中没有给出所有风险分级、回滚和停止阈值，不能推导为可忽略测试失败或取消人审。
- lint 和 Agent reviewer 本身也要验证；机械约束能够检查已表达的不变量，不保证需求完备、语义正确或没有未覆盖缺陷。
- 周期性清理、自动合并的范围、预算、误报与效果需实际测量；本库未配置定时任务、审查器、浏览器或自动合并，也未执行文章中的命令。

补充：[R0023：直播数据 LLM Wiki 实践](../R0023/README.md) 把知识加工细化为材料分流、Schema、关系图、检索与增量更新；可对照本文目录和持续维护思想。

## 我的笔记与实践

未记录。AI 摘要不代表用户已读或实践。
