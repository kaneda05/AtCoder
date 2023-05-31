a,b,c,d = map(int,input().split())
cn1 = max(a,c)
cn2 = min(b,d)
if cn2<cn1:
    print(0)
else:
    print(cn2-cn1)