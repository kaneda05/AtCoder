N = int(input())
hh = ""
if (N//3600)<10:
    hh += "0" + str(N//3600)
else:
    hh += str(N//3600)

N%=3600

mm = ""
if (N//60)<10:
    mm += "0" + str(N//60)
else:
    mm += str(N//60)

N%=60

ss = ""
if N<10:
    ss += "0" + str(N)
else:
    ss += str(N)

print(hh+":"+mm+":"+ss)