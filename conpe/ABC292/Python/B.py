N, Q = map(int,input().split())
table = [2]*(N+1)
for i in range(Q):
    num, x = map(int,input().split())
    if num == 1:
        table[x] -= 1
    
    if num == 2:
        table[x] -= 2

    if num == 3:
        if 0<table[x]:
            print("No")
        else:
            print("Yes")
