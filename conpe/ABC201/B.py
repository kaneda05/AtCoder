n = int(input())
L = []
for i in range(n):
    s,t = input().split()
    t = int(t)
    L.append((t,s))

L.sort(reverse=True)
print(L[1][1])