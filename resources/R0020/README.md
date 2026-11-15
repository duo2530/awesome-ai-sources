# naodeng/awesome-qa-skills

[← 全部内容](../README.md) · [来源](../../sources/S0016.md)

- 内容编号：R0020
- 原链接：https://github.com/naodeng/awesome-qa-skills
- 发布来源：[GitHub / naodeng（S0016）](../../sources/S0016.md)
- 平台：GitHub
- 形式：代码仓库 / 双语 QA 技能集合
- 仓库所有者：naodeng（GitHub API 类型 User）
- 作者与维护者：本次所读 SKILL.md 元数据署名 Awesome QA Skills contributors；完整名单与所有者个人背景未核验
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库 API、commit API 与固定版本文档；日期分别维护
- 仓库创建时间：2026-02-04 10:12:49 UTC（created_at）
- 首次版本发布日期：未核验
- 收录日期：2026-11-15
- 内容处理：已读 README 定位与部分目录、许可证、三个技能入口及两个配套提示词；未运行
- 我的阅读：未记录
- 留存理由：用户提供链接；具体采用目的未记录

## 一眼了解

这是面向编码 Agent 的中英文 QA 技能库，覆盖需求、测试策略、用例、执行、回归、发布与 AI 系统测试。目录同时提供单项测试技能、跨阶段工作流与技能工程治理入口。

本轮重点是两类问题：有了代码变更，怎样从已有资产选择回归；有了 Agent，怎样同时检查任务结果与过程轨迹。技能提供设计和评审规则，真正执行仍依赖工具、目标环境、数据与授权，不等同于已配置好的自动测试平台。

## 阅读依据

