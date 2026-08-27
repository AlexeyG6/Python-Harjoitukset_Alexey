lista = [] 

def parilliset(lista):
    parilliset_luvut = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset_luvut.append(luku)
    return parilliset_luvut

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = float(luku)
    lista.append(luku)

print("Lista:", lista)
Parilliset = parilliset(lista)
print(f"Parilliset luvut: {Parilliset}")