import itertools
n = int(input())
d = list(map(int,input().split()))
combinations = itertools.combinations(d,2)
ans = 0
for combination in combinations:
    ans += combination[0]*combination[1]
print(ans)
