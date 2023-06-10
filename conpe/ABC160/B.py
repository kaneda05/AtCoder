x = int(input())
ans = 0
if 500<=x:
    ans += (x//500)*1000
    x -= (x//500)*500

if 5<=x:
    ans += (x//5)*5
    x -= (x//5)*5

print(ans)