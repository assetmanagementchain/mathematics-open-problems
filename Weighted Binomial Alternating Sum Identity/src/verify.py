from fractions import Fraction
from math import comb

def T(n):
    """
    Compute T(n) = sum_{k=0}^n (-1)^k * C(n, k) / (k + 2)
    using exact rational arithmetic.
    """
    total = Fraction(0, 1)
    for k in range(n + 1):
        total += Fraction(((-1) ** k) * comb(n, k), k + 2)
    return total

if __name__ == "__main__":
    # Verify the identity T(n) = 1/((n+1)(n+2)) for n up to 50
    ok = True
    for n in range(50):
        if T(n) != Fraction(1, (n + 1) * (n + 2)):
            print("Mismatch at n =", n, "computed T(n) =", T(n))
            ok = False
            break

    print("Verified up to n=50:", ok)
