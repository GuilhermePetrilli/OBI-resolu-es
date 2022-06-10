n,s = [int(i) for i in input().split()]
ns = [int(input()) for c in range(n)]
min = s
for i,c in enumerate(ns):
    s+=c
    if s < min: 
        min = s
print(min)
