pienin = 0
suurin = 0

while True:
    luku = str(input("Anna luku: "))
    if luku == "":
        break
    luku = float(luku)
    if luku < pienin or pienin == 0:
        pienin = luku
    if luku > suurin or suurin == 0:
        suurin = luku

print(f"Pienin luku: {pienin}")
print(f"Suurin luku: {suurin}")