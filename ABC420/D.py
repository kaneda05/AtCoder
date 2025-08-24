from collections import deque

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            si, sj = i, j
        if grid[i][j] == "G":
            gi, gj = i, j

INF = 10**9
dist = [[[INF]*2 for _ in range(W)] for __ in range(H)]
dist[si][sj][0] = 0

q = deque()
q.append((si, sj, 0))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def ok_pass(ch, open_flag):
    if ch == "#":
        return False
    if ch in [".", "S", "G", "?"]:
        return True
    if ch == "o":
        return open_flag == 0
    if ch == "x":
        return open_flag == 1
    return False

while q:
    i, j, w = q.popleft()
    d = dist[i][j][w]

    if (i, j) == (gi, gj):
        print(d)
        exit()

    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if 0 <= ni < H and 0 <= nj < W:
            cell = grid[ni][nj]
            if not ok_pass(cell, w):
                continue
            nw = w
            if cell == "?":
                nw = 1 - w
            if dist[ni][nj][nw] > d+1:
                dist[ni][nj][nw] = d+1
                q.append((ni, nj, nw))

print(-1)
