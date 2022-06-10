nuns = [int(input()) for i in range(3)]
nuns2 = nuns.copy()
n1 = min(nuns)
n3 = max(nuns)
nuns.remove(n1)
nuns.remove(n3)
n2 = nuns[0]
pos = [n1,n2,n3]
for c in pos:
    print(nuns2.index(c)+1)