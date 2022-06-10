d = int(input())
x,y,z = [int(i) for i in input().split()]
r = 'N'
if d<=x and d<=y and d<=z:
    r = 'S' 
print(r)