r,n = int(input()),int(input())
figs = list(set([int(input()) for i in range(n)]))
print(r-len(figs))