n = int(input())
s = list(input())

S = []
for i in range(len(s)):
    if ord("A")<=ord(s[i])+n<=ord("Z"):
        S.append(chr(ord(s[i])+n))
    else:
        S.append(chr(ord(s[i])+n-26))

print("".join(S))
