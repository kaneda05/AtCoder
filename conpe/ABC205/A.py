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

a,b = nm()
print((b/100)*a)
