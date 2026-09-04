class Auto:
    def __init__(self):
        self.rekkari = "ABC-123"
        self.huippu_nopeus = 142
        self.nopeus = 0
        self.matka = 0

auto = Auto()


print(f"Auton rekisterinumero: {auto.rekkari}, Huippunopeus: {auto.huippu_nopeus}km/h, Nykyinen nopeus: {auto.nopeus_nyt}km/h, Matka: {auto.matka}km")