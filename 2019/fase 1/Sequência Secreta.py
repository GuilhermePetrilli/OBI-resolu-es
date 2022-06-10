n = int(input())
s = [int(input()) for i in range(n)]
c1,r=0,0
for c in s:
    if c != c1:
        r+=1
    c1 = c
print(r)