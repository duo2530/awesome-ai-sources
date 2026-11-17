# How the Claude Code team thinks about verification

[← 全部内容](../README.md) · [X / @addyosmani（S0026）](../../sources/S0026.md) · [Addy Osmani（A0021）](../../authors/A0021.md)

- 内容编号：R0033
- 原链接：https://x.com/addyosmani/status/2122590683055993308
- 发布来源：[X / @addyosmani（S0026）](../../sources/S0026.md)
- 作者：[Addy Osmani](../../authors/A0021.md)（用户于 2026-11-17 确认）
- 作者背景：个人档案见 [A0021](../../authors/A0021.md)；正文以 Claude Code 团队第一人称写作，个人与团队的分工文中未说明
- 平台：X
- 形式：文章 / X Article（含 3 幅外链配图）
- 原文发布日期：2026-11-17
- 日期依据：正文剪藏 frontmatter 记 `published: 2026-11-17`；issue #8 记录推文 `created_at` 为 2026-11-17T07:20:29Z（上海时区 15:20:29），同日一致；未打开原页核验
- 收录日期：2026-11-17
- 整理日期：2026-11-17
- 内容处理：已有正文与 AI 摘要
- 我的阅读：未记录
- 留存理由：把“给 Agent 一套能自己跑的验证反馈”拆成测试类型、验证技能、门禁规则与评测四层，可与 R0031 的评审分层、R0004 的验证技能对照

## 正文与保存依据

[阅读正文](正文.md)。正文由用户在 issue #8 评论中提供（2026-11-17），说明是从 X API 的 `article.plain_text` 提取；本库只补模板外壳与起止标记，未改写、未翻译、未重排。

- 正文开头保留了剪藏 frontmatter（title、source、author、published、created、description、tags），后接英文正文；frontmatter 在 Markdown 中会渲染成分隔线与普通行，属材料原样，不是本库新增。
- 正文含 3 幅 `pbs.twimg.com` 外链配图（开头、E2E 段、结尾），本库未下载到 `assets/`；图意只能依据正文叙述判断。
- issue 另给了一个 X Article 地址 `https://x.com/i/article/2122515769007435776`，而正文 frontmatter 的 `source` 是 `https://x.com/addyosmani/article/2122590683055993308`（把推文 ID 当作 article ID）。哪个是文章 canonical 地址未核验，本条只按原链接保留用户提交的推文地址。
- 文中链接指向 claude.dev、claude.com、code.claude.com 与 fast-check / Hypothesis / proptest 等第三方库，本库均未打开核验。
- 原页抓取：issue 说明对 X Article 的公开抓取返回 403；本库未另试，也未取得网页版页面结构。

**来源判断**：作者按用户于 2026-11-17 的确认记为 Addy Osmani，与剪藏 frontmatter 的 `author` 字段一致。正文以 Claude Code 团队第一人称写作（“On the Claude Code team, the vast majority of our code (~90%) is written and reviewed by Claude”），并说 “We have previously written about how code review works at Anthropic”，链接到 R0031 的原页；因此内容口径是团队，个人与团队的分工文中未说明。是否有共同作者、是否有 claude.dev 对应页面，均未核验，见 [S0026](../../sources/S0026.md)；与 R0031 的作者栏不能直接互推。

## 一句话说明

给 Agent 一套能自己跑的验证反馈：E2E 优先、属性与差分测试补边界，再用 verify 技能、失败三轮交人、检查不可自改与 observe 门逐步放开自动化。

## AI 摘要与要点

文章接续 R0031 的代码评审话题，回答“验证该怎么做”：先说服读者验证是并行扩产的前提，再给出三类值得投入的测试，最后是团队自己的八条做法。

**为什么先做验证**

| 论点 | 正文怎么说 | 本库判断与注意点 |
|---|---|---|
| 规模前提 | 团队约 90% 代码由 Claude 写与审；没有验证循环只能同时跑一两个 Claude，有了才能跑几十上百个 | 90% 是团队自述、口径未给；“几十上百”是并行上限的推论，不是实测 |
| 独立判分有效 | 结构化文件生成的内测中，另设 grader 按 rubric 检查，任务成功率比普通提示循环最多高 10 分，难题收益最大 | 内测、无样本与统计口径；“最多 10 分”是上限，不是平均值 |
| 验证成本下降 | 测试、基准、规格、端到端运行原本昂贵，现在可让 Agent 生成；生成后作为软件反复运行，不再大量消耗 token | 生成测试仍要人判断“测得对不对”；文章把“能生成”和“测得准”分得不够开 |
| 闭环要回写 | 若 Agent 反复在某条日志检查上失败，就加 hook 或写进 `CLAUDE.md`，让同类问题不再出现 | 与 R0031 “把失误变成规则”同源；规则会累积，文章后文也承认要定期清理 |

