x,m = int(input()),int(input())
usos = [int(input()) for i in range(m)]
cota = 0
for c in usos:
    cota+=x-c
print(cota+x)
