from collections import defaultdict
import math
n = int(input())
a = list(map(int,input().split()))

cnt = defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1

ans = math.comb(n,2)
for i in cnt.values():
    ans -= math(i,2)
print(ans)