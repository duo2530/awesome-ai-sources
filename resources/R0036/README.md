# Building always-on agents

[← 全部内容](../README.md) · [Claude 资源文章来源](../../sources/S0008.md) · [作者署名](../../authors/A0024.md)

- 内容编号：R0036
- 原链接：https://claude.com/resources/articles/building-always-on-agents
- 发布来源：[Claude / Resources Articles（S0008）](../../sources/S0008.md)
- 作者：[William Hu（A0024）](../../authors/A0024.md)
- 作者背景：[William Hu（A0024）](../../authors/A0024.md)；仅记录署名，头衔、雇主与经历未核验
- 平台：独立网站
- 形式：文章 / 工程指南（含 7 幅外链图，其中 3 幅动画）
- 原文发布日期：2026-11-13
- 日期依据：正文剪藏 frontmatter `published: 2026-11-13`；正文致谢写明 “Written by William Hu”；原页发布日期页头未单独核验
- 收录日期：2026-11-16
- 整理日期：2026-11-17
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：把“常驻 Agent”拆成可实现的五个原语与一个 run/session 循环，可与 loopx、orbi 的控制面及权限治理对照

## 正文与保存依据

[阅读正文](正文.md)。正文由用户粘贴（2026-11-17），保留剪藏 frontmatter（title、source、author、published、created、description、tags）与英文原文；本库只补模板外壳与起止标记，未改写、未翻译、未重排。

- 正文含 7 幅 `assets.claude.com` 外链图，其中 3 幅是动画（run 时间线、上下文增长、五原语拼接），本库未下载到 `assets/`；动画的完整含义只能依据图注判断。
- 正文链接到 Anthropic 的研究文章、Claude 平台文档、Claude Code 文档、MCP Apps 等，本库均未打开核验。
- 文末致谢：`Written by William Hu. Special thanks to Rodrigo Olivares and Michael Segner for their contributions.`；用户此前核验过原页署名 William Hu，与本条一致。

## 一句话说明

把 always-on agent 拆成事件收件箱、定时器、记忆、权限与发件箱五个原语，用 run/session 循环串起来，并指出权限是风险最高的一层。

## AI 摘要与要点

文章回答“产品里怎么做一个看起来一直在线、实际大部分时间在睡的 Agent”。它先纠正“always-on 就等于一直推理”的误解，再给出五个原语与它们的连接方式。

**运行循环**

一次 **run**：收到事件 → 开启或恢复 **session**（消息与工具调用的 transcript）→ 跑 agent loop → 把结果写回持久状态 → 回到睡眠。循环可以无限继续，这就是“一直在线”的来源。

**五个原语**

| 原语 | 职责 | 关键设计 | 本库判断与注意点 |
|---|---|---|---|
| Event inbox | 接收 webhook、定时任务、后台任务等事件 | 持久事件表 + handler + worker；记录状态、按来源 ID 去重；每用户一个 inbox 起步 | 让“事件直接调用 Agent”的并发与丢失问题有解；文中给了四条最佳实践 |
| Timers | 让 Agent 主动行动 | follow-up（自己设的截止时间）与 schedule（重复任务）分开存；scheduler 轮询到期项并投递事件 | 定时器不自己启动 run，而是转成 inbox 事件；这个分层避免两套触发逻辑 |
| Memory | 跨 run 保持连续性 | 用户指令、用户笔记、已发消息、任务进度四类；只存“查不回来的”，其余存指针；启动时只加载索引 | 与 R0035 的四层记忆互为补充：这篇讲运行时该存哪几类文件，那篇讲记忆如何整理与注入 |
| Permissions | 无人值守时决定放行、阻断或等待 | 凭据代理（Agent 不持有密钥）、auto mode 分类器、deferred tool call（保存 session 后等用户回复，回复作为事件恢复） | 文章明确说这是风险最高的一层；分类器误判与等待期间的状态一致性都未展开 |
| Outbox | 把结果送到用户 | send 工具即可起步；需要节流或错误恢复时再加 outbox 表与 dispatcher | 建议先安静、再逐步争取用户注意力；用评测找频率，而不是拍数字 |

**上下文与成本**

- 每次 run 的固定开销来自系统提示、工具定义与记忆文件；作者建议保持精简并用 prompt caching 降成本。
- 新 session 只带固定开销与触发事件；旧 session 会带回整段 transcript，过长时 compaction 或新开 session，两者都会丢细节，所以该持久的内容要随时写进 memory。
- 成本趋势：长时程编码基准上，Opus 5.5 每解决一个任务比 Opus 5 便宜 78%，典型工作负载便宜 40%。这是厂商自述的成本曲线，不是用户项目实测。

**拼起来**

