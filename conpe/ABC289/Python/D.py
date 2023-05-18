N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())

dp = [None]*(X+1)
for b in B:
    dp[b] = False

dp[0] = True
for i in range(1, X+1):
    if dp[i] == False:
        continue
    else:
        for a in A:
            if 0<=i-a and dp[i-a] == True:
                dp[i] = True
                continue
            
print("Yes" if dp[X] else "No")