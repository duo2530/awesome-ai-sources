# AI 生成的代码和文档怎样持续清理，避免坏模式扩散？

[← 问题索引](README.md) · [架构约束](../tags/架构约束.md) · [知识沉淀](../tags/知识沉淀.md)

检索词：代码熵、文档漂移、技术债、golden principles、doc-gardening、持续清理。

## 先看什么

[R0022：Harness engineering](../resources/R0022/README.md)，先读 Entropy and garbage collection，再读 Enforcing architecture and taste 与 We made repository knowledge the system of record。

文章将人反复指出的问题沉淀成可检查原则，并周期性扫描、小步开修订 PR；文档还要检查新鲜度、结构和交叉链接。重点是减少坏模式被后续 Agent 复制，不以清理 PR 数量衡量效果。

## 可以先试什么

以下是 AI 据材料归纳的待实践建议：挑一种反复扩散的模式，明确正确边界和可观察检测条件；先用实际例子检查误报，再做一项可审阅的小修订。对文档明确维护者与关联代码，记录为什么修改，并确认修订没有改变预期行为。

## 还缺什么

本库没有用户项目的漂移基线、维护成本或错误修订数据。不要仅凭模式相似就批量改代码或自动合并；长期架构一致性与清理规则自身的正确性仍需验证。

## 关联参考

- [R0021：TAB 大仓 Harness 实战](../resources/R0021/README.md)：补可判定门禁、基线和团队知识责任。
- [哪些约束该下沉到工具？](提示词约束何时下沉.md)：先判断检查信号是否可靠，再选约束方式。

## 我的实践

未记录。本问题由资料归纳，不表示用户已经遇到或采用。
