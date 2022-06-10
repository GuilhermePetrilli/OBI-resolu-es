c1,c2,c3,j1,j2 = [int(input()) for i in range(5)]
def main():
    if c1 <= j1 and c2 <= j2: return 'S'
    if c2 <= j1 and c1 <= j2: return 'S'
    if c3 <= j1 and c2 <= j2: return 'S'
    if c2 <= j1 and c3 <= j2: return 'S'
    if c1 <= j1 and c3 <= j2: return 'S'
    if c3 <= j1 and c1 <= j2: return 'S'
    return 'N'
print(main())