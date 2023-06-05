n = int(input())
w = [input() for _ in range(n)]
for i in range(1,n):
    if 1<w.count(w[i]):
        print("No")
        exit()
    else:
        if w[i-1][-1]==w[i][0]:
            continue
        else:
            print("No")
            exit()

print("Yes")