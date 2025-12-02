# verification.py
# Check monotonicity of restricted partition function p_k(n)

from functools import lru_cache

def partitions_with_max_part(n, k):
    # number of partitions of n whose largest part is exactly k
    @lru_cache(None)
    def count(m, maxp):
        if m == 0:
            return 1
        if m < 0 or maxp == 0:
            return 0
        return count(m, maxp-1) + count(m-maxp, maxp)
    return count(n-k, k)

def check_monotonicity(k, N=200):
    seq = [partitions_with_max_part(n, k) for n in range(k, N)]
    for i in range(len(seq)-1):
        if seq[i+1] <= seq[i]:
            print("Non-monotone at n =", k+i)
            return False
    print("Monotone up to N =", N)
    return True

if __name__ == "__main__":
    # Example: k = 4
    check_monotonicity(k=4, N=200)
