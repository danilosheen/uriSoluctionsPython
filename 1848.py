while True:
    try:
        val = ['---', '--*', '-*-', '-**', '*--', '*-*', '**-', '***']
        n = input()
        sum = 0
        while True:
            if n == 'caw caw':
                print(sum)
                sum = 0
            else:
                for i in range(len(val)):
                    if n == val[i]:
                        sum += i
            n = input()
    except EOFError:
        break