h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]

ans = 1
dist = [(1,0),(-1,0),(0,1),(0,-1)]
for d in dist:
    i = x-1
    j = y-1
    while True:
        i += d[0]
        j += d[1]
        if 0<=i<h and 0<=j<w and s[i][j] == ".":
            ans += 1
        else:
            break
    
print(ans)