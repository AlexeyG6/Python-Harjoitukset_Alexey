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
            print("\033[34mHuoneessa ei ole mitaan poimittavaa.\033[0m")

def lisaa_esine(esine): #Funktio lisää esineen "inventaario" listaan
    Pelaaja.inventaario.append(esine)
    print(f"\033[33m{esine} on lisätty inventaarioon.\033[0m")

def poista_esine(esine_nimi): #Funktio saa käyttäjän kirjoitettu esineen nimen parametriaan ja etsii sitä "inventaario"-listalta. Jos sellainen löytyy, niin sitä poistetaan
    for esine in Pelaaja.inventaario:
        if str(esine).lower() == esine_nimi.lower():
            Pelaaja.inventaario.remove(esine)
            print(f"\033[33mheitit {esine_nimi} pois\033[0m")
            return
    print(f"\033[31mEsinettä {esine_nimi} ei löytynyt inventaariosta.\033[0m")

def tallenna_peli(pelaaja):
    with open("save.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"{pelaaja.nimi}\n")
        tiedosto.write(f"{str(pelaaja.sijainti)}\n")  # Lisätty \n
        inventaario = ",".join([str(e) for e in Pelaaja.inventaario])
        tiedosto.write(f"{inventaario}\n")
    print("\033[32m\n-> Peli tallennettu onnistuneesti!\033[0m")

def lataa_peli(): #Ladataan pelaajan tidot save kansiosta
    if not os.path.exists("save.txt"):  #Jos tiedosto on tyhjä titoja ei lueta
        print("\033[31m\n-> Tallennustiedostoa ei löytynyt!\033[0m")
        return None, None, []

    with open("save.txt", "r", encoding="utf-8") as tiedosto:
        rivit = tiedosto.readlines()
        
        nimi = rivit[0].strip()
        sijainti = int(rivit[1].strip())
        
        # Luetaan inventaario jos kolmas rivi on olemassa
        inventaario = []
        if len(rivit) > 2 and rivit[2].strip():
            inventaario = rivit[2].strip().split(",")

        #PITÄÄ TEHDÄ!!!: poistetaan esine huoneesta jos se ladataan inventaario

        return nimi, sijainti, inventaario