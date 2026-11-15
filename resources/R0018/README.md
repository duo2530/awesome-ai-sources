# Tencent LoopForge

[← 全部内容](../README.md) · [来源](../../sources/S0014.md)

- 内容编号：R0018
- 原链接：https://github.com/Tencent/LoopForge
- 发布来源：[GitHub / Tencent（S0014）](../../sources/S0014.md)
- 平台：GitHub
- 形式：代码仓库 / Agent 软件交付平台
- 仓库所有者：Tencent（GitHub API 类型 Organization）
- 作者与维护者：LICENSE 版权署名 Tencent；本轮未核验具体个人作者与完整维护者名单
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库 API、commit API、固定版本 LICENSE；创建、提交与阅读时间分别维护
- 仓库创建时间：2026-07-28 03:51:01 UTC（created_at）
- 首次版本发布日期：未核验
- 收录日期：2026-11-15
- 内容处理：已读 README、架构、公开范围、验证记录与许可证；未审业务源码、未运行
- 我的阅读：未记录
- 留存理由：用户提供链接；具体采用目的未记录

## 一眼了解

按项目说明，LoopForge 是自托管的编码 Agent 工作空间与软件交付平台。Main Bot 可以在聊天中创建工作空间、调用项目角色并交付变更；已验证有效的工作方式可整理成 SOP，用固定阶段、检查与人工确认重复执行。

它编排已有编码 CLI，围绕执行过程组织角色、沙箱、状态、产物、审批与历史。另有面向个人 IDE/CLI 的 LoopForge Local；平台版的自定义 SOP 不能据此视为已能直接导出到 Local 执行。

## 阅读依据

