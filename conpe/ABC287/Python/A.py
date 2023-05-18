N = int(input())
cnt = 0
for i in range(N):
    S = input()
    if S == "For":
        cnt += 1

print("Yes" if N/2<=cnt else "No")