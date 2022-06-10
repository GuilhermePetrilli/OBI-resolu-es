mi,ma,alt,x = [int(input()) for i in range(4)]
if abs(mi - ma) <= x: r = ma
if abs(mi - ma) > x: r = alt
print(r)
