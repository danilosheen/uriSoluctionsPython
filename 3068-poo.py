class MeteorsCounter:
    def __init__(self):
        self.teste = 0

    def run(self):
        while True:
            meteoro = 0
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
                break
            else:
                self.teste += 1
                n = int(input())
                for i in range(n):
                    x, y = map(int, input().split())
                    if x1 <= x <= x2 and y1 >= y >= y2:
                        meteoro += 1

                print(f"Teste {self.teste}")
                print(f"{meteoro}")


if __name__ == "__main__":
    meteor_counter = MeteorsCounter()
    meteor_counter.run()
