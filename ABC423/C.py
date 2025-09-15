N, R = map(int, input().split())
L = list(map(int, input().split()))

open_doors = L.count(0)
left_open = any(L[:R])
right_open = any(L[R:])

ans = open_doors
if left_open and right_open:
    ans += 2
elif left_open or right_open:
    ans += 0

print(ans)