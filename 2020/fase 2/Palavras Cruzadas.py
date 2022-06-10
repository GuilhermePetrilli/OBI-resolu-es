p1,p2 = list(input()),list(input())
def main():
    c = 0
    for x in p1:
        if x in p2: c+=1
    if c == 0: return '-1 -1'
    for i1,l1 in enumerate(p1[::-1]):
        for i2,l2 in enumerate(p2[::-1]):
            print(l1,l2)
            if l1 == l2:
                return f'{len(p1)-i1} {len(p2)-i2}'
print(main())