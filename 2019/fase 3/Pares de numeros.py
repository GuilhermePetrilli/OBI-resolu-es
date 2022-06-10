n,i,f = [int(i) for i in input().split()]
vet = [int(i) for i in input().split()]
resposta = []
for c in vet:
    for c2 in vet:
        if c != c2 and c+c2>=i and c+c2<=f:
                if [c,c2] not in resposta or [c2,c] not in resposta:
                    resposta.append([c,c2])
print(int(len(resposta)/2))