fr,fa,o,r = int(input()),int(input()),int(input()),'manter'
if fa > fr*3 or o<95: r = 'diminuir'
if fa < fr*2 and o>97: r = 'aumentar'
print(r)
