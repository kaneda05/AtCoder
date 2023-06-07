n,x = map(int,input().split())
l = [0] + list(map(int,input().split()))
cnt = 0
ans = 0

for i in range(n+1):
    ans += l[i]
    if ans <= x:
        cnt += 1
    else:
        break

print(cnt)