# H1-A3: Alternating Binomial Harmonic Sum Identity

## Theorem
For all integers n ≥ 0,

    S(n) = sum_{k=0}^n (-1)^k * C(n, k) / (k + 1) = 1 / (n + 1).

## Proof

### Step 1: Evaluate the integral of (1 - x)^n
Consider the integral

    I_n = ∫_0^1 (1 - x)^n dx.

A direct computation gives

    I_n = [ -(1 - x)^{n+1} / (n+1) ]_0^1 = 1 / (n + 1).

### Step 2: Expand (1 - x)^n using the binomial theorem
Using

    (1 - x)^n = ∑_{k=0}^n (-1)^k * C(n, k) * x^k,

we substitute into the integral:

    I_n = ∫_0^1 ∑_{k=0}^n (-1)^k C(n, k) x^k dx
        = ∑_{k=0}^n (-1)^k C(n, k) ∫_0^1 x^k dx.

Since ∫_0^1 x^k dx = 1 / (k+1), this becomes

    I_n = ∑_{k=0}^n (-1)^k C(n, k) / (k+1).

### Step 3: Compare both expressions
We have shown:

    I_n = 1 / (n + 1)

and

    I_n = S(n).

Thus

    S(n) = 1 / (n + 1).

QED.
