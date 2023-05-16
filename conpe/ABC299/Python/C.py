N = int(input())
S = input()
if "-" not in S or "o" not in S:
    print(-1)
    exit()

L = S.split("-")

# print(L)

ans = 0
for i in range(len(L)):
    ans = max(ans, len(L[i]))
print(ans)