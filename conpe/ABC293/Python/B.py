N = int(input())
A = list(map(int,input().split()))
L = set([i for i in range(1,N+1)])


for i in range(N):
    if i+1 in L and A[i] in L:
        L.remove(A[i])
    else:
        continue

print(len(L))
print(' '.join(map(str, L)))