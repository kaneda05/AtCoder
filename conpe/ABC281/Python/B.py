S = input()
flag1 = False
if S[0].isupper() and S[-1].isupper():
    flag1 = True

flag2 = False
if S[1:-1].isdecimal() and S[1]!="0":
    if 100000<=int(S[1:-1])<=999999:
         flag2 = True

print("Yes" if flag1 and flag2 else "No")
