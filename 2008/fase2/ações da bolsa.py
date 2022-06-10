D = int(input())
lucros = [int(i) for i in input().split()]
for c in range(0,D-3):
    soma = lucros[c]+lucros[c+1]+lucros[c+2]+lucros[c+3]
    if c == 0:
        max = soma

    if soma > max:
        max = soma

print(max)