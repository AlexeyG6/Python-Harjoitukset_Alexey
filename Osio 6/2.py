luvut = []

while True:
    luku = str(input("Anna luku:"))
    if luku == "":
        break
    luku = float(luku)
    luvut.append(int(luku))

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

for luku in viisi_suurinta:
    print(max(luvut))
    luvut.remove(max(luvut))