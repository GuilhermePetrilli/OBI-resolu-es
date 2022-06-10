n,c,l = [int(i) for i in input().split()]
es = [int(i) for i in input().split()]
pos,resposta = 1,0
if l == 1: resposta+=1
for c in es:
    pos+=c
    if pos == n+1: pos = 1
    if pos == 0: pos = n
    if pos == l: resposta +=1
print(resposta)