**三类测试**（正文 “Not all tests are created equal”）

| 测试 | 怎么用 | 强在哪 | 边界 |
|---|---|---|---|
| E2E | 描述真实用户流程；用 CDP、模拟器或 API harness 驱动真实系统；feature map 可当评分规则与路径说明 | 难以糊弄，功能要么成立要么不成立，失败能给具体证据 | 慢、贵、样本少；依赖环境稳定，环境坏时误报 |
| 属性测试 | 先写下“不可能失败”的陈述，再用 fast-check / Hypothesis / proptest 生成上千输入试图反证 | 能覆盖人想不到的边缘情况，尤其适合重写与规格漂移 | 找到反例不等于证明正确；属性本身写错就会空转 |
| 差分测试 | 新旧系统同输入跑，比较输出；用随机输入或生产流量样本；归一化空白等无关差异，维护“批准的变化”清单 | 迁移时把旧系统当 oracle，行为差异直接可见 | 只适用于“行为应保持不变”；新旧系统同错时看不出 |

失败模式：flaky 测试会训练 Agent 重跑而不是修代码；慢测试会减少批量测试的次数、让定位变难；重测试应放在提交前。

**团队做法**（正文 “How the Claude Code team thinks about verification”）

| 做法 | 具体内容 | 本库判断与注意点 |
|---|---|---|
| 验证等于运行改动 | 用 Chrome 扩展、iOS/Android MCP、computer use 或本地服务跑整条路径；把启动与检查写成 `verify` 技能，放在 `.claude/skills/`，越贴近代码越好 | 与 R0004 的验证技能同向；文章要求把 verify 技能做到快而可靠 |
| 失败要人 | Claude 跑检查并尝试修；同一检查三轮仍失败就停下找人 | 与 R0031 的三轮上限一致；“三轮”是团队经验值 |
| owner 写检查 | 拥有代码的人写检查，并调到能标出 owner 自己会标的问题；检查拉人时说明原因 | 责任跟着代码走，避免“检查是别人的事” |
| 可靠性清单按 diff 触发 | 39 项清单，每项有可从 diff 读出的触发器、检查与背后事故；Claude 每次只查匹配的 3–10 项 | 把事故记忆变成可查询的条目；39 与 3–10 均未公开 |
| 一个 reviewer 多轮 | 不叠加第二个更贵的 reviewer，而是调主 reviewer；`REVIEW.md` 说明本仓库该看什么；每轮带上一轮的上下文与失败 | 与 R0031 “不靠加 reviewer”相同；省成本、要求主 reviewer 够准 |
| 变更不能改自己的检查 | Code Review 从 base/默认分支读 `REVIEW.md`，不读 PR 里的改动；review 只针对 commit，推送后旧结果作废；先跑便宜检查，PR 前跑测试、构建、lint（用 hook 或 `/goal` 强制） | 全文最可直接借用的一条；也解释了为什么“评审通过”要绑定到具体 commit |
| 新门先观察 | 每个 commit 打“如何验证”的标记（含 `none`）；commit gate 分 off / observe / enforce；observe 只记录本会拦下的；enforce 允许 commit message 写明理由绕过，同会话被拦两次后放行 | 分阶段上线的具体形态；两条豁免规则是为避免 Agent 卡死，也留下滥用空间 |
| 用重要的事测检查 | 看 revert 数、maintainer 拒绝的改动、以及“干净子集”；正式 eval 重建 repo 到评审时状态、给一句话答案键、用已合并且稳定的改动作控制、tuning 集与测试集分开；分别统计 raw findings、验证后、最终评审的召回；每个发现标 Important / Nit / Pre-existing；召回调到“下一次改进就会过拟合”为止 | 把评测当系统做；这是 R0031 评测方法的更细版本，但数字仍未公开 |
| 把 miss 变成规则 | 从人工评审评论与 revert 中提取模式，要求至少在两个 PR 出现且能从 diff 识别；让三个 agent 试着反驳，再经人审 PR 批准。另一法是拿三个 bug finder 重放已知事故 PR，至少两个找到才算“可检测”；小 diff 也漏才算规则缺口。flaky 测试不许 skip、加 sleep 或重试到通过；找不到根因就删测试并写下原因；规则本身也要定期清理 | 规则有准入、有反证、有人审、有退出；这套治理比“多写几条规则”重要得多 |

