n = int(input())
pessoas = [int(i) for i in input().split()]
ns = int(input())
s = [int(i) for i in input().split()]
for i in s:
    pessoas.remove(i)
print(pessoas)