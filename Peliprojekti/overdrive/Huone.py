from .Esine import Esine

class Huone: # Luo huoneen, sekä esineen ja tallentaa sen self muuttujaan
    def __init__(self, nimi, esine = "", painokg = 0):
        self.nimi = nimi
        self.esine = Esine(esine, painokg) #luo esineen kutsumalla "Esine" funktiota

    def __str__(self):
        return self.nimi