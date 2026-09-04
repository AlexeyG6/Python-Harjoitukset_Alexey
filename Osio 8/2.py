nimet = {""}
nimet.remove("")
while True:
    nimi = input("Anna pelaajan nimi: ") 
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin suötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print(nimet)