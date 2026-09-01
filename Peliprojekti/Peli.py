


print("OVERDRIVE")
nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))
print (nimi, ikä)

if ikä < 12:
    print("Pelaaja on liian nuori.")
    exit()

while True:
    print("---------------------- \nOVERDRIVE")
    vastaus = input("\nTervetuloa peliin! \nToiminnot: \nMinun nimi(nimi) \nMinun Ikä(ikä) \n(Lopeta) \nValitse toiminto: ")

    if vastaus == "Lopeta":
        break
    elif vastaus == "nimi":
        print("\nPelaajan nimi on:", nimi)
    elif vastaus == "ikä":
        print("\nPelaajan ikä on:", ikä)
