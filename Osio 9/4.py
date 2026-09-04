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

autot = []
num_int = 1
for i in range (10): 
     num = str(num_int)
     autot.append(Auto("ABC-" + num, random.randint(100, 200)))
     num_int += 1


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
          print(f"{auto.rekkari}, {auto.nopeus}km/h, {auto.matka}km")