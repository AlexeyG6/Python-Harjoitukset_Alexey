luvut = []

while True:
    luku = str(input("Anna luku:"))
    if luku == "":
        break
    luku = float(luku)
    luvut.append(int(luku))

for s in luvut:
    print(s)