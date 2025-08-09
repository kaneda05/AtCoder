from collections import defaultdict
from math import gcd

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

slope_counts = defaultdict(int)

for i in range(N):
    for j in range(i+1,N):
        x1, y1 = points[i]
        x2, y2 = points[j]

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            slope = (1, 0)
        elif dy == 0:
            slope = (0, 1)
        else:
            divisor = gcd(abs(dx), abs(dy))
            dx //= divisor
            dy //= divisor
            
            if dx < 0:
                dx, dy = -dx, -dy
            slope = (dx, dy)
        
        slope_counts[slope] += 1
    
total_parallels = 0
for k in slope_counts.values():
    total_parallels += k * (k-1) // 2
    
midpoint_counts = defaultdict(int)
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        midpoint = (x1 + x2, y1 + y2)
        midpoint_counts[midpoint] += 1

total_parallelograms = 0
for k in midpoint_counts.values():
    total_parallelograms += k * (k-1) // 2
    
ans = total_parallels - total_parallelograms
print(ans)