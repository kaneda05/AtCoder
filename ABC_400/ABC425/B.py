N = int(input())
A = list(map(int,input().split()))

used = [False] * (N + 1)
for x in A:
    if x != -1:
        if used[x]:
            print("No")
            exit()
        used[x] = True


re = [i for i in range(1, N+1) if not used[i]]

ri = 0
P = []
for x in A:
    if x == -1:
        P.append(re[ri])
        ri += 1
    else:
        P.append(x)

print("Yes")
print(*P)