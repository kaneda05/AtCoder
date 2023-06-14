n = int(input())
S = set(input() for _ in range(n))
for s in S:
    if "!" + s in S:
        print(s)
        exit()


print("satisfiable")
