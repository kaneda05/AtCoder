a = int(input())
b = int(input())

a1 = a
a2 = a
b1 = b
b2 = b

cnt1 = 0
cnt2 = 0

while a1!=b1:
    a1 -= 1
    if a1 == -1:
        a1 = 9
    cnt1 += 1

while a2!=b2:
    a2 += 1
    if a2 == 10:
        a2 = 0
    cnt2 += 1

print(min(cnt1,cnt2))