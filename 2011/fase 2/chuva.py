n = int(input())
listas = [input().split() for c in range(n*2)]
r =[]
for i in range(int(len(listas)/2)):
    f = []
    for i2,c2 in enumerate(listas[i]):
        f.append(int(c2)+int(listas[i+n][i2]))
        if len(f) == 3:
            r.append(f)
for c in r:
    print(str(c).replace(',','').replace('[','').replace(']',''))