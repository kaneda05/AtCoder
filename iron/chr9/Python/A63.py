from collections import deque

N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
 
for _ in range(M):
    A,B=map(int,input().split())
    G[A].append(B)
    G[B].append(A)


dist = [-1]*(N+1)
dist[1] = 0
Q = deque()
Q.append(1)

while 1<=len(Q):
    pos = Q.popleft()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex)

for i in range(1, N+1):
    print(dist[i])