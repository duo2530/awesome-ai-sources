# 多 Agent 协作

[← 标签](README.md) · [问题索引](../problems/README.md)

检索词：并行会话、协调、队列、调度、流水线、Crew Mode。

- [R0013：Kiro Crew 软件工厂案例](../resources/R0013/README.md)：从多标签页、共享记忆到队列流水线和动态协调，区分阶段能力与瓶颈。

相关问题：[并行会话太多，怎样降低人工协调成本？](../problems/并行会话太多如何协调.md)


- [R0014：KiroCrew 仓库](../resources/R0014/README.md)：固定版本 README 描述持久会话、隔离与委派，组件实现尚未审读。

- [R0017：Cloudflare security-audit-skill](../resources/R0017/README.md)：按覆盖单元分配搜索任务，为独立复核预留预算，明确不完整结果。

- [R0018：LoopForge](../resources/R0018/README.md)：角色复用、依赖节点与共享运行状态；平台及个人 Local 适用范围分别记录。

- [R0021：大仓 Harness 实战](../resources/R0021/README.md)：串行场景删除未用到独有能力的 Team Mode，保留认知分工与同步调用。

- [R0026：dsh-superagent-prototype](../resources/R0026/README.md)：主会话路由、各 Ticket 执行会话、追问归属与 worker slots；尚未核验源码和并发正确性。

- [R0001：Agent Harness 工程实践](../resources/R0001/README.md)：模式 1、3、5：Initializer/Executor 经文件接力、Sub-Agent 只带自己的工具、审查换独立 Context；经验是 Agent 不超过 3 个、Skill 可以无限加。

- [R0028：loopx](../resources/R0028/README.md)：注册 Agent 互为 peer，由 claim、lease、任务边界与类型化续接决定谁下一步行动，不设持久 leader。

- [R0029：orbi](../resources/R0029/README.md)：实现会话与独立评审会话分工，评审在同一会话内修复后交合并门禁。

- [R0030：Your coding agents made you a manager](../resources/R0030/README.md)：并行要按不重叠切片拆分，否则只是“一个五作者的 merge conflict”；提出编排税——超过前几个 Agent 后，每个新增都要更多注意力。

- [R0031：How the Claude Code team does code review](../resources/R0031/README.md)：多个 agent 并行找 bug、独立投票判定是否有效；也记录了 agent 作者与 agent 评审一夜互相触发 50 多轮的反面案例。

- [R0033：How the Claude Code team thinks about verification](../resources/R0033/README.md)：验证循环把并行上限从一两个提到几十上百，但不靠叠加更贵的 reviewer 提高质量。

- [R0037：All Code Is Slop (Except Mine)](../resources/R0037/README.md)：每个工程师像带几百上千个 Agent；Grokbot 的 connectors 与 routines 用于编排大规模 Agent，前提是代码库与门禁足够好。