## 关键摘要的原文依据

| 关键摘要 | 性质 | 原文依据 | 本库判断与证据缺口 |
|---|---|---|---|
| Claude Code 团队约 90% 代码由 Claude 写与审 | 团队自述（背景） | 开头第一段 “~90%”；链接 claude.dev 的评审文章 | 口径（行数或 PR 数）未给；属团队自述 |
| 没有验证循环只能跑一两个 Claude，有了可跑几十上百 | 作者陈述（推论） | 开头 “Without them, you can really only run one or two Claudes…” | 未给并行实测或失败率；是规模主张不是测量 |
| 独立 grader 让任务成功率最多提高 10 分 | 团队内部测试 | 开头 “improved task success by up to 10 points”；链接 managed agents 文章 | 无样本、任务集与统计口径；“最多”是上限 |
| 三类测试值得投入：E2E、属性、差分 | 作者主张 | “3 tests worth investing in” 三个小标题 | 是经验排序，不是对照实验 |
| flaky 与慢测试会训练出错误行为 | 作者陈述 | “If your tests are flaky…” 段 | 机制解释合理，但无数据 |
| 验证意味着运行改动，而非只看测试 | 团队做法 | “Verification means running the change”；verify skill 段 | 依赖可启动的完整环境；文中未谈环境维护成本 |
| 检查三轮失败后交人 | 团队做法 | “If a check is still failing after three rounds, Claude stops…” | 轮次是团队经验值；无逃逸率数据 |
| 可靠性清单 39 项，Claude 只查匹配的 3–10 项 | 团队做法 | “39 items…usually 3 to 10” | 清单未公开，无法核对触发条件质量 |
| 变更不能修改评判自己的检查，评审绑定 commit | 机制规则 | “Changes can't modify their own checks”；`REVIEW.md` 从 base 分支读 | 可直接借鉴；豁免与绕过路径文中已承认存在 |
| commit gate 有 off / observe / enforce，两次拦截后放行 | 团队做法（新门上线方式） | “Start a new gate in observe mode” | 观察期长度、误报率未给 |
| 用 revert 与干净子集给 reviewer 打分，调 recall 到接近过拟合 | 团队做法（评测） | “Test your checks on what actually matters” | 方法可借；数字与数据集仍未公开 |
| 把 miss 变成规则要经反证与人审，flaky 找不到根因就删 | 团队做法（规则治理） | “Turn misses into rules” | 与 R0031 的规则维护同源；删除测试是强主张，需按项目判断 |

## 标签与相关问题

**标签**：[外部验证](../../tags/外部验证.md) · [验证技能](../../tags/验证技能.md) · [E2E测试](../../tags/E2E测试.md) · [自动化闭环](../../tags/自动化闭环.md) · [Agent评测](../../tags/Agent评测.md) · [多Agent协作](../../tags/多Agent协作.md)

- [Agent 写完代码后，怎样让它自己运行应用并验证改动？](../../problems/Agent如何自行验证应用.md)：本文把“跑起来”写成 verify 技能，并给出启动方式与快慢要求。
- [AI 写的测试全绿，怎样判断它真能抓到缺陷？](../../problems/AI测试是否真能查错.md)：三类测试的选择、revert 与干净子集评分、召回调参，都在回答“怎么知道检查有效”。
- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：失败三轮交人、commit gate 的 observe 与 enforce、豁免规则。
- [自检怎样保持独立视角，并检查当前 diff 以外的影响？](../../problems/独立自检如何组织.md)：一个 reviewer 多轮、检查从 base 分支读、评审绑定 commit。
- [代码变更后，怎样选择回归测试，又说明没测到什么？](../../problems/变更后如何选择回归测试.md)：E2E、属性、差分三类测试各自的适用条件与代价。

