a,b,c = [int(i) for i in input().split()]
x,y,z = [int(i) for i in input().split()]
r = (x//a)*(y//b)*(z//c)
if a>x or b>y or c>z:
    r = 0
print(r)