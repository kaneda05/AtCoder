n, k, a = map(int,input().split())
if a+k-1<=n:
    print(a+k-1)
elif (a+k-1-n)%n!=0 and a+k-1>n:
    print((a+k-1-n)%n)
elif (a+k-1-n)%n==0 and a+k-1>n:
    print(n)