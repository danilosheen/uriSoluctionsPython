c = int(input())
for i in range(c):
    m = []
    frase = input()
    saida = ''.join(s for s in frase if s.islower())
    saida = saida[::-1]
    print(saida)
