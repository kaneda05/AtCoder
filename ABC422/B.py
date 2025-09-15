N = int(input())
L = list(map(int, input().split()))

left_reach = 0
for i in range(N):
    if L[i] == 0:
        left_reach = i + 1
    else:
        break

right_reach = N
for i in range(N-1,-1,-1):
    if L[i] == 0:
        right_reach = i
    else:
        break

left_rooms = set(range(0, left_reach+1))
right_rooms = set(range(right_reach, N+1))

all_rooms = set(range(N+1))

unreachable = all_rooms - (left_rooms | right_rooms)
print(len(unreachable))