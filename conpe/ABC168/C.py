import math
def func(a,b,radian):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(radian))

a,b,h,m = map(int,input().split())
radian = math.radians(h*30 - m*5.5)

print(func(a,b,radian))
