def func1(x):
    return x**2+2*x+3

def func2(t):
    return func1(func1(func1(t)+t)+func1(func1(t)))

t = int(input())
print(func2(t))