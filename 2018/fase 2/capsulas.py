from time import sleep
n,m = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
r=0
count =0
while True:
    count+=1
    for i in c:
        if (count % i) == 0:
            r+=1
    if r >= m:
        break
print(count)
