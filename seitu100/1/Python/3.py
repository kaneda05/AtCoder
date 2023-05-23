S = input()
li = ["A","C","G","T"]
acgt = -100000
cnt = 0
for s in S:
    if s in li:
        cnt += 1
        acgt = max(acgt,cnt)
    else:
        cnt = 0
        
acgt = max(acgt,cnt)

print(acgt)

