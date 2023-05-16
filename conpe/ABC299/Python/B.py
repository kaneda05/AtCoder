N, T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

L = []
for i in range(N):
    L.append([C[i],R[i]])

ans = []
max_R = -10**9
if T in C:
    for i in range(N):
        if L[i][0] == T and max_R<L[i][1]:
            max_R=L[i][1]
else:
    for i in range(N):
        if L[i][0] == L[0][0] and max_R<L[i][1]:
            max_R=L[i][1]

print(R.index(max_R)+1)