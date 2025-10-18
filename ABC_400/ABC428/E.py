import sys
from collections import deque

N = int(input())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        v = q.popleft()
        for nxt in g[v]:
            if dist[nxt] == -1:
                dist[nxt] = dist[v] + 1
                q.append(nxt)

    best_i = 1
    for i in range(2, N + 1):
        if dist[i] > dist[best_i]:
            best_i = i
        elif dist[i] == dist[best_i] and i > best_i:
            best_i = i

    calc = best_i
    return calc, dist


p1, _ = bfs(1)
p2, dist1 = bfs(p1)
_, dist2 = bfs(p2)

for v in range(1, N + 1):
    if dist1[v] > dist2[v]:
        print(p1)
    elif dist1[v] < dist2[v]:
        print(p2)
    else:
        print(max(p1, p2))
