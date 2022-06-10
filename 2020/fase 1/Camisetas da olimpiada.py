n,ns,p,m = int(input()),[int(i) for i in input().split()],int(input()),int(input())
cp,cm,r = 0,0,'N'
for i in ns:
    if i == 1: cp+=1
    if i ==2: cm+=1
if [cp,cm] == [p,m]: r = 'S'
print(r)