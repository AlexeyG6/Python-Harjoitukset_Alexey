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
                self.kerros_ylos()
            elif num == 2:
                self.kerros_alas()


    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

class Talo:

    def __init__(self, ylin, alin, hissi_maara):
        self.hissit = []
        self.ylin_kerros = ylin
        self.alin_kerros = alin
        self.hissien_maara = hissi_maara
        num_int = 1
        for hissi in range(self.hissien_maara):
            num = str(num_int)
            self.hissit.append(Hissi(num))

    def aja_hissia(self, hissi, kerros):
        if kerros <= self.ylin_kerros or kerros >= self.alin_kerros:
            hissi.siirry_kerrokseen(kerros)
        
    

ylin = int(input("Mikä on ylin kerros: "))
alin = int(input("Mikä on alin kerros: "))
h_maara = int(input("Mikä on hissien määrä: "))

talo = Talo(ylin, alin, h_maara)

while True:
    mika_hissi = input("Mitä hissiä haluat ajaa (Hissin numero): ")
    if mika_hissi in talo.hissit:
        talo.aja_hissia(mika_hissi)
    else:
        print("Hissiä ei löydetty")
