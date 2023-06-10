a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
card = [[False]*3 for _ in range(3)]


for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == a[i][j]:
                card[i][j] = True

# 横確認
for i in range(3):
    cnt = 0
    for j in range(3):
        if card[i][j]:
            cnt += 1

    if cnt == 3:
        print("Yes")
        exit()

# 縦確認
for j in range(3):
    cnt = 0
    for i in range(3):
        if card[i][j]:
            cnt += 1

    if cnt == 3:
        print("Yes")
        exit()

# 右斜め確認
cnt = 0
for i in range(3):
    if card[i][i]:
        cnt += 1
if cnt == 3:
        print("Yes")
        exit()

# 左斜め確認
cnt = 0
for i in range(3):
    if card[i][2-i]:
        cnt += 1
if cnt == 3:
        print("Yes")
        exit() 

print("No")