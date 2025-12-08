# Erdős Problem #14 — Roadmap and Task List (H2)

- **Problem:** Erdős Problem #14  
- **Official link:** https://www.erdosproblems.com/14  
- **Project H-level:** H2  
- **Internal name:** Unique 2-Sum Density Problem

This file tracks the **engineering-style progress** on Problem #14, in the same spirit as for Problem #1. The goal is to reach a comparable level of “project completeness” (结构 + 能量框架 + FVD 原型)，但不提前宣称证明已经完成。

---

## 0. Current status snapshot

- [x] 选择本问题作为项目中的 **Problem #2**。
- [x] 完成基本结构分解：
  - 定义 \(r_A(n)\)、区域 \(Z_N,U_N,M_N\)。
  - 把目标改写成对 \(|Z_N|+|M_N|\) 的幂次下界问题。
- [x] 建立基本能量框架：
  - 定义 \(E(A)=\sum r_A(n)^2\)。
  - 推出 \(E(A)\ge |U_N|+4|M_N|\) 以及与 \(|Z_N|+|M_N|\) 的粗关联式。
- [x] 拟定“两端策略”：低能量 / 高能量 两种 regime。
- [ ] 还 **没有** 给出明确的幂次下界 \(c>0\)。
- [ ] 还 **没有** 完整形式的 FVD-14 定理，只是概念规划。

---

## 1. Phase A — 随机模型与基准（benchmark）

**目标：** 给出一些“典型构造”下 \(|Z_N|+|M_N|\) 的规模估计，用于设定合理的目标指数。

任务：

- [ ] 选择若干简单模型：
  - 稠密随机集：\(\mathbb{P}(n\in A)\approx p\)（例如 \(p=N^{-\alpha}\) 不同 \(\alpha\)）。
  - 稀疏模型：类似 Sidon / pseudo-Sidon 的稀疏集合。
- [ ] 对每个模型估算：
  - \(\mathbb{E} r_A(n)\)、\(\mathbb{E} r_A(n)^2\)、\(\mathbb{E} E(A)\)。
  - \(\mathbb{E}|Z_N|\)、\(\mathbb{E}|M_N|\) 的量级。
- [ ] 从这些估计中抽象出“自然指数”的候选：
  - 例如：随机模型是否自然给出 \(|Z_N|+|M_N|\sim N^{1/2}\) 的结构。
- [ ] 将结果整理成 `14-random-benchmarks.md`（可选新文件）。

---

## 2. Phase B — 低能量 ⇒ 大 \(Z_N\)（Near-Sidon 端）

**目标：** 在“能量不大”的前提下，证明 \(Z_N\) 至少有多项式规模。

任务：

- [ ] 设定一个“低能量阈值”函数 \(T_{\text{low}}(N)\)，例如 \(E(A)\le |A|^{2+\delta}\) 或类似形式。
- [ ] 用
  \[
  E(A)\ge \frac{|A|^4}{|A+A|}
  \]
  这类不等式，下界 \(|A+A|\)，从而控制 sumset 的密度。
- [ ] 把 sumset 的稠密/稀疏情况转成对 \([1,N]\setminus(A+A)\) 的下界；
  再进一步转成 \(Z_N\) 下界（不可表示区规模）。
- [ ] 在某个合理假设（例如 \(|A|\) 与 \(N\) 的关系）下，给出命题原型：
  - 若 \(E(A)\le T_{\text{low}}(N)\)，则 \(|Z_N|\ge N^{c_1}\)。
- [ ] 将推导过程写入 `14-structure-and-energy.md` 的新段落（Phase B）。

---

## 3. Phase C — 高能量 ⇒ 大 \(M_N\)（Collision 端）

**目标：** 在“能量很大”的前提下，证明 \(M_N\) 至少有多项式规模。

任务：

- [ ] 设定一个“高能量阈值”函数 \(T_{\text{high}}(N)\)，与 Phase B 的阈值配合。
- [ ] 在 \(E(A)\ge T_{\text{high}}(N)\) 的前提下，从
  \[
  E(A)\ge |U_N|+4|M_N|
  \]
  出发，排除“能量集中在区间外”的不利情形，得到 \(|M_N|\) 的下界。
