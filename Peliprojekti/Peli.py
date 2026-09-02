

def Peli():
    exit()
    



print("OVERDRIVE") #Printataan Pelin nimi
nimi = input("Anna pelaajan nimi: ") #Kysytään pelaajan nimeä
ikä = int(input("Anna pelaajan ikä: ")) #Kysytään pelaajan ikää ja muutetaan se kokonaisluvuksi
print (nimi, ikä) #Kirjataan Pelaajan nimi ja ikä

if ikä < 12: #Jos pelaajan ikä on alle 12, niin peli sulkee ohjelman ja ilmoittaa että pelaaja on liian nuori
    print("Pelaaja on liian nuori.")
    exit()

while True: #Ohjelma kirjoittaa pelin toiminnot ja kysyy pelaajalta mitä hän haluaa tehdä. Pelaaja voi valita Aloittaa tai lopettaa pelin, tarkistaa nimensä tai ikänsä.
    print("---------------------- \nOVERDRIVE")
    vastaus = input("\nTervetuloa peliin! \nToiminnot: \nAloita peli(Aloita) \nMinun nimi(nimi) \nMinun Ikä(ikä) \n(Lopeta) \nValitse toiminto: ")

    if vastaus == "Lopeta": #Peli loppuu
        exit()
    elif vastaus == "nimi": #Kirjataan nimi
        print("\nPelaajan nimi on:", nimi)
    elif vastaus == "ikä": #Kirjataan ikä
        print("\nPelaajan ikä on:", ikä)
    elif vastaus == "Aloita": #Peli alkaa
        print("\nPeli alkaa!")
        break


Peli() #Kutsutaan Peli funktiota, joka luo pelin ikkunan