- 最近阅读日期：2026-11-15
- 默认分支：main
- 固定 commit：[`dd56585276d8ecb6e0d6865f55e255194d75f85a`](https://github.com/Tencent/LoopForge/commit/dd56585276d8ecb6e0d6865f55e255194d75f85a)
- 此 commit 提交时间：2026-11-14 22:02:50 UTC
- 已读：仓库元数据、根目录列表、README.md、LICENSE、docs/architecture.md、docs/open-source-scope.md、docs/validation.md。
- 未读：业务源码与测试实现、部署指南全文、Local 指南全文、第三方完整声明、发布历史与当前 CI 结果。
- 方式：GitHub 连接只读获取；未克隆、安装、执行或调用模型服务。

## AI 摘要

| 关注点 | 文档描述 | 可以研究的问题 |
|---|---|---|
| 聊天与固定流程 | 聊天适合探索和迭代，SOP 适合可重复交付，两者关联同一需求 | 怎样把临时操作沉淀成稳定流程 |
| SOP 节点 | Agent、Script、Human gate、Sub-SOP、Preview build；按依赖推进，支持退回、重试与重跑 | 哪些步骤交给模型、脚本或人 |
| 角色分离 | 规划、实现、审查、测试各自配置提示词、执行器、模型与工具 | 怎样减少同一 Agent 自我验收 |
| 状态与产物 | 节点状态、工具轨迹、日志、产物快照与审批入口 | 怎样定位卡点并恢复执行 |
| 平台与 Local | 平台有共享工作空间和自定义 SOP；Local 有独立内置工作流及宿主集成 | 团队协调与个人工作流分别适合什么 |
| 验证记录 | 历史记录区分源码检查、运行环境版本与外部服务覆盖，保留失败和跳过范围 | 如何避免把“测试通过”扩大成全部能力已验证 |

README 列出多种编码 CLI，但不同功能和执行环境支持范围不同。例如部分辅助功能仍限定 CodeBuddy，部分 CLI 未装入 SOP 沙箱；不能把执行器名单理解为所有功能具有相同适配程度。

## 关键入口

所有链接固定到本次 commit；推荐后续阅读不表示目标正文已读。

| 路径 | 为什么值得看 | 本轮范围 |
|---|---|---|
| [README.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/README.md) | 聊天 / SOP 两条路径、节点、运行前提和 Local 差异 | 已读 |
| [docs/architecture.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/docs/architecture.md) | engine、repo、httpapi、runtime、runner 等职责；公共版沿用原有执行与持久化契约 | 已读 |
| [docs/open-source-scope.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/docs/open-source-scope.md) | 公开代码、平台资产和私有部署内容的界线 | 已读 |
| [docs/validation.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/docs/validation.md) | 历史验证日期、失败修复、跳过项及实测范围 | 已读；未读取其本地原始日志 |
| [docs/deployment.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/docs/deployment.md) | 账号、Docker、远程执行及接入边界 | README 引出，推荐后续阅读 |
| [docs/local/usage.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/docs/local/usage.md) / [editions.md](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/docs/local/editions.md) | Local 宿主入口与 Classic / Portable 差异 | README 引出，推荐后续阅读 |
| [LICENSE](https://github.com/Tencent/LoopForge/blob/dd56585276d8ecb6e0d6865f55e255194d75f85a/LICENSE) | MIT 条款、Tencent 署名及第三方归属说明 | 已读 |

架构文档说明 Go 模块名 agentflow、AGENTFLOW_ 环境变量和部分兼容字段被保留，目的是减少上游同步冲突。它是理解旧命名的线索，不据此推断全部历史来源或私有系统细节。

## 标签与相关问题

**标签**：[自动化闭环](../../tags/自动化闭环.md) · [多 Agent 协作](../../tags/多Agent协作.md) · [运行时治理](../../tags/运行时治理.md)

- [怎样建立可信的自动化闭环？](../../problems/可信自动化闭环怎么建.md)：关注节点产物、脚本检查、人工门与退回。
- [并行会话太多，怎样协调？](../../problems/并行会话太多如何协调.md)：对照角色、SOP、共享运行状态与审批入口。

## 适用条件与限制

- 平台默认 Compose 路径使用 Docker，模型任务还需要对应凭据；文档提供不调用模型的脚本加人工审批演示。Local 的文档前提是 Node.js 20+、Python 3.8+ 与编码助手。本库未验证环境兼容性。
- README 明确默认 Docker socket 接入授予宿主 daemon 控制能力，部署面向可信团队，不作为不可信多租户隔离方案；账号可见范围、注册和首次管理员设置需按部署文档核对。
- docs/validation.md 明确其结果来自 2026-10-16 历史候选版本，不能认证本次 11 月 commit。部分付费模型、外部服务、多机运行与系统环境没有完整实测，本库没有重跑。
- README 所述平台 SOP 导出为独立 Local 工作流仍为计划；两者运行资产按架构文档分别维护。
- GitHub API 许可证识别为 Other / NOASSERTION，但实际 LICENSE 明确主体采用 MIT，并列第三方原始条款与 superpowers 归属；不把 API 分类当作无许可证，也不把主体许可扩展为全部依赖的统一许可。本轮未逐项审核 THIRD_PARTY_NOTICES.md。
- 当前 main commit 与稳定发布版本分开，首次 release、当前稳定版未核验；查询时未 archived 不代表成熟度或维护承诺。

## 更新关注

未配置自动采集。后续关注 SOP 恢复与审批语义、执行器适配范围、平台 / Local 的边界和当前版本验证证据；更新时记录新 commit，不沿用历史测试结论。

## 关联阅读

- [R0014：KiroCrew](../R0014/README.md)：比较持久工作空间、会话与调度的组织方式；两个项目都只做了文档阅读。
- [R0009：端到端交付2.0](../R0009/README.md)：对照标准产物、独立检查与阶段衔接，平台功能不能直接证明文章流程已在用户项目落地。

补充：[R0019：AI-DLC workflows](../R0019/README.md)，对照原生编码宿主工作流与平台 SOP 的组织方式；两者均未在本库运行。

## 我的笔记与实践

未记录。未部署或运行，没有创建审批、SOP 或外部变更；无需正文文件。
