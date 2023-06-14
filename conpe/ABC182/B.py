n = int(input())
a = list(map(int,input().split()))
ans = 0
num = 0
for i in range(2,1000+1):
    cnt = 0
    for j in range(n):
        if a[j]%i == 0:
            cnt += 1
    if ans<cnt:
        ans = cnt
        num = i


print(num)