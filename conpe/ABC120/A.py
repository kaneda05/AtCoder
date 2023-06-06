a,b,c = map(int,input().split())
if b<a:
    print(0)
else:
    print(min(b//a,c))