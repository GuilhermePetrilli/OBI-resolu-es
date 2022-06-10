t = [[int(i) for i in input().split()] for i in range(15)]
v = 0
def main():
    for row,linha in enumerate(t):
        for col,nun in enumerate(linha):
            # horizontal
            if col - 1 > 4 and nun != 0:
                if nun == linha[col-1] and nun == linha[col-2] and nun == linha[col-3] and nun == linha[col-4]:
                    return nun
            if col + 1 < 11 and nun != 0:
                if nun == linha[col+1] and nun == linha[col+2] and nun == linha[col+3] and nun == linha[col+4]:
                    return nun
            # vertical
            if row - 1 > 4 and nun != 0:
                if nun == t[row-1][col] and nun == t[row-2][col] and nun == t[row-3][col] and nun == t[row-4][col]:
                    return nun
            if row + 1 < 11 and nun != 0:
                if nun == t[row+1][col] and nun == t[row+2][col] and nun == t[row+3][col] and nun == t[row+4][col]:
                    return nun
            # diagonal
            if row + 1 < 11 and col + 1 < 11 and nun != 0:
                if nun == t[row+1][col+1] and nun == t[row+2][col+2] and nun == t[row+3][col+3] and nun == t[row+4][col+4]:
                    return nun
            if row - 1 > 4 and col - 1 > 4 and nun != 0:
                if nun == t[row-1][col-1] and nun == t[row-2][col-2] and nun == t[row-3][col-3] and nun == t[row-4][col-4]:
                    return nun
            if row + 1 < 11 and col - 1 > 4 and nun != 0:
                if nun == t[row+1][col-1] and nun == t[row+2][col-2] and nun == t[row+3][col-3] and nun == t[row+4][col-4]:
                    return nun
            if row - 1 > 4 and col + 1 < 11 and nun != 0:
                if nun == t[row-1][col+1] and nun == t[row-2][col+2] and nun == t[row-3][col+3] and nun == t[row-4][col+4]:
                    return nun
            
print(main())