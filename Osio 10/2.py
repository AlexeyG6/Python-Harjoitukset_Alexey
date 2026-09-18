
class Hissi:

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = self.alin

    def siirry_kerrokseen(self, kerros):
        while self.kerros == kerros:
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

h = Hissi(0, 5)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)