S = input()
b = []
r = []
for i in range(8):
    if S[i] == "B":
        b.append(i+1)
    if S[i] == "R":
        r.append(i+1)

if (b[0]%2==0 and b[1]%2!=0) or (b[1]%2==0 and b[0]%2!=0):
    flag1 = True
else:
    print("No")
    exit()

if r[0]<S.index("K")+1<r[1]:
    flag2 = True
else:
    print("No")
    exit()

if flag1 and flag2:
    print("Yes")
