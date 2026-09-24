import os
class Pelaaja:

    huoneet = [] # Lista kaikista huoneista
    inventaario = [] #Luodaan tyhjä inventaario

    def __init__(self, nimi, huone = 0): #Luo pelaajan jolla on nimi, sijainti, sekä inventaario
        self.nimi = nimi
        self.sijainti = huone

    def liiku(self, kohde): # liikuttaa pelaajan sijaintia eteeenpäin saadun parametriaan kohti
        self.sijainti = kohde

    def keraa_esine(self): # etsii esineen huoneesta ja lisää kutsuu lisää_esine funktiota
        nykyinen_huone = self.huoneet[self.sijainti]

        if hasattr(nykyinen_huone, 'esine') and nykyinen_huone.esine:# Jos huoneessa on esine, poimitaan se
            esine = nykyinen_huone.esine
            lisaa_esine(esine)  # Kutsutaan lisaa_esine metodia
            nykyinen_huone.esine = None  # Poistetaan esine huoneesta
        else:
            print("Huoneessa ei ole mitaan poimittavaa.")

def lisaa_esine(esine): #Funktio lisää esineen "inventaario" listaan
    Pelaaja.inventaario.append(esine)
    print(f"{esine} on lisätty inventaarioon.")

def poista_esine(esine_nimi): #Funktio saa käyttäjän kirjoitettu esineen nimen parametriaan ja etsii sitä "inventaario"-listalta. Jos sellainen löytyy, niin sitä poistetaan
    for esine in Pelaaja.inventaario:
        if str(esine).lower() == esine_nimi.lower():
            Pelaaja.inventaario.remove(esine)
            print(f"heitit {esine_nimi} pois")
            return
    print(f"Esinettä {esine_nimi} ei löytynyt inventaariosta.")

def tallenna_peli(pelaaja):
    with open("save.txt", "w") as tiedosto:
        tiedosto.write(pelaaja.nimi)
        tiedosto.write(pelaaja.sijainti)
        inventaario = ",".join([str(e) for e in Pelaaja.inventaario])
        tiedosto.write(f"{inventaario}\n")

def lataa_peli(self, pelaaja): #Ladataan pelaajan tidot save kansiosta
    if not os.path.exists("tallennus.txt"):  #Jos tiedosto on tyhjä titoja ei lueta
        print("\n-> Tallennustiedostoa ei löytynyt!")
        return None, None

    with open("save.txt", "r", encoding="utf-8") as tiedosto:
        nimi = tiedosto.readline().strip()
        sijainti = int(tiedosto.readline().strip())
        inventaario = [tiedosto.readline().strip()]

        pelaaja.nimi = nimi
        pelaaja.sijainti = sijainti
        pelaaja.inventaario = inventaario
