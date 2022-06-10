d = int(input())
r,c = [(int(i)-1) for i in input().split()]
r2,c2 = r,c
r3,c3 = r,c
tabela = [list(map(lambda x: int(x),input().split())) for i in range(d)]
visited = [[r2,c2]]
count=-1
count2 = 0
def path_find(r,c):
    global count
    global count2
    
    try:
        if tabela[r+1][c] >=  tabela[r][c] and [r+1,c] not in visited:
            visited.append([r+1,c])
            count2 = -1
            return (r+1,c)
    except IndexError:
        pass

    try:
        if tabela[r][c+1] >=  tabela[r][c] and [r,c+1] not in visited:
            visited.append([r,c+1])
            count2 = -1
            return (r,c+1)
    except IndexError:
        pass
    try:
        if tabela[r][c-1] >=  tabela[r][c] and c-1 >= 0 and [r,c-1] not in visited:
            visited.append([r,c-1])
            count2 = -1
            return (r,c-1)
    except IndexError:
        pass
    try:
        if tabela[r-1][c] >=  tabela[r][c] and r-1 >= 0 and [r-1,c] not in visited:
            visited.append([r-1,c])
            count2 = -1
            return (r-1,c)
    except IndexError:
        pass
    
    count2-=1
    try:
        f = visited[count2]
    except IndexError:
        return (-1*d**2,-1*d**2)
    return f
    
while True:  
    count+=1
    r,c = path_find(r3,c3,)
    if r == -1*d**2 and c == -1*d**2:
        break
    r3,c3 = r,c
    
print(len(visited))
