pi = int(input())
n = [int(input()) for i in range(2)]
if pi == 0:
    if (n[0]+n[1]) % 2 == 0:
        r = 0
    else:
        r = 1
if pi == 1:
    if n[0]+n[1] % 2 == 0:
        r = 1
    else:
        r = 0
print(r)