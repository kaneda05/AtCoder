sx,sy,gx,gy = map(int,input().split())
ans = (sx*gy+gx*sy)/(sy+gy)
print(ans)