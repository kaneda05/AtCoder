s = input()
for i in range(len(s)):
    if i%2!=0:
        if s[i].isupper()==True:
            pass
        else:
            print("No")
            exit()
    
    else:
        if s[i].islower()==True:
            pass
        else:
            print("No")
            exit()

print("Yes")