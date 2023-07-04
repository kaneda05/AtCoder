s = input()
t = input()
a = [ord(char)-ord('a') for char in s]
b = [ord(char)-ord("a") for char in t]

#print(a)
#print(b)

ans = set()
for x,y in zip(a,b):
    diff = (x-y)%26
    ans.add(diff)
    
#print(ans)
if len(ans) == 1: print("Yes")
else: print("No")