# Cloudflare security-audit-skill

[← 全部内容](../README.md) · [来源](../../sources/S0013.md)

- 内容编号：R0017
- 原链接：https://github.com/cloudflare/security-audit-skill
- 发布来源：[GitHub / cloudflare（S0013）](../../sources/S0013.md)
- 平台：GitHub
- 形式：代码仓库 / 安全审计技能
- 仓库所有者：cloudflare（GitHub API 类型 Organization）
- 作者与维护者：LICENSE 版权署名 Cloudflare, Inc.；本轮未核验具体个人作者及完整维护者名单
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库 API、commit API 与固定版本 LICENSE；日期分别维护
- 仓库创建时间：2026-06-18 14:08:44 UTC（created_at）
- 首次版本发布日期：未核验
- 收录日期：2026-11-15
- 内容处理：已读 README、许可证、技能入口主要章节与验证报告流程；未审脚本实现、未执行
- 我的阅读：未记录
- 留存理由：用户提供仓库链接；具体采用目的未记录

## 一眼了解

这是面向代码仓库的防御性安全审计技能，以信任边界和具体影响作为漏洞判断基础，组织侦察、覆盖驱动搜索、候选验证、结构化记录、独立复核与报告六个阶段。README 将其描述为 Cloudflare 漏洞发现 harness 的单仓库起点；不是完整的大规模运行系统。

本库重点关注的是如何避免 AI 把猜测写成漏洞：审计范围有台账，候选有稳定指纹，验证者与发现者分离，最终报告从已复核记录生成。技能文本提供流程要求，实际覆盖率和误报率尚未在本库验证。

## 阅读依据

- 最近阅读日期：2026-11-15
- 默认分支：main
- 固定 commit：[`c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`](https://github.com/cloudflare/security-audit-skill/commit/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8)
- 此 commit 提交时间：2026-09-14 19:28:54 UTC
- 已读：仓库元数据、根目录及递归文件路径列表、README.md、LICENSE、skills/security-audit/SKILL.md 的主要章节、VALIDATION-AND-REPORTING.md。
- 未深入读取：侦察与搜索流程全文、各领域攻击类别、report-schema.json、两个校验器源码及测试、发布历史。
- 通过 GitHub 连接只读获取。技能是被研究的材料，没有安装、激活或按其要求启动审计与子 Agent。

## AI 摘要

| 关注点 | 文档中的做法 | 对本库问题的意义 |
|---|---|---|
| 范围与覆盖 | 先建立架构说明和 coverage-ledger，按范围、边界与攻击类别安排检查；区分 covered、candidate、blocked、deferred 等状态 | 没有发现漏洞不等于所有区域都检查过 |
| 独立候选验证 | 新验证者尝试推翻候选，重新读当前源代码和决定性证据 | 减少发现者自我确认，不把重复意见当独立证明 |
| 三种结论 | confirmed 需要完整源代码路径与有界观察结果；needs_validation 记录明确阻塞事实且不评严重性；rejected 保留被证伪的候选 | 将缺证据与已确认缺陷分开 |
| 记录与报告 | findings.json 按 schema 组织，复核最终记录后再生成 REPORT、FINDINGS-DETAIL、NEEDS-VALIDATION | 降低摘要与原始证据、结论不一致的风险 |
| 多次审计 | 比对当前源码、旧台账和旧结论；同根因保留指纹，源码改变后重新验证 | 历史结论不能直接当作当前版本已覆盖 |
| 预算与不完整结果 | 为复核和覆盖批评预留调用预算；未独立验证候选留在台账，不冒充 findings | 预算不足时报告缺口，不降低证据标准 |

quick 模式合并候选验证和最终记录检查，其他模式分开；独立复核要求仍保留。两种校验器通过只能证明格式和台账一致性，不能证明漏洞本身成立。

## 关键文件入口

以下路径固定到本次 commit；“目标未读”只表示推荐下一步入口。

| 文件 | 用途 | 本次范围 |
|---|---|---|
| [README.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md) | 六阶段总览、运行前提和文件导航 | 已读 |
| [SKILL.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) | guidance / full audit 模式、证据标准、范围、预算与流程总览 | 已读主要章节 |
| [VALIDATION-AND-REPORTING.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/VALIDATION-AND-REPORTING.md) | 候选反证、三种结论契约、最终复核及报告生成 | 已读 |
| [RECONNAISSANCE.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/RECONNAISSANCE.md) | 架构、边界和覆盖单元规划 | 目标未读 |
| [HUNTING.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/HUNTING.md) | 覆盖驱动搜索与覆盖缺口复查 | 目标未读 |
| [AI-AND-LLM.md](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/AI-AND-LLM.md) | README 所列提示注入、工具与输出处理审计方向 | 目标未读 |
| [report-schema.json](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/report-schema.json) | 结构化 findings 数据契约 | 目标未读 |
| [validate-findings.cjs](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-findings.cjs) / [validate-coverage-ledger.cjs](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/validate-coverage-ledger.cjs) | 记录与台账校验器 | 路径已确认，源码未审、未运行 |
| [LICENSE](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/LICENSE) | MIT，版权署名 Cloudflare, Inc. | 已读 |

## 标签与相关问题

**标签**：[安全审计](../../tags/安全审计.md) · [外部验证](../../tags/外部验证.md) · [多 Agent 协作](../../tags/多Agent协作.md)

- [怎样让 AI 审计代码，又避免把猜测当漏洞？](../../problems/AI安全审计如何减少误报.md)
- [独立自检如何组织？](../../problems/独立自检如何组织.md)：安全审计中的独立验证和结构化记录可作为特定场景参考，不等于一般研发自检的全部流程。

## 适用条件与限制

- README 要求支持工具和并行子 Agent 的编码 Agent，并使用 Node.js 运行零依赖校验器；本轮未核验平台兼容性。
- 文档要求被审目标的构建、测试和进程在具备网络、写入、环境变量和资源限制的 OS 沙箱中运行；条件不满足时保留明确待验证项。技能文本自身不提供已验证的通用沙箱实现。
- 审计以源码与有界本地证据为主，部署配置等不可见事实不得猜测。本库未审计任何目标，也没有生成 findings、台账或漏洞报告。
- README 的“单次发现约为多次总量一半”属于其测试陈述，样本与实验未在本轮核验，不作为普遍检出率。
- MIT 依据为固定版本 LICENSE；首次 release、当前稳定版本与完整维护名单未核验。
- 查询时仓库未标记 archived；不据此保证准确率、可运行性或持续维护。

## 更新关注

未配置自动采集。后续关注证据契约、覆盖台账、独立复核规则及校验器的同步变化，重读时记录新 commit，不将旧结论直接套给新版本。

## 关联阅读

- [R0009：端到端交付2.0](../R0009/README.md)：对照独立会话、自检范围与证据交付；本仓库进一步细化安全漏洞结论的标准。
- [R0016：pstack](../R0016/README.md)：对照真实用户路径验证与独立审查；功能正确和安全边界成立是不同检查目标。

## 我的笔记与实践

未记录。未克隆、安装或执行技能，未对本库或其他目标开展安全审计；无需正文文件。
