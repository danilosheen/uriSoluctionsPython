matriz = []
operacao = input()

for i in range(12):
  matriz.append([0]*12)

for linha in range(12):
  for coluna in range(12):
    matriz[linha][coluna] = (float(input()))


ci = 1
cf = 11

li = 11
lf = 1
soma = 0

for l in range(li, lf-1, -1):
  for c in range(ci, cf+1):
    soma += matriz[l][c]
  ci += 1

if operacao == "S":
  print("{:.1f}".format(soma))

elif operacao == "M":
  media = soma/66
  print("{:.1f}".format(media))
