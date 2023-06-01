s = input()
ans = []
for i in range(len(s)):
    if i%2==0:
        ans.append(s[i])
        
print("".join(ans))