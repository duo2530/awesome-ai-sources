# Agent 写完代码后，怎样让它自己运行应用并验证改动？

[← 问题索引](README.md) · [验证技能](../tags/验证技能.md) · [Agent 工具设计](../tags/Agent工具设计.md)

检索词：反复人工检查、自验证、应用控制、截图证据、调试、性能追踪、verification skill。

## 先看什么

1. [R0004：pstack 指南 Pt. 1](../resources/R0004/README.md)，定位 `Make it Reproducible` 和 `How to use your verification skill`：看应用控制 CLI、环境准备与具体验证路径。
2. [R0002：更有野心地使用模型](../resources/R0002/README.md)，定位 Depth 与外部评判：补充为什么要把结论交给可检查的反馈，而不是只看模型自述。
3. [R0003：项目说明结构](../resources/R0003/README.md)，看截图第 7 节：把项目适用的测试入口写入说明文件。

补充：[R0005](../resources/R0005/README.md) 看证据交接与停止条件；[R0007](../resources/R0007/README.md) 在 00:07:05—00:12:29 讨论验证工具。

补充：[R0010：AI 构建 E2E 测试体系](../resources/R0010/README.md) 给出从验收目录、浏览器预演到 Playwright 回归的具体流程，注意其本地运行选择是场景取舍。

## 可以先试什么

以下是据材料归纳的待实践建议：先选一个可稳定复现的功能，准备启动方式和测试身份，串联进入页面、操作、检查预期与保留证据。先验证这条路径可靠，再判断是否值得封装 CLI 或扩展云端并行；不是为所有项目先建一整套工具。

## 还缺什么

本库尚无用户项目的验证工具实现、覆盖率评估或实际效率对照。截图和界面交互不能覆盖全部业务逻辑；需要结合具体验收条件与适用测试。

## 仓库参考

[R0015：mattpocock/skills](../resources/R0015/README.md)：tdd 补公共接口测试与逐步反馈；没有为用户项目构建应用操作环境。

补充仓库参考：[R0016：pstack](../resources/R0016/README.md)。从 create-verification-skill 看项目调查、启动、健康检查、用户路径与证据；再读 maintain-verification-skill 看持续核验。 本库未为用户项目实际生成或验证。

## 我的实践

未记录。本文中的安装、云 Agent 和定时命令仅作为资料收录，没有执行。
