n = 0
x = 1
while True:
    
    n = int(input())
    if(n == -1):
        break
    else:
        y = 0
        for i in range(n , 0, -1):
            if  i%2 == 0:
             y+=1

        print("Experiment {}: {} full cycle(s)".format(x, y))
        x += 1
