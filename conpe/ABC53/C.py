n = int(input())
if n<=6:
    print(1)
elif (n<=11):
    print(2)
else:
    ans=0
    if 0<n%11 and n%11<=6:
        ans = 1
    if 6<n%11:
        ans = 2
    
    print(2*(n//11)+ans)