d,na = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
c = input().split()
t = 0
apagar = []
for tempo in c:
    for i,arvore in enumerate(p):
        if tempo == 'E':
            p[i]-=1
        if tempo == 'C':
            p[i]+=1
        if p[i] == 0:
            apagar.append(i)
        print(tempo,arvore,t)
        t+=arvore
        
    for a in apagar:
        p =[int(i) for i in str(p).replace('[','').replace(']','').replace(',','').replace('0','').split()]
    apagar.clear()
print(t)