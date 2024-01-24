x, y = map(int, input().split())
flag = 1
for i in range(1, y+1):
  if flag == x:
    print(i)
    flag = 1

  else:
    print(i, end=" ")
    flag += 1