N = int(input())
S = input()
x = 0
y = 0
mark = set()
mark.add((x,y))
flag = False
for i in range(N):
    if S[i] == "R":
        x += 1

       
    if S[i] == "L":
        x -= 1

    if S[i] == "U":
        y += 1


    if S[i] == "D":
        y -= 1

    if (x,y) in mark:
        print("Yes")
        exit()

    mark.add((x,y))

print("No")