# The components of agent memory

[← 全部内容](../README.md) · [Anthropic Engineering（S0030）](../../sources/S0030.md)

- 内容编号：R0035
- 原链接：https://www.anthropic.com/research/components-of-agent-memory
- 发布来源：[Anthropic Engineering（S0030）](../../sources/S0030.md)
- 作者：原页标注 Engineering 团队（正文剪藏 `author` 字段为 Anthropic）
- 作者背景：机构署名，不为未知个人创建档案
- 平台：独立网站
- 形式：工程研究文章（含 15 幅外链图表）
- 原文发布日期：2026-11-06
- 日期依据：正文剪藏 frontmatter `published: 2026-11-06`；与 S0030 核对的原页页首 Published Nov 6, 2026 一致
- 收录日期：2026-11-15
- 整理日期：2026-11-17
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：把 agent 记忆拆成可实现的层级与操作，并用自评实验说明“记什么、怎么整理、怎么注入”的取舍

## 正文与保存依据

[阅读正文](正文.md)。正文由用户粘贴（2026-11-17），保留剪藏 frontmatter（title、source、author、published、created、description、tags）与英文原文；本库只补模板外壳与起止标记，未改写、未翻译、未重排。

- 正文含 15 幅 `assets.claude.com` 外链图表（记忆层级、CL-Bench、Pokémon 记忆目录、wiki 网络图等），本库未下载到 `assets/`；图意只能依据正文叙述与图注判断。
- 正文链接到 Claude 平台文档、CL-Bench、Letta/UC Berkeley 的 sleep-time compute、Harvey LAB、karpathy 的 wiki 示例等，本库均未打开核验。
- 原文没有个人署名，只有机构与团队口径；文中实验（CL-Bench、Pokémon、Stainless 语料、Harvey LAB）均为 Anthropic 自述，未取得原始数据或复现步骤。

## 一句话说明

把 agent 记忆拆成 transcripts、notes、wiki 与注入上下文四层，用离线的“dreaming”整理、纠错并决定下一次会话预加载什么。

## AI 摘要与要点

文章回答“agent 该记住什么、记忆如何组织”。它先把记忆分成四层，再用 dreaming（离线反思日志）做整理动作，最后用若干自评实验说明每一层的作用与代价。

**四层记忆层级**

| 层 | 内容 | 何时使用 | 本库判断与注意点 |
|---|---|---|---|
| Transcripts | 可搜索的会话事件日志 | 作为事实来源与 dreaming 的输入 | 是“ground truth”，但会不断增长；文章没有给保留与清理策略 |
| Memory notes | Claude 主动写下的笔记与规则 | 会话中标记显著事件，或直接写文件 | “显著”判断发生在还不知道后续结果时，文章承认这是预测 |
| Memory representations | 结构化表示，例如 wiki 页面及其链接 | 需要跨主题检索与跳转时 | 建立与维护成本高；可能长到比原始语料还大 |
| Injected context | 每次会话开始预加载的上下文 | 希望 Claude 不必搜索就知道 | 占 token；错误笔记会被带进每个会话，必须保持很小 |

**记忆笔记与“预测”**

- 文章把记忆定义为“从经验获得、跨会话保留的知识”，并明确排除权重更新、单次会话内的学习与 compaction。
- “写下一条规则”等于预测未来会再次用到它；“记下一个已核实的事实”等于预测以后不必再核对。这句话是全文最值得借用的判断标准。
- 在 CL-Bench 的数据库任务里，模型从“记下未验证的猜测”逐步进步到“记下已验证的规则与陷阱”。不同模型的记忆收益差别很大。

**自评实验里的数字**（均为团队自述）

