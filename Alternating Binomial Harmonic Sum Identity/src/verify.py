from fractions import Fraction
from math import comb

def S(n):
    """
    Compute S(n) = sum_{k=0}^n (-1)^k * C(n,k) / (k+1)
    using exact rational arithmetic.
    """
    total = Fraction(0, 1)
    for k in range(n+1):
        total += Fraction(((-1)**k) * comb(n, k), k+1)
    return total

if __name__ == "__main__":
    # Verify S(n) = 1/(n+1) for n up to 50
    ok = True
    for n in range(51):
        if S(n) != Fraction(1, n+1):
            print("Mismatch at n =", n, "S(n) =", S(n))
            ok = False
            break
    print("Verified up to n=50:", ok)
