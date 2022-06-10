r,o,m,res = int(input()),int(input()),int(input()),['*','*']
if r > o: res[1] = 'RO'
if r > m: res[0] = 'RM'
print(res[0]),print(res[1])
