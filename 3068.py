teste = 0
while True:
  meteoro = 0 
  x1, y1, x2, y2 = map(int, input().split())
  if (x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0):
    break

  else:
    teste += 1
    n = int(input())
    for i in range(n):
      x, y = map(int, input().split())
      if(x >= x1 and y <= y1 and x <= x2 and y >= y2):
        meteoro += 1

    print(f"Teste {teste}")
    print(f"{meteoro}")