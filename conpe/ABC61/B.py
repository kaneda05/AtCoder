n,m = map(int,input().split())
roads = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    roads[a]+=1
    roads[b]+=1

for i in range(1,n+1):
    print(roads[i])