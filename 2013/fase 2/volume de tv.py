vi,n = [int(i) for i in input().split()]
nuns = [int(i) for i in input().split()]
for i in nuns:
    vi+=i
    if vi>100: vi = 100
    if vi<0: vi = 0
print(vi)