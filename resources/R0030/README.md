# Your coding agents made you a manager

[← 全部内容](../README.md) · [X / @addyosmani](../../sources/S0026.md) · [作者档案](../../authors/A0021.md)

- 内容编号：R0030
- 原链接：https://x.com/addyosmani/status/2119332146485891501
- 发布来源：[X / @addyosmani（S0026）](../../sources/S0026.md)
- 作者：[Addy Osmani（A0021）](../../authors/A0021.md)
- 作者背景：[Addy Osmani](../../authors/A0021.md)，依据用户提供的账号与 LinkedIn 主页；公开头衔与雇主未核验
- 平台：X
- 形式：长贴 / 管理实践对照（含 11 个小节与配图）
- 原文发布日期：2026-11-08
- 日期依据：用户提供原帖显示时间“下午3:32 · 2026年11月8日”；只取日期部分，显示时区未标注，不转换为本地时间
- 收录日期：2026-11-15
- 整理日期：2026-11-15
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：把“管理团队”的经验映射到“管理 Agent”，与库内 Harness、验证、约束下沉几条线直接可比

## 正文与保存依据

[阅读正文](正文.md)。正文由用户粘贴，本库只补模板外壳与起止标记，未改写、翻译或重排。

- 正文为 X 长贴全文，含小节标题与两处配图位置；图片是 `pbs.twimg.com` 外链，本轮未下载到 `assets/`，不保证长期可用。
- 文内链接保留原地址：作者两篇博客（coding-agents-manager、cognitive-surrender）、Claude Code best-practices 文档，以及 `claude.md` 与 `@claude` 两处引用。
- 原文提到 Andy Grove《High Output Management》与“Wharton 关于 cognitive surrender 的研究”，前者无链接，后者没有给出处链接，本库均未核验。
- 原帖显示时间为用户提供，未远程打开帖子核验；正文与标题一致，未见截断。

## 一句话说明

把“带团队”的做法搬到“带 Agent”：给验证手段、写清仓库里没有的上下文、同一纠正只犯一次、能用硬门禁才用硬门禁、先计划再并行、两次纠正无效就重开、别把判断也委派出去。

## AI 摘要与要点

全文 11 节，大致按作者认为的影响力排序；每节都是“最佳实践 / 反模式”成对出现，这一点让它可以当检查表用。

