from re import A


n = int(input())
a = [list(map(int,input().split())) for _ in range(2)]
dp = [[0]*n for _ in range(2)]
dp[0][0] = A[0][0]
for i in range(2):
    for j in range(n):
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+a[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1]+a[i][j])

print(dp[1][n-1])



