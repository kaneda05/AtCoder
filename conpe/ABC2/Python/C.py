xa,ya,xb,yb,xc,yc = map(int,input().split())
xb-=xa
xc-=xa
yb-=ya
yc-=ya
xa-=xa
ya-=ya
print(abs(xb*yc-yb*xc)/2)