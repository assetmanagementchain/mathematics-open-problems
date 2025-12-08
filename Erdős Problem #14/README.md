# Erdős Problem #14  
**Sidon Subset Structure Problem**  
**Status: Open**  
**Tags: number theory, Sidon sets, additive combinatorics**  
**Prize: no reward listed**

---

## 🔗 Official Problem Link  
https://www.erdosproblems.com/14

---

## 📘 Problem Statement

Let $A \subseteq \mathbb{N}$ be an infinite Sidon set, meaning all sums  
$a + b$ with $a \leq b$ are distinct.

Does every infinite Sidon set contain a Sidon subset  
$A' \subseteq A$  
with **arbitrarily large gaps**?

More precisely, for every $L \in \mathbb{N}$, does there exist a finite sequence  
$$a_1 < a_2 < \dots < a_L \in A'$$  
such that  
$$a_{i+1} - a_i > a_i - a_{i-1} \quad \text{for all } i?$$  

Equivalently,  
$$a_{i+1} - a_i \to \infty \quad \text{as } i \to \infty.$$

A Sidon set satisfies the collision-free constraint  

$$\displaystyle
a + b = c + d \quad \Longrightarrow \quad \{a,b\} = \{c,d\}.
$$


This asks whether **every infinite Sidon set contains a strongly sparse Sidon subsequence**.

---

## 🧩 Why This Problem Is Difficult  

Sidon sets satisfy the collision-free constraint  

$$\displaystyle
a + b = c + d \quad \implies \quad \{a,b\} = \{c,d\}.
$$


This creates a very rigid additive structure, but **not rigid enough** to directly imply long-gap behavior.

The difficulty is:

- Sidon sets may be *dense enough* to avoid long gaps  
- but *rigid enough* that sparsity patterns might be forced  
- yet there is no monotonicity or standard energy method available  
- and classical theorems (Erdős–Turán, Roth, etc.) do not apply

Thus Problem #14 sits at the interface of:

- additive combinatorics  
- discrete geometry of sumsets  
- extremal Sidon constructions  
- metric behavior inside collision-free sets

It is a **pure structure problem** without a known effective analytic inequality.

---

## 📂 Repository Structure  

This problem follows the unified structure used for all open problems in this project:

```
Erdos Problem #14/
│
├── README.md
├── structure-and-energy.md
├── roadmap.md
├── summary-en.md
└── summary-cn.md
```

- **structure-and-energy.md**  
  Contains the formal decomposition, invariants, and proof engine.

- **roadmap.md**  
  Task list and progress tracker.

- **summary-en.md / summary-cn.md**  
  Public-facing explanations.

---

## 🏁 Current Status  

Work on this problem is in progress.  
The goal is to construct:

- a complete structural decomposition  
- an additive energy bound compatible with Sidon constraints  
- a forced expansion lemma ensuring growing gaps  
- a contradiction argument if gaps remain bounded  
- or a constructive infinite-gap Sidon subsequence

The aim is to reach the same level of completeness as  
**"Finite Verification Domain for Erdős Problem #1"**.

---

## 🧭 Next Step  

Development continues in:

**structure-and-energy.md**

This file contains the full mathematical engine, including:

- Sidon collision geometry  
- pair-sum hypergraph modelling  
- energy lower/upper control  
- gap forcing mechanisms  
- candidate infinite subsequence construction

---

## 📜 Citation  

If you use or reference this repository:

**XUXIN & ChatGPT**  
*Erdős Problem #14 — Sidon Subset Structure Analysis*  
GitHub: https://github.com/assetmanagementchain/mathematics-open-problems

