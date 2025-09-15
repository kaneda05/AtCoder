N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

S1 = [0]*(N+1)
S2 = [0]*(N+1)
S3 = [0]*(N+1)

for i in range(1, N+1):
    S1[i] = S1[i-1] + A[i]
    S2[i] = S2[i-1] + A[i]*i
    S3[i] = S3[i-1] + A[i]*i*i

for _ in range(Q):
    L, R = map(int, input().split())
    sumA = S1[R] - S1[L-1]
    sumAj = S2[R] - S2[L-1]
    sumAj2 = S3[R] - S3[L-1]

    ans = (R+1)*(sumAj - (L-1)*sumA) - sumAj2 + (L-1)*sumAj
    print(ans)
