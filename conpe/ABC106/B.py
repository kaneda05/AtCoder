n = int(input())
ans = 0
for i in range(1,n+1):
    cnt = 0

    if i % 2 != 0:
        for j in range(1,i+1):
            if i%j==0:
                cnt += 1
                j/=i

        if cnt==8:
            ans += 1

print(ans)