## 接下来读哪篇

- [R0031：How the Claude Code team does code review](../R0031/README.md)：同一团队的前一篇，讲评审分层；本篇讲验证反馈，两篇合起来才是“写—验—审”的完整链条。
- [R0004：pstack 指南 Pt. 1](../R0004/README.md)：验证技能与功能地图的实现步骤，可补本篇“建 verify 技能”缺的操作细节。
- [R0020：awesome-qa-skills](../R0020/README.md)：回归选择与任务结果、轨迹测试，补“测试该选哪些”的一面。
- [R0022：Harness engineering](../R0022/README.md)：可观察环境与架构检查，补“验证信号从哪来”。

## 回正文定位

| 想查的内容 | 定位词 |
|---|---|
| 规模与并行前提 | `~90%`；`dozens or hundreds in parallel` |
| 独立评分的收益 | `up to 10 points`；`separate grader` |
| 测试成本变化 | `What was once expensive to verify` |
| 闭环回写 | `hook or a more explicit rule in your CLAUDE.md` |
| 三类测试总入口 | `Not all tests are created equal` |
| 失败模式 | `flaky`；`slow` |
| E2E | `E2E tests`；`difficult to fool`；`feature map` |
| 属性测试 | `Property tests`；`Round-trip encoding`；`Idempotency` |
| 差分测试 | `Differential tests`；`old system is the oracle` |
| 运行即验证 | `Verification means running the change`；`verify` skill |
| 失败交人 | `three rounds` |
| owner 写检查 | `Code owners write their own checks` |
| 可靠性清单 | `39 items`；`3 to 10` |
| 一个 reviewer | `One reviewer, multiple rounds`；`REVIEW.md` |
| 检查不可自改 | `Changes can't modify their own checks`；`base or default branch` |
| 新门观察期 | `observe mode`；`off, observe, and enforce` |
| 评测检查本身 | `Test your checks on what actually matters`；`recall` |
| 失误变规则 | `Turn misses into rules`；`bug finders` |
| 结论 | `Good tests, good results.` |

## 适用边界与查漏补缺

- **作者已确认，团队口径未拆分**：作者记为 Addy Osmani（用户 2026-11-17 确认），正文以 Claude Code 团队第一人称写作，文中未说明哪些工作由他本人完成，也没有共同作者名单。引用时可写“Addy Osmani（Claude Code 团队口径，X Article）”。
- **数字均属团队自述**：90%、10 分、39 项、3–10 项、三轮，均无可公开核对的样本、窗口或口径；不能当行业基准。
- **大规模前提**：并行几十上百个 Claude、commit gate、可靠性清单、评审评测集，都建立在团队规模与内部工具链上；小团队照搬会先被维护成本压垮。
- **评测方法强但贵**：重建 repo 状态、人工答案键、tuning/test 分离，是正规做法，也意味着持续投入；文章没讨论这套评测自身的维护成本。
- **“删掉 flaky 测试”是强主张**：只在找不到根因时使用，且要写下原因；不能读成“测试不稳就删”。
- 未核验的引用材料：claude.dev 的评审文章与 R0031 的关系、claude.com/blog 的 managed agents 与 verification loops 文章、`code.claude.com/docs` 的 hooks / goal / code-review 文档、三类测试库的具体用法，本库均未打开。
- 本库未在实践中采用任何做法，也没有用户项目的 revert 率、评审轮次或并行数据。

## 对已有知识的影响

- 补齐 R0031 的“验证”半边：R0031 讲评审如何分层，本篇讲检查如何产生、如何证明检查本身有效。
- 与 R0004 / R0005 / R0016 的验证技能线合并后，“怎么让 Agent 验证”已有操作步骤、信任条件与团队门禁三种粒度；暂不新建综合页，因为取舍尚未在用户项目中验证。
- 对问题页的影响：在“Agent 如何自行验证应用”“AI 测试是否真能查错”“可信自动化闭环怎么建”“独立自检如何组织”“变更后如何选择回归测试”五页各补一条补充参考。
- 未修改任何现有摘要或问题页结论；R0031 的“六层检查”与本篇的“三类测试”是不同层面，不能互相替代。

## 我的笔记与实践

未记录。AI 已阅读并整理，不代表用户已读、理解或采用。
