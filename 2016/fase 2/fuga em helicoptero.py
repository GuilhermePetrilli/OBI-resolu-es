h,p,f,s = [int(i) for i in input().split()]
def find(h,f,p,s):
    while True:
        f+=s
        if f == -1:
            f = 15
        if f == 16:
            f = 0
        if f == p:
            return 'N'
        if f == h:
            return 'S'
print(find(h,f,p,s))