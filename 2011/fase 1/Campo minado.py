n = int(input())
t = [int(input()) for i in range(n)]
s = []
def find(l,i):
    r=0
    r+=l[i]
    if i > 0:
        r+=l[i-1]
    if i < len(l)-1:
        r+=l[i+1]
    return r

for i,c in enumerate(t):
    print(find(t,i))
