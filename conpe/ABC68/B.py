n = int(input())
cnt = 0
cur_cnt = 0
for i in range(1,n+1):
    cur_cnt = 0
    x = i
    while x%2==0:
        cur_cnt += 1
        x/=2
    if cnt<=cur_cnt:
        ans = i
        cnt = cur_cnt

print(ans)