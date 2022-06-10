c,n = [int(i) for i in input().split()]
tempos = [sum([int(i) for i in input().split()]) for i in range(c)]
for i,c in enumerate(tempos):
    if i == 0:
        min = [c,i+1]
    if c<min[0]:
        min[0] = c
        min[1] = i+1
print(min[1])
