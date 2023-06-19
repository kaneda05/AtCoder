n = int(input())
for k in range(10**18):
    if 2 ** k > n:
        print(k-1)
        exit()