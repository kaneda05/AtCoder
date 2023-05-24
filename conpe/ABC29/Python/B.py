S = [input() for _ in range(12)]
ans = 0
for s in S:
    if 1<=s.count("r"):
        ans += 1
print(ans)