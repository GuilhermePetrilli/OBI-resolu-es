n1,n2 = [[int(input()),int(input())],[int(input()),int(input())]]
if n1[0]*n1[1] > n2[0]*n2[1]: r = n1[0]*n1[1]
if n2[0]*n2[1] > n1[0]*n1[1]: r = n2[0]*n2[1]
print(r)