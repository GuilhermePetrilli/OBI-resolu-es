j,r = [[input() for i in range(6)],0]
if 'V' not in j: r = -1
for i in j: 
    if i == 'V': r+=1
if r == 1 or r == 2: r = 3
if r == 3 or r == 4: r = 2
if r == 5 or r == 6: r = 1
print(r)