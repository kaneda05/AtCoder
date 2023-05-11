N = int(input())
A = list(map(int, input().split()))
D = int(input())

L = [0] * D
R = [0] * D

P = [0] * (N+1)
for i in range(N):
    P[i+1] = max(A[i],P[i])

Q = [0] * (N+2)
for i in reversed(range(N)):
    Q[i+1] = max(A[i],Q[i+2])

for i in range(D):
    L, R = map(int, input().split())
    print(max(P[L-1],Q[R+1]))