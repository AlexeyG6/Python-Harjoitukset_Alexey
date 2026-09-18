class Julkaisu:

    julkaisuudet = 0

    def __init__(self, nimi):
        self.julkaisuudet += 1
        self.julkaisun_numero = self.julkaisuudet
        self.nimi = nimi = nimi
        
    def tulosta_tiedot(self):
        print(self.nimi)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivut):
        self.sivumäärä = sivut
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.kirjoittaja, self.sivumäärä)

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.päätoimittaja)
        
julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o6", "Rosa Liksom", 200))

for j in julkaisut:
    j.tulosta_tiedot()