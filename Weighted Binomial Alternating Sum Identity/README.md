# H1-A4: Weighted Binomial Alternating Sum Identity

We prove the closed-form identity

    T(n) = sum_{k=0}^n (-1)^k * C(n, k) / (k + 2)
         = 1 / ((n + 1)(n + 2)),

valid for all integers n ≥ 0.

The proof uses the expansion of (1 - x)^n, multiplying by x,
integrating term-by-term on [0,1], and comparing with a direct integral evaluation.

Full proof in /docs/Proof.md.
Verification code in /src.
