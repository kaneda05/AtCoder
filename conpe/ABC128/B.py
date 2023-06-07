n=int(input())
sp=[input().split() for _ in range(n)]

ans=[i for i in range(n)]
ans.sort(key=lambda x: (sp[x][0], -int(sp[x][1])))

for a in ans:
    print(a+1)