import itertools
n = int(input())
grid = []
for i in range(n):
    x,y = map(int,input().split())
    grid.append([x,y])

ans = 0
combs = itertools.combinations(grid, 2)
for comb in combs:
    x1 = comb[0][0]
    x2 = comb[1][0]

    y1 = comb[0][1]
    y2 = comb[1][1]

    x1-=x2
    y1-=y2

    if -1<=y1/x1<=1:
        ans += 1

print(ans)