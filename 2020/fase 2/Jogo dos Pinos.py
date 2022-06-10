t = [list(input()) for c in range(7)]
c=0
for rows,l in enumerate(t):
    for i,ca in enumerate(l):
        if ca == 'o':
            try:
                if l[i-1] == 'o' and l[i-2] == '.':
                    c+=1
            except IndexError:
                pass
            try:
                if l[i+1] == 'o' and l[i+2] == '.':
                    c+=1
            except IndexError:
                pass
            try:
                if t[rows+1][i] == 'o' and t[rows+2][i] == '.':
                    c+=1
            except IndexError:
                pass
        
            try:
                if t[rows-1][i] == 'o' and t[rows-2][i] == '.':
                    c+=1
            except IndexError:
                pass
print(c)
