A = int(input())
N = int(input())

total = 0
used = set()

for i in range(1, 10):
    if i <= N:
        s = str(i)
        x = i
        digits = []
        while x > 0:
            digits.append(str(x % A))
            x //= A
        if digits == digits[::-1]:
            total += i
            used.add(i)

for half in range(1, 10**6):
    s = str(half)

    even_pal = int(s + s[::-1])
    if even_pal <= N and even_pal not in used:
        x = even_pal
        digits = []
        while x > 0:
            digits.append(str(x % A))
            x //= A
        if digits == digits[::-1]:
            total += even_pal
            used.add(even_pal)

    odd_pal = int(s + s[:-1][::-1])
    if odd_pal <= N and odd_pal not in used:
        x = odd_pal
        digits = []
        while x > 0:
            digits.append(str(x % A))
            x //= A
        if digits == digits[::-1]:
            total += odd_pal
            used.add(odd_pal)

print(total)
