from .Peli import Peli
from .Pelaaja import lataa_peli

def nayta_nimi(nimi): #Funktio, joka printtaa pelaajan nimen
    print("\nPelaajan nimi on:", nimi)

def nayta_ikä(ikä): #Funktio, joka printtaa pelaajan iän
    print("\nPelaajan ikä on:", ikä)

def Kaynnista():
    print("OVERDRIVE") #Printataan Pelin nimi
    nimi = input("Anna pelaajan nimi: ") #Kysytään pelaajan nimeä
    ikä = int(input("Anna pelaajan ikä: ")) #Kysytään pelaajan ikää ja muutetaan se kokonaisluvuksi
    print ("\n" + nimi + ", " + str(ikä)) #Kirjataan Pelaajan nimi ja ikä

    if ikä < 12: #Jos pelaajan ikä on alle 12, niin peli sulkee ohjelman ja ilmoittaa että pelaaja on liian nuori
        print("Pelaaja on liian nuori.")
        exit()

    while True: #Ohjelma kirjoittaa pelin toiminnot ja kysyy pelaajalta mitä hän haluaa tehdä. Pelaaja voi valita Aloittaa tai lopettaa pelin, tarkistaa nimensä tai ikänsä.
        print('---------------------- \n\033[31mOVERDRIVE\033[0m')
        vastaus = input("\nTervetuloa peliin! \nToiminnot: \nAloita peli(Aloita) \nMinun nimi(nimi) \nMinun Ikä(ika) \n(Lopeta) \nValitse toiminto: ")

        if vastaus == "Lopeta": #Peli loppuu
            exit()
        elif vastaus == "nimi": #Kirjataan nimi
            nayta_nimi(nimi)
        elif vastaus == "ika": #Kirjataan ikä
            nayta_ikä(ikä)
        elif vastaus == "Aloita": #Peli alkaa
            nimi, sijainti, inventaario = lataa_peli(nimi)
            break

    print("\033[32mOhjeet:\033[0m")
    with open("ohjeet.txt", "r") as ohjeet: #Luetaan ohjeet tiedostosta
        ohje = ohjeet.read()
        print(f"\033[32m{ohje}\033[0m")
    
    with open("intro.txt", "r") as intro: # luetaan intro teksti tiedistosta
        teksti = intro.read()
        print(f"\033[34m{teksti}\033[0m")

    print("" + "-" * 40 )
    Peli(nimi, lataa_sijainti=sijainti, lataa_inventaario=inventaario) #Kutsutaan Peli funktiota