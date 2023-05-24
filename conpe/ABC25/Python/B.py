N, A, B = map(int,input().split())
pos = 0
for i in range(N):
    s, d = input().split()
    d = int(d)
    if s == "East":
        if A<=d<=B:
            pos += d
        elif d<A:
            pos += A
        elif B<d:
            pos += B
    else:
        if A<=d<=B:
            pos -= d
        elif d<A:
            pos -= A
        elif B<d:
            pos -= B

if 0<pos:
    print("East", pos)
elif pos == 0:
    print(0)
else:
    print("West", abs(pos))