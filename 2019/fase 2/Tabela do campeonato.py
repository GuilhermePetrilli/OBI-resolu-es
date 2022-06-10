j,p,v,e,d = [int(i) for i in input().split()]

if d == -1: d = j-v-e
if e == -1: e = p-v*3
if v == -1: v = p-e
if j == -1: j = v+e+d
if p == -1: p = 3*v+e

print(j,p,v,e,d)