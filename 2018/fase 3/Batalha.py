at1,df1,at2,df2 = [int(input()) for i in range(4)]

def main():
    if at1 != df2 and at2 != df1: return -1
    if at1 != df2: return 1
    if at2 != df1: return 2
    return -1
print(main())