# loopx-project/loopx

[← 全部内容](../README.md) · [GitHub 来源](../../sources/S0024.md)

- 内容编号：R0028
- 原链接：https://github.com/loopx-project/loopx
- 发布来源：[GitHub / loopx-project（S0024）](../../sources/S0024.md)
- 平台：GitHub
- 形式：代码仓库 / 长时程 Agent 控制面
- 仓库所有者：loopx-project（GitHub 元数据为 Organization）
- 作者与维护者：README 自述由 [`@huangruiteng`](https://github.com/huangruiteng) 创建，版权署名为 LoopX contributors；个人角色与组织成员名单未核验，不以组织所有者代替个人作者
- 原文发布日期：不适用（代码仓库）
- 日期依据：仓库元数据与固定 commit；创建时间、提交时间与 release 时间分别记录
- 仓库创建时间：2026-05-31 14:58:56 UTC（GitHub created_at）
- 首次版本发布日期：未核验；README 列出 v1.0.0（2026-09-06）与 v2.0.0（2026-10-20），更早 release 未逐一核对
- 收录日期：2026-11-15
- 内容处理：已读 README 与仓库元数据；未读 docs、源码与基准数据，未安装未运行
- 我的阅读：未记录
- 留存理由：用户提供地址要求收录；后续关注长时程 Agent 的状态与证据管理

## 一眼了解

按 README，LoopX 不是又一个 Agent 框架或运行时，而是一个**与宿主无关的控制面**：Codex、Claude Code、DeepSeek Harness 等宿主负责跑模型与工具，LoopX 保存 Goal、待办、待决策项、证据、配额、租约与恢复记录，让跨会话、跨宿主的长期工作能继续。

2.0 起把事务、授权与恢复规则迁到 TypeScript，Python 保留宿主与 provider 的 IO；本地用 SQLite，团队路径延伸到 PostgreSQL。README 同时明确：**它不是自主生产控制器**，危险权限、发布、生产写入与最终归属仍归人。

本库判断：值得研究的是“状态、证据、配额、人工门”如何被拆成可检查的契约，以及它怎样把“一直有 Agent 在跑”与“有进展”区分开；不能凭“control plane”这个名字判断它已经解决了长时程可靠性。

## 阅读依据

- 最近阅读日期：2026-11-15
- 分支：main
- 固定 commit：[`c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e`](https://github.com/loopx-project/loopx/commit/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e)
- 该提交时间：2026-11-15T06:04:42Z
- 最新提交作者邮箱域名为 `bytedance.com`；仅记录元数据现象，未核验其任职或组织关系
- 已读取：仓库元数据、默认分支最新提交元数据、README 全文
- 未读取：`docs/` 下架构、配额、边界文档与 RFC；`loopx/` 源码与测试；`benchmark/` 数据文件；桌面端与插件包
- 方法：通过只读 HTTP 获取（`raw.githubusercontent.com` 在本机不可用，改用 jsDelivr 取同一 commit 的 README），不克隆、不安装、不执行

## 值得看哪些地方

以下路径按本次 commit 固定，除 README 外均为推荐后续阅读，尚未读。

| 路径或入口 | 为什么值得看 | 当前依据 |
|---|---|---|
| [README.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/README.md) | 定位声明、五类常驻子系统、证据与许可边界 | 已读 |
| [docs/architecture.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/docs/architecture.md) | Kernel / Capability / Provider / Extension 的职责划分 | 推荐，未读 |
| [docs/quota-allocation.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/docs/quota-allocation.md) | “这一轮该干、该问、该等还是该停”的判定 | 推荐，未读 |
| [docs/public-private-boundary.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/docs/public-private-boundary.md) | 可公开材料与私有产物的边界 | 推荐，未读 |
| [docs/guides/installing-loopx.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/docs/guides/installing-loopx.md) | 安装、升级与回滚的实际条件 | 推荐，未读 |
| [benchmark/LHTB/studies/five-arm-gpt56sol-max/README.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/benchmark/LHTB/studies/five-arm-gpt56sol-max/README.md) | 五项对照研究的方法与限制 | 推荐，未读 |
| [packages/dsh-loopx-plugin/README.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/packages/dsh-loopx-plugin/README.md) | 与 DeepSeek Harness 的实际接入方式 | 推荐，未读 |
| [examples/collaboration-delivery/README.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/examples/collaboration-delivery/README.md) | 三 Agent 协作交付的有界示例 | 推荐，未读 |

## 关键结论的依据

| 关键结论 | 性质 | 固定版本依据 | 本库判断与证据缺口 |
|---|---|---|---|
| LoopX 不执行模型，只保存跨会话的工作状态 | 项目自述 | [README.md](https://github.com/loopx-project/loopx/blob/c5ff8fdc32b6a6b806cf91f4c0154d912a381e8e/README.md) Why LoopX、Current Status | 与 R0001 铁律三“状态写文件”同向；但状态层的实际边界要看 `docs/architecture.md`，本轮未读 |
| 把常驻 Agent 拆成 Event Inbox、Timers、Memory、Permissions、Outbox 五类 | 项目自述，借用 Anthropic 的分类 | README Building 24/7 Always-On Agents 一节 | 分类来自引用文章，LoopX 声称打包成开放控制层；引用关系不等于实现等价 |
| LHTB 46 任务均分 0.4948，比 Plain Codex 高 17.3% | 项目自测 | README Evidence 表与脚注 | 作者自己写明：单次有效试验、部分替换试验预算更长、**不是等预算效率结论，也不是因果估计**；本库未复现 |
| 更严格的通过率并未随之提高 | 项目自测 | README：严格解 7/46（15.2%），与 Plain Codex 持平 | 均分增益包含部分完成度，不等于更多任务被真正解决 |
| “更多自我验证”未必带来更高分 | 项目自测（SWE-Marathon） | README Exploratory Benchmark Studies | 少见的反向发现，值得单独读方法与任务选择；不足以推翻验证手段的价值 |
| 基础使用统计默认开启 | 项目自述 | README First-Run Feedback 一节 | 可按设置或 `LOOPX_USAGE_PING=0` 关闭；企业评估应先确认，本轮未验证实际行为 |
| 不是自主生产控制器，发布与生产写入仍需人 | 项目声明（限制） | README Current Status、Advanced 折叠段 | 与 R0026 的研究原型声明态度一致；具体 gate 是否强制，需审代码与配置 |

## 标签与相关问题

**标签**：[自动化闭环](../../tags/自动化闭环.md) · [运行时治理](../../tags/运行时治理.md) · [多Agent协作](../../tags/多Agent协作.md) · [按需上下文](../../tags/按需上下文.md)

- [怎样让 Agent 自动处理反馈，又能在做错前停下来？](../../problems/可信自动化闭环怎么建.md)：配额判定、人工门与安全回退的文档参考。
- [并行会话太多如何协调？](../../problems/并行会话太多如何协调.md)：peer claims、租约、证据回写与 worker 归属。

## 适用条件与限制

- 运行要求：Python 3.11+、Node.js 22.22.3+（README 推荐 24 LTS）；安装方式为 `pip install loopx`。本轮未安装、未验证兼容性。
- 本地默认 SQLite，团队路径为 PostgreSQL；README 把 RBAC、SSO、配额与签名审计列在路线图，不视为已具备。
- 不提供凭据、不代替人批准破坏性操作、不代发内容；这套边界是项目自述，实际是否有硬性阻断需要读代码与配置。
- README 的性能与交付证据均为项目自测或用户自述（独立用户案例标注为“用户报告”），存在自选任务、单次试验与预算不等等问题，本库未独立复现。
- 星标 6.5k、fork 623、开放 issue 228 只说明关注度，不证明稳定性或维护质量；本轮未读 issue 与路线执行情况。
- 仓库体量较大（约 391 MB），包含多个子包与桌面端；本轮只读 README，不能据此判断代码质量、测试覆盖或依赖风险。
- Apache-2.0 从 `v0.4.8` 起生效，更早版本为 MIT；再分发需遵守 NOTICE、商标与署名要求，本库未做法务判断。
- 原文中的安装命令、插件安装与示例提示词仅作材料，本轮未执行。

## 更新关注

未配置自动采集。后续可对照固定 commit 追踪：控制面契约、配额判定、人工门强制方式、benchmark 方法变化，以及组织与资助信息；不把本次阅读结论自动套用到新版本。

## 关联阅读

- [R0026：dsh-superagent-prototype](../R0026/README.md)：同样区分事件、授权、任务与执行，但那是一个仓库的研究原型；本篇是跨宿主的控制面产品，两者不构成同一实现。
- [R0018：LoopForge](../R0018/README.md)：对照 SOP 与人工门的组织方式，场景与部署形态不同。
- [R0001：Agent Harness 工程实践](../R0001/README.md)：可对照“状态写文件、约束可执行”的主张，看控制面把哪些变成了契约。
- [R0027：My AI Adoption Journey](../R0027/README.md)：个人视角的常驻 Agent 实践；可与本篇的“大规模控制面”路线比较取舍。

## 我的笔记与实践

未记录；读 README 与装好运行、验证有效分别记录。
