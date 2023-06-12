n = int(input())
A = list(map(int,input().split()))
numbers = [0]*(n+1)
for a in A:
    numbers[a] += 1

for i in range(1,n+1):
    print(numbers[i])