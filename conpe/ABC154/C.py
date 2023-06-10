n = int(input())
a = list(map(int,input().split()))
a_set = set(a)
print("YES" if len(a_set)==n else "NO")