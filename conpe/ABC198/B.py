n = input()
if n==n[::-1]:
    print("Yes")
    exit()

else:
    num = 1
    m = len(n)
    while num<m+1:
        n = "0" + n
        #print(n)
        if n==n[::-1]:
            print("Yes")
            exit()
        num += 1

print("No")