n = int(input())
nun1,op,nun2 = [i for i in input().split()]
nun1,nun2 = int(nun1),int(nun2)
res = 'OVERFLOW'
if op == '+':
    r = nun1+nun2
if op == '*':
    r = nun1*nun2
if r <= n:
    res = 'OK'
print(res)
