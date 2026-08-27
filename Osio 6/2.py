luvut = []


while True:
    luku = str(input("Anna luku:"))
    if luku == "":
        break
    luku = float(luku)
    luvut.append(int(luku))

for luku in luvut:
    print(max(luvut))
    luvut.remove(max(luvut))