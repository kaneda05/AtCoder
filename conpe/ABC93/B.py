a, b, k = map(int, input().split())
ans = set()
for i in range(k):
    ans.add(min(a + i, b))
    ans.add(max(b - i, a))

print(*sorted(list(ans)), sep="\n")
