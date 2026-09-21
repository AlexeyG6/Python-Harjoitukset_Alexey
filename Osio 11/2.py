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
        print(f"\n{'Rekisteri':<10} | {'Huippunopeus':<13} | {'Nykyinen nopeus':<16} | {'Matka':<10}")
        print("-" * 58)
        for auto in self.auto_lista:
            print(f"{auto.rekkari:<10} | {auto.huippu_nopeus:<3} km/h       | {auto.nopeus:<3} km/h          | {auto.matka:<6.1f} km")

    def kilpailu_ohi(self):
        if any(auto.matka >= self.pituus_km for auto in self.auto_lista):
            return True
        else:
            return False
    

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


class Sähköauto(Auto):

    def __init__(self, akku_kw_h, rekkari, huippunopeus):
        self.akkukapasiteetti = akku_kw_h
        super().__init__(rekkari, huippunopeus)


class Polttomoottoriauto(Auto):

    def __init__(self, bensatankki_L, rekkari, huippunopeus):
        self.bansatankinkoko = bensatankki_L
        super().__init__(rekkari, huippunopeus)

autot = []

autot.append(Sähköauto(52.5, "ABC-15", 180))
autot.append(Polttomoottoriauto(32.2, "ACD-123", 165))

K = Kilpailu(autot, "Bensa vs Sähkö", 10000) #matka ei tee mitään, en ole vaan poistanu sitä viime tehtävän jälkeen
autot[0].kiihdyta(80)
autot[1].kiihdyta(100)
autot[0].kulje(3)
autot[1].kulje(3)
K.tulosta_tilanne()

