import math
while True:
    l = list(map(float, input().split()))
    if l[0] == 0:
        break
    else:
        casa = 0
        casa = int(l[0]) * int(l[1])
        porcentagem = int(l[2])
        terreno = int(math.sqrt((casa*100)/porcentagem))
        print("{:.0f}".format(terreno))
