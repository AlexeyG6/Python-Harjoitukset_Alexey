
inventaario = [] #Luodaan tyhjä inventaario
    
def nayta_nimi():
    print("\nPelaajan nimi on:", nimi)
def nayta_ikä():
    print("\nPelaajan ikä on:", ikä)

def lisää_esine():
    esine = input("Anna esineen nimi: ")
    inventaario.append(esine)
    print(f"{esine} on lisätty inventaarioon.")

def poista_esine(esine):
    if esine in inventaario:
        inventaario.remove(esine)
        print(f"heitit {esine} pois")

def Peli():
    while True: 
        Toiminto = input("Toiminnot: \n1. Lisää esine inventaarioon \n2. Tarkista inventaario \n3. Heitä esine pois \n4. Lopeta \nValitse toiminto: ")

        if Toiminto == "1":
            lisää_esine()
        elif Toiminto == "2":
            print("Inventaario:", inventaario)
        elif Toiminto == "3":
            esine = input("Minkä esineen haluat heittää pois?:")
            poista_esine(esine)
        elif Toiminto == "4":
            exit()

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