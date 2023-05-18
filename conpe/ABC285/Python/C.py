S = input()
L =[]
for s in S:
    L.append(ord(s)-64)

L = L[::-1]

ans = 0
for i in range(len(L)):
    ans += 26**i*L[i]   # 26進数へ

print(ans)