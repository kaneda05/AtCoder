def gcd(A, B):
    while 1<=A and 1<=B:
        if B<=A:
            A %= B
        else:
            B %= A
    if 1<=A:
        return A
    else:
        return B
            
A, B = map(int,input().split())
print(gcd(A, B))