事件从 inbox 进入 → worker 启动 run → Agent 读 memory、在 permissions 内行动 → 写回 memory → 结果进 outbox → dispatcher 送达；run 可以设 timer 稍后再醒，用户回复又变成 inbox 事件。

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| always-on 实际大部分时间在睡，按 run 工作 | 作者陈述（定义） | “The cycle behind the always-on agent” 与 Figure 1 图注 | 定义清楚；没有给单 run 的时长或唤醒频率经验值 |
| 五个原语：inbox、timers、memory、permissions、outbox | 作者陈述（架构） | “The core primitives” 与各小节标题 | 是面向产品的参考架构，不是唯一实现；文中未给完整参考代码 |
| 事件应先进 inbox，而不是直接调用 Agent | 作者主张 | “Event inbox” 首段列举同时到达与崩溃丢失 | 合理；文中未给 inbox 吞吐或延迟数据 |
| inbox 的四条最佳实践 | 作者主张 | “Event inbox” 末尾列表 | 可直接借用；其中“单 worker”与批量合并会影响延迟，需按产品权衡 |
| timers 与 inbox 分表存放 | 作者主张 | “Timers” 段 | 好处是 inbox 只放待处理事件；文中未讨论时钟漂移或重复投递 |
| memory 只存查不回来的内容，其余存指针 | 作者主张 | “Memory” 段 | 与 R0035 的层级一致；指针失效与权限未讨论 |
| 上下文固定开销应保持精简并用 prompt caching | 作者主张 | “Inside the context window” | 属工程建议；节省幅度未量化 |
| 权限是 always-on agent 风险最高的一层 | 作者陈述（风险判断） | “Permissions” 首段 | 与 R0028、R0029、R0031 的人工门方向一致；分类器误判率未给 |
| deferred tool call 保存 session 后等用户回复，回复作为事件恢复 | 作者陈述（机制） | “Permissions” 的 Deferred tool calls | 是“停下来等人”的具体实现；等待期的隔离、超时与取消未展开 |
| outbox 适合节流与错误恢复，起步可用 send 工具 | 作者主张 | “Outbox” 段 | 与“先安静”的建议配套；消息频率的评测方法只说“build evals” |
| Opus 5.5 在长时程编码任务上每任务成本低 78% | 厂商自述 | 开头 “78% less per solved task” | 基准与口径未给；不能当用户项目成本预测 |
| 用户回复与 timer 都能重新唤醒 Agent | 作者陈述（架构） | “How everything fits together” | 是循环闭合的关键；未讨论事件风暴下的背压 |

## 标签与相关问题

**标签**：[架构约束](../../tags/架构约束.md) · [运行时治理](../../tags/运行时治理.md) · [自动化闭环](../../tags/自动化闭环.md)

- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：五个原语补上“谁触发、何时停、结果怎么送达”的产品侧结构。
- [项目资料太多，怎样让 Agent 按需读取？](../../problems/项目资料如何按需读取.md)：memory 的索引注入与按需读取，是“常驻 Agent 也要控制上下文”的实现。

## 接下来读哪篇

- [R0035：The components of agent memory](../R0035/README.md)：同源文章，讲记忆内部结构与 dreaming；本篇只把 memory 当作原语。
- [R0028：loopx](../R0028/README.md)：把目标、证据、配额与租约做成控制面，可与五个原语对照“控制面 vs 产品结构”。
- [R0026：dsh-superagent-prototype](../R0026/README.md)：事件、授权任务、执行与恢复的文档流程，补本篇没写的权限与恢复细节。
- [R0029：orbi](../R0029/README.md)：以 Issue 为状态、独立评审与失败即停，是另一种“常驻交付”的取舍。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 运行循环 | `The cycle behind the always-on agent`；`run`；`session` |
| 五个原语 | `The core primitives` |
| 事件收件箱 | `Event inbox`；`handler`；`worker`；`deduplicated` |
| 定时器 | `Timers`；`follow-up`；`schedule`；`scheduler` |
| 记忆 | `Memory`；`User instructions`；`Task progress` |
| 上下文开销 | `Inside the context window`；`prompt caching`；`compaction` |
| 权限 | `Permissions`；`Credential store`；`Auto mode`；`Deferred tool calls` |
| 发件箱 | `Outbox`；`dispatcher`；`send` |
| 拼装 | `How everything fits together` |
| 成本 | `78% less per solved task` |

## 适用边界与查漏补缺

- **参考架构，不是实现**：五个原语是产品侧的设计建议，文中没有参考代码、吞吐、延迟或故障率；照抄前要先确认自己的事件量、延迟要求与权限模型。
- **成本数字是厂商自述**：78% 与 40% 来自官方基准，未给任务集与统计方式；不能直接换算成用户项目的单任务成本。
- **权限只给了方向**：凭据代理、分类器与 deferred call 都会影响可用性；误判、超时、取消与审计的细节没有展开。
- **与 R0035 同源**：两篇都来自 Anthropic 的 agent memory 叙事，memory 部分互相引用；不能把它们当成两份独立证据。
- 未核验：7 幅图、Claude 平台与 Claude Code 文档、MCP Apps、Anthropic 的研究文章。
- 本库未在用户项目中实现这套结构，也没有事件量、唤醒频率或人工介入数据。

## 对已有知识的影响

- “可信自动化闭环”问题页得到一份产品侧结构：此前材料多讲控制面（R0028）、Issue 流水线（R0029）或评审门（R0031），本篇补上事件收件箱、定时器、记忆、权限与发件箱如何拼成循环。
- 与 R0035 形成“记忆内部结构 vs 运行时原语”的互补；两篇同源，不构成独立核验。
- 在“项目资料如何按需读取”补一条：常驻 Agent 的 memory 也要靠索引注入控制上下文。
- 未修改任何现有结论；本篇未改变 R0028、R0029 的适用判断。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
