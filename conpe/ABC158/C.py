import math
a,b = map(int,input().split())

for i in range(1, 10**6+1):
    A = math.floor(i * 0.08)
    B = math.floor(i * 0.1)
    if a==A and b==B:
        ans = i
        print(i)
        exit()

print(-1)