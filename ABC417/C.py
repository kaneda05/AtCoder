from collections import Counter

# 入力
N = int(input())
A = list(map(int, input().split()))

# A[i] + i の値をカウントしておく
count = Counter()
for i in range(N):
    key = A[i] + i + 1  # iは1-indexで考えるため+1
    count[key] += 1

# 条件を満たすペアの個数を数える
ans = 0
for j in range(N):
    target = (j + 1) - A[j]  # jも1-indexで考える
    ans += count.get(target, 0)

print(ans)
