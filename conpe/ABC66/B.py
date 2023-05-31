s = input()

n = len(s)
ans = 0
for i in range(n):
    if i%2==0:
        a = s[:i//2]
        b = s[i//2:i]
        if a==b:
            ans = max(ans,i)
print(ans)