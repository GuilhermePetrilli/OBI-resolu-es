n,m = [int(input()),[int(i) for i in input().split()]]
def main():
    for i,c in enumerate(m):
        if i <= len(m)-2 and i > 0:
            if c < m[i-1] and c < m[i+1]:
                return 'S'
    return 'N'
print(main())