n = int(input())
nuns = [[int(i) for i in input().split()] for i in range(n)]
r = 0
for c in nuns:
    if c[0]>c[1]:
        r+=c[1]
print(r)