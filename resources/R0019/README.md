# awslabs/aidlc-workflows — AI-DLC

[← 全部内容](../README.md) · [来源](../../sources/S0015.md)

- 内容编号：R0019
- 原链接：https://github.com/awslabs/aidlc-workflows
- 发布来源：[GitHub / awslabs（S0015）](../../sources/S0015.md)
- 平台：GitHub
- 形式：代码仓库 / AI 驱动研发工作流
- 仓库所有者：awslabs（GitHub API 类型 Organization）
- 作者与维护者：LICENSE 版权署名 Amazon.com, Inc. or its affiliates；具体个人作者与完整维护者名单未核验
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库 API、commit API、固定版本 README 与 LICENSE；日期分别维护
- 仓库创建时间：2025-11-13 22:05:08 UTC（created_at）
- 首次版本发布日期：未核验
- 收录日期：2026-11-15
- 内容处理：已读 README、工作流档位、用户介绍、开发参考索引与许可证；未审引擎源码、未运行
- 我的阅读：未记录
- 留存理由：用户提供链接；具体采用目的未记录

## 一眼了解

AI-DLC（AI-Driven Development Life Cycle）把 AI 辅助开发组织成可重复、可追踪的生命周期。按当前文档，一套宿主无关的 core 方法与引擎，经薄适配层在 Claude Code、Kiro、Codex、Cursor、opencode 和 GitHub Copilot 等宿主运行。

它关注需求、设计、实现、测试和运行阶段之间的连接，以及状态、审计和人工审批。不同任务选择不同 workflow profile（引擎称 scope），而非所有任务固定走完整流程。这是文档定位与设计描述，尚未验证各宿主实际执行效果。

## 阅读依据

