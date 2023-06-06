s = input()
yy,mm,dd = s.split("/")
if int(yy)<2019:
    print("TBD")
elif int(yy)<=2019 and 5<=int(mm):
    print("TBD")
else:
    print("Heisei")