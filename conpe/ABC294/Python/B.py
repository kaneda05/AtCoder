H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

L = ["."]
for i in range(ord("A"),ord("Z")+1):
    L.append(chr(i))

B = [[None]*(W) for _ in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] = L[A[i][j]]

for i in range(H):
    print("".join(B[i]))