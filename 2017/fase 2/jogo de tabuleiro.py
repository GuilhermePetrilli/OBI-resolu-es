n = int(input())
tabuleiro = [list(map(lambda x: int(x),input().split())) for i in range(n)]
for row,linha in enumerate(tabuleiro):
    for col,casa in enumerate(linha):
        casa= int(casa)
        if row > 0 and col > 0:
            if linha[col-1]+tabuleiro[row-1][col]+tabuleiro[row-1][col-1] < 1:
                linha[col] = 1
            else:
                linha[col] = 0
print(tabuleiro[n-1][n-1])