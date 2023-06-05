a = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
for i in range(3):
    if i == 0:
        continue
    else:
        ans += abs(a[i]-a[i-1])
        
print(ans)
