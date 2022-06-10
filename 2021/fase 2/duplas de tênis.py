a,b,c,d = [int(input()),int(input()),int(input()),int(input())]
pa = [abs((a+b) - (c+d)),abs((a+c) - (b+d)),abs((a+d) - (b+c))]
resposta = min(pa)
print(resposta)

# a,b,c,d = [int(input()),int(input()),int(input()),int(input())]
# print(min([abs((a+b) - (c+d)),abs((a+c) - (b+d)),abs((a+d) - (b+c))]))

