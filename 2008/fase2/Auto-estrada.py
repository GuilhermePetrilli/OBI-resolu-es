inutil,c = int(input()),input()

resposta = sum(map(lambda x:int(x),list(c.replace('P','2').replace('C','2').replace('A','1').replace('D','0'))))

# for p in c:
#     if p == 'P':
#         resposta+=2
#     if p == 'C':
#         resposta+=2
#     if p == 'A':
#         resposta+=1

print(resposta)