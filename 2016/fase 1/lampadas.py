n = int(input())
sequence = [int(i) for i in input().split()]
a,b = 0,0
for p in sequence:
    if p == 1:
        a = not a
    if p == 2:
        a = not a
        b = not b
print(int(a))
print(int(b))
