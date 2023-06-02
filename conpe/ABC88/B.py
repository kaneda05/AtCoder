n = int(input())
a = list(map(int,input().split()))
ans = 0
a.sort(reverse=True)
alice = a[0::2]
bob = a[1::2]
ans = sum(alice)-sum(bob)
print(ans)