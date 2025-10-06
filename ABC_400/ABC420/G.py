import sys
import math

X = int(input())

D = 4*X - 1
n_set = set()

for d in range(1, int(abs(D)**0.5) + 1):
    if D % d != 0:
        continue
    for a in (d, -d):
        b = D // a
        if (a+b) % 4 == 0 and (b-a) % 2 == 0:
            n = (b - a - 2) // 4
            n_set.add(n)

n_list = sorted(n_set)
print(len(n_list))
print(*n_list)