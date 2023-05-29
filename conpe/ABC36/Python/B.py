N = int(input())
S = [list(input()) for _ in range(N)]

ans =[['']*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans[j][N-1-i] = S[i][j]
for x in ans:
    print(*x,sep='')