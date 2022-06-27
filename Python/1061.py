#tempo de um evento
di = int(input().split()[1])
hi, mi, si = map(int, input().split(":"))
df = int(input().split()[1])
hf, mf, sf = map(int, input().split(":"))

diaini = (di*24*60*60)+(hi*60*60)+(mi*60)+si
diafin = (df*24*60*60)+(hf*60*60)+(mf*60)+sf

dia = 0
hora = 0
min = 0
seg = 0

tempototal = (diafin - diaini)
while tempototal != 0:
    if tempototal >= 86400:
        tempototal -= 86400
        dia += 1
    elif tempototal >= 3600:
        tempototal -= 3600
        hora += 1

    elif tempototal >= 60:
        tempototal -= 60
        min += 1

    elif tempototal < 60:
        seg = tempototal
        break

print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(min))
print("{} segundo(s)".format(seg))
