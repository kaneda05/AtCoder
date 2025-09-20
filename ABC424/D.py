import sys
sys.setrecursionlimit(10**7)

T = int(input())
res = []

def find_block(grid, H, W):
    for i in range(H - 1):
        for j in range(W - 1):
            if (grid[i][j] == "#" and grid[i][j+1] == "#" and
                grid[i+1][j] == "#" and grid[i+1][j+1] == "#"):
                return i, j
    return None

def dfs(grid, H, W, steps, best):
    if steps >= best[0]:
        return

    pos = find_block(grid, H, W)
    if pos is None:
        best[0] = min(best[0], steps)
        return

    i, j = pos
    for di, dj in [(0,0), (0,1), (1,0), (1,1)]:
        ni, nj = i + di, j + dj
        if grid[ni][nj] == "#":
            grid[ni][nj] = "."
            dfs(grid, H, W, steps + 1, best)
            grid[ni][nj] = "#"

for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]

    best = [float("inf")]
    dfs(grid, H, W, 0, best)
    res.append(best[0])

for i in range(len(res)):
    print(res[i])