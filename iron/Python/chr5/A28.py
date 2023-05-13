N = int(input())
ans = 0
for i in range(N):
    T, A = input().split()
    A = int(A)
    if T == "+":
        ans += A
        print(ans%10000)

    elif T == "-":
        ans -= A
        print(ans%10000)
        
    else:
        ans *= A
        print(ans%10000)