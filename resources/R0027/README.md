# My AI Adoption Journey

[← 全部内容](../README.md) · [个人博客](../../sources/S0023.md) · [作者档案](../../authors/A0020.md)

- 内容编号：R0027
- 原链接：https://mitchellh.com/writing/my-ai-adoption-journey
- 发布来源：[Mitchell Hashimoto 的个人博客（S0023）](../../sources/S0023.md)
- 作者：[Mitchell Hashimoto（A0020）](../../authors/A0020.md)
- 作者背景：[Mitchell Hashimoto](../../authors/A0020.md)，依据原页署名；文中自述维护 Ghostty；公开头衔与公司关系未核验
- 平台：独立网站
- 形式：文章 / 个人经验记录
- 原文发布日期：2026-02-05
- 日期依据：原页页首与页脚均标注 “February 5, 2026”，按页面标注记录，不转换为本地时间
- 收录日期：2026-11-15
- 整理日期：2026-11-15
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：Harness Engineering 说法的原始出处；R0001 引用其定义，本库需要一手文本核对

## 正文与保存依据

[阅读英文原文](正文.md)。2026-11-15 直接从原页取得全文（HTTP 200），不需要用户粘贴。

- 保存范围：文章标题、日期、六个步骤与 Today 全部正文、四条脚注；已去除站点导航、目录和社交页脚。
- 原页脚注使用页内锚点，本库改为纯数字编号 `[1]`–`[4]`，脚注正文按原顺序保留。
- 正文为英文原文，未翻译、未删节、未改标点；文内链接（Claude Code、Anthropic 技能形成论文、Ghostty 的 AGENTS.md、Amp deep mode）保留原地址。
- 原文无插图，本次未下载任何图片。
- 著作权归原作者，不因收入本库而改用本库 MIT 许可。

## 一句话说明

一位资深工程师记录自己如何从“聊天框写代码”走到“发现错误就把环境改造好”，并明确承认自己还停在半路——这是 Harness Engineering 这个说法的一手出处。

## AI 摘要与要点

文章是六步个人采纳史，不是方法论手册；价值在于它展示的**顺序**和**作者停在何处**。

| 步骤 | 作者做了什么 | 本库判断与注意点 |
|---|---|---|
| 1. Drop the Chatbot | 停用聊天界面做实际工作，改用能读文件、执行程序、发 HTTP 请求的 Agent | 作者用一次“截图复刻命令面板”的成功和多次 brownfield 失败解释这个转向；属个人观察，不是对比实验 |
| 2. Reproduce Your Own Work | 强制用 Agent 重做自己已提交的全部工作，再比较质量 | 换来的三条经验：拆小任务、规划与执行分会话、给 Agent 验证手段。代价是“极其痛苦”的重复劳动，作者明说这拖慢了交付 |
| 3. End-of-Day Agents | 每天最后 30 分钟启动 Agent 做深度调研、并行探索、issue/PR 分诊 | 关键约束是“不许 Agent 回复”，只要第二天的报告；作者自述没有整夜跑循环 |
| 4. Outsource the Slam Dunks | 只把有把握的任务交给后台 Agent，人去做别的事 | 强调关掉桌面通知、由人决定何时打断；并主动讨论 Anthropic 技能形成论文的取舍 |
| 5. Engineer the Harness | 每次 Agent 犯错就工程化一个不再犯的解：改 `AGENTS.md` 或写真正的工具 | 这是“harness engineering”的一手定义；作者自己说“我不知道业界有没有公认术语” |
| 6. Always Have an Agent Running | 目标是始终有 Agent 在跑 | 现状只有工作时间的 10–20%；明确说不打算并行跑多个 Agent |
| Today | 承认自己仍在半路，且不确定 AI 是否长期存在 | 与常见“Agent 已成熟”的叙事相反，这是本篇最值得记住的态度 |

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| 采纳新工具通常要经过低效期、够用期、改变工作流三个阶段 | 作者个人经验陈述 | 正文开头，搜索 `three phases` | 是作者对多种工具采纳经历的归纳，没有研究数据；不能当作团队推行 AI 的路线图 |
| 聊天界面不适合真实编码，必须用 Agent | 作者经验断言 | Step 1，搜索 `To find value, you` | 作者区分了“日常聊天有用”和“编码低效”，但证据是他自己的项目经历与一次成功复刻 |
| 给 Agent 验证手段，它多数时候能自己修错 | 作者经验规则 | Step 2 第 3 条，搜索 `If you give an agent a way to verify its work` | 与 R0004、R0017 的“让 Agent 自行验证”方向一致；但“more often than not”没有给出失败率或反例 |
| 发现错误后工程化，使其不再犯，就是 harness engineering | 作者本人提出的概念 | Step 5，搜索 `I've grown to calling this` | 一手定义，比 R0001 的转述更谨慎：作者紧接着说 `I don't need to invent any new terms here`，并未主张这是成熟范式 |
| 两类手段：改 AGENTS.md 与写程序化工具 | 作者做法 + 可核验案例 | Step 5 两种形式，含 Ghostty 的 `AGENTS.md` 固定链接 | Ghostty 文件可点开核对，但“几乎完全解决了所有问题”是作者自述，没有前后对照 |
| 关闭 Agent 通知，由人控制打断时机 | 作者操作建议 | Step 4，搜索 `turn off agent desktop notifications` | 理由（上下文切换昂贵）成立，但缺少实测；对必须实时响应的岗位未必适用 |
| 不并行跑多个 Agent，常驻率仅 10–20% | 作者现状自述 | Step 6，搜索 `10 to 20%`；`currently don't really want to` | 与“多 Agent 协作”流行建议形成真实分歧；属个人偏好与工作方式，不是对多 Agent 效果的否定 |
| 允许 Agent 分诊但不允许它回复 | 作者边界设定 | Step 3，搜索 `I would NOT allow agents to respond` | 对外动作的人为闸门，和 R0001 案例中的“外发消息硬护栏”形成同向证据；仍是单点经验 |

