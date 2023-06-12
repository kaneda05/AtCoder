import math
x = int(input())
ans = 100
for i in range(1,10**9+1):
    ans += int(ans*0.01)
    if x <= ans:
        print(i)
        exit()