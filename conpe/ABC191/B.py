n,x = map(int,input().split())
a = list(map(int,input().split()))
L = []
for i in range(n):
    if a[i] != x:
        L.append(a[i])

print(*L)