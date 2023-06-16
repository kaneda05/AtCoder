import sys
if sys.platform =='ios':
	import clipboard
	a=clipboard.get()
	a = a.split('\n')
	text = '\n'.join(a)
	with open('input_file.txt','w') as f:
		f.write(text)
	sys.stdin = open('input_file.txt')
sys.setrecursionlimit(410000000)
stdin = sys.stdin 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()
nm = lambda: map(int,input().split())

x, y = nm()
if x==y: print(x)
elif (x==2 and y==1) or (x==1 and y==2): print(0)
elif (x==1 and y==0) or(x==0 and y==1): print(2)
else: print(1)