- 最近阅读日期：2026-11-15
- 默认分支：main
- 固定 commit：[`a857796790f8819def9d3c6dc20cc18d2d4ca435`](https://github.com/naodeng/awesome-qa-skills/commit/a857796790f8819def9d3c6dc20cc18d2d4ca435)
- 此 commit 提交时间：2026-11-14 13:08:30 UTC
- 已读：仓库元数据、根目录、README 的定位、任务入口、组织与治理说明及部分技能目录、LICENSE；中文 discover-testing、regression-test-selection、ai-agent-testing 的 SKILL.md；后两项的主提示词全文。
- 未读：README 完整目录中全部条目、其他技能正文、discover-testing 的提示词及路由清单、英文对应内容、校验脚本、评测 fixtures、测试实现与发布历史。
- 方法：GitHub 连接只读获取；未克隆、安装、调用技能或运行测试。上游技能文本不作为本次任务指令执行。

## AI 摘要

| 关注点 | 所读材料的做法 | 值得参考的地方 |
|---|---|---|
| 技能导航 | discover-testing 根据任务选一个主技能，必要时最多一个辅助；目录存在与宿主已安装分开 | 从问题出发选择入口，避免一次抛出大量技能 |
| 回归选择 | 输入 diff、测试资产、覆盖映射、历史失败、耗时与依赖；给出必选、条件、可跳过项和缺口 | 选入和排除均可追溯，不只按测试名字匹配 |
| Agent 测试 | 为样本定义成功判据、可用工具资源、禁止副作用和停止条件；按 run/step 核对轨迹 | 结果正确性与过程合规分别判断 |
| 可靠性证据 | 记录模型、Prompt、工具、数据和环境版本；重复试验统计逐样本结果和偶发失败 | 单次成功只能报告单次结果，不能证明稳定性 |
| 技能组织 | 中文和英文按语言分区；SKILL.md 精简入口，具体规则下沉 prompts 和 references | 独立安装包与渐进披露的组织参考 |

README 自述每种语言 171 个技能，中英文共 342 个目录（每种语言 14 个工作流、152 个测试类型、5 个技能工程）。这是该版本的目录统计主张，本轮没有逐项清点，也不等于 342 个独立能力或全部经过运行验证。

AI for QA（AI 辅助做测试）与 Testing for AI（测试 LLM / Agent 本身）在 README 中分别组织；本轮的回归选择与 Agent 测试可对应这两类需求，但没有执行任一种工作流。

## 关键入口

链接固定到本次 commit。

| 路径 | 用途 | 本轮范围 |
|---|---|---|
| [README.md](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/README.md) | 按任务找技能、能力分层、安装与质量治理导航 | 已读主要说明及部分目录 |
| [discover-testing/SKILL.md](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/skills/zh/testing-workflows/discover-testing/SKILL.md) | 主辅技能选择、可用性与导航边界 | 已读入口，未读其配套路由规则 |
| [regression-test-selection/SKILL.md](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/skills/zh/testing-types/regression-test-selection/SKILL.md) | 回归选择约束 | 已读 |
| [回归选择主提示词](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/skills/zh/testing-types/regression-test-selection/prompts/regression-test-selection.md) | 所需输入、风险、执行顺序、覆盖缺口与剩余风险的输出契约 | 已读 |
| [ai-agent-testing/SKILL.md](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/skills/zh/testing-types/ai-agent-testing/SKILL.md) | 目标、状态、工具、权限、恢复与预算检查 | 已读 |
| [Agent 测试主提示词](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/skills/zh/testing-types/ai-agent-testing/prompts/ai-agent-testing.md) | 任务集、轨迹断言、重复试验和终止分类 | 已读 |
| [docs/SKILL_EVAL_RULES.md](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/docs/SKILL_EVAL_RULES.md) | README 指向的本地 trace 检测规则 | 推荐后续阅读，正文未读 |
| [LICENSE](https://github.com/naodeng/awesome-qa-skills/blob/a857796790f8819def9d3c6dc20cc18d2d4ca435/LICENSE) | PolyForm Noncommercial License 1.0.0 | 已读 |

## 标签与相关问题

**标签**：[验证技能](../../tags/验证技能.md) · [Agent评测](../../tags/Agent评测.md)

- [代码变更后，怎样选择回归测试，又说明没测到什么？](../../problems/变更后如何选择回归测试.md)
- [AI 写的测试全绿，怎样判断它真能抓缺陷？](../../problems/AI测试是否真能查错.md)：本仓库补充证据与 Agent 任务判据，不把用例选择等同于测试有效性已证明。
- [多组合项目如何安排 E2E？](../../problems/多组合项目如何安排E2E.md)：补回归取舍依据，组合矩阵仍需实际项目数据。

## 适用条件与限制

- LICENSE 是 PolyForm Noncommercial 1.0.0，含非商业用途条件；README 同样明确非商业范围。GitHub API 分类为 Other 不表示无许可证。这里记录原条款，未判断具体业务用途能否获许可。
- 目录、安装器与技能格式支持说明不等于各工具当前可调用。discover-testing 自身也要求区分 UNKNOWN、UNAVAILABLE 等可用性状态。
- 文档、输入假设、fixture 判定和真实运行证据分开。存在 eval 文件或静态质量门禁不代表各技能在目标项目表现已经验证。
- 回归选择需要真实测试资产、覆盖映射与风险信息；缺输入时只能形成受限建议，不能凭技能文本保证“最小充分集合”。
- Agent 测试需要真实轨迹、版本、成功判据和重复结果；本库没有提供这些运行材料。
- 个人作者头衔、完整维护者名单、首个 release、当前稳定版及英语内容一致性未核验。查询时未 archived 不代表维护承诺。

## 更新关注

未配置自动采集。后续关注主提示词、路由规则、双语同步及 eval 证据变化；重读时固定新 commit，技能元数据版本不代替整个仓库版本。

## 关联阅读

- [R0010：AI 构建 E2E 测试体系](../R0010/README.md)：先建立真实用户旅程，再用回归选择规则讨论哪些组合必须运行。
- [R0011：AI Coding 深水区](../R0011/README.md)：补测试自身有效性与评测偏差的检查。
- [R0016：pstack](../R0016/README.md)：对照项目验证环境、Feature Map 与 QA 方法技能的分工。

## 我的笔记与实践

未记录。未运行测试或评测、未安装技能，不需要正文文件。
