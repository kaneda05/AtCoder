a,b,c = map(int,input().split())
x = a * b * c
ans = x%(10**9+7)
print(ans)