- [ ] 目标形式：
  - 若 \(E(A)\ge T_{\text{high}}(N)\)，则 \(|M_N|\ge N^{c_2}\)。
- [ ] 将推导写入 `14-structure-and-energy.md`，用一个独立小节记录（Phase C）。

---

## 4. Phase D — 双端拼接：第一个明确幂次 \(c>0\)

**目标：** 把 Phase B（低能量）和 Phase C（高能量）拼起来，得到统一的全局下界：

> 存在 \(c>0\)，使得对所有 \(A\subseteq\mathbb{N}\) 和充分大 \(N\)，有  
> \[
> |Z_N|+|M_N| \ge N^c.
> \]

任务：

- [ ] 选择合适的阈值函数 \(T_{\text{low}}(N)\)、\(T_{\text{high}}(N)\)，并证明：
  - 对所有 \(A\)，要么 \(E(A)\le T_{\text{low}}(N)\)，要么 \(E(A)\ge T_{\text{high}}(N)\)，
    或者用一族重叠区间覆盖。
- [ ] 在两种情形中分别应用 Phase B 和 Phase C 得到下界：
  \[
  |Z_N|+|M_N|\ge N^{c_1}\quad\text{或}\quad |Z_N|+|M_N|\ge N^{c_2}.
  \]
- [ ] 取 \(c := \min(c_1,c_2)\) 得到统一的幂次 \(c>0\)。
- [ ] 在 `14-structure-and-energy.md` 中增加“Proposition (first exponent lower bound)”小节，**清晰标注为“已证明 / 进行中 / 猜想”**。

> 说明：这一阶段的目标是拿到 **任何** 明确的 \(c>0\)，而不是直接追求 conjectural 的 \(1/2\)。后续可在这个基础上迭代改进。

---

## 5. Phase E — FVD-14（Finite Verification Domain，Problem #14 版）

**目标：** 模仿 Problem #1 的 FVD 框架，为 Problem #14 构造一个“有限验证域”形式化定理。

任务：

- [ ] 定义局部结构块：
  - 在长度 \(L\) 的短区间上，记录 \(r_A(n)\) 或其压缩信息（例如只记录 \(0,1,\ge2\) 三值）。
- [ ] 证明：任何满足一定“全局条件”的集合 \(A\)，在每个长度 \(L\) 的区间上都落入有限个局部结构类型之一。
- [ ] 设计 FVD-14 的形式定理（草案形态）：
  - **Reduction Theorem (FVD-14 v1.0)：**  
    若对所有局部结构类型 \(\mathcal{T}\)，在某个有限范围内（比如 \([1,N_0]\)）都可以验证
    \[
    |Z_{N_0}|+|M_{N_0}| \ge C N_0^{1/2},
    \]
    则对所有 \(N\) 结论成立。
- [ ] 将定义与定理草案写入新文件（例如 `14-FVD.md`）。

---

## 6. Phase F — 文档化与对外版本

**目标：** 像 Problem #1 一样，把 Problem #14 的进展写成对外可读的版本（中文/英文）。

任务：

- [ ] 英文简版说明（for GitHub / research audience）：
  - 文件：`14-summary-en.md`
  - 内容：问题简介、结构剖分、能量框架、主要命题与 conjecture、FVD-14 思路。
- [ ] 中文长文（for 知乎）：
  - 文件：`14-summary-cn.md`（可与知乎文章主体共用）
  - 内容：用直观语言解释：
    - “唯一二元和”的意义；
    - 为什么这个问题接近 Sidon / 加法组合的核心；
    - 我们的结构和能量方法；
    - 当前已完成的阶段，以及下一步要做什么。

---

## 7. 标记规范与恢复接口

为了避免“下次忘记做到哪里”：

- 每次在编辑 `14-roadmap.md` 时：
  - 用 `[x]` / `[ ]` 标记任务是否完成。
  - 在对应文件（比如 `14-structure-and-energy.md`）顶部附一行“Last updated: YYYY-MM-DD”。
- 作为恢复口令：
  - 当我们之后需要恢复项目状态，可以用一句：
    > 「恢复 Erdős Problem #14 的状态」  
  - 然后根据本文件的勾选状态和对应 `.md` 内容继续推进。

