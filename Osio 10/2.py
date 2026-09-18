import random

class Hissi:

    def __init__(self, alin_kerros):
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, hissi, kerros):
        while True:
            if hissi.kerros == kerros:
                break
            num = random.randint(1,2)
            if num == 1:
                Talo.hissit[hissi].kerros_ylos()
            elif num == 2:
                Talo.hissit[hissi].kerros_alas()


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
        for hissi in range(self.hissien_maara):
            hissi = Hissi(self.alin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(hissi, kerros):
        if kerros <= Talo.hissit[hissi].ylin_kerros or kerros >= Talo.hissit[hissi].alin_kerros:
            Hissi.siirry_kerrokseen(hissi, kerros)
        
    
while True:
    ylin = int(input("Mikä on ylin kerros: "))
    alin = int(input("Mikä on alin kerros: "))
    if ylin > alin:
        break
    else:
        print("ylemmän kerroksen pitää olla alemman korkeamalla!")

h_maara = int(input("Mikä on hissien määrä: "))

talo = Talo(ylin, alin, h_maara)

while True:
    mika_hissi = int(input("Mitä hissiä haluat ajaa (Hissin numero 1 - ...): "))
    mika_hissi -= 1
    if 0 <= mika_hissi < len(talo.hissit) :
        while True:
            kerros = int(input("Hissi on alemmalla kerrosksella. Mihin kerrokseen haluat liikkua: "))
            if kerros >= alin and kerros <= ylin:
                break
            print("Kerros ei löytyny!")
        Talo.aja_hissia(mika_hissi, kerros)
    else:
        print("Hissiä ei löydetty")
