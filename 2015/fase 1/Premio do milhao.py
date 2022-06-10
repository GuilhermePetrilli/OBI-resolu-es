n = int(input())
acessos = [int(input()) for c in range(n)]
t = 0
c = 0
while t < 10**6:
    c+=1
    t += acessos[c-1]
print(c)
