V = int(input())
P = int(input())

lista = []
x = V//P
pc = V%P

if V % P == 0:
    for c in range(0,P):
        lista.append(x)

for c in range(0,pc):
    lista.append(x+1)
for c in range(0,P-pc):
    lista.append((x))   

for c in lista:
    print(c)
