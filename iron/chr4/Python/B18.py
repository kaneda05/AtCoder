N, S = map(int,input().split())
A = list(map(int,input().split()))
dp = [[None]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1,N+1):
    dp[0][i] = False

for i in range(1, N+1):
    for j in range(S+1):
        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

        if A[i-1] <= j:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == False:
    print("-1")
    exit()

for i in range(N+1):
    print(*dp[i])

ans = []
pos = S
for i in reversed(range(1,N+1)):
    if dp[i-1][pos] == True:
        pos = pos - 0
    else:
        print(i)
        pos -= A[i-1]
        ans.append(i)

ans.reverse()
print(len(ans))
print(*ans)