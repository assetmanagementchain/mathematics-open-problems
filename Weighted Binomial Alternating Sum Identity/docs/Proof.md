# H1-A4: Weighted Binomial Alternating Sum Identity

## Theorem
For every integer n ≥ 0,
    
    T(n) = sum_{k=0}^n (-1)^k * C(n, k) / (k + 2)
         = 1 / ((n + 1)(n + 2)).

## Proof

### Step 1: Evaluate the integral ∫₀¹ x(1 - x)ⁿ dx
Consider the integral

    I_n = ∫_0^1 x(1 - x)^n dx.

Integration by parts (or standard tables) shows:

    I_n = 1 / ((n + 1)(n + 2)).

### Step 2: Expand (1 - x)ⁿ using the binomial theorem
Using the identity

    (1 - x)^n = ∑_{k=0}^n (-1)^k C(n, k) x^k,

we obtain

    x(1 - x)^n = ∑_{k=0}^n (-1)^k C(n, k) x^(k+1).

### Step 3: Integrate term-by-term
Thus,

    I_n = ∫_0^1 x(1 - x)^n dx
        = ∑_{k=0}^n (-1)^k C(n, k) ∫_0^1 x^(k+1) dx
        = ∑_{k=0}^n (-1)^k C(n, k) / (k + 2).

Hence

    I_n = T(n).

### Step 4: Compare both expressions
Since

    I_n = 1 / ((n + 1)(n + 2))
and
    I_n = T(n),

it follows that

    T(n) = 1 / ((n + 1)(n + 2)).

QED.
