N,W = map(int,input().split())
w = [None]*(N+1)
v = [None]*(N+1)
for i in range(1,N+1):
  w[i],v[i] = map(int,input().split())

dp = [[-10**9]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
  for j in range(W+1):
    if j < w[i]:
      dp[i][j] = dp[i-1][j]
    if w[i]<=j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
      
print(max(dp[N]))