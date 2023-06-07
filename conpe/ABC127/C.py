n,m = map(int,input().split())

lmax = 0
rmin = n

for i in range(m):
    l,r = map(int,input().split())
    lmax = max(lmax, l)
    rmin = min(rmin, r)


print(max(0, rmin-lmax+1))

