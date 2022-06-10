n = int(input())
l1 = str(input())
l2 = str(input())

l = zip(l1,l2)
p = 0

for a,b in l:
    if a == b:
        p+=1

print(p)