N = int(input())
A = sorted(list(map(int,input().split())))
unique_sorted = sorted(set(A))

print(len(unique_sorted))
print(*unique_sorted)