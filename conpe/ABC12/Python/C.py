N = int(input())
wa = 2025
for i in range(1,10):
    for j in range(1,10):
        if wa-N == i*j:
            print(str(i)+" x "+str(j))