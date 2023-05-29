N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]

set_list = set()
for a in A:
    for i in range(N-1):
        x,y = a[i],a[i+1]
        set_list.add((x,y))
        set_list.add((y,x))

ans = N*(N-1)//2 - len(set_list)//2
print(ans)
