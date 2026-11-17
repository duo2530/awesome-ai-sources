# Vibing a Non-Trivial Ghostty Feature

[← 全部内容](../README.md) · [Mitchell Hashimoto 的个人博客（S0023）](../../sources/S0023.md) · [Mitchell Hashimoto（A0020）](../../authors/A0020.md)

- 内容编号：R0034
- 原链接：https://mitchellh.com/writing/non-trivial-vibing
- 发布来源：[Mitchell Hashimoto 的个人博客（S0023）](../../sources/S0023.md)
- 作者：[Mitchell Hashimoto](../../authors/A0020.md)
- 作者背景：原文以第一人称写作并署名本人，自述维护 Ghostty；头衔与公司关系未核验，见 [A0020](../../authors/A0020.md)
- 平台：独立网站
- 形式：文章 / 长文（逐会话记录，含 2 段外链视频与 2 幅外链图片）
- 原文发布日期：2025-10-11
- 日期依据：正文末尾 “October 11, 2025”；issue #5 未另给日期，原页未打开核验
- 收录日期：2026-11-17
- 整理日期：2026-11-17
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：逐会话公开一个真实上线功能的 agentic coding 全过程，保留修不掉、弃用、pivot 与人工接管，可与 R0027 的采纳史对照

## 正文与保存依据

[阅读正文](正文.md)。正文由用户在 issue #5 评论中提供（2026-11-15），是博客全文；本库只补模板外壳与起止标记，未改写、未翻译、未重排。

- 评论开头有一行 `## Vibing a Non-Trivial Ghostty Feature`，与文章标题重复，是 issue 评论的排版标题，不是原文的小节；本库原样保留，未删。
- 正文含 2 段 `<video>` 外链（`static.mitchellh.com` 的 webm / mp4）与 2 幅 `mitchellh.com/_next/image` 外链图片（OpenAI 发布会截图、边做早餐边看 agent 的照片），本库未下载到 `assets/`。
- 正文保留原文脚注 1–6 与文末日期 “October 11, 2025”；未做 HTML 清洗或链接改写。
- 原文页未抓取；正文中的会话链接（`ampcode.com/threads/…`）、PR 链接（`ghostty-org/ghostty/pull/9116`）与 Sparkle 文档链接均未核验。
- 正文没有剪藏 frontmatter，也没有站点导航段落。

**来源判断**：issue 只说“文章”，未给站点或作者；正文以第一人称写“我发布了一个 Ghostty 功能”，文末署名日期，文中自述“不为任何 AI 公司工作、投资或提供咨询”。据此与已收录的 [S0023](../../sources/S0023.md) 合并，作者沿用 [A0020](../../authors/A0020.md)。该博客在 2026-11-15 曾核验过页首与页脚署名，本文按同一来源记录。

## 一句话说明

一位资深工程师逐会话公开 16 次 agent 协作：先规划与 UI 原型、撞墙后人工接管、cleanup 强制理解、最后整体人工 review。

## AI 摘要与要点

文章按时间顺序贴出这个功能的每一次 agent 会话，作者只补充背景与判断。功能是 Ghostty 的 macOS 非打扰式更新提示：不弹窗、不抢焦点，在标题栏或窗口角落显示状态。

