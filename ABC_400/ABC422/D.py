n, k = map(int, input().split())
a = [k >> n] * (1 << n)
k %= 1 << n
for i in range(k):
    a[(i << n) // k] += 1

print(1 if k else 0)
print(*a)