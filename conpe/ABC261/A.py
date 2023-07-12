l1,r1,l2,r2 = map(int,input().split())
A = [i for i in range(l1,r1+1)]
B = [i for i in range(l2,r2+1)]

res = []
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            res.append(A[i])

if len(res) == 0: print(0)
else: print(len(res)-1)