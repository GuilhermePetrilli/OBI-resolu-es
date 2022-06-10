a,b,c = [int(input()) for i in range(3)]
if a == b: r = c
if a == c: r = b
if b == c: r = a
print(r)