n = int(input())
p = [int(i) for i in input().split()]
b = 0
remo = []
for i,c in enumerate(p):
    if c <= 8:
        remo.append(i)
for c in remo:
    p.pop(c)
p.reverse()
def main(b):
    if len(p) % 2 == 1:
        return 'N'
    for c in range(int(len(p)/2)):
        c = c+b
        if (p[c]-p[c+1]) > 8:
            return 'N'
        b+=1
    return 'S'

print(main(b))
