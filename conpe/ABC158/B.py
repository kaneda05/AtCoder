n,a,b = map(int,input().split())
m = a + b
ans = (n//m)*a + min(a, n%m)
print(ans)