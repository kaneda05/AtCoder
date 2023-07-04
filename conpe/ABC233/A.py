import math
x, y = map(int,input().split())
if y < x:
    print(0)
else:
    diff = y - x
    ans = math.ceil(diff/10)
    print(ans)