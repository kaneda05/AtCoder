import math
n = int(input())
n *= 1.08
n = math.floor(n)
if n<206: print("Yay!")
elif n==206: print("so-so")
else: print(":(")
