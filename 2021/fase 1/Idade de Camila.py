i1,i2,i3 = int(input()),int(input()),int(input())
r = i2

if i1 == i2:
    if i1<i3:
        r = i1
    if i1>i3:
        r = i3
if i2 == i3:
    if i2<i1:
        r = i2
    if i2>i1:
        r = i1
if i3 == i1:
    if i3<i2:
        r = i3
    if i3>i2:
        r = i2

if i1<i2 and i1>i3:
    r = i1

if i1>i2 and i1<i3:
    r = i1

if i2<i1 and i2>i3:
    r = i2

if i2>i1 and i2<i3:
    r = i2

if i3<i1 and i3>i2:
    r = i3

if i3>i1 and i3<i2:
    r = i3
print(r)