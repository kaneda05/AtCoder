n = int(input())
ans = 10**10
for i in range(1,n+1):
    ans = min(ans, abs(i-(n//i)) + (n-i*(n//i)))
    
print(ans)