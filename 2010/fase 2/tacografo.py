n = int(input())
l = [input().split() for i in range(n)]
r =[]
for c in l:
    r.append(int(c[0])*int(c[1]))
print(sum(r))