- 最近阅读日期：2026-11-15
- 默认分支：main
- 固定 commit：[`8c4f79b4b77c5a64738b01b350be2bf72c357dae`](https://github.com/awslabs/aidlc-workflows/commit/8c4f79b4b77c5a64738b01b350be2bf72c357dae)
- 此 commit 提交时间：2026-11-15 02:21:40 UTC
- README 版本标识：2.11.4；未另核验 release、安装包和当前稳定版本
- 已读：仓库元数据、根目录列表、README.md、LICENSE、docs/guide/00-introduction.md、docs/guide/workflow-profiles.md、docs/reference/00-overview.md。
- 未读：核心引擎、阶段定义、hooks、适配器和测试实现、各宿主指南全文、规范 PDF、发布历史。
- 方法：GitHub 连接只读获取，没有克隆、安装、配置项目或运行工作流；上游命令仅作为资料。

## AI 摘要

| 关注点 | 文档中的组织方式 | 阅读价值 |
|---|---|---|
| 阶段与产物 | 5 个阶段、33 个 stage，阶段文件描述输入、步骤、输出和负责人 | 研究需求与交付证据如何衔接 |
| 引擎与执行会话 | 确定性 engine 决定下一步与停止条件，conductor 执行阶段、提出问题和展示决定 | 区分路由控制与模型执行质量 |
| 工作流档位 | 11 个预置 profile，可按任务建议或组合路线；scope 存入状态 | 避免小任务套用过重流程 |
| 角色与协作 | 11 个领域专家、2 个 reviewer、1 个 composer；多数阶段 inline，少数使用委派拓扑 | 不把角色总数理解为所有阶段同时运行的 Agent 数 |
| 状态与审计 | aidlc-state.md 保存状态，intent 的 audit 分片记录决定 | 研究跨会话恢复与追踪 |
| 单一核心与适配 | core 是手写方法与引擎来源；harness 提供宿主集成，dist 输出为生成结果 | 理解复用边界和版本差异 |

### 流程怎样按任务变化

以下数字来自本次 workflow-profiles 文档，仅指 Initialization 的 3 个设置阶段之后的静态路线，条件阶段仍可能跳过。

| Profile | 主要用途 | 设置之后的阶段数 |
|---|---|---:|
| PoC | 验证可行性 | 5 |
| Bugfix | 已知缺陷与回归检查 | 6 |
| Express | 需求已清楚的轻量实现与测试 | 7 |
| Classic | 侧重 Inception 与 Construction，结束于构建测试 | 15 |
| Feature | 完整生产功能生命周期 | 30 |
| Enterprise | 高保障与完整追溯 | 30 |

档位不仅改变阶段数量，也改变默认产物深度、测试策略、review 上限与附加仪式。Express 明确跳过设计与 Unit 拆分，并关闭阶段 reviewer 派发；它不适合含糊、跨团队或架构复杂的任务。完整路线也不代表所有模式有相同强度的审查。

Construction 的执行顺序与审批策略分别设置：新建、产出源码的 solo Unit 流程默认逐 Unit 串行；适用条件下首个 Unit 可作为真实集成的 walking skeleton。自动继续与并行执行不自动取消计划批准、验证命令选择等决定。具体行为需结合当前 profile、配置和宿主验证。

## 关键入口

链接固定到本次 commit；推荐后续阅读不表示目标正文已读。

| 路径 | 为什么值得看 | 本轮范围 |
|---|---|---|
| [README.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/README.md) | 定位、宿主、安装方式与文档导航 | 已读 |
| [docs/guide/00-introduction.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/docs/guide/00-introduction.md) | engine / conductor、阶段、角色与协作拓扑 | 已读 |
| [docs/guide/workflow-profiles.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/docs/guide/workflow-profiles.md) | 档位适用边界、阶段数、默认策略和 Construction 审批 | 已读 |
| [docs/reference/00-overview.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/docs/reference/00-overview.md) | 区分方法配置、实现修改与宿主生成产物 | 已读索引，章节正文未读 |
| [docs/guide/05-scopes-and-depth.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/docs/guide/05-scopes-and-depth.md) | 精确阶段矩阵与覆盖设置语义 | 文档引出，推荐后续阅读 |
| [docs/reference/17-skill-system.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/docs/reference/17-skill-system.md) | next / report / park 引擎契约与编排机制 | 文档引出，推荐后续阅读 |
| [docs/guide/10-state-and-audit.md](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/docs/guide/10-state-and-audit.md) | 状态与审计的使用方式 | 文档引出，推荐后续阅读 |
| [LICENSE](https://github.com/awslabs/aidlc-workflows/blob/8c4f79b4b77c5a64738b01b350be2bf72c357dae/LICENSE) | MIT No Attribution，标识 MIT-0 | 已读 |

## 标签与相关问题

**标签**：[规范驱动开发](../../tags/规范驱动开发.md) · [需求澄清](../../tags/需求澄清.md) · [自动化闭环](../../tags/自动化闭环.md)

- [AI 原生 SDLC 应该从哪里开始？](../../problems/AI原生SDLC从哪里开始.md)：先比较 profile，选择合适范围，不先追求最大阶段数。
- [需求与方案如何先验证？](../../problems/需求与方案如何先验证.md)：需求含糊时与需求已清楚时，采用的发现、设计和确认步骤不同。

## 适用条件与限制

- 文档描述本机安装包包含运行所需原生命令，手动复制 runtime 路径需要 Bun；不同宿主还依赖自身版本、信任配置、工具与模型接入。本轮没有核验这些前提。
- 核心方法声称与模型提供商无关，模型访问仍由宿主管理；不能把支持宿主名单理解为所有环境行为、权限与性能完全一致。
- README 的 2.11.4 与 main commit 分别记录，未把最新源码视为已发布安装包。文档还提示 Kiro 的 harness 命名在历史版本间发生变化，使用旧教程需核对版本。
- 角色数、阶段数与审计事件数是当前文档配置说明，不是效率或正确率指标；审批与确定性路由也不能独立保证生成代码满足需求。
- LICENSE 实际标识 MIT No Attribution（MIT-0），与普通 MIT 分开记录；本轮未审第三方依赖完整许可证。
- 查询时仓库未标记 archived；首次 release、当前 CI、实际恢复效果和全宿主兼容性未核验。

## 更新关注

未配置自动采集。后续关注阶段与 profile 矩阵、默认审批策略、引擎契约与宿主映射变化；重读时记录新 commit，不将旧流程结论自动套给新版。

## 关联阅读

- [R0012：The AI-native SDLC playbook](../R0012/README.md)：对照六阶段建议与本仓库可配置的五阶段工作流，两者分类不同，不强行一一等同。
- [R0018：LoopForge](../R0018/README.md)：对照平台 SOP 与原生宿主工作流的组织方式，按实际协调需求比较。
- [R0008：端到端业务需求专家 Agent](../R0008/README.md)：对照需求澄清、阶段人工确认与产物沉淀。

## 我的笔记与实践

未记录。未运行工作流、启动子 Agent 或修改宿主设置；无需正文文件。
