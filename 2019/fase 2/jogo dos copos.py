n,r = int(input()), input()
trocas = [int(input()) for i in range(n)]
if r == 'A': r = 1
if r == 'B': r = 2
if r == 'C': r = 3

def um(r):
    if r == 1:
        return 2
    if r == 2:
        return 1
    return 3
def dois(r):
    if r == 2:
        return 3
    if r == 3:
        return 2
    return 1

def tres(r):
    if r == 3:
        return 1
    if r == 1:
        return 3
    return 2
for c in trocas:
    if r == None: break
    if c == 1:
        r = um(r)
    if c == 2:
        r = dois(r)
    if c == 3:
        r = tres(r)
    
if r == 1: r = 'A'
if r == 2: r = 'B'
if r == 3: r = 'C'
    
print(r)
