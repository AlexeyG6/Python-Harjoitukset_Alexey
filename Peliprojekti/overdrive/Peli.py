from .Pelaaja import Pelaaja, poista_esine, tallenna_peli 
from .Huone import Huone

def Peli(nimi): #Pää peli funktio

    kohde = 0
    pelaaja = Pelaaja(nimi) #Luo pelaajan, jolle annetaan nimeksi nimen jonka antoi käyttäjä. pelaajalle voi myös antaa haluessa alku sijainnin
    pelaaja.huoneet.append(Huone("ilmalukko","taskulamppu", 2)) #Luo huoneen "metsä" ja sille miekka esineen, jonka paino on 2. Huone tallentuu "huoneet" listaan
    pelaaja.huoneet.append(Huone("Pääkäytävä", "Ensiapupakkaus")) #Luo huoneen, jonka tallentaa "huoneet" listaan
    pelaaja.huoneet.append(Huone("Konehuone", "Sulake")) #Luo huoneen, jonka tallentaa "huoneet" listaan
    while True: #Pelin silmukka, jossa pyörii toiminnot, joita pelaaja voi käyttää
        tallenna_peli(pelaaja)
        print(f"Paikka: {pelaaja.huoneet[pelaaja.sijainti]}") # printataan nykyinen huone
        Toiminto = input("Toiminnot: \n1. Mene eteepäin \n2. Etsi esinettä \n3. Tarkista inventaario \n4. Heitä esine pois \n5. Lopeta \nValitse toiminto: ") #kaikki toiminnot

        if Toiminto == "1":
            if kohde + 1 < len(pelaaja.huoneet):
                kohde += 1
                pelaaja.liiku(kohde) #liikutetaan pelaaja "liiku" funktiolla
            else:
                print("Et pääse pidemmälle.")
        elif Toiminto == "2":
            pelaaja.keraa_esine() #Lisätään esine "keraa_esine" funktion kautta
        elif Toiminto == "3":
            print([str(e) for e in pelaaja.inventaario]) #printataan pelaajan inventaarion
        elif Toiminto == "4":
            esine = input("Minkä esineen haluat heittää pois?:")
            poista_esine(esine) #poistetaan esine inventaariosta "poista_esine" funktiolla
        elif Toiminto == "5":
            exit() #Lopetataan pelin