import itertools

n,k = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(n)]

num = list(range(1,n))
ans = 0
for index in itertools.permutations(num):
    index = [0] + list(index)
    cal = 0
    for i in range(n):
        cal += t[index[i]][index[(i+1)*n]]
    if cal == k:
        ans += 1

print(ans)