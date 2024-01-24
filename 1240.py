n = int(input())
for i in range(n):
    x, y = input().split()
    teste = 0
    cont = 0
    if len(x) < len(y):
        print("nao encaixa")

    else:
        for j in range(len(y)):
            teste -= 1
            if x[teste] == y[teste]:
                cont += 1

        if cont == len(y):
            print("encaixa")

        else:
            print("nao encaixa")
