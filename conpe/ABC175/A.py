s = input()
ans = 0
cnt = 0
for i in s:
    if i == "R":
        cnt += 1
        ans = max(ans,cnt)
    else:
        cnt = 0
print(ans)