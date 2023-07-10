s = list(map(int,input()))

for i in range(10):
    if i not in s:
        print(i)
        exit()