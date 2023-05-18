N, M = map(int,input().split())

S = [None]*(N)
T = [None]*(M)
cnt = 0
for i in range(N):
    S[i] = input()

for i in range(M):
    T[i] = input()

for i in range(N):
    flag = False
    for j in range(M):
        if S[i][-3:]==T[j]:
            flag = True
    if flag:
        cnt += 1

print(cnt)