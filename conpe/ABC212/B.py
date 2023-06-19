x = list(map(int,input()))
flag = True

if x[0] == x[1] == x[2] == x[3]:
    print("Weak")
    exit()
else:
    for i in range(3):
        if x[i]!=9:
            if x[i] + 1 == x[i+1]:
                continue
            else:
                flag = False
        if x[i]==9:
            if x[i+1] == 0:
                continue
            else:
                flag = False

if flag: print("Weak")
else: print("Strong")