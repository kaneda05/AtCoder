from collections import deque
S = input()
stack = deque()
for i in range(len(S)):
    if S[i] == "(":
        stack.append(i+1)
    if S[i] == ")":
        print(stack.pop(), i+1)
