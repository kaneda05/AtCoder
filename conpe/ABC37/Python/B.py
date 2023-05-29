n, q = map(int,input().split())
A = [0]*(n+1)

for i in range(q):
    l,r,t = map(int,input().split())
    for k in range(l,r+1):
        A[k] = t

for i in range(1,n+1):
    print(A[i])