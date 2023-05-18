N, M = map(int,input().split())

A =[]
for i in range(M):
    C = int(input())
    a = list(map(int,input().split()))
    A.append(a)

LS = set(range(1,N+1))
cnt = 0
for i in range(2**M):
    if i == 0:
        continue
    else:
        S = set()
        for j in range(M):
            if ((i>>j)& 1):
                S = S | A[j] # 和集合
            if S == LS:
                cnt += 1
print(cnt)
