a,b = input().split()
ans1 = ""
ans1 += a*int(b)
ans2 = ""
ans2 += b*int(a)


print(ans1 if ans1<ans2 else ans2)