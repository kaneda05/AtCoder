m = int(input())
m /= 1000

if m<0.1:
    print("00")

elif 0.1<=m<=5:
    if 0.1<=m<=0.99:
        ans = "0"
        ans += str(int(10*m))
        print(ans)
    else:
        ans = str(int(10*m))
        print(ans)


elif 6<=m<=30:
    print(50+int(m))

elif 35<=m<=70:
    print(int((int(m)-30)/5)+80)

elif 70<m:
    print(89)
