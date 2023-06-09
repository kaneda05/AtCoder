a = int(input())
b = int(input())
for i in range(1,4):
    if a == i or b == i:
        continue
    else:
        print(i)