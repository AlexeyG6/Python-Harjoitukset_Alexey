#Tehtävä 2.2: Duplikaattien poisto säilyttäen järjestyksen
#Kirjoita funktio poista_duplikaatit(lista), joka ottaa vastaan listan ja palauttaa uuden listan, josta on poistettu samat alkiot, mutta alkuperäinen alkioiden järjestys on säilytetty.

def poista_dublikaatit(lista):
    lista_ilman_dublikaatteja = []
    for luku in lista:
        if luku not in lista_ilman_dublikaatteja:
            lista_ilman_dublikaatteja.append(luku)
    return lista_ilman_dublikaatteja
luvut = [1, 3, 2, 1, 5, 3, 2, 8]
print(poista_dublikaatit(luvut))