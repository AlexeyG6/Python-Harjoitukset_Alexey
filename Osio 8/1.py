vuodenajat = ["talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi"]
while True:
    kuukaus = int(input("Anna kuukausi (1-12): "))

    if kuukaus < 1 or kuukaus > 12:
        print("Virheellinen kuukausi. Anna luku väliltä 1-12.")
    else:
        break

indeksi = kuukaus - 1
print("Kuukausi on vuodenajassa:", vuodenajat[indeksi])