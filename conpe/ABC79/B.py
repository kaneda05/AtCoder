from functools import lru_cache

@lru_cache(maxsize=1000)
def func(n):
    if n==0:
        return 2
    elif n == 1:
        return 1
    else:
        return func(n-1)+func(n-2)

n = int(input())
print(func(n))