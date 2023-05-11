H, W, N = map(int,input().split())
Z = [[0]*(W+2) for _ in range(H+2)]
for i in range(N):
    A,B,C,D = map(int,input().split())
    Z[A][B]+=1
    Z[C+1][D+1]+=1
    Z[A][D+1]-=1
    Z[C+1][B]-=1

# 横方向の累積
for i in range(H):
    for j in range(W):
        Z[i+1][j+1] += Z[i+1][j]
 
# 縦方向の累積
for i in range(H):
    for j in range(W):
        Z[i+1][j+1] += Z[i][j+1]


for i in range(1,H+1):
    print(*Z[i][1:W+1])