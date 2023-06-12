n,m = map(int,input().split())
h = [0] + list(map(int,input().split()))
grid = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    grid[a].append(b)
    grid[b].append(a)

ans = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(len(grid[i])):
        if h[grid[i][j]] < h[i]:
            cnt += 1
    if cnt == len(grid[i]):
        ans += 1

print(ans)