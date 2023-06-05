k = int(input())
if k%2==0:
    k//=2
    print(k*k)
else:
    k//=2
    print(k*(k+1))