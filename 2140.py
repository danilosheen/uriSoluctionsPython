notas = [2, 5, 10, 20, 50, 100]
n, m = map(int, input().split())
while n != 0 and m != 0:
    flag = 5
    troco = m-n
    sum = 0
    if troco > 150:
        print("impossible")

    else:
        while True:
            
            if troco >= notas[flag]:
                troco -= notas[flag]
                flag -= 1
                sum += 1
        
            elif sum > 2:
                print("impossible")
                break

            else:
                flag -= 1
                if flag <= -1:
                    break

        if sum == 2:
            print("possible")

        elif sum < 2:
            print("impossible")
    

    n, m = map(int, input().split())
    