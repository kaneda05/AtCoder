n,m,t = map(int,input().split())
v = n

L = []
for i in range(m):
    a,b = map(int,input().split())
    L.append([a,b])


for i in range(m):
    if i == 0:
        n -= L[0][0]
    else:
        n -= (L[i][0]-L[i-1][1])
    if n <= 0:
        print("No")
        exit()
    else:
        if v<=n + (L[i][1]-L[i][0]):
            n = v
        else:
            n += (L[i][1]-L[i][0])

if n-(t-L[-1][1])<=0:   
    print("No")
else:
    print("Yes")
