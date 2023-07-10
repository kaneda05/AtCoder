v,a,b,c = map(int,input().split())
cnt = 1
while 0<v:
    if cnt%3==1:
        if v<a:
            break
        else:
            v-=a

    if cnt%3==2: 
        if v<b:
            break
        else:
            v-=b
    
    if cnt%3==0: 
        if v<c:
            break
        else:
            v-=c
    cnt += 1

if cnt%3==1: print("F")
elif cnt%3==2: print("M")
else: print("T")
#print(cnt)