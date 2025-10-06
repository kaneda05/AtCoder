N = int(input())
S = [input().strip() for _ in range(N)]

res = set()

for i in range(N):
    for j in range(N):
        if i != j:
            c = S[i] + S[j]
            res.add(c)

print(len(res))
