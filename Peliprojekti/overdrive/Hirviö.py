from .Peli import pelaaja, inventaario
from .Pelaaja import Pelaaja, poista_esine

def taphtuma():
    print("\033[31mHirviö hyökkää sinua kohti! Sinulla ei ole taskulamppua, joten et näe sitä ja se syö sinut!\033[0m")
    for esine in inventaario:
        if esine.nimi == "Ensiapupakkaus":
            print("\033[32mSinulla on ensiapupakkaus, jolla voit pelastautua hirviön hyökkäykseltä!\033[0m")
            pelaaja.inventaario.remove(esine)
            return
    exit()