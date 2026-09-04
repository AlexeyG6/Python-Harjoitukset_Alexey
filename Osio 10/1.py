import random

class Hissi:

    def __init__(self):
        self.kerros = 0

    def siirry_kerrokseen(self, kerros):
        while True:
            if self.kerros == kerros:
                break
            num = random.randint(1,2)
            if num == 1:
                hissi.kerros_ylos()
            elif num == 2:
                hissi.kerros_alas()


    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {hissi.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {hissi.kerros}")

hissi = Hissi()

loppu_kerros = int(input("Mihin kerrokseen hissi siirtyy: "))
hissi.siirry_kerrokseen(loppu_kerros)


