N = int(input())
W = []
H = []
B = []
for _ in range(N):
    w, h, b = map(int, input().split())
    W.append(w)
    H.append(h)
    B.append(b)

MAXW = sum(W)
OFFSET = MAXW
SIZE = 2 * MAXW + 1
NEG_INF = -10**30

dp = [NEG_INF] * SIZE
dp[OFFSET] = 0

for i in range(N):
    w = W[i]
    h = H[i]
    b = B[i]
    ndp = [NEG_INF] * SIZE
    for idx in range(SIZE):
        if dp[idx] == NEG_INF:
            continue

        ni = idx - w
        if 0 <= ni < SIZE:
            if ndp[ni] < dp[idx] + h:
                ndp[ni] = dp[idx] + h

        ni = idx + w
        if 0 <= ni < SIZE:
            if ndp[ni] < dp[idx] + b:
                ndp[ni] = dp[idx] + b
    dp = ndp

ans = max(dp[OFFSET:])
print(ans)