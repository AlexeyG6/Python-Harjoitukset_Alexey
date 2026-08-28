nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))
print (nimi, ikä)

if ikä < 12:
    print("Pelaaja on liian nuori.")
    exit()

while True:
    vastaus = input("---------------------- \nTervetuloa peliin! \nToiminnot: \nMinun nimi(nimi) \nMinun Ikä(ikä) \n(Lopeta) \nValitse toiminto: ")


    if vastaus == "Lopeta":
        break
    elif vastaus == "\nnimi":
        print("Pelaajan nimi on:", nimi)
    elif vastaus == "\nIkä":
        print("Pelaajan ikä on:", ikä)
