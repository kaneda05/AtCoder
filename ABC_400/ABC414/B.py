N = int(input())
total_length = 0
result = []

for _ in range(N):
    c, l = input().split()
    l = int(l)
    total_length += l
    if total_length > 100:
        print("Too Long")
        exit()
    result.append(c * l)

print("".join(result))
