n,k = map(int,input().split())
for i in range(k):
    n = int(n)
    if n%200==0:
        n//=200
        #print(n)
    else:
        n = str(n) + "200"
        #print(n)

print(n)