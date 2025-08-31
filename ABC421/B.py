X, Y = map(int, input().split())

def f(x):
    return int(str(x)[::-1])

a_prev2 = X
a_prev1 = Y

for i in range(3, 11):
    a = f(a_prev1 + a_prev2)
    a_prev2, a_prev1 = a_prev1, a

print(a_prev1)
