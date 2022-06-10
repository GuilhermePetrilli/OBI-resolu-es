n = int(input())
l = [input().split() for i in range(n)]
r = 1
for c in l:
    if c[1] == '/':
        r/=int(c[0])
    if c[1] == '*':
        r*=int(c[0])
print(int(r))
    