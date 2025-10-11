N, M = map(int, input().split())

edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))

best = 0
for mask in range(1 << N):
    cnt = 0
    for u, v in edges:
        if ((mask >> u) & 1) != ((mask >> v) & 1):
            cnt += 1
    if cnt > best:
        best = cnt

print(M-best)