N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 動的計画法
dp = [None]*(N+1)
dp[1] = 0
dp[2] = A[0]
for i in range(3,N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

ans = []
pos = N
while True:
    ans.append(pos)
    if pos == 1:
        break
    if dp[pos-1]+A[pos-2] == dp[pos]:
        pos -= 1
    else:
        pos -= 2

print(len(ans))
ans.reverse()
print(*ans)