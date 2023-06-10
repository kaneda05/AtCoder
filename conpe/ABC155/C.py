from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    s = input()
    d[s] += 1

#print(d)
#print(d.values())
max_vote = max(d.values())
d = sorted(d.items())
for key,value in d:
    if value==max_vote:
        print(key)