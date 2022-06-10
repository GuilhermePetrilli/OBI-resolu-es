n = int(input())
ns = [input() for i in range(n)]
print(sum([int(i[:-1])**int(i[len(i)-1]) for i in ns]))
