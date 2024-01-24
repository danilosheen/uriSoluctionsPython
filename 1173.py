vetor = [0,1,2,3,4,5,6,7,8,9]
valor = int(input())

dobro = 0
for i in range (len(vetor)):
    vetor[i] = valor
    valor = valor*2
    print("N[{}] = {}".format(i, vetor[i]))