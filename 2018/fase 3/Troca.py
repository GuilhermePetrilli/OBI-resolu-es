n,nt= [int(i) for i in input().split()]
l1,l2 = [[int(i) for i in input().split()],[int(i) for i in input().split()]]
tt = [[int(i) for i in input().split()] for i in range(nt)]
for t in tt:
    for c in range(t[0]-1,t[1]):
        l1[c],l2[c] = l2[c],l1[c]
        
print(str(l1).replace(',',' ').replace('[','').replace(']',''))