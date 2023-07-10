a,b,c,d,e,f,x = map(int, input().split())

st = x // (a+c)
sa = x // (d+f)

T = b * (st*a + min(a, x%(a+c)))
A = e * (sa*d + min(d, x%(d+f)))

if T == A: print("Draw")
elif T > A: print("Takahashi")
else: print("Aoki") 