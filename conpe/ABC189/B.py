n,x = map(int,input().split())
al = 0
for i in range(n):
    v,p = map(int,input().split())
    al += v*p
    if x*100 < al:
        print(i+1)
        exit()

print(-1)