n,m,x,y = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

for z in range(x+1,y+1):
    if max(X) < z and z<= min(Y):
        print("No War")
        exit()

print("War")