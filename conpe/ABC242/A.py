a,b,c,x = map(int,input().split())
if x <= a:
    print(1)
elif x<=b:
    p = c/(b-a)
    print(p)
else:
    print(0)