| 实验 | 做法 | 结果 |
|---|---|---|
| CL-Bench 数据库任务 | 无记忆基线 vs 有记忆目录，30 题 | Opus 5.5 0.655→0.838；Opus 5 0.564→0.828；Opus 4.7 0.383→0.700；Sonnet 5 0.306→0.610；Sonnet 4.6 0.330→0.364 |
| Pokémon Red 的“记什么” | 比较 Sonnet 3.7 与 Fable 5 约 1 万步时的记忆目录 | Sonnet 3.7 写了 413 个文件 / 225 个目录，得 1 枚徽章；Fable 5 只写 9 个文件加 1 个 `global.md`，得 4 枚徽章 |
| 固定规则 vs 自由判断 | 加一条“只记录失败”的规则 | Opus 5 的记忆增益 −0.234，Opus 4.7 −0.150；越强的模型，越适合让它自己判断显著度 |
| dreaming 纠错 | Mt. Moon 的 Pokémon 场景 | 错误笔记让 Claude 三次掉回旧路线后放弃；对照 transcript 纠正后，1,935 步到达 Cerulean City |
| wiki 表示 | 约 35 万文件 / 4.2 亿 token 的 Stainless 语料，25 道题 | 2 个会话到 128 个会话，达标率 13%→48%；wiki + 搜索 54%→61%，只用搜索约 53%；每题省约 2 万 token |
| wiki 的边界 | Harvey LAB 法律简报任务 | 需要跨多份文档综合的题，wiki 87% 对只用搜索 73%；单文档可检索的题没有明显收益；有一个 wiki 长到语料体积的 1.77 倍 |
| 指令与覆盖 | 多个 agent 同时写一张共享条款表 | 覆盖导致 57 条评分事实只剩 41 条；改为每份合同一页、逐字引用后 57/57 |
| 注入层大小 | Claude Code auto memory | 只把 `MEMORY.md` 前 200 行或 25 KB 注入上下文，其余按需读 |

**dreaming 能做的六件事**：纠正错误笔记、建立或修剪 wiki、把重要笔记提升到注入层、让记忆围绕特定目标生长、补上多个会话留下的缺口、跨会话发现共同模式。文章同時说明 dreaming 要花算力，建议只对易变信息或按访问频率安排节奏。

**未解问题**（正文 “Thinking backward, looking forward”）：什么时候该写记忆（当场写会分心，离线写又不一定及时可用）；如何让记忆不过期；是否值得持续检查全部记忆；transcript 搜索是否应作为记忆的基础。

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| 记忆分四层：transcripts、notes、representations、injected context | 作者陈述 | 开头 Figure 1 与图注；第一节 | 层级清楚，但保留、清理与迁移规则未给 |
| 写下规则等于预测未来会用到它 | 作者陈述（观点） | “Memory can be a prediction about what the future will need” | 可作为判断“该不该记”的启发，不是测量结果 |
| CL-Bench 上 Opus 5.5 从 0.655 提到 0.838 | 团队自述（自评） | Figure 3 图注与同节正文 | 题目、评分器与运行次数未公开；不能当通用基准 |
| Pokémon 里 Sonnet 3.7 写 413 个文件只得 1 枚徽章，Fable 5 写 10 个文件得 4 枚 | 团队自述（观察） | “Claude has learned to judge salience”；Figure 4 | 单次运行对比，模型代际不同，不能只归因于记忆策略 |
| 固定规则“只记录失败”反而降低记忆增益 | 团队自述（消融） | Figure 5 右；同节正文 | 只测了一条规则；其他规则是否同样反效果未知 |
| dreaming 对照 transcript 纠正错误笔记后到达 Cerulean City | 团队自述（个案） | “Dreaming can correct memory”；Figure 7、8 | 单场景个案，不能推出普遍纠错率 |
| 128 个会话把 25 题达标率从 13% 提到 48% | 团队自述（自评） | Figure 10；Stainless 语料段 | 语料与评分标准为企业内部数据，未公开 |
| wiki + 搜索 61%，只用搜索 53% | 团队自述（自评） | Figure 10 与同节正文 | 差异依赖题库；单文档题上 wiki 无明显收益 |
| 每题省约 2 万 token | 团队自述（观测） | “Using search and the wiki also saved…” | 口径（输入或输出、是否含 wiki 维护成本）未说明 |
| 共享表覆盖导致 41/57，改为每合同一页后 57/57 | 团队自述（个案） | Figure 14；合同条款段 | 单个 LAB 任务，不能直接外推到其他并发写入场景 |
| Claude Code 只注入 `MEMORY.md` 前 200 行 / 25 KB | 产品文档陈述 | “Dreaming can promote notes up the memory hierarchy” | 属产品行为说明，本库未在本地验证 |
| 何时写记忆、如何防过期仍是开放问题 | 作者陈述（未解问题） | “Thinking backward, looking forward” | 文章自己承认没有答案；引用时不要当成已完成的方法论 |

