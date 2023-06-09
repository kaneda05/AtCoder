n = int(input())
s = input()
ans = 0
for i in range(n-2):
    if s[i]+s[i+1]+s[i+2] == "ABC":
        ans += 1
print(ans)