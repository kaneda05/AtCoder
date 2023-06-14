import numpy as np
h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
a = np.array(a)
print(np.sum(a-np.min(a)))
