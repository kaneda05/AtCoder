def prime_number(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        else:
            return True


Q = int(input())
for i in range(Q):
    X = int(input())
    if prime_number(X):
        print("Yes")
    else:
        print("No")