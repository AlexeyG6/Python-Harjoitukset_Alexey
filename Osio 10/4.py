import random

class Kilpailu():

    def __init__(self, autot, nimi, pituus):
        self.kilpailun_nimi = nimi
        self.pituus_km = pituus
        self.auto_lista = autot 

    def tunti_kuluu(self):
        for auto in self.auto_lista:
            maara = auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.auto_lista:
            print(f"Rekkari: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus}km/h, Matka: {auto.matka}km")

    def kilpailu_ohi(self):
        if any(auto.matka >= self.pituus_km for auto in self.auto_lista):
            return("True")
        else:
            return("False")
    

class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus = 0, matka = 0):
        self.rekkari = rekkari
        self.huippu_nopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

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

K = Kilpailu(autot, "Suuri romuralli", 8000)
i = 0
while True:
    K.tunti_kuluu()
    if K.kilpailu_ohi() == "True":
        break
    elif i % 10 == 0:
        K.tulosta_tilanne()
        print("-----------------------------------")
    i += 1

K.tulosta_tilanne