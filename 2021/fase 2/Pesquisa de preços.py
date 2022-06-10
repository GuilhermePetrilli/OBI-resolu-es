n = int(input())
s = [input().split() for i in range(n)]
r = []
for c in s:
    if float(c[1]) <= float(c[2])*0.70:
        r.append(c[0])
if len(r) != 0: 
    for c in r: print(c)
else: print("*")