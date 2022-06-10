n = int(input())
caminho = [int(i) for i in input().split()]
gato=-1
def main(gato):
    pp=-1
    ok=0
    for i,passo in enumerate(caminho):

        if ok == 1:
            c+=1
            if c== 2:
                ok =0

        if passo == 1:
            gato+=1
        if i-2 == -1 or i-2 == -2:
            pass
        else:
            if passo == pp and pp == caminho[i-2] and caminho[i-2] == 1 and ok == 0:
                ok= 1
                gato-=1
                c=0
        if pp == passo and passo == 0:
            return -1
        pp = passo 
    return gato
print(main(gato))
