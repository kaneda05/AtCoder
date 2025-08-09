S = input().strip()
n = len(S)

ans = 0.0

for i in range(n):
    if S[i] != 't':
        continue
    for j in range(i + 2, n):
        if S[j] != 't':
            continue
        sub = S[i:j+1]
        x = sub.count('t')
        if x >= 3:
            rate = (x - 2) / (len(sub) - 2)
            ans = max(ans, rate)

print(ans)
