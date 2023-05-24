X = input()
S = X.replace("ch","g")
li = ["g","o","k","u"]
for s in S:
    if s in li:
        continue
    else:
        print("NO")
        exit()

print("YES")
