n = int(input())
L = list(map(int,input().split()))

ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if L[i] != L[j] and L[i]!=L[k] and L[j]!=L[k] :
                if L[i]+L[j]>L[k] and L[i]+L[k]>L[j] and L[k]+L[j]>L[i] :
                    ans += 1
print(ans)

