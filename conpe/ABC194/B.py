n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

L = []
for i in range(n):
    for j in range(n):
        if i!=j:
            L.append(max(A[i],B[j]))
        else:
            L.append(A[i]+B[i])

print(min(L))
