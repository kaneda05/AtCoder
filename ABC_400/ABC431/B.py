X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

attached = set()
current_w = X

for _ in range(Q):
    p = int(input())
    if p in attached:
        current_w -= W[p-1]
        attached.remove(p)
    else:
        current_w += W[p-1]
        attached.add(p)
    print(current_w)