import math
b,d,q = [int(i) for i in input().split()]

bits = 2**b



def main():
    gcd = math.gcd(d,q)
    if (d/gcd < bits or q/gcd < bits):
        return f'{int(d/gcd)} {int(q/gcd)}'
    return 'IMPOSSIVEL'

print(main())