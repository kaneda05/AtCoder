n = int(input())
if n >=10 and n < 42:
  print("AGC0"+str(n))
elif n >= 42:
  n += 1
  print("AGC0"+str(n))
else:
  print("AGC00"+str(n))