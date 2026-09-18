class Auto:
    def __init__(self, rekkari, nopeus):
        self.rekkari = rekkari
        self.huippu_nopeus = nopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)


print(f"Auton rekisterinumero: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus}km/h, Matka: {auto.matka}km")