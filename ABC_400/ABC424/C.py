from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
learned = [False] * (N+1)
q = deque()

for i in range(1, N+1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        learned[i] = True
        q.append(i)
    else:
        if a != 0:
            adj[a].append(i)
        if b != 0:
            adj[b].append(i)

while q:
    x = q.popleft()
    for y in adj[x]:
        if not learned[y]:
            learned[y] = True
            q.append(y)
            
print(sum(learned))