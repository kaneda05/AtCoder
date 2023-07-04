n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
#print(grid)
def distance(x1,x2,y1,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

ans = 0
for i in range(n):
    for j in range(i+1,n):
        x1 = grid[i][0]
        y1 = grid[i][1]
        x2 = grid[j][0]
        y2 = grid[j][1]

        cal = distance(x1,x2,y1,y2)
        #print(cal)

        ans = max(ans,cal)

print(round(ans,10))