lista = [] 

def summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = float(luku)
    lista.append(luku)

print("Lista:", lista)
Summ = summa(lista)
print(f"Summa: {Summ}")