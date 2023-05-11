H, W = map(int,input().split())

grid = [[0]*(W+1) for _ in range(H+1)] # C,DがH,Wの時を考慮してW+1,H+1分作っておく

X = [None]*(H)
for i in range(H):
    X[i] = list(map(int,input().split()))


# 横方向に累積
for i in range(1, H+1):
    for j in range(1,W+1):
        grid[i][j] += grid[i][j-1] + X[i-1][j-1]


# 縦方向に累積
for j in range(1, W+1):
    for i in range(1, H+1):
        grid[i][j] += grid[i-1][j]
        

Q = int(input())
for i in range(Q):
    A,B,C,D = map(int,input().split())
    ans = grid[C][D]+grid[A-1][B-1] - grid[A-1][D] - grid[C][B-1]
    print(ans)