p,m = [int(i) for i in input().split()]
mp = []
for c in range(p):
    mp.append((sum([int(i) for i in input().split()]),c+1))
mp.sort(reverse=True)
for c in mp:
    print(c[1],end='')
    print(' ',end='')