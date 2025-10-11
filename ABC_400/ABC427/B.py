from functools import lru_cache

def f(x):
    return sum(int(d) for d in str(x))

@lru_cache(maxsize=None)
def A(n):
    if n == 0:
        return 1
    return sum(f(A(j)) for j in range(n))

N = int(input())
print(A(N))
