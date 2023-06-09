from itertools import permutations
from math import sqrt, factorial

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for  pattern in permutations(xy,n):
    cal = 0
    for i in range(1,n):
        xy_now = pattern[i-1]
        xy_next = pattern[i]
        cal += sqrt((xy_next[0]-xy_now[0])**2 + (xy_next[1]-xy_now[1])**2)
    ans += cal
    


print(ans/factorial(n))