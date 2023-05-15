# 幅優先探索
from collections import deque

R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

G = [input() for _ in range(R)]

Q = deque()
Q.append([sy, sx])

dist = [[-1]*C for _ in range(R)]
dist[sy][sx] = 0 # スタート地点に0を代入

# 移動する4方向
dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while 0<len(Q):

    y, x = Q.popleft() # 全て訪れた場合はpopleftしかされなくなる

    for dx,dy in dirc:
        y2 = y + dy
        x2 = x + dx

        # 壁の範囲内だったらcontinue
        if not (0<=y2<R and 0<=x2<C):
            continue

        # 壁だったらcontinue
        if G[y2][x2] == "#":
            continue

        # 壁の内部　＋　. ＋　まだ訪れてない(dist[y2][x2]=-1)
        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1
            Q.append([y2, x2])

# ゴールの距離を出力
print(dist[gy][gx])