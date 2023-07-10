h,w = map(int,input().split())
r,c = map(int,input().split())

ans = 0
if 1<=r+1<=h: ans += 1
if 1<=r-1<=h: ans += 1
if 1<=c+1<=w: ans += 1
if 1<=c-1<=w: ans += 1
print(ans)