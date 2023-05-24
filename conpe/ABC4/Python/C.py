N = int(input())
li = ["1","2","3","4","5","6"]
mod = N
ans1 = 0
ans2 = 0
L = []

for i in range(30):
    ans1 = (i%5)+1
    ans2 = (i%5)+2
    li[ans1-1],li[ans2-1] = li[ans2-1],li[ans1-1]
    L.append("".join(li))


print(L[N%30-1])
