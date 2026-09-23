
class Pelaaja:
    def __init__(self, nimi, lista, huone = 0, huoneet):
        self.nimi = nimi
        self.sijainti = huone
        self.inventaario = lista
        self.huoneet = huoneet

    def liiku(self, kohde):
        self.sijainti = kohde

    def keraa_esine(self):
        esine = huoneet[self.sijainti]
        lisää_esine(esine)

class Huone:
    def __init__(self, nimi, esine = ""):
        self.nimi = nimi
        self.esine = esine

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

def nayta_nimi(): #Funktio, joka printtaa pelaajan nimen
    print("\nPelaajan nimi on:", nimi)
def nayta_ikä(): #Funktio, joka printtaa pelaajan iän
    print("\nPelaajan ikä on:", ikä)

def lisää_esine(esine): #Funktio lisää esineen "inventaario" listaan
    Pelaaja.inventaario.append(esine)
    print(f"{esine} on lisätty inventaarioon.")

def poista_esine(esine): #Funktio saa käyttäjän kirjoitettu esineen nimen parametriaan ja etsii sitä "inventaario"-listalta. Jos sellainen löytyy, niin sitä poistetaan
    if esine in inventaario:
        Pelaaja.inventaario.remove(esine)
        print(f"heitit {esine} pois")

def Peli(): #Funktio kirjoittaa toiminnot, joista käyttäjä valitsee mitä tehdään

    kohde = 0
    huoneet = []
    huoneet.append(Huone("metsä","miekka"))
    huoneet.append("Linnan etuovi")
    huoneet.append("Linna")
    Pelaaja(nimi, inventaario, huoneet)
    while True: 
        print(f"Paikka: {huoneet[Pelaaja.huone]}")
        Toiminto = input("Toiminnot: \n1. Mene eteepäin \n2.Etsi esinettä \n3. Tarkista inventaario \n4. Heitä esine pois \n5. Lopeta \nValitse toiminto: ")

        if Toiminto == "1":
            kohde += 1
            Pelaaja.liiku(kohde, huoneet)
        elif Toiminto == "2":
            Pelaaja.keraa_esine()
        elif Toiminto == "3":Pelaaja.inventaario
        elif Toiminto == "4":
            esine = input("Minkä esineen haluat heittää pois?:")
            poista_esine(esine)
        elif Toiminto == "5":
            exit()

inventaario = [] #Luodaan tyhjä inventaario

print("OVERDRIVE") #Printataan Pelin nimi
nimi = input("Anna pelaajan nimi: ") #Kysytään pelaajan nimeä
ikä = int(input("Anna pelaajan ikä: ")) #Kysytään pelaajan ikää ja muutetaan se kokonaisluvuksi
print ("\n" + nimi + ", " + str(ikä)) #Kirjataan Pelaajan nimi ja ikä

if ikä < 12: #Jos pelaajan ikä on alle 12, niin peli sulkee ohjelman ja ilmoittaa että pelaaja on liian nuori
    print("Pelaaja on liian nuori.")
    exit()

while True: #Ohjelma kirjoittaa pelin toiminnot ja kysyy pelaajalta mitä hän haluaa tehdä. Pelaaja voi valita Aloittaa tai lopettaa pelin, tarkistaa nimensä tai ikänsä.
    print("---------------------- \nOVERDRIVE")
    vastaus = input("\nTervetuloa peliin! \nToiminnot: \nAloita peli(Aloita) \nMinun nimi(nimi) \nMinun Ikä(ika) \n(Lopeta) \nValitse toiminto: ")

    if vastaus == "Lopeta": #Peli loppuu
        exit()
    elif vastaus == "nimi": #Kirjataan nimi
        nayta_nimi()
    elif vastaus == "ika": #Kirjataan ikä
        nayta_ikä()
    elif vastaus == "Aloita": #Peli alkaa
        print("\nPeli alkaa!")
        break


Peli() #Kutsutaan Peli funktiota