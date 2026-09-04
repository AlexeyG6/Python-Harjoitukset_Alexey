import random


class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippu_nopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, maara):
        self.nopeus += maara
        if self.nopeus > self.huippu_nopeus:
            self.nopeus = self.huippu_nopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        return maara

    def kulje(self, aika):
        self.matka += self.nopeus * aika

auto1 = Auto("ABC-1", random.randint(100,200))
auto2 = Auto("ABC-2", random.randint(100,200))
auto3 = Auto("ABC-3", random.randint(100,200))
auto4 = Auto("ABC-4", random.randint(100,200))
auto5 = Auto("ABC-5", random.randint(100,200))
auto6 = Auto("ABC-6", random.randint(100,200))
auto7 = Auto("ABC-7", random.randint(100,200))
auto8 = Auto("ABC-8", random.randint(100,200))
auto9 = Auto("ABC-9", random.randint(100,200))
auto10 = Auto("ABC-10", random.randint(100,200))

autot = [auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10]

for auto in autot:
        print(f"Rekkari: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus}km/h, Matka: {auto.matka}km")
print("--------------------------------")

while True:
    for auto in autot:
        maara = auto.kiihdyta(random.randint(-10, 15))
        print(f"Rekkari: {auto.rekkari}, Muutos: {maara}km/h")
        auto.kulje(1)
    print("--------------------------------")
    if any(auto.matka >= 10000 for auto in autot):
        break

print("Tulos:")
for auto in autot:
        print(f"Rekkari: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus}km/h, Matka: {auto.matka}km")

print("Voittaja:")
for auto in autot:
     if auto.matka >= 10000:
          print(auto.rekkari, auto.nopeus ,auto.matka)