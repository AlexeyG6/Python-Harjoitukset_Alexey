import random

hissit = []

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

class Talo:

    def __init__(self, ylin, alin, hissi_maara):
        self.ylin_kerros = ylin
        self.alin_kerros = alin
        self.hissien_maara = hissi_maara
        num_int = 1
        for hissi in range(self.hissien_maara):
            num = str(num_int)
            hissit.append(Hissi(num))

    def aja_hissia():
        loppu_kerros = int(input("Mihin kerrokseen hissi siirtyy: "))
    hissi.siirry_kerrokseen(loppu_kerros)

