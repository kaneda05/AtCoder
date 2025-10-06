X, Y = input().split()

order = {"Ocelot": 1, "Serval": 2, "Lynx": 3}

if order[X] >= order[Y]:
    print("Yes")
else:
    print("No")
