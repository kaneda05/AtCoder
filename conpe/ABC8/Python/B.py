import collections
N = int(input())

S = [input() for _ in range(N)]
c = collections.Counter(S)

cnt = -10**9
for key,value in c.items():
    if cnt < int(value):
        ans = key
        cnt = int(value)


print(ans)
