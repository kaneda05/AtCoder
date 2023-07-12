x,y,n = map(int,input().split())
ans = 0
if y<=3*x:
    ans += (n//3)*y
    res = n-(n//3)*3
    ans += res*x
else:
    ans += x*n

print(ans)
