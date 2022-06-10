n = int(input())
if n == 0: print('*'); print('*')
else:
    for c in range(n):
        e = ''
        if c == 4: e='\n'
        print('I',end=e)