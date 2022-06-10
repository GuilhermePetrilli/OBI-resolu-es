n,min = [int(i) for i in input().split()]
resposta = 0

for c in range(n):
    pontos = sum([int(i) for i in input().split()])
    if pontos>=min:
        resposta+=1

print(resposta)