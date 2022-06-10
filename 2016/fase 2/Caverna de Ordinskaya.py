h,p,f,s = [int(i) for i in input().split()]
def main(f):
    while True:
        if f == p:
            return 'N'
        if f == h:
            return 'S'
        f+=s
        if f == 16:
            f=0
        if f == -1:
            f == 15 
        
print(main(f))