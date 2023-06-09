s = input()
s1 = s
s2 = s[::-1]
cnt = 0
for i in range(len(s)):
    if s1[i] != s2[i]:
        cnt += 1

print(cnt//2)