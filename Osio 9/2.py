
class Auto:
    def __init__(self, rekkari, nopeus):
        self.rekkari = rekkari
        self.huippu_nopeus = nopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, maara):
        self.nopeus += maara
        if self.nopeus > self.huippu_nopeus:
            self.nopeus = self.huippu_nopeus
        elif self.nopeus < 0:
            self.nopeus = 0


auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(50)
auto.kiihdyta(70)

print(f"Auton rekisterinumero: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus}km/h, Matka: {auto.matka}km")