| 环节 | 作者的做法 | 结果与判断 |
|---|---|---|
| 规模与成本 | 共 16 个会话，token 花费 $15.98；作者估计约 8 小时、跨 3 天，同时还在做别的项目工作 | 作者明确“仍有很多人工编码”，AI 产出与最终代码有差异；8 小时是估计，不是计时 |
| 预规划 | 不先打开 AI：先读 Sparkle 文档，确认可用 Obj-C 协议自定义 UI；前端只确定“标题栏里一个小按钮”的方向 | 作者说知道“自己不知道什么”就足够开始；AI 是执行与原型，不是需求来源 |
| 第一个会话 | 只做 UI、只出计划不写码；用只读子 agent “oracle” 参与规划；把计划存成 `spec.md` 供后续会话引用 | UI 方向对，但有大量间距、颜色等细节问题；作者说 AI 常被当灵感来源，有时全扔掉自己重写 |
| 撞墙 | 第 11–14 个会话进入“slop zone”：一个关键 bug 反复修不掉，作者自己也不知道怎么修 | 几次“hail mary”后承认：此时 AI 从解法变成负债，需要人退回去理解和规划 |
| cleanup | 连续几个会话移动方法、补文档、把 view model 从窗口作用域移到 AppDelegate；作者自嘲“anti-slop session” | 清理迫使自己读懂代码；组织好、有文档的代码也让后续 agent 表现更好 |
| 面对 bug | 从模糊描述到越来越具体的四次提示，全部失败；期间自己也查资料 | 改方案而不是硬修：难处理的标题栏样式改为窗口右下角浮层——隐藏标题栏本来也需要这个模式 |
| 后端 | 手写带 `TODO` 的函数骨架，让 agent 补全；agent 产出的实现能用但设计错，整体丢弃 | 作者从错误实现反推出 view model 结构问题，手动改成 tagged union，再让 agent 迁移依赖代码 |
| 清理与模拟 | 删死代码、修自己弄坏的构建、把 view 拆成独立类型；把模拟代码抽成文件，生成正常、未找到、报错等场景 | 模拟代码质量差但不上线，作者不在意；靠跑模拟发现多处 UX 问题 |
| 收尾 | 仿 Sparkle 的 `SPUStandardUpdaterController` 写 `UpdateController`；最后总问 agent“还缺什么”，并让它先别写码 | 这个最后提问“不管代码是不是自己写的都会做”；agent 跑偏时会直接叫停 |
| 交付 | 最终人工整体 review 后合并；tip 渠道可用，正式版随 Ghostty 1.3 发布 | 作者在脚注强调“最终人工 review 超级重要，别把 AI 写的代码未经彻底审查就发出去” |

**作者的用法清单**（正文中以 Tip 标出）：先规划并保存 spec；小步提交、方便审阅；用 AI 做“填空”和“把剩下的猫画完”；让 agent 生成测试与模拟；自己弄坏构建后让 agent 修；最后问“还缺什么”。这些是作者个人习惯，不是对照实验结论。

**成本口径**：$15.98 是 16 个会话的 token 费用，不含作者时间；作者估计约 8 小时，主要用于清理、理解与接手，而不是首次生成。作者没有给出与纯手写的对照。

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| 16 个会话、$15.98、约 8 小时、跨 3 天 | 作者自述 | “Cost and Time” 一节 | 时间是估计；$15.98 是特定工具与时间点的价格，不是通用成本 |
| 仍有大量人工编码 | 作者自述 | 开头 “Important: there is a lot of human coding, too.” | 没有人工/自动代码比例，无法量化 |
| 先规划、只出计划不写码 | 作者做法 | “First Session: Prototyping the UI”；“Consult the oracle” | 计划质量依赖作者的领域判断；无对照 |
| AI 适合做原型与灵感 | 作者主张 | “AI is a very good prototyper”；“AI is excellent at being my muse” | 是个人经验，文中也承认会整段丢弃 |
| 撞墙时人必须接管 | 作者陈述 | “Hitting a Wall”；chats 11–14 | 何时该接管没有客观判据，靠作者判断 |
| cleanup 让作者真正理解代码 | 作者陈述 | “Cleanup Sessions”；“anti-slop session” | 因果是作者自述，没有测量理解程度 |
| 四次更具体的提示全部失败，最后改方案 | 作者自述（过程记录） | “Facing The Bug” 四次 prompt | 失败原因未独立核验；改方案依赖“隐藏标题栏本来也要支持” |
| 后端 agent 实现被整体丢弃，因 view model 结构不好 | 作者自述 | “Starting the Backend”；“Cleanup Again, Big Time” | 说明 AI 产出质量受中间数据结构影响；单例 |
| 最终人工 review 是交付前提 | 作者主张（脚注强调） | 脚注 5 “Final manual review is super super super important” | 与库内 R0031、R0030 的人工门方向一致；本文没有 review 清单 |
| 作者不为 AI 公司工作 | 利益声明 | 脚注 3；正文 “I'm not associated financially with any AI company” | 降低软文嫌疑，但不等于结论可推广 |

## 标签与相关问题

**标签**：[原型验证](../../tags/原型验证.md) · [需求澄清](../../tags/需求澄清.md) · [AI辅助学习](../../tags/AI辅助学习.md)