## 标签与相关问题

**标签**：[外部验证](../../tags/外部验证.md) · [Agent工具设计](../../tags/Agent工具设计.md) · [按需上下文](../../tags/按需上下文.md) · [自动化闭环](../../tags/自动化闭环.md)

- [反复提醒 Agent 仍犯错，哪些约束该下沉到工具或框架？](../../problems/提示词约束何时下沉.md)：本文是“按失败逐条加约束”的一手描述，含 `AGENTS.md` 与程序化工具两种落法。
- [Agent 写完代码后，怎样让它自己运行应用并验证改动？](../../problems/Agent如何自行验证应用.md)：第 2 步第 3 条与第 5 步说明优先级——先给验证手段，再谈更复杂的编排。
- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：下班前启动、只收报告不放手回复，是一种人为闸门的具体做法。

## 接下来读哪篇

- [R0001：Agent Harness 工程实践](../R0001/README.md)：把本文定义包装成“系统阐述的工程范式”的那篇中文文章；对照阅读可见转述加强了多少。也解释了为什么本文被引用。
- [R0022：Harness engineering（OpenAI 团队实践）](../R0022/README.md)：团队视角的 `AGENTS.md` 目录化、架构检查与持续清理，可与本文的个人视角互补。
- [R0021：大仓 Harness 实战](../R0021/README.md)：中文大仓场景的门禁基线与角色契约；与本文“按失败逐条加约束”相比，团队级做法更重前置约束。
- [R0004：pstack 指南 Pt. 1](../R0004/README.md)：把“给 Agent 验证手段”落成可复用的验证技能与 CLI。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 六步标题 | `Drop the Chatbot`；`Reproduce Your Own Work`；`End-of-Day Agents`；`Outsource the Slam Dunks`；`Engineer the Harness`；`Always Have an Agent Running` |
| harness engineering 定义 | `I've grown to calling this`；`never makes that mistake again` |
| 规划与执行分会话 | `planning vs. execution sessions` |
| 让 Agent 自行验证 | `a way to verify its work` |
| 不许 Agent 回复 | `I would NOT allow agents to respond` |
| 现状数字 | `10 to 20%`；`not \[yet?\] running multiple agents` |

## 适用边界与查漏补缺

- 单人、单一年份的经验记录，没有对照组、样本量或效率测量；“显著效率提升”是主观判断。
- 作者自己声明“完全手写”，本库无法验证写作过程，也不因此提高或降低对内容可信度的判断。
- 时间因素很强：文章写于 2026 年 2 月，提到的模型与工具（如 GPT-5.2-Codex、Amp deep mode）会过时；方法结论未必随模型一起失效，但需要重新验证。
- 作者明确表示不打算并行跑多个 Agent，这不是对多 Agent 方案的否定，只是个人取舍；不要把“单 Agent”读成普适建议。
- Ghostty 的 `AGENTS.md` 示例是他人项目文件，本库只核对了链接地址，未评估该文件是否真的“几乎解决了所有问题”。
- 本库只保存了这一篇文章，未读该作者其他文章；未验证其身份与从属关系，也未联系作者。
- 本库未实践其中任何一条建议（没有在用户项目中改 `AGENTS.md`、写截图工具或改变工作节奏）。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
