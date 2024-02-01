import math

def calcularCaes(peso):
  return 10.1*(peso**0.666)/100

def calcularGatos(peso):
  return 10*(peso**0.666)/100

def menu():
  print("----------")
  print("Escolha uma opção")
  print("0 - Sair")
  print("1 - Cães")
  print("2 - Gatos")
  print("----------")

menu()

entrada = int(input())

while entrada != 0:
  if entrada == 0:
    break
  elif entrada == 1:
    peso = float(input("Informe o peso do cão: "))
    res = calcularCaes(peso)
    cortado = int(res * 100) / 100.0

    print(f'{cortado}')

  elif entrada == 2:
    peso = float(input("Informe o peso do gato: "))    
    print(f'{calcularGatos(peso):.3f}')

  else:
    print("Valor digitado incorreto, tente outro")

  menu()
