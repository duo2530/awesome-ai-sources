# mattpocock/skills — Skills For Real Engineers

[← 全部内容](../README.md) · [来源](../../sources/S0011.md) · [作者](../../authors/A0011.md)

- 内容编号：R0015
- 原链接：https://github.com/mattpocock/skills
- 发布来源：[GitHub / mattpocock（S0011）](../../sources/S0011.md)
- 平台：GitHub
- 形式：代码仓库 / Agent 技能集合
- 仓库所有者：mattpocock（GitHub API 类型 User）
- 作者与维护者：README 自述为个人日常使用的技能；LICENSE 署名 Matt Pocock，本次 commit 作者也映射到 @mattpocock。未核验完整维护者与贡献者名单
- 原文发布日期：不适用（代码仓库）
- 日期依据：GitHub 仓库与 commit API；创建、提交和阅读日期分别维护
- 仓库创建时间：2026-02-03 11:15:53 UTC（created_at）
- 首次版本发布日期：未核验
- 收录日期：2026-11-15
- 内容处理：已读 README、许可证与三个技能文件；未安装、未实践
- 我的阅读：未记录
- 留存理由：用户提供仓库链接；具体采用目的未记录

## 一眼了解

这是以 Markdown 技能文件组织的工程实践集合。README 主张技能应小、可修改、可组合，让使用者按需组织研发过程；主要覆盖需求对齐、领域术语、规格与任务拆分、实现、测试、审查及交接。

它适合作为“如何把工程经验写成 Agent 可重复遵循的步骤”的参考。它提供流程文本，不等于已经为某个项目建好测试环境，也不能仅凭技能描述判断执行效果。

## 阅读依据

- 最近阅读日期：2026-11-15
- 默认分支：main
- 固定 commit：[`5863806dd4e15c63174bee4e7515a4256792ecfa`](https://github.com/mattpocock/skills/commit/5863806dd4e15c63174bee4e7515a4256792ecfa)
- 此 commit 提交时间：2026-11-12 08:42:38 UTC
- 已读：仓库元数据、根目录列表、README.md、LICENSE、grill-with-docs/SKILL.md、tdd/SKILL.md、writing-for-agents/SKILL.md。
- 未读：其他技能正文、上述技能引用的附属文件、插件实现、脚本、测试与版本发布历史。
- 方法：GitHub 连接只读获取；上游技能是研究材料，其指令未作为本次任务指令执行。

## 摘要与关键入口（AI 整理）

| 文件 | 本轮认识与用途 | 阅读范围 |
|---|---|---|
| [README.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/README.md) | 从需求误解、术语不统一、反馈不足和架构复杂化切入；区分用户调用的编排技能与可由模型按需使用的基础技能 | 已读 |
| [grill-with-docs/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/grill-with-docs/SKILL.md) | 文件本身很短，只转交 grilling 与 domain-modeling 两个技能；适合研究“入口如何组合基础能力” | 已读入口，未读两个被调用技能正文 |
| [tdd/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/tdd/SKILL.md) | 通过公共接口验证行为，先约定测试边界；一次一个失败测试与最小实现，避免测试耦合内部结构或照抄实现逻辑 | 已读，未读 tests.md、mocking.md 等附属参考 |
| [writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/productivity/writing-for-agents/SKILL.md) | 明确指针触发条件、步骤完成标准、渐进披露和单一事实来源；区分常驻上下文成本与人的导航成本 | 已读，未读 SKILL-MECHANICS.md |
| [to-spec/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-spec/SKILL.md) | README 描述为将已有对话综合成规格 | 仅 README 索引，目标未读 |
| [to-tickets/SKILL.md](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/to-tickets/SKILL.md) | README 描述为拆分可逐步交付的任务并声明阻塞关系 | 仅 README 索引，目标未读 |
| [LICENSE](https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE) | MIT，版权署名 Matt Pocock | 已读 |

阅读时注意版本细节：README 用 red-green-refactor 概括测试流程，但本次 tdd 文件把重构安排到 review 阶段，而非每轮 red→green 内。后续采用应核对具体技能及其引用文件，不把首页概括当成完整规范。

## 标签与相关问题

**标签**：[需求澄清](../../tags/需求澄清.md) · [验证技能](../../tags/验证技能.md) · [按需上下文](../../tags/按需上下文.md)

- [需求与方案如何先验证？](../../problems/需求与方案如何先验证.md)：先从 README 的对齐思路和技能入口关系看起。
- [项目资料如何按需读取？](../../problems/项目资料如何按需读取.md)：优先读 writing-for-agents 的 Context pointers 与 Information hierarchy。
- [Agent 如何自行验证应用？](../../problems/Agent如何自行验证应用.md)：tdd 补测试设计纪律；应用操作与环境搭建仍需其他材料。

## 适用条件与限制

- README 提供插件和可编辑文件两类分发路径，提醒同一 Agent 同时使用两种会重复安装技能；本次只记录文档描述，未执行安装或设置。
- 技能可能依赖其他技能、附属文档、项目术语表、问题跟踪器或工具；只读单个 SKILL.md 不代表完整掌握其调用链。
- 项目声称适用于不同模型；本库没有模型适配与实际效果对照。
- 固定版本 LICENSE 为 MIT；复制或实质性复用时应保留其版权与许可声明。
- 查询时未标记 archived；这不等于稳定性、质量或未来维护承诺。当前固定到 main commit，未核验稳定发布版本。

## 更新关注

未配置自动采集。后续关注技能路径、调用关系、用户/模型调用边界及配套参考变化；重读时记录新 commit，与当前依据比较。

## 关联阅读

- [R0003：长期业务系统的项目说明结构](../R0003/README.md)：对照关键文件指针与按需加载的写法。
- [R0006：pstack Pt. 2](../R0006/README.md)：对照实现前的需求复述、调查与方案验证。
- [R0004：pstack Pt. 1](../R0004/README.md)：补充实际应用的操作与验证工具入口，与 tdd 的测试纪律配合阅读。

补充：[R0016：pstack 插件目录](../R0016/README.md)，对照项目级验证技能与工程工作流的组织方式。

## 我的笔记与实践

未记录。未克隆、安装或运行任何技能；无需另建正文文件。
