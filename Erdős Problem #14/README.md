# Erdős Problem #14 — Unique 2-Sum Density Problem

- **Erdős problem number:** 14  
- **Official page:** https://www.erdosproblems.com/14  
- **Status:** Open (as of 2025-09-14)  
- **Tags:** number theory, sidon sets, additive combinatorics  
- **Prize:** (see official Erdős problem database)  
- **Project H-level:** H2 (结构型加法组合问题，无范式跳跃)

## 1. Problem statement (from the official site)

Let \(A\subseteq \mathbb{N}\). Let \(B\subseteq \mathbb{N}\) be the set of integers which are representable in exactly one way as the sum of two elements from \(A\).

The questions are:

1. Is it true that for all \(\varepsilon>0\) and all sufficiently large \(N\),
   \[
   |\{1,\dots,N\}\setminus B|\ \gg_\varepsilon\ N^{1/2-\varepsilon}\ ?
   \]

2. Is it possible that
   \[
   |\{1,\dots,N\}\setminus B|\ = o(N^{1/2})\ ?
   \]

Informally: **how small can the set of integers _not_ representable in exactly one way as a 2-sum from \(A\) be, up to \(N\)?** :contentReference[oaicite:0]{index=0}

The official page also records constructions showing that, for certain sets \(A\),
\[
|\{1,\dots,N\}\setminus B| \ll_\varepsilon N^{1/2+\varepsilon},
\]
and that for all \(\varepsilon>0\) there exist infinitely many \(N\) with
\[
|\{1,\dots,N\}\setminus B| \gg_\varepsilon N^{1/3-\varepsilon},
\]
and discusses a finite analogue studied by Erdős and Freud. :contentReference[oaicite:1]{index=1}

---

## 2. Structural rephrasing

Define the **representation function**
\[
r_A(n) := \#\{(a,b)\in A^2 : a+b = n\}.
\]

Then:

- \(n\in B\) iff \(r_A(n)=1\).
- \(n\notin B\) iff \(r_A(n)=0\) (not representable) or \(r_A(n)\ge2\) (multiple representations).

For a given \(N\), we decompose:

- \(Z_N := \{1\le n\le N : r_A(n)=0\}\)  (unrepresentable zone)
- \(U_N := \{1\le n\le N : r_A(n)=1\}\)  (uniquely representable zone)
- \(M_N := \{1\le n\le N : r_A(n)\ge 2\}\) (multi-representable zone)

Thus
\[
[1,N] = Z_N \;\dot\cup\; U_N \;\dot\cup\; M_N,\qquad
|\{1,\dots,N\}\setminus B| = |Z_N| + |M_N|.
\]

Problem #14 is equivalently asking whether, for every \(A\subseteq\mathbb{N}\),

- one always has \(|Z_N|+|M_N|\ge N^{1/2-o(1)}\), and
- whether there exist \(A\) with \(|Z_N|+|M_N| = o(N^{1/2})\).

---

## 3. Energy framework

We introduce the **additive energy**
\[
E(A) := \sum_{n} r_A(n)^2.
\]

Basic facts:

- Total number of ordered 2-sums:
  \[
  \sum_n r_A(n) = |A|^2.
  \]
- By Cauchy–Schwarz,
  \[
  E(A) \;\ge\; \frac{|A|^4}{|A+A|},
  \]
  where \(A+A := \{a+b : a,b\in A\}\) is the sumset.

On the other hand, splitting over the three regions:

\[
E(A)
  = \sum_{n\in U_N} 1^2 \;+\; \sum_{n\in M_N} r_A(n)^2
    \;+\; \sum_{n\notin[1,N]} r_A(n)^2.
\]

Since every \(n\in M_N\) satisfies \(r_A(n)\ge2\), we get

\[
E(A) \;\ge\; |U_N| + 4 |M_N|.
\]

Together with \( |Z_N|+|M_N| = N - |U_N| - |M_N| \), this yields a first rough inequality relating energy and the size of the “bad set”
\(\{1,\dots,N\}\setminus B\):

\[
|\{1,\dots,N\}\setminus B|
  = |Z_N|+|M_N|
  = N - |U_N| - |M_N|
  \;\ge\; N - E(A) + 3|M_N|.
\]

This suggests a natural **two-regime strategy**:

1. **Low-energy regime** (near-Sidon):  
   \(E(A)\) small ⇒ \(A+A\) large ⇒ many gaps in \([1,2\max A]\) ⇒ \(Z_N\) large.

2. **High-energy regime** (many collisions):  
   \(E(A)\) large ⇒ strong lower bounds on \(|M_N|\) ⇒ \(M_N\) large.

Problem #14 asks whether, after quantifying this dichotomy and optimizing parameters, one can force \(|Z_N|+|M_N|\) to be at least \(N^{1/2-o(1)}\).

---

## 4. Relation to Problem #1 (Distinct Subset Sums)

In our project, Erdős Problem #1 (distinct subset sums) was attacked via:

- a structural partition of the representation function,
- an energy-based analysis,
- and the introduction of a **Finite Verification Domain (FVD)** that reduces the infinite problem to a finite catalogue of local configurations.

Problem #14 is structurally similar:

- representation function \(r_A(n)\) instead of subset-sum counts,
- a decomposition into three zones \((Z_N,U_N,M_N)\),
- and a natural energy \(E(A)\) controlling collisions of 2-sums.

Our aim is to reach **the same level of “project completeness” as for Problem #1**:

- a full structural and energy framework,
- a clean two-regime lower bound (low-energy vs high-energy),
- and an FVD-style reduction theorem for Problem #14.

At this stage, **we do not claim a proof of the full conjectured \(N^{1/2-o(1)}\) bound**, but we build the machinery needed to approach it and to formalize finite reductions.

---

## 5. Repository layout (suggested)

Following the layout used in the repository for Erdős Problem #1, a suggested structure is:

```text
Erdős Problem #14/
  README.md
  14-structure-and-energy.md
  14-roadmap.md
  (later: 14-examples.md, 14-FVD.md, etc.)
