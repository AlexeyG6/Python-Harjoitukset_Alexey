nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))
print (nimi, ikä)

if ikä < 12:
    print("Pelaaja on liian nuori.")
    exit()

while True:
    vastaus = input("Tervetuloa peliin! (Lopeta) ")
    if vastaus == "Lopeta":
        break
