n,p1,p2 = int(input()),input().replace('.','a').replace(' ','a').replace(',','a'),input().replace('.','a').replace(' ','a').replace(',','a')
c = 0
r = 'N'
for i,c1 in enumerate(p1):
    if c1 in p2: c+=1;list(p2).pop(i)
if c == n: r = 'S'
print(r)