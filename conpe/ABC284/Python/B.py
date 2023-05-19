T = int(input())
for i in range(T):
    cnt = 0
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i]%2!=0:
            cnt += 1
    print(cnt)