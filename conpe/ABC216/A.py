X,Y=map(int,input().split(sep="."))
print(str(X)+("-" if Y<=2 else "" if Y<=6 else "+"))