## 标签与相关问题

**标签**：[知识沉淀](../../tags/知识沉淀.md) · [按需上下文](../../tags/按需上下文.md) · [知识检索](../../tags/知识检索.md)

- [需求做完后，怎样把经验留下，又不把临时推断当成长期知识？](../../problems/过程经验如何沉淀长期知识.md)：dreaming 把会话日志整理成规则、笔记与 wiki，并区分已验证与未验证。
- [项目资料太多，怎样让 Agent 按需读取？](../../problems/项目资料如何按需读取.md)：四层层级、索引注入与按需展开，是“按需上下文”的具体实现。
- [资料散落、口径冲突，怎样建可追溯的知识库？](../../problems/散落资料如何形成可追溯知识库.md)：wiki + 搜索、跨会话补缺与来源核对。

## 接下来读哪篇

- [R0024：LLM Wiki](../R0024/README.md)：同样是“原始材料 + 生成知识 + 维护规则”的分层；本文补上 agent 运行时的记忆层级与 dreaming 操作。
- [R0023：直播数据 LLM Wiki 实践](../R0023/README.md)：从工程侧实现 wiki 的来源治理、结构与检索，可与本文的表示层对照。
- [R0036：Building always-on agents](../R0036/README.md)：同一批作者把 memory 列为 always-on agent 的原语之一，补上运行循环与注入时机。
- [R0028：loopx](../R0028/README.md)：把目标、证据与配额放进持久状态，可与本文的“记忆是持久层”对照。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 记忆定义与排除项 | `Memory notes`；`weights`；`compaction` |
| 四层层级 | `Figure 1`；`transcripts`；`memory representations` |
| 记忆是预测 | `prediction about what the future will need` |
| CL-Bench 实验 | `Continual Learning Bench`；`Figure 3` |
| Pokémon 显著度 | `Claude has learned to judge salience`；`413`；`global.md` |
| 规则与指导 | `Steering Claude to write memory`；`record only failures` |
| dreaming 纠错 | `Dreaming can correct memory`；`Mt. Moon`；`Cerulean` |
| wiki 表示 | `Dreaming can build new memory representations`；`Stainless`；`128` |
| wiki 边界 | `larger than the raw files`；`Borges` |
| 注入层 | `Dreaming can promote notes up the memory hierarchy`；`200 lines`；`25 KB` |
| 目标导向 | `Dreaming can focus memory on a specific goal`；`41 of the 57` |
| 补缺 | `Dreaming can fill in gaps a session leaves behind` |
| 未解问题 | `Thinking backward, looking forward` |

## 适用边界与查漏补缺

- **自评而非独立复现**：所有数字来自 Anthropic 自己的任务与评分器，题目、语料与运行次数未公开；引用时保留“团队自述”限定。
- **产品绑定**：CL-Bench 实验用 Claude Managed Agents，注入层描述的是 Claude Code 的 auto memory；其他宿主能否复刻同样效果未验证。
- **成本未完整计入**：dreaming 要花算力，文章建议按易变程度或访问频率安排节奏，但没有给出端到端成本对比；wiki 的维护成本也只在“可能比语料还大”处被提到。
- **模型代际混杂**：Pokémon 对比用的是 Sonnet 3.7 与 Fable 5，结论同时受模型与策略影响，不能只归因于“记忆写得好不好”。
- **判断标准仍是启发式**：“记忆是预测”很好用，但文章没有给出可执行的写入阈值。
- 未核验：10 幅图表、Claude 平台文档、CL-Bench 公开页、Harvey LAB 仓库、karpathy 的 wiki 示例。
- 本库未在用户项目中实践这些层级或 dreaming，也没有用户记忆库的数据。

## 对已有知识的影响

- 与 R0024、R0023 的 LLM Wiki 线合并后，“知识沉淀”从静态文档扩展到 agent 运行时的四层记忆与离线整理。
- 与 R0036 同源：R0036 把 memory 当作 always-on agent 的原语，本文给出记忆内部的结构与实验。
- 在三个问题页各补一条：过程经验如何沉淀长期知识、项目资料如何按需读取、散落资料如何形成可追溯知识库。
- 未修改任何现有摘要或问题页结论；本文的“记忆是预测”可作为候选判断标准，但尚未在用户项目中检验。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
