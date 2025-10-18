S, A, B, X = map(int, input().split())

cycle = A + B
full = X // cycle
remain = X % cycle

distance = S * (A * full + min(remain, A))
print(distance)
