from collections import deque

H, W = map(int, input().split())
S = [list(input().strip()) for _ in range(H)]

def pos(i,j):
    return i*W + j

tx = ty = -1
mask = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "T":
            tx, ty = i, j
        elif S[i][j] == "#":
            mask |= 1 << pos(i,j)

queue = deque([(mask, 0)])
visited = set()
visited.add(mask)

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

ans = -1

while queue:
    state, step = queue.popleft()

    if state == 0:
        ans = step
        break

    bits = [i for i in range(H*W) if (state >> i) & 1]
    for dx, dy in dirs:
        new_mask = 0
        safe = True
        for b in bits:
            x, y = divmod(b, W)
            nx, ny = x + dx, y + dy

            if not (0 <= nx < H and 0 <= ny < W):
                continue

            if (nx, ny) == (tx, ty):
                safe = False
                break

            new_mask |= 1 << pos(nx, ny)

        if not safe:
            continue

        if new_mask not in visited:
            visited.add(new_mask)
            queue.append((new_mask, step + 1))

print(ans)
