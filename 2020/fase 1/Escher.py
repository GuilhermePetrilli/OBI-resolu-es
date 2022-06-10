n,l = int(input()),[int(i) for i in input().split()]
f,r = l[0]+l[-1],'S'
for c1,c2 in zip(l,l[::-1]):
    if c1 + c2 != f:
        r = 'N' 
        break
print(r)