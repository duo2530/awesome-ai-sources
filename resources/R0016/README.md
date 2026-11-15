# pstack（cursor/plugins 子目录）

[← 全部内容](../README.md) · [来源](../../sources/S0012.md) · [作者](../../authors/A0003.md)

- 内容编号：R0016
- 原链接：https://github.com/cursor/plugins/tree/main/pstack
- 发布来源：[GitHub / cursor（S0012）](../../sources/S0012.md)
- 平台：GitHub
- 形式：代码仓库子目录 / Agent 插件
- 所属仓库：https://github.com/cursor/plugins
- 收录范围：pstack/；不将整个插件市场或其他插件视为已收录
- 仓库所有者：cursor（仓库 API 类型 Organization）
- 作者与维护者：插件清单 author 为 Lauren Tan，README 自述为 @poteto；关联 [A0003](../../authors/A0003.md)。完整维护者名单未核验，不以 cursor 组织代替个人作者
- 原文发布日期：不适用（代码仓库）
- 日期依据：所属仓库 API、固定 commit、子目录插件清单与 LICENSE；不同日期与范围分别记录
- 所属仓库创建时间：2026-01-23 01:57:42 UTC（created_at；不是 pstack 子项目创建时间）
- pstack 创建日期：未核验
- 首次版本发布日期：未核验
- 收录日期：2026-11-15
- 内容处理：已读 README、插件清单、许可证与两个验证技能文件；未安装、未实践
- 我的阅读：未记录
- 留存理由：用户提供链接；与已收录 pstack 指南关联，个人具体采用目的未记录

## 一眼了解

pstack 是一组工程工作流技能、原则和 Agent 定义。README 把 poteto-mode 作为任务入口，根据任务选择 playbook，再调用调查、设计、验证或审查能力。其目标是先提高单个任务的工程质量，再开展可验证的并行工作；这是项目定位，不是本库测量结果。

本轮重点读了“如何为具体项目建立并维护验证能力”：从真实启动与交互方式出发，生成项目本地验证技能、证据规则和 Feature Map，随后用源码核对与真实运行维护它们。可与 pstack Pt. 1 的方法说明对照阅读。

## 阅读依据

- 最近阅读日期：2026-11-15
- 用户链接分支 / 默认分支：main
- 固定 commit：[`bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7`](https://github.com/cursor/plugins/commit/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7)
- 此 commit 提交时间：2026-11-15 03:36:17 UTC（整个仓库的 commit，不代表 pstack 最后一次变更）
- 插件清单版本：0.15.42（pstack/plugin.json 与 pstack/.cursor-plugin/plugin.json 一致；不是已核验 release）
- 已读：仓库元数据、根目录及 pstack 目录列表、递归文件路径列表、pstack/README.md、两份插件清单、pstack/LICENSE、create-verification-skill/SKILL.md、maintain-verification-skill/SKILL.md。
- 所属仓库 README 本次用于定位 pstack 所在的插件市场，未深入研究其他插件说明。
- 未读：poteto-mode 正文、各 playbook 正文、其他技能、示例及辅助脚本、测试实现、适配器正文、发布历史。
- 方式：GitHub 连接只读获取，没有克隆；上游技能中的操作步骤仅作为研究材料。

## 关键入口与摘要（AI 整理）

| 文件 | 用途与要点 | 本次范围 |
|---|---|---|
| [README.md](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/README.md) | 工作流入口、技能目录、原则索引、分发与外部依赖 | 已读 |
| [.cursor-plugin/plugin.json](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/.cursor-plugin/plugin.json) | Cursor 插件名称、版本、作者及 skills/、agents/ 入口 | 已读；同时核对 plugin.json |
| [create-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/skills/create-verification-skill/SKILL.md) | 先调查项目的运行、驱动、观察及实例隔离，再生成 Launch、Doctor、Drive、Evidence、Cleanup 等说明；建立最初 3—5 个功能的地图，并实际跑通其中一个功能 | 已读，未读引用的 Feature Map 示例 |
| [maintain-verification-skill/SKILL.md](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/skills/maintain-verification-skill/SKILL.md) | 维护时每个功能都要有源码与实际运行覆盖；区分文档漂移、控制工具缺口和产品回归；修改范围限验证技能自身目录 | 已读，未执行 |
| [poteto-mode/SKILL.md](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/skills/poteto-mode/SKILL.md) | README 所述任务路由与工程原则入口 | 推荐后续阅读，目标正文未读 |
| [docs/guide/README.md](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/docs/guide/README.md) | README 指向的首次任务指南 | 推荐后续阅读，目标正文未读 |
| [LICENSE](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/LICENSE) | 子目录 MIT 许可证，版权署名 Lauren Tan | 已读 |

生成与维护的验证范围不同：生成流程要求跑通一个映射功能，维护流程要求覆盖每个功能。不能把一次生成成功写成全部功能已经验证。维护流程还明确：产品回归应报告，不能通过修改文档把它掩盖成正常行为。

## 作者关系

固定版本 README 以第一人称链接到 https://x.com/poteto，两份插件清单及 LICENSE 署名 Lauren Tan。因此与已收录的 lauren / @poteto 作者档案关联。README 关于 Meta、Netflix、Cursor 和 React Compiler 的经历属于本人公开自述，本轮没有独立核验雇主、职级或团队任职。

## 标签与相关问题

**标签**：[验证技能](../../tags/验证技能.md) · [Agent 工具设计](../../tags/Agent工具设计.md) · [按需上下文](../../tags/按需上下文.md)

- [Agent 如何自行验证应用？](../../problems/Agent如何自行验证应用.md)：从 create-verification-skill 的项目调查和生成流程入手。
- [Agent 如何找到应用功能？](../../problems/Agent如何找到应用功能.md)：看 Feature Map 的用户路径、可观察结果，以及维护流程。

## 适用条件与限制

- README 说明 pstack 不打包所有依赖：control-cli、control-ui、deslop 在 cursor-team-kit，部分能力依赖 Cursor。不能假定安装 pstack 就有完整应用控制环境。
- README 描述 Claude Code 使用仓库另一处生成的 harness/pstack 副本和适配器；本轮收录的是 pstack/，未审生成副本或验证跨平台一致性。
- 自动合并、定时任务、Slack 自动化、多模型调用和并行执行仅为上游文档内容；本轮没有配置或执行。
- MIT 依据是 pstack/LICENSE，不将它推广为整个 cursor/plugins 仓库或其他插件的许可证。
- 仓库 API 查询时未标记 archived；不据此保证成熟度、模型适配或持续维护。
- 固定版本清单号、main commit 和正式发布版本分开；首个 release 和当前稳定版未核验。

## 更新关注

未配置自动采集。后续关注 pstack 子目录变化、验证技能与示例的关系、外部依赖以及适配器差异；所属仓库有新 commit 不一定表示 pstack 更新。

## 关联阅读

- [R0004：pstack Pt. 1](../R0004/README.md)：先理解验证基础设施，再看生成与维护技能的具体写法。
- [R0006：pstack Pt. 2](../R0006/README.md)：补充实现前的调查、原型与架构选择；本轮未审对应技能全文。
- [R0015：mattpocock/skills](../R0015/README.md)：对照可组合工程技能的组织方式；TDD 的行为测试与实际应用路径验证可相互补充。

补充：[R0017：Cloudflare security-audit-skill](../R0017/README.md) 展示漏洞候选反证、覆盖台账与独立复核，可对照功能验证的证据组织方式。

## 我的笔记与实践

未记录。未安装、克隆、执行技能或生成用户项目的验证环境；无需粘贴正文。
