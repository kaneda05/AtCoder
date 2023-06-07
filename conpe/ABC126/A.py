n,k = map(int,input().split())
s = input()
S = []
for i in range(n):
    if i == k-1:
        S.append(s[i].lower())
    else:
        S.append(s[i])

print("".join(S))