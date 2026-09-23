from .Peli import Peli

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
            print("\nPeli alkaa!")
            break

    print("Olet osa astronauttiryhmää, joka havaitsi tutkassa tuntemattoman, hylätyn avaruusaluksen. Päätitte siirtyä tutkimaan sitä.")
    print("Kesken siirtymän jotain menee vakavasti pieleen.")
    print("Sähköinen räsähdys täyttää ilman, hälytysvalot välähtävät ja raskas hätäovi iskeytyy kiinni takanasi. \nKuulet radiossasi vain lyhyen huudon ja pimeyden laskeutuessa yhteys katkeaa täysin.")
    print("Kun hälytysvalot syttyvät uudelleen, tajuat olevasi yksin hylätyn aluksen ilmalukossa. \nRadiostasi kuuluu vain statiikkaa, eikä ovi takaisin omaan alukseesi enää akea. Olet täysin omillasi.")
    print("Peli alkaa...")
    Peli(nimi) #Kutsutaan Peli funktiota