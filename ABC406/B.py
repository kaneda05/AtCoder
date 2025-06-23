N, K = map(int,input().split())
A = list(map(int,input().split()))
error = 10**K
call = 1
for i in range(N):
    call *= A[i]
    if call >= error:
        call = 1

print(call)