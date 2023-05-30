N = int(input())
A = list(map(int,input().split()))
dp = [0]*N
dp[0] = 0
dp[1] = abs(A[0]-A[1])

for i in range(1,N-1):
    dp[i+1] = min(dp[i]+abs(A[i+1]-A[i]), dp[i-1]+abs(A[i+1]-A[i-1]))

print(dp[-1])
#print(dp)