tunnus = ("python")
salasana = ("rules")

while True:
    k = input("Anna tunnus: ")
    s = input("Anna salasana: ")
    if k == tunnus and s == salasana:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty")