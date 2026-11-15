# How the Claude Code team does code review

[← 全部内容](../README.md) · [claude.dev](../../sources/S0027.md) · [作者档案](../../authors/A0021.md)

- 内容编号：R0031
- 原链接：https://claude.dev/blog/solving-code-review-at-anthropic/
- 发布来源：[claude.dev（S0027）](../../sources/S0027.md)
- 作者：[Addy Osmani](../../authors/A0021.md) · [Morgan Westlee Lunt](../../authors/A0022.md) · [Qing Wang](../../authors/A0023.md)（原页作者栏，2026-11-15 核对）
- 作者背景：三人合署，页面未说明分工；个人头衔与经历均未核验，见各自档案
- 平台：独立网站
- 形式：文章 / 长文（含 4 幅内联图表）
- 原文发布日期：2026-10-15
- 日期依据：原页 PUBLISHED “Oct 15, 2026”（2026-11-15 抓取核对），与正文元数据 `published: 2026-10-15` 一致；不按收录时间推断
- 收录日期：2026-11-15
- 整理日期：2026-11-15
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：完整描述一套大规模 AI 代码评审的分层门禁、评测与收敛机制，可与库内“独立自检”“约束下沉”几条线对照

## 正文与保存依据

[阅读正文](正文.md)。正文由用户粘贴，本库只补模板外壳与起止标记，未改写、未翻译、未重排。

- 2026-11-15 首次粘贴的是一份内容相近但不同的文本（元数据 `source` 指向 @addyosmani 的 X 帖、`published` 为 2026-10-26、末尾自述“是对原文的重写”）；用户随后替换为本次正文，本条目以当前正文为准，旧文本未保留。
- 当前正文含 4 幅内联 SVG 图表（变更生命周期、六层检查、事故评测、收敛前后对比）和 1 张外链示意图，后者指向 `claude.dev/media/…png`；本库未把图片下载到 `assets/`。
- 正文末尾原有站点导航与文章列表（`FINDER`、18 篇文章目录、快捷键提示），属网页装饰而非文章内容；已按用户要求于 2026-11-15 删除，文章正文与文末致谢保持原样。
- 文末致谢：“With thanks to Emma Webb, Michael Segner and Amie Rotherham for their reviews.”

**来源已核验**：2026-11-15 抓取原页（HTTP 200），页面作者栏、分类（Engineering）、发布日期与正文均与粘贴内容一致；站点与 `code.claude.com`、`claude.com` 互链，按一方开发者站点记录。数字仍属团队内部自述，没有公开数据集。

## 一句话说明

把代码评审从“有没有人读过”改成“这次改动的风险由哪一层负责拦住”：六层检查加一条回滚线，用事故当评测集，并把“评审能收敛”当成必须满足的性质。

## AI 摘要与要点

文章以“Claude 写了约 90% 的 Claude Code 代码”为背景，回答这个量级还怎么做评审，主体是分层门禁、评测方法与收敛机制。

| 环节 | 团队的做法 | 本库判断与注意点 |
|---|---|---|
| 目标重定义 | 不问“谁读过”，而问“可能出什么问题、哪道检查（自动或人）能拦住” | 这是全文的核心转换；比任何具体工具都值得先借用 |
| 评审时机 | 评审前移到写代码过程中，像拼写检查；多数改动在人看之前已被 Claude 修过一轮 | 与 R0030、R0027 的“给验证手段、让 Agent 自己修”一致；代价是自动评审自身也要维护与评测 |
| 人工成本 | 人工时间算两面：评审花的时间 + 修坏代码花的时间；用 revert 与 incident 率作护栏 | 全篇最容易被忽略的一条：只减前者等于把成本挪到后面 |
| 预 PR 验证 | 让 Claude 跑测试、构建、比对截图，要求出示结果；另一 subagent 用新上下文审 diff | 与 R0004 同向；Boris Cherny 的“2–3 倍质量”是估计而非测量 |
| 规则文件 | `CLAUDE.md` 简短、指向其他文档；`REVIEW.md` 由 owner 定义“本仓库什么算失败、哪些路径跳过、要文件行号证据” | 与 R0022 的 AGENTS.md 目录化同构；两份文件的分工写得很具体 |
| AI 评审 | 每个 PR 先过 Claude 评审；多个 agent 并行找 bug，再独立投票定有效性，风格类过滤后按严重度贴行内评论 | 多 agent + 投票是减少误报的工程手段；过滤规则做过 A/B，但数据未公开 |
| 安全评审 | 有未关闭发现时禁止合并；作者可修复或写明理由关闭 | 属“可阻塞”的门；细节需对一手材料 |
| 合并前检查 | lint、类型、全平台测试、构建；PR 模板问“怎么测的、怎么回滚” | 常规但完整；模板三问比多数团队具体 |
| 人工审批分级 | 风险由变更决定而非作者；低风险自动检查绿灯即可无人工；中风险一人；高风险两人；敏感路径与 CI 文件永远要人 | 这几条可直接抄；分类器误判如何兜底未讨论 |
| 硬规则 | bot 批准不算人工批准；新 commit 撤销旧批准；代理人（prompt 的人）算必需评审人之一 | 三条都能防“AI 批准 AI”的自我循环 |
| 合并与发布 | merge queue 在 main 上重跑；feature flag 先内部后公开；latest/stable 分渠道 | 回滚能力是前置条件，不是事后补救 |
| 反馈与回滚 | 每周 on-call；事故复盘反查“哪一层本该拦住”；尚未做自动收紧审批的熔断器 | 作者明确说这是缺口，工程师想在“零人工合并”前补上 |
| 评测方法 | 事故 PR + 修复 + 回滚构成评测集，专家逐例确认，评审器每日跑分；任何提示词/工具/模型改动都重跑 | 把“回归资产”用在评审器上；集合如何防污染未讨论 |
| 噪声控制 | 按人对每条评论的处理方式分类；另在已知干净的 PR 上跑，统计“会导致有害改动”的误报 | 同时看召回与噪声，比只报“发现多少问题”可靠 |
| 收敛 | 限三轮、之后要求重估方案；只审增量；按 bug 类别提要求；不重复报 | 全文最有价值的具体教训，见下方数字 |
| 团队学习 | 没有正式机制；需要时让 Claude 对该模块生成讲解或可视化产物 | 承认“读 diff 学习”被自动化削弱，但没给出替代的制度 |
| 责任归属 | “you land it, you own it”：小改动自己修、一切可回滚、爆炸半径决定审查强度 | 与 R0030“任务可委派、判断不可委派”呼应 |
| 实施清单 | 分四段：PR 前、每个 PR、审批、合并后 | 可当落地检查表；小团队需要裁剪 |

**收敛前后的四个数字**（正文 FIG D，均为团队自测）：一轮评审即通过的比例 65% → 78%；需要五轮以上的 8.9% → 1.5%；平均通过轮次 2.08 → 1.32。

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| Claude 写了 Claude Code 约 90% 的代码 | 团队自述（背景陈述） | 正文开头，搜索 `90 percent` | 未给口径（行数或 PR 数）；站点非官方，需回一手核对 |
| monorepo 日变更量从 5 月约 2,500 增至 9 月 30,000 以上 | 团队自述 | 正文 RETHINKING THE PURPOSE，链接到 Anthropic 工程博客 | 引用的工程博客本轮未读；数字口径未说明 |
| 6–9 月合并 PR 翻倍以上、revert 占比降 40% 以上 | 团队自述 | 正文开头 | 基数、窗口定义与统计方式未给 |
| 有实质评审评论的 PR 从 16% 升到 54% | 团队自述（研究预览以来） | 正文第 2 层 | 可能是“被标记的 PR 变多”而非“缺陷变多”，作者未区分 |
| 只有 1.5% 的内部 PR 需要五轮以上 | 团队自述（收敛后） | FIG D 数字与正文收敛段 | 未给样本量与时间窗；属自测 |
| 被反复标记的代码约 59% 在首轮就已存在 | 团队自述（git blame 观察） | 正文 Review has to converge | 样本范围未给；结论是“评审很少发现新 bug” |
| 一个 CLI PR 一夜循环 50 多轮 | 团队自述（个案） | 同上 | 单例，但足以说明收敛机制的必要性 |
| 验证流程把结果质量提高 2–3 倍 | 转述 Boris Cherny 的估计 | 正文第 1 层，链接其 X 帖 | 估计值，无方法说明；本库未核对原帖 |
| 人工时间要算两面，revert 与 incident 作护栏 | 方法主张 | 正文 THE SCARCE RESOURCE | 指标定义（审批中位数、95 分位、等待时长）清楚，采集成本未讨论 |
| bot 批准不能替代人工批准，新 commit 需重新批准 | 机制规则 | 正文第 5 层 | 可直接借鉴的硬规则；细则需对一手材料 |
| 事故集合即评测集，评审器改动必须重跑 | 方法主张 | 正文 HOW WE MAKE THE REVIEWER BETTER | 把回归资产用在评审器上，值得借用 |
| 合规的低风险改动可自动合并，边界仍在移动 | 现状 + 未来方向 | 正文 WHERE THIS IS GOING | 属团队自身仓库的做法，不是产品默认能力 |

## 标签与相关问题

**标签**：[外部验证](../../tags/外部验证.md) · [自动化闭环](../../tags/自动化闭环.md) · [多Agent协作](../../tags/多Agent协作.md) · [运行时治理](../../tags/运行时治理.md) · [Agent评测](../../tags/Agent评测.md)

- [自检怎样保持独立视角，并检查当前 diff 以外的影响？](../../problems/独立自检如何组织.md)：六层检查、新上下文 subagent 评审、按风险分层的人工审批。
- [AI 写的测试全绿，怎样判断它真能抓缺陷？](../../problems/AI测试是否真能查错.md)：用事故 PR 集合给评审器打分，同时用人类反应衡量噪声。
- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：merge queue、feature flag、分阶段发布与一键回滚。
- [怎样让 AI 审计代码，又避免把猜测当漏洞？](../../problems/AI安全审计如何减少误报.md)：多 agent 并行 + 独立投票 + 风格过滤 + 按严重度标注。

## 接下来读哪篇

- [R0009：端到端交付2.0](../R0009/README.md)：独立自检与新旧代码规则边界，是“六层检查”在业务交付侧的相似思路。
- [R0017：Cloudflare security-audit-skill](../R0017/README.md)：候选反证与独立复核，可对照本文的投票与过滤机制。
- [R0030：Your coding agents made you a manager](../R0030/README.md)：同一账号的长贴（管理框架），与本篇的团队流程细节互为宏观/微观。
- [R0022：Harness engineering](../R0022/README.md)：AGENTS.md 目录化与架构检查，配合本篇的 CLAUDE.md / REVIEW.md 分工。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 为什么要改评审目标 | `RETHINKING THE PURPOSE OF CODE REVIEW`；`imprecise proxy` |
| 人工时间两面成本 | `THE SCARCE RESOURCE`；`both sides of review's cost` |
| 六层检查总览 | `THE LIFE OF A CHANGE`；`Six layers of checks`；`FIG A`、`FIG B` |
| 预 PR 验证 | `The work is verified before anyone else looks`；`REVIEW.md` |
| AI 评审与投票 | `AI review on every pull request`；`a separate group votes` |
| 可阻塞的安全评审 | `Security review that can block` |
| 风险分级 | `Human approval, scaled by risk`；`The change sets the tier` |
| 硬规则 | `An agent's approval never counts as a person's`；`An approval covers one specific commit` |
| 合并与回滚 | `Merge queue, flags and a gradual release`；`Fast detection, fast rollback` |
| 事故即评测 | `Any incidents are now an eval`；`FIG C` |
| 收敛机制 | `Review has to converge`；`fifty rounds`；`59%`；`FIG D` |
| 人类仍负责什么 | `WHERE HUMANS STAY IN THE LOOP` |
| 团队学习 | `SHARING CONTEXT ACROSS THE TEAM`；`explainer` |
| 实施清单 | `HOW YOU CAN ADOPT THIS PROCESS` |

## 适用边界与查漏补缺

- **数字属团队自述**：来源与作者已核验，但 90%、40%、30,000、16%→54%、59%、50 轮等均无公开口径、样本与窗口说明；引用时应保留这一限定。
- 团队规模与产品成熟度差异很大：六层检查、merge queue、分级审批、每周 on-call 都有组织成本，小团队照搬会先被流程压垮。
- 量化结论均缺少口径、样本与窗口说明，属内部自述；FIG C 与 FIG D 的数字来自团队自测图，本库未取得原始数据。
- 引用材料未核验：Boris Cherny 的 X 帖、Claude Code best-practices 与 code-review 文档、Anthropic 的 source control 与 CI 工程博客、`/security-review` 与相关 GitHub Action。
- 4 幅内联 SVG 与 1 张外链图未本地化；图的完整含义只能依据正文叙述判断。
- 正文末尾的站点导航已按用户要求删除；文中 4 幅内联 SVG 与 1 张外链图未本地化，图的细节只能依据正文叙述判断。
- “低风险改动可自动合并”是团队在自家仓库的做法，不等于产品默认能力；作者也承认边界仍在移动。
- 本库未在实践中采用任何建议，也没有用户项目的 revert 率、评审轮次或人力数据。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
