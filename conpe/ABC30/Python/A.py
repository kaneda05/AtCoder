A,B,C,D = map(int,input().split())
if B/A < D/C:
    print("AOKI")
elif B/A==D/C:
    print("DRAW")
else:
    print("TAKAHASHI")