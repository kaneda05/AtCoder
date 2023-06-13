s = input()
t = input()

ans = len(s)
 
for i in range(len(s)-len(t)+1):
    diff = 0
    for j in range(len(t)):
        if t[j] != s[i+j]:
            diff += 1
    ans = min(ans, diff)
 
print(ans)