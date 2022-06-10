lin,col = [int(i) for i in input().split()]
pele = [input().split() for i in range(lin)]
r=0

for il,linha in enumerate(pele):
    for ic,nun in enumerate(linha):
        ok=0
        nun = int(nun)
        if nun == 1:
            r+=1
            try:
                if len(linha)>1:
                    f = il -1
                    if f == -1: f = len(col)
                    if int(pele[f][ic]) == 1: ok+=1
            except IndexError:
                pass
            try:
                if int(linha[ic-1]) == 1: ok+=1
            except IndexError:
                pass
            if ok >=1:
                r -=1
            
print(r)