a,s,d = int(input()),int(input()),int(input())
c,m = 0,0
while True:
    c+=1
    m+=s
    if m >= a:
        break
    m-=d
print(c)