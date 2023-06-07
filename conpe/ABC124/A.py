a,b = map(int,input().split())
if a>b:
    ans = a + (a-1)
elif b>a:
    ans = b + (b-1)
else:
    ans = a + b

print(ans)