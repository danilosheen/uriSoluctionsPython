import math
n = int(input())
for i in range(n):
    c, d = map(int, input().split())
    if c != 0 and d != 0:
        qtd = int((math.pow(26, c))*(math.pow(10, d)))
        print(qtd)

    elif c == 0 and d != 0:
        qtd = int(math.pow(10, d))
        print(qtd)

    elif d == 0 and c != 0:
        qtd = int(math.pow(26, c))
        print(qtd)

    else:
        print(0)