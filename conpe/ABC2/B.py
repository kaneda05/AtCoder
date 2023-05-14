W = input()
ans = []
l = ["a", "i", "u", "e", "o"]
for i in range(len(W)):
    if W[i] not in l:
        ans.append(W[i])
print("".join(ans))