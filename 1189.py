matriz = []
operacao = input()

for i in range(12):
  matriz.append([0]*12)

for linha in range(12):
  for coluna in range(12):
    matriz[linha][coluna] = (float(input()))


ci = 7
cf = 11

li = 5
lf = 6
soma = 0

for c in range(ci, cf+1):
  for l in range(li, lf+1):
    soma += matriz[l][c]
  li -= 1
  lf += 1

if operacao == "S":
  print("{:.1f}".format(soma))

elif operacao == "M":
  media = soma/30
  print("{:.1f}".format(media))
