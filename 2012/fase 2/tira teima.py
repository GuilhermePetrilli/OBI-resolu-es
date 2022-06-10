x,y = [int(i) for i in input().split()]
r ='dentro'
if x<0 or y<0: r = 'fora'
if x>432 or y>468: r = 'fora'
print(r)