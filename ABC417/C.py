from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter()
for i in range(N):
    key = A[i] + i + 1
    count[key] += 1

ans = 0
for j in range(N):
    target = (j + 1) - A[j]
    ans += count.get(target, 0)

print(ans)
