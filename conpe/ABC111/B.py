n = int(input())
if n%111==0:
    print(n)
elif n<111:
    print(111)
else:
    for i in range(1,10):
        if 111*i<n<111*(i+1):
            print(111*(i+1))
            exit()