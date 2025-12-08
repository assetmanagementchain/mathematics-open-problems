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

README.md: this file

14-structure-and-energy.md: detailed structural and energy-based analysis

14-roadmap.md: task list, milestones, and status tracking for this problem


---

## 📐 文件 2：`14-structure-and-energy.md`

```markdown
# Erdős Problem #14 — Structure and Energy Framework

**Official link:** https://www.erdosproblems.com/14

> Let \(A\subseteq \mathbb{N}\). Let \(B\subseteq \mathbb{N}\) be the set of integers which are representable in exactly one way as the sum of two elements from \(A\).  
> 
> 1. Is it true that for all \(\varepsilon>0\) and large \(N\),
>    \[
>    |\{1,\ldots,N\}\setminus B|\ \gg_\varepsilon N^{1/2-\varepsilon}?
>    \]
> 2. Is it possible that
>    \[
>    |\{1,\ldots,N\}\setminus B| = o(N^{1/2})?
>    \]

This note sets up the structural and energy framework we will use to study the problem, in a way that mirrors our treatment of Erdős Problem #1.

---

## 1. Representation function and region decomposition

Let \(A\subseteq\mathbb{N}\). Define the **representation function**
\[
r_A(n) := \#\{(a,b)\in A^2 : a+b = n\}.
\]

Then:

- An integer \(n\) is in \(B\) iff \(r_A(n)=1\).
- An integer \(n\) is outside \(B\) iff \(r_A(n)=0\) or \(r_A(n)\ge2\).

For each positive integer \(N\), we introduce:

- **Unrepresentable zone:**
  \[
    Z_N := \{1\le n\le N : r_A(n)=0\};
  \]

- **Uniquely representable zone:**
  \[
    U_N := \{1\le n\le N : r_A(n)=1\};
  \]

- **Multi-representable zone:**
  \[
    M_N := \{1\le n\le N : r_A(n)\ge 2\}.
  \]

Then we have a disjoint union
\[
[1,N] = Z_N \;\dot\cup\; U_N \;\dot\cup\; M_N
\]
and therefore
\[
|\{1,\dots,N\}\setminus B|
  = |Z_N| + |M_N|.
\]

Problem #14 is precisely about lower bounds (and possible upper bounds) on \(|Z_N|+|M_N|\).

---

## 2. Additive energy and basic inequalities

We introduce the **additive energy** of \(A\):
\[
E(A) := \sum_{n\in\mathbb{Z}} r_A(n)^2.
\]

We recall the standard identities/inequalities:

1. The total number of ordered 2-sums:
   \[
   \sum_{n} r_A(n) = |A|^2.
   \]

2. Cauchy–Schwarz implies
   \[
   E(A)
   = \sum_{n} r_A(n)^2
   \;\ge\;
   \frac{\left(\sum_n r_A(n)\right)^2}{|\{n : r_A(n)>0\}|}
   = \frac{|A|^4}{|A+A|},
   \]
   where \(A+A := \{a+b : a,b\in A\}\).

This connects **energy** with the **size of the sumset** \(A+A\).

---

## 3. Energy in terms of \(Z_N,U_N,M_N\)

We now relate \(E(A)\) directly to \(|U_N|\) and \(|M_N|\). Decompose:

\[
E(A)
  = \sum_{n\in Z_N} r_A(n)^2
    + \sum_{n\in U_N} r_A(n)^2
    + \sum_{n\in M_N} r_A(n)^2
    + \sum_{n\notin[1,N]} r_A(n)^2.
\]

By definition of the three regions:

- For \(n\in Z_N\), \(r_A(n)=0\).
- For \(n\in U_N\), \(r_A(n)=1\).
- For \(n\in M_N\), \(r_A(n)\ge2\).

Thus
\[
E(A)
  = \sum_{n\in U_N} 1
    + \sum_{n\in M_N} r_A(n)^2
    + \sum_{n\notin[1,N]} r_A(n)^2.
\]

Since for each \(n\in M_N\) we have \(r_A(n)\ge 2\), we obtain a crude but useful lower bound
\[
\sum_{n\in M_N} r_A(n)^2 \;\ge\; 4|M_N|.
\]

Therefore,
\[
E(A) \;\ge\; |U_N| + 4|M_N|.
\tag{3.1}
\]

On the other hand,
\[
|Z_N|+|M_N|
  = N - |U_N|.
\]

Combining this with (3.1), we obtain
\[
|Z_N|+|M_N|
  = N - |U_N|
  \;\ge\; N - (E(A) - 4|M_N|)
  = N - E(A) + 4|M_N|.
\]

Equivalently,
\[
|\{1,\dots,N\}\setminus B|
  \;\ge\; N - E(A) + 4|M_N|.
\tag{3.2}
\]

This already reveals a **tension**:

- If \(E(A)\) is large, then (3.1) forces \(|M_N|\) to be large.
- If \(E(A)\) is small, then the term \(N-E(A)\) in (3.2) is large unless \(N\) is small or \(E(A)\) is comparable to \(N\).

Of course, this is far from optimal, but it indicates the natural **two-regime strategy** (low-energy vs high-energy) for bounding \(|Z_N|+|M_N|\).

---

## 4. Low-energy vs high-energy regimes

To organize the analysis, we consider two extremes.

### 4.1 Low-energy regime (near-Sidon behaviour)

If \(E(A)\) is relatively small compared to \(|A|^2\), then by
\[
E(A) \ge \frac{|A|^4}{|A+A|}
\]
we infer that \(|A+A|\) must be large; in an extreme Sidon-like situation one would expect
\(|A+A|\approx |A|^2\).

Heuristically, if \(A+A\) is “very large” compared to the interval \([1,2\max A]\), then there must be many gaps in \([1,N]\setminus (A+A)\), which contribute to the unrepresentable zone \(Z_N\).

In this regime, we therefore aim for **lower bounds on \(|Z_N|\)** in terms of \(|A|\), \(|A+A|\) and ultimately \(N\). Roughly:

- low energy ⇒ large sumset ⇒ large complement of the sumset in \([1,N]\) ⇒ large \(Z_N\).

The precise quantitative bounds will likely depend on:

- how \(|A|\) grows with \(N\),
- and how concentrated the sumset \(A+A\) is within \([1,2N]\).

### 4.2 High-energy regime (many collisions)

If \(E(A)\) is large, then by (3.1)
\[
E(A) \ge |U_N|+4|M_N|
\]
forces \(|M_N|\) to be large unless almost all of the energy is concentrated outside \([1,N]\).

In particular, for any threshold \(T>0\) we may separate:

- Case H1: \(E(A)\le T\) ⇒ low-energy analysis;
- Case H2: \(E(A)>T\) ⇒ we use (3.1) to deduce a lower bound on \(|M_N|\).

The aim is to choose \(T = T(N)\) in such a way that, in both H1 and H2, one can derive non-trivial lower bounds on
\(|Z_N|+|M_N|\).

---

## 5. A first quantitative target

The full conjectural bound (from the official statement) is that
\[
|Z_N|+|M_N| \;\ge\; N^{1/2-o(1)}.
\]

As a **first stage**, we do not aim for the \(1/2\) exponent, but rather for an explicit exponent \(c>0\) such as:

> **Proposition (target form, not yet proved).**  
> There exists \(c>0\) such that for all \(A\subseteq\mathbb{N}\), for all sufficiently large \(N\),
> \[
> |Z_N|+|M_N| \;\ge\; N^c.
> \]

The long-term goal is to push \(c\) upwards, ideally towards \(1/2\), but even a modest explicit \(c\) would already demonstrate that the “bad set” cannot be too small.

---

## 6. Towards a Finite Verification Domain (FVD-14)

In our work on Erdős Problem #1, a key conceptual tool was the **Finite Verification Domain (FVD)**:

- One identifies a finite space of local configurations (e.g. patterns of small sums),
- proves that any global configuration must locally fall into one of these patterns,
- and shows that verifying the desired inequality on this finite domain is enough to guarantee the global statement.

For Problem #14, a similar strategy can be envisioned:

1. Identify local patterns of the representation function \(r_A(n)\) over short intervals.
2. Classify these patterns into a finite family of types (using additive combinatorial structure, such as near-Sidon, cluster, arithmetic progressions, etc.).
3. Prove a **reduction theorem** of the form:

   > *If every locally admissible pattern satisfies a certain inequality on an interval of length \(N_0\), then the global inequality \(|Z_N|+|M_N|\ge f(N)\) holds for all \(N\).*

This document does not yet formalize FVD-14 but sets up the quantities and decompositions needed to state such a reduction precisely.

---

## 7. Status and next steps

At this point we have:

- A clean reformulation in terms of the zones \(Z_N,U_N,M_N\).
- A basic energy inequality \(E(A)\ge |U_N|+4|M_N|\) and the derived inequality (3.2).
- A conceptual split into low-energy and high-energy regimes.
- A first quantitative **target shape** for a non-trivial exponent lower bound.

**Next steps** (as tracked in `14-roadmap.md`):

1. Analyze random model benchmarks for \(|Z_N|+|M_N|\) (what exponent does a “typical” set \(A\) suggest?).
2. Derive explicit low-energy ⇒ large \(Z_N\) bounds using sumset estimates.
3. Derive explicit high-energy ⇒ large \(M_N\) bounds.
4. Combine these to prove a first explicit exponent \(c>0\).
5. Design and formalize an FVD-style reduction theorem for Problem #14 (FVD-14 v1.0).

