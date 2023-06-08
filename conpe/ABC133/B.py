import itertools

n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]

ans = 0
squares = set([i**2 for i in range((40*10)*2+1)])
combinations = itertools.combinations(x,2)

for combination in combinations:
    D = 0
    for i in range(d):
        D += (combination[0][i]-combination[1][i])**2

    if D in squares:
        ans += 1

print(ans)
