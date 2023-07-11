n,m,x,t,d = map(int,input().split())
if x <= m <= n: print(t)
elif n <= m: print(t)
else: print(t-d*(x-m))