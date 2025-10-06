S = input().strip()
T = input().strip()

ok = True
for i in range(1, len(S)):
    if S[i].isupper() and S[i - 1] not in T:
        ok = False
        break

print("Yes" if ok else "No")
