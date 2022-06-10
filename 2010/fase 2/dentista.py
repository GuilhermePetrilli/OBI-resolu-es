n = int(input())
times = [input().split() for i in range(n)]
r = 0
count=0
for c in times:
    if count == 0:
        last = int(c[0])
        count=1
    if int(c[0]) >=last:
        r+=1
        last = int(c[1])
print(r)