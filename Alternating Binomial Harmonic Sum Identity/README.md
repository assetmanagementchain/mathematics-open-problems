# H1-A3: Alternating Binomial Harmonic Sum Identity

We prove the closed-form identity

    S(n) = sum_{k=0}^n (-1)^k * C(n, k) / (k + 1) = 1 / (n + 1),

valid for all integers n ≥ 0.

The proof is based on expanding (1 - x)^n using the binomial theorem,
integrating term-by-term on [0, 1], and comparing both expressions.

A complete formal proof is available in /docs/Proof.md.
Verification code is provided in /src.

This problem belongs to the class of “AI-completely-provable small problems”
and is part of the H1 series.