- [AI 生成的代码和文档怎样持续清理，避免坏模式扩散？](../../problems/AI生成代码如何持续清理.md)：本文的 cleanup 会话、删死代码与“清理迫使理解”是可操作的一种做法。
- [需求不清楚、方案拿不准时，怎样先验证再写完整实现？](../../problems/需求与方案如何先验证.md)：先规划、存 `spec.md`、UI 先出原型。
- [AI 做出的原型能跑了，怎样判断能否走向生产？](../../problems/AI原型如何走向生产.md)：功能最终上线，但作者把“最终人工 review”列为不可省的一步。
- [用 AI 提效后怎样保住自己的技能？](../../problems/用AI提效后如何保住技能.md)：作者坚持“不理解就不发”，把 AI 当老师与缪斯；这是专家自述，不能反证 R0032 的实验结果。

## 接下来读哪篇

- [R0027：My AI Adoption Journey](../R0027/README.md)：同一作者的六步采纳史，是本文做法的“原则版”；先看原则再看这个完整案例，容易对上。
- [R0030：Your coding agents made you a manager](../R0030/README.md)：把委派、上下文与验证讲成管理框架，可补本文只讲过程、不讲边界的部分。
- [R0006：pstack 指南 Pt. 2](../R0006/README.md)：需求复述、调研与可运行原型，是本文“先规划再写码”的另一种方法。
- [R0032：How AI assistance impacts the formation of coding skills](../R0032/README.md)：实验证据说 AI 辅助可能降低掌握；本文是一个“资深工程师主动要求理解”的对照案例，但只有一人、无测量。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 范围与免责 | `there is a lot of human coding, too`；`assistant, not a replacement` |
| 预规划 | `Pre-AI Planning`；`Sparkle`；`titlebar accessory controllers` |
| 第一个会话 | `First Session: Prototyping the UI`；`ONLY work on UI`；`oracle` |
| 存 spec | `spec.md`；`Consult the @spec.md` |
| 撞墙 | `Hitting a Wall`；`slop zone` |
| cleanup | `Cleanup Sessions`；`anti-slop session` |
| 面对 bug | `Facing "The Bug"`；四次 prompt；`pivot` |
| 改浮层 | `bottom-right corner`；`hide the titlebar entirely` |
| 后端 | `Starting the Backend`；`fill-in-the-blank`；`tagged union` |
| 模拟 | `Simulation`；`happy path, not found, errors` |
| 收尾 | `Last Mile`；`UpdateController`；`Anything Else?` |
| 成本 | `16 separate sessions`；`$15.98`；`8 hours` |
| 交付与 review | `final manual review`；`Ghostty 1.3` |
| 利益声明 | `not associated financially with any AI company` |

## 适用边界与查漏补缺

- **单人经验，且作者是领域专家**：作者是 Ghostty 维护者、资深系统工程师，对 Sparkle、SwiftUI、macOS 标题栏都有判断力；换成不熟悉领域的人，预规划与“该不该接管”的判断未必成立。
- **成本不可直接换算**：$15.98 是 token 费用，不含时间；8 小时是估计，与作者同时做其他工作重叠；不能据此推出“这个功能只值 8 小时”或“AI 让效率翻倍”。
- **“仍有很多人工编码”没有比例**：作者只用一句话说明，读者看不到最终代码里 AI 与人的占比，也就无法复算速度与成本。
- **过程完整但结论是自述**：会话链接可点，但本库未打开核验；会话内容由作者挑选与编排，失败保留得多，是本文可信度较高的原因，也仍是一次叙述。
- **工具绑定**：作者用 Amp 与 oracle 子 agent，成本与体验不能直接搬到其他工具。
- 未核验：Sparkle 的自定义 UI 协议、`ghostty-org/ghostty` PR #9116 的实际 diff、Ghostty 1.3 的发布状态、文中所有会话链接。
- 本库未在实践中采用本文方法，也没有用户项目里“agent 会话数 / 成本 / 人工接管点”的记录。

## 对已有知识的影响

- 与 [R0027](../R0027/README.md) 同作者、同项目：R0027 讲“采纳到哪一步”，本文讲“一次真实交付怎么走”，两篇互补。
- 与 [R0032](../R0032/README.md) 形成一处真实对照：R0032 的随机实验显示 AI 辅助组掌握度更低；本文作者坚持读懂、不 ship 不懂的代码，把 AI 当学习对象。前者是群体实验，后者是单人自述，**不能互相证明**，但可以提示“使用方式”与“人的要求”可能改变结果。
- 在“AI 生成代码如何持续清理”“需求与方案如何先验证”“AI 原型如何走向生产”“用 AI 提效后如何保住技能”四页各补一条补充参考。
- 未修改任何现有摘要或问题页结论；本文没有推翻既有判断。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
