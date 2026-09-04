
asemat = {"EFHK": "Helsinki - Vantaa", "EFOU": "Oulu", "EFRO": "Rovaniemi"}

while True:
    v = input("Hauluatko syöttää uuden lentoaseman? (Uusi) \nHakea syötetyn tiedot (Hae) \nLopettaa (Lopeta) \nValitse: ")

    if v  == "Uusi":
        while True:
            icao = str(input("Lentoaseman ICAO koodi: "))
            nimi = str(input("Lentoaseman nimi: "))
            if icao in asemat:
                print("ICAO koodi on jo syötetty.")
            else:
                break
        asemat[icao] = nimi
    elif v == "Hae":
        etsi_icao = str(input("Lentoaseman ICAO koodi: "))
        if etsi_icao in asemat:
            print("Lentaaseman nimi:", asemat[etsi_icao])
        else:
            print("Koodia ei löytynyt.")
    elif v == "Lopeta":
        exit()
    else:
        print("Virhellinen kommento.")
    print("------------------------------------------")