s = input()

if s[0] == "A" and  s[2:-1].count("C")==1:
    if sum(map(str.isupper, s)) != 2:
        print("WA")
        exit()

else:
    print("WA")
    exit()

print("AC")