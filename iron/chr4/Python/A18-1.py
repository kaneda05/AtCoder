# 問題例1
# 長さが違うN個の棒があります。
# これらを使ってXcmは作れますか?

N = int(input()) # 棒の本数
X = int(input()) # 長さ
L = list(map(int,input().split())) # 棒の本数を入力

dp = [[False for _ in range(X+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(X):
        if dp[i][j]:
            dp[i+1][j] = True
            if j + L[i] <= X:
                dp[i+1][j+L[i]] = True
print(dp[-1][-1])