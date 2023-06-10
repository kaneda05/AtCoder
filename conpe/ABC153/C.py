n,k = map(int,input().split())
h = list(map(int,input().split()))
cnt = 0
if n<=k:
    print(0)
    exit()
else:
    h.sort(reverse=True)
    for i in range(n):
        if 0<k:
            k-=1
            pass
        else:
            cnt += h[i]

print(cnt)