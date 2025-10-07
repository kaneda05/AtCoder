H, W = map(int,input().split())
S = [input() for _ in range(H)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            cnt = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "#":
                    cnt += 1
            if cnt not in [2, 4]:
                print("No")
                exit()

print("Yes")