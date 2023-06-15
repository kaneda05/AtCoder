n = int(input())
a = list(map(int,input().split()))
cnt = [0]*200

#2つの数字の差が200で割り切れるということは
#2つの数字をそれぞれ200で割った際の余りが同じということ
#200の除算の余り1-199なので、それぞれの余りについて数をカウントする。
for i in a:
    cnt[i%200]+=1

#余りが同じ組み合わせを２つとる。
#nC2は重複を排除するため、必然的にi<Jとできる。
ans = 0
for i in range(200):
    ans += cnt[i]*(cnt[i]-1)//2
    
print(ans)