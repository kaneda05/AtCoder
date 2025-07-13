A = int(input())
N = int(input())

total = 0
used = set()

# 1桁の回文（1～9）
for i in range(1, 10):
    if i <= N:
        s = str(i)
        # A進数変換
        x = i
        digits = []
        while x > 0:
            digits.append(str(x % A))
            x //= A
        if digits == digits[::-1]:
            total += i
            used.add(i)

# 2桁以上の回文（偶数・奇数桁）
for half in range(1, 10**6):  # 6桁以上は N=10^12 でも安全
    s = str(half)

    # 偶数桁: 123 + 321 → 123321
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

    # 奇数桁: 123 + 21 → 12321
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
