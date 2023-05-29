s = input()
S = s.split("+")

ans = 0
for i in S:
    if i.count("0")==0:
        ans += 1

print(ans)
