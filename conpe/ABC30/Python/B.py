n, m = map(int,input().split())

tan = ((n%12)/12)*360 + (m/60)/12 * 360
tyo = (m/60)*360
if tan>tyo:
    print(min(tan-tyo, tyo+360-tan))
else:
    print(min(tyo-tan, tan+360-tyo))