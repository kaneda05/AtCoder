c = [list(input().split()) for _ in range(4)]
for i in range(3,-1,-1):
    for j in range(3,-1,-1):
        print(c[i][j], end=" ")
    print()