s = input()
k = int(input())

ans = set()
for i in range(len(s)+1-k):
    # print(s[i:i+k])
    ans.add(s[i:k+i])

print(len(ans))
