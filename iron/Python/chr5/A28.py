N = int(input())
ans = 0
for i in range(N):
    T, A = input().split()
    A = int(A)
    if T == "+":
        ans += A

    elif T == "-":
        ans -= A
        
    else:
        ans *= A

    if ans < 0:
        ans += 10000

    ans %= 10000
    print(ans)