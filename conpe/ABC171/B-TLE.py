# itertoolsを使うやり方 TLEとなってしまう

import itertools
n,k = map(int,input().split())
p = list(map(int,input().split()))

combs = itertools.combinations(p,k)

ans = 10**9
for comb in combs:
    cal = 0
    for i in range(k):
        cal += comb[i]

    ans = min(ans,cal)

print(ans)