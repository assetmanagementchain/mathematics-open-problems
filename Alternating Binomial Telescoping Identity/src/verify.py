from fractions import Fraction
from math import comb

def V(n):
    total = Fraction(0,1)
    for k in range(n+1):
        total += Fraction(((-1)**k) * comb(n,k), k+1)
    return total

if __name__ == "__main__":
    ok = True
    for n in range(50):
        if V(n) != Fraction(1, n+1):
            print("Mismatch at n =", n, "V(n) =", V(n))
            ok = False
            break
    print("Verified up to n=50:", ok)
