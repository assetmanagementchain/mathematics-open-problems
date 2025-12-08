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
