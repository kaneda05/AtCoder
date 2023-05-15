N = int(input())
cnt = 0
A= list(map(int, input().split()))
for a in A:
    if a%3 == 2:
        cnt += 1  
        if a % 2 == 1:
            cnt += 1
    elif a%2 == 0:
        cnt += 1
        if a % 3 == 0:
            cnt += 2
    else:
        pass
print(cnt)