Q = int(input())
m = []
balance = 0
min_balance = 0

history = [(0, 0)]

for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        c = query[1]
        m.append(c)
        if c == "(":
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
        m.append(c)
        history.append((balance, min_balance))
    else:
        m.pop()
        history.pop()
        balance, min_balance = history[-1]
    
    if balance == 0 and min_balance >= 0:
        print("Yes")
    else:
        print("No")