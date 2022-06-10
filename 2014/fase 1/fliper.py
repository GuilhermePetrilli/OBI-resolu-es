p,r = [int(i) for i in input().split()]
r2 = 'C'
if p == 1 and r == 0:
    r2 = 'B'
if p == 1 and r == 1:
    r2 = "A"

print(r2)