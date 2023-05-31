h,w = map(int,input().split())

a = [["#"]+list(input())+["#"] for _ in range(h)]

a.insert(0,["#"*(w+2)])
a.insert(h+1,["#"*(w+2)])

for i in range(h+2):
    print("".join(a[i]))