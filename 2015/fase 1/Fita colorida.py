n = int(input())
qs = [int(i) for i in input().split()]
r = ''
p = 0

def f(c):
    d=0
    for c2 in range(n):
        d+=1
        try:
            if qs[c-c2] == 0 or qs[c+c2] == 0:
                return d-1
        except IndexError:
            pass
    

for count,q in enumerate(qs):
    if q == 0:
        r += '0 '
    if q == -1:
        r += f'{f(count)} '

print(r)