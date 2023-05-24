import math
txa, tya, txb, tyb, T, V = map(int,input().split())
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    ans1 = math.sqrt((x-txa)**2+(y-tya)**2)
    ans2 = math.sqrt((x-txb)**2+(y-tyb)**2)
    if ans1+ans2 <= T*V:
        print("YES")
        exit()

print("NO")