n = int(input())
S = input()
x = 0
ans = [0]
for s in S:
    if s == "I":
        x += 1
        ans.append(x)
    else:
        x -= 1
        ans.append(x)

print(max(ans))