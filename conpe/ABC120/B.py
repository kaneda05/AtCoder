a,b,k = map(int,input().split())
n = max(a,b)
L = []
for i in range(1,n+1):
    if a%i==0 and b%i==0:
        L.append(i)
        
L.sort(reverse=True)
print(L[k-1])