import itertools
import math

n = int(input())
X = []
for _ in range(n):
    x,y = map(int,input().split())
    X.append((x,y))

combs = itertools.combinations(X,3)
for comb in combs:
    x1,y1 = comb[0][0],comb[0][1]
    x2,y2 = comb[1][0],comb[1][1]
    x3,y3 = comb[2][0],comb[2][1]

    x1 -= x3
    x2 -= x3
    y1 -= y3
    y2 -= y3
    if x1 * y2 == x2*y1:
        print("Yes")
        exit()
        
print("No")