| 小节 | 最佳实践 | 反模式 | 本库判断 |
|---|---|---|---|
| Give it a way to check its work | 给 Agent 可判定的验证手段（测试、构建、截图、lint），让它自己发现并修错 | 把“看起来完成了”当确认，等于自己当 Agent 的测试套件 | 本库最有复用价值的一条，与 R0004、R0017 同向；“最高杠杆”是作者判断，无对照数据 |
| Set clear context | 只写 Agent 从仓库里读不到的东西：目标、为什么、约束、不在范围内、完成标准 | 一句话任务 + 期待藏在脑子里；或把代码里能读到的再抄一遍 | 与 R0003、R0022 的按需读取一致；前提是模型真的会去读仓库 |
| Make every correction compound | 同一处纠正出现两次就写进 CLAUDE.md 或沉淀为 skill，并随新模型复查是否还需要 | 每个会话手工纠一遍，或依赖只存在于本机的默契 | 与 R0001 铁律四、R0022 的“每条规则对应一次失败”互相印证 |
| Let it decide, enforce only what can't bend | 默认让 Agent 判断；只有“必须/绝不”的事才上 hooks、deny 规则、托管设置 | 全大写命令、给可选偏好配 hook、沿用旧模型时代的习惯 | 本库认为这是全篇最有决策价值的一节：prompts 是请求，门禁是要求；“过度流程是新的微观管理”是作者判断 |
| Plan before it builds | 先对齐计划、读隐含假设，再按不重叠的切片并行 /batch | 多个 Agent 做重叠任务，下午在解冲突和重复决策 | 与 R0021 的串行简化、R0026 的任务边界同类；“5 个 Agent 不等于 5 倍产出”是经验判断 |
| Steer early, reset fast | 第一分钟就盯，发现偏航立刻 Esc；纠两次不成就换会话重写提示 | 在同一会话里纠第三、第四次 | “两次”是经验阈值，没有测量依据；但比无限重试更可执行 |
| Delegate the task, never the judgment | 产品、安全边界、发不发版由人定；每个 diff 都当作会被叫起来处理 | 测试绿 + 命名像样就批准大 diff——那是「批准」，不是审查 | 作者给了自己踩坑的例子（差点推一个 600 行 diff），属自述轶事但方向清楚 |
| Design the run that doesn't need you | 无人值守前想清五件事：完成定义、自验证、边界、护栏、产出与批准点 | 睡前启动长任务，早上发现它在错误前提上干了一夜 | 五问可直接对照 R0026 的授权与 R0028 的配额/门禁设计 |
| Scale verification, not attention | 按“检查、目标、独立评审”能接管多少来扩张 Agent 数量；同时量质量与吞吐 | 开会话超过自己能审的程度，用 AI 写了多少行当成绩 | 提出“编排税”：超过前几个之后，每多一个都要更多注意力；作者自述日常 4–5 个后台 Agent |
| Decide what not to build | 谁需要、怎么算成功、什么情况下停；限制在制品数量 | “反正便宜”把每个想法都塞进 PR，攒出一个要长期维护的抽屉 | 与 R0021/R0029 的“评审才是稀缺资源”同向 |
| Where the analogy breaks | 承认类比不完美：技能不回流、返工几乎免费、Agent 没有经验只有笔记本、更顺从、只有一种原型、初级工程师仍需人带 | 以为能管 5 个 Agent 就能管 5 个人 | 这是全篇最该被引用的一段，很多转述会把它删掉 |

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| 管理 Agent 用到的技能基本就是管理团队的技能 | 作者主张 | 正文开头，搜索 `The skills for managing agents` | 作者随即限定“management”指“让他人的工作产生好结果”，并说不必去做那种消失进日历的管理者；不能只截前半句 |
| 验证机制是最高杠杆的一条 | 作者判断（章节排序） | 正文 `Give it a way to check its work`，搜索 `guardrails` | 排序是作者经验，没有实验支持；机制本身与 R0004/R0017 一致 |
| Agent 停下是因为“看起来完成了” | 转述官方文档 | 正文引用 [Claude Code best-practices](https://code.claude.com/docs/en/best-practices)，搜索 `agents stop when the work looks done` | 属对产品文档的转述，本轮未打开该文档核对版本与原文 |
| 只写仓库里没有的上下文 | 作者方法 | 正文 `Set clear context`，搜索 `not in the repo` | 依赖“Agent 会主动读代码”这一前提；对不读仓库或弱模型的场景不成立 |
| prompts 是请求，hooks / deny 规则是要求 | 转述产品机制 + 作者判断 | 正文 `Let it decide, enforce only what can't bend`，搜索 `requests that the model can consider` | 机制属产品事实，本轮未核验当前版本行为；“过度流程是新的微观管理”是价值判断 |
| 两次纠正失败就该换会话重写 | 作者经验阈值 | 正文 `Steer early, reset fast`，搜索 `two failed attempts` | 没有数据支持“两次”；可执行，但不同任务复杂度下阈值应不同 |
| 大 diff 绿灯就批准是“批准”而非审查 | 作者自身教训 | 正文 `Delegate the task, never the judgment`，搜索 `code ratification` | 单一轶事（600 行 diff、差点推送），但作者明确自陈踩坑，方向可借鉴 |
| 规模化的关键是“少监控”而不是“多监控” | 作者主张 | 正文 `Scale verification, not attention`，搜索 `orchestration tax` | 与 R0028 的配额/门禁、R0026 的待人工面板同向；缺少注意力成本测量 |
| 用 AI 写的代码占比不是好指标，应同时量返工 | 引用 Grove 的“测量配反向测量” | 正文 `measure with a countermeasure` | 指标方向合理；具体指标（PR 周期、revert 率）的采集成本与口径未讨论 |
| 类比在七处不成立 | 作者自陈限制 | 正文 `Where the analogy breaks`，七条列表 | 这是文中最重要的自我限制，转述时最容易丢；不能据此推断“能管 Agent 就能管人” |

## 标签与相关问题

**标签**：[需求澄清](../../tags/需求澄清.md) · [外部验证](../../tags/外部验证.md) · [架构约束](../../tags/架构约束.md) · [多Agent协作](../../tags/多Agent协作.md) · [自动化闭环](../../tags/自动化闭环.md)

- [反复提醒 Agent 仍犯错，哪些约束该下沉到工具或框架？](../../problems/提示词约束何时下沉.md)：`Let it decide, enforce only what can't bend` 给出“请求 vs 要求”的划分。
- [Agent 写完代码后，怎样让它自己运行应用并验证改动？](../../problems/Agent如何自行验证应用.md)：第一节的验证手段清单与“不要当 Agent 的测试套件”。
- [自检怎样保持独立视角，并检查当前 diff 以外的影响？](../../problems/独立自检如何组织.md)：`/code-review` 交给没看过对话的子 Agent，以及“reviewed by someone who didn't see your conversation”。
- [并行会话太多如何协调？](../../problems/并行会话太多如何协调.md)：编排税、跨度控制、按验证能力扩张而不是按注意力扩张。
- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：无人值守运行前的五个问题与“试点 + 观察前几次运行”。

## 接下来读哪篇

- [R0027：My AI Adoption Journey](../R0027/README.md)：Hashimoto 的个人路径与本篇的“管理”框架互补；两篇都强调先给验证手段，但 R0027 明确不并行跑多 Agent，可与本篇的编排税对照。
- [R0001：Agent Harness 工程实践](../R0001/README.md)：铁律四“能写成 Linter 的别写文档”与本篇“prompts 是请求、hook 是要求”是同一判断的两种表述；那篇把“可靠十倍”说过头了。
- [R0022：Harness engineering（OpenAI 团队实践）](../R0022/README.md)：团队视角的 AGENTS.md 目录化与架构检查，可补本篇“CLAUDE.md 该写什么”的组织方式。
- [R0004：pstack 指南 Pt. 1](../R0004/README.md)：把“给 Agent 验证手段”落成可复用的验证技能与 CLI，是本篇第一节的工程化版本。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 总论点 | `The skills for managing agents`；`you are managing` |
| 给验证手段 | `Give it a way to check its work`；`the single most useful line` |
| 上下文与提示词模板 | `Set clear context`；`commander's intent`；`p95 load time` |
| 纠正沉淀 | `Make every correction compound`；`corrected twice` |
| 请求 vs 要求 | `prompts, CLAUDE.md, and skills are requests`；`hooks, deny rules, and managed settings are requirements` |
| 计划与并行 | `Plan before it builds`；`/batch`；`one merge conflict with five authors` |
| 早纠正早重开 | `Steer early, reset fast`；`two failed attempts`；`/rewind` |
| 判断不可委派 | `Delegate the task, never the judgment`；`code ratification` |
| 无人值守设计 | `Design the run that doesn't need you`；五问列表 |
| 编排税 | `Scale verification, not attention`；`orchestration tax` |
| 少建一点 | `Decide what not to build`；`the most important word a manager says` |
| 类比边界 | `Where the analogy breaks` |

## 适用边界与查漏补缺

- 这是经验总结 + 对产品文档的转述，不是对照实验；“按影响力排序”是作者判断，没有测量。
- 文中提到的 `/goal`、`/code-review`、`/batch`、`/rewind`、Stop hook、auto mode 均属 Claude Code 的具体功能，本轮未核验版本、行为与默认策略，也未使用。
- 引用材料未逐一打开：Claude Code best-practices 文档、作者的两篇博客、Grove 的书、所谓 Wharton 的 cognitive surrender 研究（文中未给链接）。
- 两张配图（`pbs.twimg.com`）未保存，图中文字内容无法核对。
- 管理类比有明确边界：作者自己列了七条，其中“技能不回流”最关键——**能跑五个 Agent 不等于能带五个人**。
- “两次纠正就重开”“4–5 个后台 Agent”这类数字是个人经验，不构成建议阈值。
- 本库未在实践中检验任何一条建议；也没有用户项目的周期时间、返工率或注意力成本数据。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
