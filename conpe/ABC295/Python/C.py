from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))

d = defaultdict(int)

for a in A:
    d[a]+=1

ans = 0
for a in d:
    ans += d[a]//2
print(ans)
