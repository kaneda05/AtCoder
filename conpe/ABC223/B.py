s = input()
L = []
n = len(s)
for i in range(n):
    S = s[i:] + s[:i]
    L.append(S)

L.sort()
print(L[0])
print(L[-1])
#print(L)