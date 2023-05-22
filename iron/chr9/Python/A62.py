import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)


N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
 
for _ in range(M):
    A,B=map(int,input().split())
    G[A].append(B)
    G[B].append(A)
 
visited = [False]*(N+1)
dfs(1, G, visited)

ans = True
for i in range(1,N+1):
    if visited[i] == False:
        ans = False

if ans:
    print("The graph is connected.")
else:
	print("The graph is not connected.")