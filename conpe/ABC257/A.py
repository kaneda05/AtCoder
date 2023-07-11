n, x = map(int,input().split())

L = []
for i in range(ord("A"),ord("Z")+1):
    for j in range(n):
        L.append(chr(i))
print(L[x-1])