n,k,m = map(int,input().split())
a = list(map(int,input().split()))
if n*m-sum(a)<=k:
    if n*m-sum(a)<=0:
        print(0)
    else:
        print(n*m-sum(a))
else:
    print(-1)