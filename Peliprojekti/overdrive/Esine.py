class Esine: #Luo esineen, joka tallentuu huoneeseen
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return self.nimi