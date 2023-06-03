n = int(input())
s = input()

ans = 0
alphabet = [chr(i) for i in range(ord("a"),ord("z")+1)]

for i in range(n):
    x = s[i:]
    y = s[:i]

    cnt = 0
    for j in alphabet:
        if (j in x) and (j in y):
            cnt += 1

    ans = max(ans,cnt)

print(ans)