S = input()
li = [chr(i) for i in range(ord("A"),ord("F")+1)]
cnt_list = []
for i in range(len(li)):
    cnt_list.append(S.count(li[i]))

print(*cnt_list)