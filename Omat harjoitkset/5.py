#Tehtävä 3.1: Muistiinpanojen tallennus ja lukeminen
#Kirjoita ohjelma, joka tarjoaa käyttäjälle yksinkertaisen tekstimenu-käyttöliittymän:

def kirjoita_muistiinpano():
    teksti = input("Kirjoita muistiinpano: ")
    with open ("text.txt", "a", encoding="utf-8") as T:
        T.write(teksti + "\n")
    print("Muistiinpano tallennettu!")

def lue_muistiinpanot():
    try:
        with open ("text.txt", "r", encoding="utf-8") as R:
            luettu = R.read()
            print("\n--- MUISTIINPANOT ---")
            print(luettu if luettu else "Tiedosto on tyhjä")
            print("-" * 21)
    except FileNotFoundError:
        print("\nEi vielä tallennettuja muistiinpanoja.\n")


def main():
    while True:
        valinta = str(input("1. Kirjoita muistiinpano \n2. Lue kaikki muistiinpanot \n3. Lopeta \nValitse: "))
        if valinta == "1":
            kirjoita_muistiinpano()
        elif valinta == "2":
            lue_muistiinpanot()
        elif valinta == "3":
            exit()
        else:
            print("Virheellinen kommento")

if __name__ == "__main__":
    main()
