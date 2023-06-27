s = list(input())
t = list(input())
flag = True
for i in range(len(t)):
    if s[i] == t[i]:
        pass
    else:
        if t[i+1] == s[i] and flag == True:
            t[i],t[i+1] = t[i+1],t[i]
            flag = False
        else:
            print("No")
            exit()

print("Yes")