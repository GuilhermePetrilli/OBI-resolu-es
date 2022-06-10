n,max = [int(i) for i in input().split()]
dis = [int(i) for i in input().split()]



def main():
    for c,p in enumerate(dis):
        if c==0:
            pp = p
        elif c!=0:
            if (p - pp) > max:
                return 'N'
        pp = p
    return 'S'

print(main())