a,b,c,x,y = map(int,input().split())

if x >= y:
    print(min(a*x+b*y, 2*c*x, 2*c*y+(x-y)*a))
else:
    print(min(a*x+b*y, 2*c*y, 2*c*x+(y-x)*b))
