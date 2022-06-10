n = int(input())
dados = [list(map(lambda x: int(x),input().strip())) for i in range(n)]
for c,dado in enumerate(dados):
    for c2,dado2 in enumerate(dados):
        pares = [[dado[0],dado[5]],[dado[1],dado[3]],[dado[2],dado[4]]]
        pares2 = [[dado2[0],dado2[5]],[dado2[1],dado2[3]],[dado2[2],dado2[4]]]
        if c != c2:
            
