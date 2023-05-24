N = int(input())
S = input()

ans = "b"

if S == ans:
    print(0)
    exit()

for i in range(1,101):
    if i % 3 == 1:
        ans = "a" + ans + "c"

    elif i % 3 == 2:
        ans = "c" + ans + "a"

    else:
        ans = "b" + ans + "b"

    if len(S)<len(ans):
        print(-1)
        exit()

    if S == ans:
        print(i)
        exit()
