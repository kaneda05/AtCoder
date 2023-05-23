N = int(input())
ans = 0

for i in range(1,N+1):
    cnt1 = 0
    if i%2==0:
        continue
    else:
        for j in range(1,i+1):
            if i%j==0:
                cnt1 += 1

        if cnt1==8:
            ans += 1

print(ans)
