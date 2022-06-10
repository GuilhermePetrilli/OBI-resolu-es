l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
r=-1
nomes = ['azar','azar',"terno", "quadra", "quina","sena"]
for i in l1:
    if i in l2:
        r+=1
print(nomes[abs(r)])