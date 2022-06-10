L = int(input())
L=L**2
c= 1
x = 1
if L % 2 == 1:
    x = 2
while L > x:
    L/=2
    c*=2
print(c)

