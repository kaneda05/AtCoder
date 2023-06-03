n = int(input())
print("ABC" if n<=999 else "ABD")

"""
n = int(input())
if n<=999:
    ans = "ABC"
    if 1<=n<=9:
        ans += "00"
        ans += str(n)
        print(ans)
    elif 10<=n<=99:
        ans += "0"
        ans += str(n)
        print(ans)
    else:
        ans += str(n)
        print(ans)
        
    
else:
    ans = "ABD"
    n-=999
    if 1<=n<=9:
        ans += "00"
        ans += str(n)
        print(ans)
    elif 10<=n<=99:
        ans += "0"
        ans += str(n)
        print(ans)
    else:
        ans += str(n)
        print(ans)
"""