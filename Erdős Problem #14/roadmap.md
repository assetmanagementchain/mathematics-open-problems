# 🧭 Erdős Problem #14 — Research Roadmap

---

## 1. Problem Overview

We study **Erdős Problem #14**, concerning the internal structure of infinite Sidon sets.

A *Sidon set* ( A \subseteq \mathbb{N} ) satisfies:

* each sum ( a + b ) with ( a \leq b ) is **unique**,
* equivalently:

$$\displaystyle
a + b = c + d \quad \Longrightarrow \quad {a,b} = {c,d}.
$$

The open question is:

> **Does every infinite Sidon set contain a Sidon subset with arbitrarily large gaps?**

Formally, we ask whether there exists ( A' \subseteq A ) such that:

* ( A' ) is still a Sidon set,
* its gaps grow without bound:

$$\displaystyle
a_{i+1} - a_i \to \infty.
$$

---

## 2. Roadmap Structure

This roadmap tracks the full workflow needed to develop a rigorous, publishable solution.

---

## 3. Phase I — Formal Problem Encoding

### 3.1 Define all objects precisely

* Sidon set definition
* Collision-free constraint
* Additive energy bounds
* Growth rate and spacing conditions

### 3.2 Establish equivalent formulations

* Distinct pair-sum formulation
* Energy-minimization viewpoint
* Graph-theoretic interpretation
* Sparse sequence model

### 3.3 Reduce the problem to a **finite verification domain**

Tasks:

1. Formalize Sidon constraints as local forbidden configurations.
2. Identify finite substructures forcing large gaps.
3. Show that any infinite Sidon set must contain arbitrarily long “gap stretches”.

Deliverables:

* FVD lemma statements
* Proof sketches
* Verification tables (if applicable)

---

## 4. Phase II — Structural Analysis

### 4.1 Build canonical decompositions of Sidon sets

Consider models such as:

* greedy Sidon sequences
* quasi-random Sidon constructions
* Bose–Chowla constructions
* finite-field Sidon lifts

### 4.2 Identify mechanisms that create unbounded gaps

Potential strategies:

* growth-rate amplification
* additive-combinatoric sparsification
* forced expansions under collision freedom
* iterative “gap stretching” arguments

### 4.3 Derive gap-propagation inequalities

Goal:

$$\displaystyle
\Delta_{i+1} \ge f(\Delta_i)
$$

for some monotone ( f ).

---

## 5. Phase III — Candidate Proof Approaches

### Approach A — Greedy Compression Argument

Show that if gaps stay bounded, Sidon constraints are eventually violated.

### Approach B — Additive Energy Collapse

Bounded gaps imply too many near-collisions:

$$\displaystyle
E(A) \text{ becomes too large}.
$$

Contradiction.

### Approach C — Iterated Density Drop

Use decreasing local density to force increasing spacing.

### Approach D — Finite Obstruction Classification (FVD)

Rule out all bounded-gap Sidon substructures via finite inspection.

---

## 6. Phase IV — Formal Proof Assembly

### 6.1 Build the multi-step implication chain

1. local structure ⇒
2. density constraints ⇒
3. energy growth ⇒
4. forced gap expansion ⇒
5. unbounded gaps.

### 6.2 Write a rigorous LaTeX formal version

* all lemmas numbered
* all inequalities explicit
* every transition justified
* no heuristic steps

### 6.3 Prepare Lean-compatible outline

(optional but desirable)

---

## 7. Phase V — Verification & Validation

### 7.1 Internal consistency checks

### 7.2 Edge-case constructions

### 7.3 Comparison against known Sidon constructions

### 7.4 Attempt to generate counterexamples

(if impossible → strengthens proof)

---

## 8. Phase VI — Final Deliverables

* `README.md` (clean exposition)
* `proof.md` (full formal proof)
* `structure/` (lemmas, constructions, examples)
* `FVD/` (finite verification domain, if used)
* `notes/` (exploratory paths and dead ends)
* `lean/` (optional mechanized components)

---

## 9. Repository Links

* Problem page:
  [https://www.erdosproblems.com/14](https://www.erdosproblems.com/14)

* Project directory (to be updated after upload):
  `Erdős Problem #14/`

---

## 10. Status Tracking

| Stage | Description              | Status    |
| ----- | ------------------------ | --------- |
| I     | Formal problem encoding  | ⬜ Pending |
| II    | Structural analysis      | ⬜ Pending |
| III   | Proof strategy selection | ⬜ Pending |
| IV    | Proof assembly           | ⬜ Pending |
| V     | Verification             | ⬜ Pending |
| VI    | Publication package      | ⬜ Pending |

---

