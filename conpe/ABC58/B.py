O = input()
E = input()
ans = str()
if len(O) == len(E): 
    for i in range(len(O)):
        ans += O[i] + E[i]
elif len(O) > len(E):
    for i in range(len(E)):
        ans += O[i] + E[i]
    ans += O[len(O)-1]

print(ans)