n, k = map(int, input().split())
lista = list(map(int, input().split()))
cont = 0
for i in lista:
    if i == k:
        cont += 1

if cont > n:
    print(n)

else:
    print(cont)