# -*- coding: utf-8 -*-

entrada = []
try:
    while True:
        linha = input().split()
        entrada.extend(linha)
except EOFError:
    cont = 0
    linha = []
    for i in entrada:
        if i in ("<br>", "<hr>"):
            if i == "<br>":
                if len(linha): print(" ".join(linha))
                else: print()
            else:
                if len(linha): print(" ".join(linha))
                print("-" * 80)
            linha = []
            cont = 0
        else:
            lenI = len(i)
            if cont + lenI < 81:
                cont += lenI + 1
                linha.append(i)
            else:
                print(" ".join(linha))
                linha = [i]
                cont = lenI + 1

    if len(linha): print(" ".join(linha))
    