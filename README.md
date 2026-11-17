# AI 学习资源库

以具体账号、频道、博客和官方文档站为来源，持续收录 AI 研发资料。先留下链接，再保存正文、整理摘要，最后把资料关联到实际问题。

[信息源](sources/README.md) · [作者](authors/README.md) · [全部内容](resources/README.md) · [综合](synthesis/README.md) · [标签](tags/README.md) · [带着问题找参考](problems/README.md) · [维护日志](log.md) · [维护流程](WORKFLOW.md)

## 我在关注的信息源

| 信息源 | 平台 | 已收录 | 来源入口 |
|---|---|---:|---|
| Felix Rieseberg 的个人博客 | 独立网站 | 1 篇 | [来源记录](sources/S0002.md) · [作者背景](authors/A0001.md) |
| X / @uudonX | X | 1 条 | [来源记录](sources/S0003.md) · [作者背景](authors/A0002.md) |
| X / lauren（@poteto） | X | 4 条 | [来源记录](sources/S0004.md) · [作者背景](authors/A0003.md) |
| 千问AI平台 | 微信公众号 | 4 篇 | [来源记录](sources/S0005.md) |
| vikingz.me 博客（名称待确认） | 独立网站 | 1 篇 | [来源记录](sources/S0006.md) |
| 腾讯技术工程 | 微信公众号 | 2 篇 | [来源记录](sources/S0007.md) |
| Claude / Resources Articles | 独立网站 | 2 篇 | [来源记录](sources/S0008.md) |
| Kiro Blog | 独立网站 | 1 篇 | [来源记录](sources/S0009.md) |
| GitHub / kirodotdev | GitHub | 1 个仓库 | [来源记录](sources/S0010.md) |
| GitHub / mattpocock | GitHub | 1 个仓库 | [来源记录](sources/S0011.md) · [作者背景](authors/A0011.md) |
| GitHub / cursor | GitHub | 1 条仓库子目录 | [来源记录](sources/S0012.md) · [作者背景](authors/A0003.md) |
| GitHub / cloudflare | GitHub | 1 个仓库 | [来源记录](sources/S0013.md) |
| GitHub / Tencent | GitHub | 1 个仓库 | [来源记录](sources/S0014.md) |
| GitHub / awslabs | GitHub | 1 个仓库 | [来源记录](sources/S0015.md) |
| GitHub / naodeng | GitHub | 1 个仓库 | [来源记录](sources/S0016.md) |
| OpenAI / Index | 独立网站 | 1 篇 | [来源记录](sources/S0018.md) · [作者背景](authors/A0014.md) |
| Gist / karpathy | GitHub Gist | 1 篇 | [来源记录](sources/S0020.md) · [作者背景](authors/A0017.md) |
| Paul Dix 的博客 | 独立网站 | 1 篇 | [来源记录](sources/S0021.md) · [作者背景](authors/A0018.md) |
| GitHub / deepseek-ai | GitHub | 1 个仓库 | [来源记录](sources/S0022.md) |
| Mitchell Hashimoto 的个人博客 | 独立网站 | 2 篇 | [来源记录](sources/S0023.md) · [作者背景](authors/A0020.md) |
| GitHub / loopx-project | GitHub | 1 个仓库 | [来源记录](sources/S0024.md) |
| GitHub / orbi-build | GitHub | 1 个仓库 | [来源记录](sources/S0025.md) |
| X / @addyosmani | X | 2 条 | [来源记录](sources/S0026.md) · [作者背景](authors/A0021.md) |
| claude.dev | 独立网站 | 1 篇 | [来源记录](sources/S0027.md) |
| Anthropic Research | 独立网站 | 1 篇 | [来源记录](sources/S0028.md) |
| Jane Street Blog | 独立网站 | 0 篇 | [来源记录](sources/S0029.md) |
| Anthropic Engineering | 独立网站 | 1 篇（正文待提供） | [来源记录](sources/S0030.md) |
| YouTube / AI Engineer | YouTube | 1 条 | [来源记录](sources/S0031.md) |

## 已整理，可以开始读

- [综合：长时程 Agent 的状态与控制面](synthesis/T0001-长时程Agent的状态与控制面.md)（2026-11-15）：对照 loopx 与 orbi 两条路线，把“状态放哪里”的取舍、共同的人工门与共同的证据缺口收在一页；随新资料修订。

- [How the Claude Code team thinks about verification](resources/R0033/README.md)（2026-11-17）：E2E 优先、属性与差分测试补边界，再用 verify 技能、失败三轮交人、检查不可自改与 observe 门放开并行；数字为团队自述。

