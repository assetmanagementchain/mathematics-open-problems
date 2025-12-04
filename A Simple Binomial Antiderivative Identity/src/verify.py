from fractions import Fraction
from math import comb

def U(n):
    total = Fraction(0,1)
    for k in range(n+1):
        total += Fraction(((-1)**k) * comb(n,k), (k+1)*(k+2))
    return total

if __name__ == "__main__":
    ok = True
    for n in range(50):
        if U(n) != Fraction(1, 2*(n+1)*(n+2)):
            print("Mismatch at n =", n, "U(n) =", U(n))
            ok = False
            break
    print("Verified up to n=50:", ok)
