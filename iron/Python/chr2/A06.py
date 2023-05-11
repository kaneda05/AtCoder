N, Q = map(int,input().split())
A = list(map(int,input().split()))
sum_A = [0]
for i in range(N):
    sum_A.append(sum_A[i]+A[i])

# print(sum_A)

for i in range(Q):
    L,R = map(int,input().split())
    print(sum_A[R]-sum_A[L-1])
