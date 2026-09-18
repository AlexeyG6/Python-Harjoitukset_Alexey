
class Hissi:

    def __init__(self):
        self.kerros = self.alin

    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerros_ylos()
            elif self.kerros > kerros:
                self.kerros_alas()


    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

class Talo:

    hissien_lukumaara = 0

    def __init__(self, alin, ylin, hissit):
        self.hissit = []
        self.alin = alin
        self.ylin = ylin
        self.hissien_lukumaara = hissit
        for hissi in self.hissien_lukumaara:
            self.hissit.append(hissi = Hissi())

    def aja_hissiä(self, hissi, kerros):
        hissi.siirry_kerrokseen(kerros)

T = Talo(0, 5, 2)

T.aja_hissiä(1, 5)
T.aja_hissiä(0, 4)