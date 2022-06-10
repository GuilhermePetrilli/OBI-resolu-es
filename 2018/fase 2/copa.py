k = int(input())
l = int(input())

resposta = 'oitavas'

# FINAL -----------------------------------

if (k <= 8 and l >= 9):
    resposta = 'final'
if (l <= 8 and k >= 9):
    resposta = 'final'

# SEMIFINAL --------------------------------

if (l <= 4 and k <= 8 and  k >=5):
    resposta = 'semifinal'

if (k <= 4 and l <= 8 and l >=5):
    resposta = 'semifinal'

if (l >= 13 and k >= 9 and k <= 12):
    resposta = 'semifinal'

if (k >= 13 and l >= 9 and l <= 12):
    resposta = 'semifinal'

# QUARTAS ----------------------------------

if (k <=2 and l >= 3 and l<=4):
    resposta = 'quartas'

if (l <=2 and k >= 3 and k<=4):
    resposta = 'quartas'

if (l>=5 and l<=6 and k>=7 and k<=8):
    resposta = 'quartas'

if (k>=5 and k<=6 and l>=7 and l<=8):
    resposta = 'quartas'

if (k>=9 and k<=10 and l>=11 and l<=12):
    resposta = 'quartas'

if (l>=9 and l<=10 and k>=11 and k<=12):
    resposta = 'quartas'

if (k>=13 and k<=14 and l>=15 and l<=16):
    resposta = 'quartas'

if (l>=13 and l<=14 and k>=15 and k<=16):
    resposta = 'quartas'



print(resposta)