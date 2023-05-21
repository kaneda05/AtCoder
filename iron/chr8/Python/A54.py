Q = int(input())
queries = [ input().split() for i in range(Q) ] 

D = {}

for q in queries:
    if q[0] == "1":
        D[q[1]] = q[2]

    if q[0] == "2":
        print(D[q[1]])