
class Auto:
    def __init__(self):
        self.rekkari = "ABC-123"
        self.huippu_nopeus = 142
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, maara):
        self.nopeus += maara
        if self.nopeus > self.huippu_nopeus:
            self.nopeus = self.huippu_nopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika

auto = Auto()

auto.kiihdyta(30)
auto.kiihdyta(50)
auto.kiihdyta(70)

auto.kulje(1.5)

print(f"Auton rekisterinumero: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus}km/h, Matka: {auto.matka}km")