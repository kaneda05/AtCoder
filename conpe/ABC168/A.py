n = input()
l1 = [2,4,5,7,9]
l2 = [0,1,6,8,9]
l3 = [3]

if len(n) == 3:
    if int(n[2]) in l1:
        print("hon")
    elif int(n[2]) in l2:
        print("pon")
    else:
        print("bon")

elif len(n) == 2:
    if int(n[1]) in l1:
        print("hon")
    elif int(n[1]) in l2:
        print("pon")
    else:
        print("bon")

else:
    if int(n[0]) in l1:
        print("hon")
    elif int(n[0]) in l2:
        print("pon")
    else:
        print("bon")
