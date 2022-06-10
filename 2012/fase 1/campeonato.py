c1,c2,c3,f1,f2,f3 = [int(i) for i in input().split()]
r,fr,cr = 'C',0,0
if c1<f1: fr +=1
if c2<f2: fr +=1
if c3<f3: fr +=1
if f1<c1: cr +=1
if f2<c2: cr +=1
if f3<c3: cr +=1
if fr>=2:
    r = 'F'

if cr == fr:
    r = '='
print(r)