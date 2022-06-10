nome = input()
letras = [['A', 'B', 'C'],[ 'D', 'E', 'F'],['G', 'H', 'I'],[ 'J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
resposta = ''
for c in nome:
    if c == '-':
        resposta+=c
    if c in letras[0]:
        resposta+='2'
    if c in letras[1]:
        resposta+='3'
    if c in letras[2]:
        resposta+='4'
    if c in letras[3]:
        resposta+='5'
    if c in letras[4]:
        resposta+='6'
    if c in letras[5]:
        resposta+='7'
    if c in letras[6]:
        resposta+='8'
    if c in letras[7]:
        resposta+='9'

print(resposta)