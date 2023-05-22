N, T = map(int,input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1):
    if T<A[i+1]-A[i]:
        ans += T
    else:
        ans += A[i+1]-A[i]

ans += T
print(ans)
