dividendo = 3
divisor = 2

soma = 1

while dividendo < 40:
  soma += dividendo/divisor
  dividendo += 2
  divisor = divisor*2

print("{:.2f}".format(soma))