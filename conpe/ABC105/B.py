n = int(input())
ans = []
for i in range(30):
    for j in range(30):
        if 4*i+7*j==n:
            print("Yes")
            exit()
            
print("No")