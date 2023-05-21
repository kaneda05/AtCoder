from collections import defaultdict
N = int(input())
A = [int(input()) for _ in range(N)]

d = defaultdict(int)
ans = 0
for a in A:
    d[a] += 1

for i in d.values():
    ans += i*(i-1)//2

print(ans)
