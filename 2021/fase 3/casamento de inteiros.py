n1,n2 = [[int(i) for i in input()],[int(i) for i in input()]]
f1,f2 = str()
while len(n1)!=len(n2):
    if len(n1)<len(n2): n1.insert(0,0)
    if len(n2)<len(n1): n2.insert(0,0)
for c1,c2 in list(zip(n1,n2)):
    if c1<c2: f2+=str(c2)
    if c2<c1: f1+=str(c1)
    if c2 == c1: f1+=str(c1);f2+=str(c2)
if len(f1) == 0: f1 = -1
if len(f2) == 0: f2 = -1
print(f2,f1)