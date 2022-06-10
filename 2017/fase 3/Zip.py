lia,car = [int(input()),int(input())],[int(input()),int(input())]
l,c = lia[0]+lia[1],car[0]+car[1]
if lia[0] == lia[1]:
    l = 0
    l += 2*(lia[0]+lia[1])
if car[0] == car[1]:
    c = 0
    c += 2*(car[0]+car[1])
if lia[0] - 1 == lia[1] or lia[0] + 1 == lia[1]:
    l = 0
    l += 3*(lia[1]+lia[0])
if lia[1] - 1 == lia[0] or lia[1] + 1 == lia[0]:
    l = 0
    l += 3*(lia[1]+lia[0])
if car[0] - 1 == car[1] or car[0] + 1 == car[1]:
    c = 0
    c += 3*(car[1]+car[0])
if car[1] - 1 == car[0] or car[1] + 1 == car[0]:
    c = 0
    c += 3*(car[1]+car[0])

if l == c : r ='empate'
if l > c: r = 'Lia'
if c > l: r = 'Carolina'
print(r)