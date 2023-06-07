from itertools import permutations
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
 
time = [A,B,C,D,E]
ans = 10**18
 
for order in permutations(time,5):
    current_time = 0
    for j in range(5):
        if j == 4:
            current_time += order[j]
        elif order[j]%10 == 0:
            current_time += order[j]
        else:
            current_time += (order[j]//10+1)*10
            
    ans = min(ans,current_time)
 
print(ans)