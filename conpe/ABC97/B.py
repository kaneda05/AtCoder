x = int(input())
ans = 1
for p in range(2,10):
    for b in range(2,50):
        if x >= b**p:
            ans = max(ans,b**p)
print(ans)