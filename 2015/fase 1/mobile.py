A,B,C,D = [int(input()) for i in range(4)]
r = 'N'

if A == B + C + D and B + C == D and B == C: r = 'S'

print(r)