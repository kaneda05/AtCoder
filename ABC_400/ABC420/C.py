import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = sum(min(A[i], B[i]) for i in range(N))

for _ in range(Q):
    c, x, v = input().split()
    x = int(x) - 1
    v = int(v)

    S -= min(A[x], B[x])

    if c == "A":
        A[x] = v
    else:
        B[x] = v
    
    S += min(A[x], B[x])

    print(S)