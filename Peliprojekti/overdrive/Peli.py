from .Pelaaja import Pelaaja, poista_esine, tallenna_peli 
from .Huone import Huone

def Peli(nimi, lataa_sijainti=0, lataa_inventaario=[]): #Pää peli funktio

    kohde = 0
    pelaaja = Pelaaja(nimi, huone=lataa_sijainti) #Luo pelaajan, jolle annetaan nimeksi nimen jonka antoi käyttäjä. pelaajalle voi myös antaa haluessa alku sijainnin
    if lataa_inventaario:
        Pelaaja.inventaario = lataa_inventaario
    pelaaja.huoneet.append(Huone("ilmalukko","taskulamppu", 2)) #Luo huoneen "metsä" ja sille miekka esineen, jonka paino on 2. Huone tallentuu "huoneet" listaan
    pelaaja.huoneet.append(Huone("Pääkäytävä", "Ensiapupakkaus")) #Luo huoneen, jonka tallentaa "huoneet" listaan
    pelaaja.huoneet.append(Huone("Konehuone", "Sulake")) #Luo huoneen, jonka tallentaa "huoneet" listaan

    while True: #Pelin silmukka, jossa pyörii toiminnot, joita pelaaja voi käyttää
        tallenna_peli(pelaaja)
        print(f"Paikka: {pelaaja.huoneet[pelaaja.sijainti]}") # printataan nykyinen huone
        Toiminto = input("Toiminnot: \n1. Mene eteepäin \n2. Mene taaksepäin \n3. Etsi esinettä \n4. Tarkista inventaario \n5. Heitä esine pois \n6. Lopeta \nValitse toiminto: ") #kaikki toiminnot

        if Toiminto == "1":
            if kohde + 1 < len(pelaaja.huoneet):
                kohde += 1
                pelaaja.liiku(kohde) #liikutetaan pelaaja "liiku" funktiolla
            else:
                print("Et pääse pidemmälle.")
        elif Toiminto == "2":
            if kohde == 0:
                print("\033[31mTakana ei enää ole huonetta\033[0m")
            else:
                kohde -= 1
                pelaaja.liiku(kohde)
        elif Toiminto == "3":
            pelaaja.keraa_esine() #Lisätään esine "keraa_esine" funktion kautta
        elif Toiminto == "4":
            print([str(e) for e in pelaaja.inventaario]) #printataan pelaajan inventaarion
        elif Toiminto == "5":
            esine = input("Minkä esineen haluat heittää pois?:")
            poista_esine(esine) #poistetaan esine inventaariosta "poista_esine" funktiolla
        elif Toiminto == "6":
            exit() #Lopetataan pelin