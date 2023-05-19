N, M = map(int,input().split())
S = [input() for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        flag = True
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                flag = False

        if flag:
            cnt += 1
        
print(cnt)