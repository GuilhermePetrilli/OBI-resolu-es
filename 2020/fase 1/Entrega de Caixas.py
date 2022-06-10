a,b,c = int(input()),int(input()),int(input())
v = 3

if a<b or a<c:
    v = 2

if a<b and b<c:
    v=1
if a+b<c:
    v=1
print(v)