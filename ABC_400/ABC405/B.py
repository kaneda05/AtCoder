N, M = map(int,input().split())
A = list(map(str,input().split()))

numlist = [str(i) for i in range(1,M+1)]
cnt = 0
for i in reversed(range(N)):
    flag = True
    for j in range(M):
        if numlist[j] in A:
            continue
        else:
            flag = False
    if flag:
        cnt += 1
        A.pop(-1)
    else:
        break

print(cnt)