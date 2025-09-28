H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while True:
    to_black = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                cnt = 0
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                        cnt += 1
                if cnt == 1:
                    to_black.append((i,j))
    if not to_black:
        break
    for i, j in to_black:
        grid[i][j] = '#'

ans = sum(row.count('#') for row in grid)
print(ans)