- [Vibing a Non-Trivial Ghostty Feature](resources/R0034/README.md)（2025-10-11）：逐会话公开 16 次 agent 协作，保留撞墙、弃用与人工接管；[用 AI 提效后怎样保住技能？](problems/用AI提效后如何保住技能.md)

- [How AI assistance impacts the formation of coding skills](resources/R0032/README.md)（2026-01-29）：52 人随机对照实验显示 AI 辅助降低任务后掌握度、速度提升不显著；[用 AI 提效后怎样保住技能？](problems/用AI提效后如何保住技能.md)

- [How the Claude Code team does code review](resources/R0031/README.md)（2026-10-15）：六层检查加回滚线、用事故当评测集、评审必须收敛；三位作者合署，数字为团队自述。

- [Your coding agents made you a manager](resources/R0030/README.md)（2026-11-08）：把带团队的做法搬到带 Agent，11 节“最佳实践 / 反模式”，并自陈类比的七处边界；[约束何时下沉](problems/提示词约束何时下沉.md)

- [orbi-build/orbi](resources/R0029/README.md)：给 GitHub Issue 打 `ai-ready` 标签，走到独立评审、合并与发布；只有 reviewed head 能合并，失败即标 `ai-blocked` 交人。已读 README，未审源码。

- [loopx-project/loopx](resources/R0028/README.md)：与宿主无关的长时程 Agent 控制面，把 Goal、证据、配额与租约放在持久状态里；作者自陈不是生产控制器。已读 README，未审源码。

- [My AI Adoption Journey](resources/R0027/README.md)（2026-02-05）：Harness Engineering 的一手出处；六步采纳史，作者自认仍在半路，且明确不并行跑多 Agent。

- [DeepSeek dsh-superagent 研究原型](resources/R0026/README.md)：单仓库事件、授权任务、会话执行与待人工处理面板；非正式产品，已读文档，未审源码或运行。

- [The end of programming](resources/R0025/README.md)（2026-08-25，用户提供）：作者关于编程工作方式的预测及两个未发布实验；[AI 原型怎样走向生产？](problems/AI原型如何走向生产.md)

- [LLM Wiki：Karpathy 的个人知识库模式](resources/R0024/README.md)（2026-04-04）：原始材料、生成知识与维护规则分层，收录、查询回存与巡检。

- [直播数据 LLM Wiki 实践](resources/R0023/README.md)（2026-06-26）：来源治理、结构化页面、关系图与检索；[散落资料怎样形成可追溯知识库？](problems/散落资料如何形成可追溯知识库.md)

- [Harness engineering：OpenAI 团队实践](resources/R0022/README.md)（2026-02-11）：可观察环境、AGENTS.md 导航、架构检查与持续清理；对照 TAB 的人工关卡取舍。

- [从 Vibe Coding 到 Harness：大仓实战](resources/R0021/README.md)（2026-07-07）：角色契约、门禁基线与删除无收益 Team Mode 的复盘。

- [awesome-qa-skills](resources/R0020/README.md)：双语 QA 技能与工作流，重点整理回归选择和 Agent 结果、轨迹测试；[怎样选择回归并说明缺口？](problems/变更后如何选择回归测试.md)

- [awslabs/aidlc-workflows](resources/R0019/README.md)：一套核心适配多个编码宿主，按任务选择工作流范围；已读档位、阶段与审批说明，未运行。

- [Tencent LoopForge](resources/R0018/README.md)：聊天工作空间、角色与 SOP 交付，区分团队平台和个人 Local；已读文档，未部署。

- [Cloudflare security-audit-skill](resources/R0017/README.md)：覆盖台账、候选反证、独立复核和结构化报告；[怎样减少 AI 安全审计误报？](problems/AI安全审计如何减少误报.md)

- [pstack 插件目录](resources/R0016/README.md)：关联 pstack 指南，已读验证技能生成与维护流程，作者署名 Lauren Tan。

- [mattpocock/skills](resources/R0015/README.md)：可组合的工程技能；已读需求对齐入口、TDD 与面向 Agent 的文档写法。

- [KiroCrew 代码仓库](resources/R0014/README.md)：已读固定版本的文档、目录与维护者信息；从会话、记忆和治理入口继续查实现。

- [Kiro Crew 软件工厂案例](resources/R0013/README.md)（2026-09-18）：五阶段并行演进、协调瓶颈与治理；已关联三位作者及截图证据。

- [The AI-native SDLC playbook](resources/R0012/README.md)（2026-08-21，剪藏元数据）：六阶段交接、验证、治理与维护闭环。

