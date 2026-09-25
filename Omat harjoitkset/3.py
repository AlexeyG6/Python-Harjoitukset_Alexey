# Tehtävä 2.1: Sanojen pituuksien laskeminen
#Kirjoita funktio laske_sanojen_pituudet( lause ), joka ottaa parametrinaan merkkijonon (lauseen) ja palauttaa sanakirjan (dict), jossa avaimina ovat lauseen sanat ja arvoina sanojen pituudet.

def laske_sanojen_pituudet(lause):
    sanat = lause.split()
    pituudet = {}
    for sana in sanat:
        pituudet[sana] = len(sana)
    return pituudet
tulos = "Python ohjelmointi on mukavaa"

print(laske_sanojen_pituudet(tulos))