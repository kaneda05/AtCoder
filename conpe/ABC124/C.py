s = list(input())
n = len(s)
cnt = 0
for i in range(n-1):
    if s[i]==s[i+1]:
        cnt += 1
        if s[i+1] == "1":
            s[i+1] = "0"
        else:
            s[i+1] = "1"

print(cnt)