- [AI Coding 深水区：编码让位，人退到哪里](resources/R0011/README.md)（2026-08-27）：框架与 runtime、评测题集、独立证据和人的判断。

- [我是怎样使用 AI 构建 E2E 测试体系的？](resources/R0010/README.md)（发布于 2026-06-06，用户提供）：关键用户旅程、浏览器预演与多组合回归。

- [端到端交付2.0](resources/R0009/README.md)：标准产物、独立自检、新旧代码规则边界与统计改进。

- [如何搭建一个端到端业务需求专家 Agent](resources/R0008/README.md)：需求澄清、人工确认门、证据验收与结项知识回收；[怎样让经验进入长期知识？](problems/过程经验如何沉淀长期知识.md)
- lauren 阅读路线：[可信闭环](resources/R0005/README.md) → [验证工具 Pt. 1](resources/R0004/README.md) → [调研与设计 Pt. 2](resources/R0006/README.md) → [工程环境视频（字幕摘要）](resources/R0007/README.md)。

- [《The Complete Guide to pstack Pt. 1》](resources/R0004/README.md)：可重复的验证工具、功能地图与持续维护。带着问题看：[Agent 如何自行验证？](problems/Agent如何自行验证应用.md) · [如何找到应用功能？](problems/Agent如何找到应用功能.md)
- [AGENTS.md：长期业务系统的项目说明结构参考](resources/R0003/README.md)：短帖与截图已归档，保留你的留存理由，可按项目说明、按需上下文和验证方式检索。
- [How to be more ambitious: A tutorial for humans with models](resources/R0002/README.md)：从目标、专业方法和跨领域视角拓展 AI 的用法。可查看作者背景、摘要、正文与可点击标签。
- [给野马套上缰绳：Agent Harness 工程实践](resources/R0001/README.md)（2026-06-30）：四条铁律、六个工程模式与钉钉 2 Agent + N Skill 的招聘案例；[反复提醒 Agent 仍犯错，约束何时下沉](problems/提示词约束何时下沉.md)
- 带着问题来：[怎样从小任务转向结果？](problems/从小任务转向结果.md) · [怎样做专业分析并验证？](problems/让AI做专业分析.md) · [怎样借助跨领域方法？](problems/借助跨领域方法.md)

## 下一步处理

本轮按 issue #8、#5 收录 [R0033](resources/R0033/README.md) 与 [R0034](resources/R0034/README.md)，两条都有正文与 AI 摘要。R0033 的作者已按用户确认记为 Addy Osmani（正文以团队第一人称写作）；R0032 的发布日期已按用户 2026-11-17 提供的 2026-01-29 补上，原页未打开核验。R0035 为历史索引迁入，R0036、R0037 为链接入库，三者的正文与字幕待提供。下一步是读正文、带问题检索，而不是补元信息。综合页目前只有 1 页，语义巡检按需执行，尚未配置定时任务。

## 如何开始

直接提供标题和原链接，知道账号或频道名称时一并提供。无需先想标签和摘要。

AI 会建立条目、返回正文文件位置；你粘贴正文后通知 AI，再补充摘要、标签、相关问题和推荐阅读。

也可以在 GitHub 提交 [建议收录资料 Issue](.github/ISSUE_TEMPLATE/suggest-resource.yaml)：只给标题、链接和留存理由，不必粘贴正文；Issue 只是候选，进入资料库前不计入收录。

**代码仓库也可以直接收录**：贴仓库名称、地址和留存理由即可。仓库使用独立的[收录与阅读流程](WORKFLOW.md#代码仓库收录与阅读流程)，记录用途、版本、关键目录和问题关系，不需要粘贴正文；默认不克隆或运行代码。

这里是正式资料库入口。早期设计样稿、模拟数据、旧索引副本与演练脚本已清除，本地只保留正式收录内容。

维护后运行 `python scripts/check_url.py --check-library`，只读检查状态、日期、内部链接、索引一致性与孤立页提醒；[检查范围与退出码](WORKFLOW.md#本地资料检查)。摘要中的原文依据用于追溯出处，问题页保留观点差异与证据缺口，综合页的“当前认识”是本库归纳，都不代表方法已经实践验证。

## 许可与来源

本库自行编写的脚本、模板、索引及整理文字采用 [MIT License](LICENSE)。收录或引用的第三方文章正文、字幕、截图、图片和代码片段不因收入本库而改用 MIT，相关权利与许可仍属于原作者或权利人；请以各条目的原链接、署名和上游许可为准。
