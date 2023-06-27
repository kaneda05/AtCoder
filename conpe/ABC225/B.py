n = int(input())
grid = [[i] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(1,n+1):
    if len(grid[i])==n:
        print("Yes")
        exit()
    
print("No")