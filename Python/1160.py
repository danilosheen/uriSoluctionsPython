n = int(input())
for i in range(n):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    anos = 0
    teste = pa

    while True:

        pa += int((g1/100)*pa)
        pb += int((g2/100)*pb)

        anos += 1

        if anos > 100:
            print("Mais de 1 seculo.")
            break

        elif pa > pb:
            print("{} anos.".format(anos))
            break


    


