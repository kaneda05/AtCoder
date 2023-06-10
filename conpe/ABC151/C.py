n,m = map(int,input().split())
cnt_ac_num = set()
cnt_wa = [0]*(n+1)
for i in range(m):
    p,s = input().split()
    p = int(p)
    if s == "AC":
        cnt_ac_num.add(p)
    elif s == "WA" and p not in cnt_ac_num:
        cnt_wa[p] += 1


for i in range(1,n+1):
    if i not in cnt_ac_num:
        cnt_wa[i] = 0

ans_ac_num = len(cnt_ac_num)
ans_wa_num = sum(cnt_wa)
print(ans_ac_num, ans_wa_num)