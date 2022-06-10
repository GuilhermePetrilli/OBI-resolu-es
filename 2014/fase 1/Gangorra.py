P1, C1, P2 , C2 = [int(i) for i in input().split()]
if P1 * C1 == P2 * C2: r = 0
if P1 * C1 > P2 * C2: r = -1
if P1 * C1 < P2 * C2: r = 1
print(r)