Q = int(input())
bag = []
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        bag.append(query[1])
    else:
        bag.sort()
        print(bag[0])
        bag.pop(0)