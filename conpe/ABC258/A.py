k = int(input())

HH = 21+k//60
MM = k%60


if k%60<10:
    print(str(HH)+":"+"0"+str(MM))
else:
    print(str(HH)+":"+str(MM))